import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Attempt to retrieve the API key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Print the key for verification (be careful not to expose it publicly)
print(f"OPEN API Key: {google_api_key}")