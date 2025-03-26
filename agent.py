class BrowserUseAgent:
    def __init__(self, model="gpt-4o", browser=None):
        self.model = model
        self.browser = browser
        print(f"Initialized BrowserUseAgent with model: {model}")
        
    def run(self, instruction):
        """
        Run the agent with the given instruction.
        """
        print(f"Running instruction: {instruction}")
        # This is a placeholder implementation
        return f"Executed: {instruction}"
