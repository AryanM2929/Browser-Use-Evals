import os
from dotenv import load_dotenv
from browser_use.agent import BrowserUseAgent
from browser_use.browser import Browser

# Load environment variables
load_dotenv("browser-use/.env")

# Check if API key is available
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

print(f"API key found: {api_key[:5]}...")

# Initialize Browser Use components
browser = Browser()
agent = BrowserUseAgent(browser=browser)

# Test a simple navigation
browser.navigate("https://www.google.com") 
print("Successfully navigated to Google")

# Close the browser
browser.close()
print("Test completed successfully")
