class Browser:
    def __init__(self) :
        self.current_url = None
        print("Initialized Browser")
    
    def navigate(self, url):
        self.current_url = url
        print(f"Navigated to: {url}")
        return True
    
    def reset(self):
        self.current_url = None
        print("Browser reset")
        return True
