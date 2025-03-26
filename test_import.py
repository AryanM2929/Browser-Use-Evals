import sys
import os

# Add the browser-use directory to the Python path
sys.path.append(os.path.abspath("browser-use") )

try:
    from browser_use.agent import BrowserUseAgent
    from browser_use.browser import Browser
    
    print("Successfully imported browser_use modules!")
    
    agent = BrowserUseAgent(model="gpt-4o")
    browser = Browser()
    
    result = agent.run("Test instruction", browser, return_steps=True, return_token_usage=True)
    print("Test run successful!")
    
except ImportError as e:
    print(f"Import error: {str(e)}")
    print(f"Current Python path: {sys.path}")
