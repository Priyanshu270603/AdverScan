pip install google-generativeai
import google.generativeai as genai

# Set up Gemini API Key
genai.configure(api_key="AIzaSyAdehFdko2Z3NMyDE_I0oUYtSTGJJgDitA")

# Function to generate text response using Gemini API
def generate_adv_snippet(message):
    model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" for better quality
    response = model.generate_content(message)
    return response.text.strip() if response and response.text else "No response generated."

# Function to format prompts with surrounding context
def generate_new_prompt(content, pre_context, post_context):
    new_prompts = []

    for idx in range(len(content)):
        prompt = content[idx]['prompt'].replace('\n', '').replace('\r', '')
        pre_con = pre_context[idx]
        post_con = post_context[idx]
        
        # Constructing the enhanced prompt
        new_promp = (f"With the partial preceding codes provided as: {pre_con}. "
                     f"{prompt} "
                     f"and with the partial following codes provided as: {post_con}")
        
        new_prompts.append(new_promp)

    return new_prompts

# Function to generate responses for multiple prompts
def save_adv_snippet(new_prompts):
    adv_snippets = []

    for new_prom in new_prompts:
        message = f"You are an experienced programmer. {new_prom}"
        answer = generate_adv_snippet(message)
        adv_snippets.append(answer)

    return adv_snippets

# Example Usage
if __name__ == "__main__":
    content = [{"prompt": "Write a function to reverse a string in Python."}]
    pre_context = ["# This function takes a string as input"]
    post_context = ["# Output should be the reversed string"]

    new_prompts = generate_new_prompt(content, pre_context, post_context)
    responses = save_adv_snippet(new_prompts)

    for idx, response in enumerate(responses):
        print(f"Prompt {idx+1}: {new_prompts[idx]}\nResponse: {response}\n")
