import google.generativeai as genai

# Configure API key (replace with your actual key)
genai.configure(api_key="AIzaSyD9Gi3C3IWovq8BvLykbheaWU8XmUqKBDs")

# List available models
models = genai.list_models()

# Print model names
print("Available Gemini AI Models:")
for model in models:
    print(model.name)
