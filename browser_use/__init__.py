"""Browser Use package."""

# Set up logging
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("browser_use")
logger.info("BrowserUse logging setup complete with level info")

# Import main classes for easier access
from browser_use.agent import BrowserUseAgent
from browser_use.browser import Browser

__all__ = ["BrowserUseAgent", "Browser"]
