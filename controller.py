class Controller:
    def __init__(self, browser=None, agent=None):
        self.browser = browser
        self.agent = agent
        print("Initialized Controller")
        
    def execute(self, instruction):
        """
        Execute an instruction using the agent and browser.
        """
        print(f"Controller executing: {instruction}")
        if self.agent:
            return self.agent.run(instruction)
        return "Agent not initialized"
