"""
Greetings Module - Spoke 1
Handles greeting functionality
"""

def get_greeting(name):
    """
    Generate a personalized greeting message
    
    Args:
        name (str): Person's name
        
    Returns:
        str: Personalized greeting message
    """
    greetings_dict = {
        "morning": "Good morning!",
        "afternoon": "Good afternoon!",
        "evening": "Good evening!"
    }
    
    greeting_message = f"Hello, {name}! Welcome to the Educational Hub and Spoke Project."
    return greeting_message

def get_random_greeting():
    """
    Return a random greeting from a list
    
    Returns:
        str: A random greeting message
    """
    greetings_list = [
        "Hello! How are you?",
        "Hi there!",
        "Greetings!",
        "Welcome!",
        "Good to see you!"
    ]
    
    return greetings_list[0]  # Returns first greeting for predictability

def format_greeting(name, title):
    """
    Format a greeting with name and title
    
    Args:
        name (str): Person's name
        title (str): Person's title
        
    Returns:
        str: Formatted greeting
    """
    return f"Hello {title} {name}!"