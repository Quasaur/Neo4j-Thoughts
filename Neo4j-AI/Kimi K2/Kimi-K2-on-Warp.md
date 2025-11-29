# Q:
I use the Warp terminal on MACOS Sequoia (https://www.warp.dev). How do I configure Warp to use Kimi K2 instead of Claude 3.5 (include step-by-step instructions to remove Claude 3.5 from Warp)?

# A:
Warp Terminal has been evolving rapidly, especially with its AI integration. While Warp directly supports certain AI models like Claude 3.5 Sonnet and Haiku through its "Agent Mode," it doesn't currently offer a direct, in-app setting to switch to an arbitrary, non-partnered AI model like Kimi K2.
Kimi K2 is a newly released, powerful open-source model. To use it with Warp, you would typically need to interact with it via its API or a local instance if you were running it yourself. Warp's "Agent Mode" is designed to work with pre-configured integrations.
Therefore, directly "configuring Warp to use Kimi K2 instead of Claude 3.5" in the same way you select an option from a dropdown within Warp's settings is not currently possible.
However, you can use Kimi K2 with Warp by interacting with its API through shell commands or custom scripts within Warp. This means you'd be using Warp as your terminal interface to send requests to Kimi K2, rather than Kimi K2 being natively integrated into Warp's AI features.
Here's how you can approach this, along with instructions for understanding how to manage Warp's current AI integrations:
Understanding Warp's AI Integration (and why Kimi K2 isn't a direct switch)
Warp's AI features, specifically "Agent Mode," are built around direct integrations with certain AI providers. When you see Claude 3.5 listed, it means Warp has a built-in connector for that specific model. Kimi K2 is a newer, open-source model, and as of now, Warp hasn't announced a direct, native integration for it.
How to "Remove" Claude 3.5 (or switch off Agent Mode)
You don't typically "remove" Claude 3.5 from Warp, as it's an integrated option. Instead, you would simply choose not to use Agent Mode with Claude, or select a different available model if one is offered.
 * Disable Agent Mode (if you don't want to use AI at all):
   * When in Warp, you can typically exit Agent Mode by pressing ESC or CTRL-C, or by toggling out with CMD-I (on macOS).
   * This stops the active AI interaction.
 * Select a different AI model (if available):
   * Warp's changelog mentions a dropdown menu above Agent Mode prompts to choose which model to use. If Warp adds other integrated models in the future, this is where you would switch. As of now, Claude 3.5 Sonnet and Haiku are the mentioned options.
How to Use Kimi K2 with Warp (Indirectly)
To use Kimi K2 with Warp, you would interact with it through its API. This usually involves:
 * Obtaining a Kimi K2 API Key: You'll need to check the Moonshot AI platform (platform.moonshot.ai/console) or the Kimi K2 project's documentation for details on how to get an API key. This is essential for sending requests to the model.
 * Using curl or a Python script within Warp: You can write curl commands or Python scripts (or scripts in other languages) to send prompts to the Kimi K2 API and receive responses.
   Example (Conceptual - you'll need to adapt with actual API endpoints and authentication):
   * Using curl:
     curl -X POST "https://api.moonshot.ai/v1/kimi-k2/chat/completions" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_KIMI_K2_API_KEY" \
     -d '{
           "model": "Kimi-K2-Instruct",
           "messages": [
             {"role": "user", "content": "Explain quantum entanglement in simple terms."}
           ]
         }'

     Replace YOUR_KIMI_K2_API_KEY with your actual API key.
     The API endpoint and request body structure might vary, so refer to the official Kimi K2 API documentation.
   * Using Python (requires requests library - install with pip install requests):
     * Create a Python file (e.g., kimi_k2_query.py):
       import requests
import os

API_KEY = os.getenv("KIMI_K2_API_KEY") # Get API key from environment variable
API_ENDPOINT = "https://api.moonshot.ai/v1/kimi-k2/chat/completions" # Adjust as per Kimi K2 docs

def query_kimi_k2(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "model": "Kimi-K2-Instruct", # Or Kimi-K2-Base
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status() # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    user_prompt = input("Enter your prompt for Kimi K2: ")
    response_data = query_kimi_k2(user_prompt)

    if "error" in response_data:
        print(f"Error: {response_data['error']}")
    else:
        # Parse and print the actual response from Kimi K2
        if 'choices' in response_data and response_data['choices']:
            print("Kimi K2 Response:")
            print(response_data['choices'][0]['message']['content'])
        else:
            print("No valid response from Kimi K2.")


     * Set your API key as an environment variable in Warp:
       export KIMI_K2_API_KEY="YOUR_KIMI_K2_API_KEY"

       (For permanent storage, add this line to your shell's configuration file, like ~/.zshrc or ~/.bashrc, and then run source ~/.zshrc or source ~/.bashrc)
     * Run the script in Warp:
       python kimi_k2_query.py

This indirect method allows you to leverage Kimi K2's capabilities through your Warp terminal, even though it's not a native integration like Warp's current Claude offerings. Keep an eye on Warp's changelog and features, as they may add direct support for more AI models in the future.
