from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


print("Testing the Gemini Model...")

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # In a real implementation, this would call a weather API.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract two numbers."""
    return a - b

