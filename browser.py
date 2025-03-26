class Browser:
    def __init__(self):
        self.history = []
        print("Initialized Browser")
        
    def navigate(self, url):
        """
        Navigate to the specified URL.
        """
        print(f"Navigating to: {url}")
        self.history.append({"action": "navigate", "url": url})
        
    def reset(self):
        """
        Reset the browser state.
        """
        print("Resetting browser")
        self.history = []
        
    def get_history(self):
        """
        Get the browser history.
        """
        return self.history
