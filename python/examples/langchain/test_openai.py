import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Test OpenAI API directly
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Using the cheaper model first
        messages=[
            {"role": "user", "content": "Hello, just testing the API. Respond with 'API is working!'"}
        ],
        max_tokens=20
    )
    print("✅ OpenAI API is working!")
    print(f"Response: {response.choices[0].message.content}")
    
    # Check usage/billing info
    print(f"\nModel used: {response.model}")
    print(f"Usage: {response.usage}")
    
except Exception as e:
    print(f"❌ OpenAI API Error: {e}")
    print("Check your API key and billing status at https://platform.openai.com/account/billing")
