import os
from dotenv import load_dotenv
from stripe_agent_toolkit.langchain.toolkit import StripeAgentToolkit

load_dotenv()

# Test the Stripe toolkit without using OpenAI
stripe_secret_key = os.getenv("STRIPE_SECRET_KEY")
if not stripe_secret_key:
    raise ValueError("STRIPE_SECRET_KEY environment variable is required")

stripe_agent_toolkit = StripeAgentToolkit(
    secret_key=stripe_secret_key,
    configuration={
        "actions": {
            "payment_links": {
                "create": True,
            },
            "products": {
                "create": True,
            },
            "prices": {
                "create": True,
            },
        }
    },
)

# Get the available tools
tools = stripe_agent_toolkit.get_tools()

print("Available Stripe tools:")
for tool in tools:
    print(f"- {tool.name}: {tool.description}")

print(f"\nTotal tools available: {len(tools)}")
