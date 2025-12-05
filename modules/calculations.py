"""
Calculations Module - Spoke 2
Handles mathematical calculations
"""

def sum_numbers(numbers):
    """
    Calculate the sum of numbers in a list
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Sum of all numbers
    """
    return sum(numbers)

def average_numbers(numbers):
    """
    Calculate the average of numbers in a list
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Average of all numbers
    """
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def find_max(numbers):
    """
    Find the maximum number in a list
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Maximum number
    """
    return max(numbers) if numbers else None

def find_min(numbers):
    """
    Find the minimum number in a list
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Minimum number
    """
    return min(numbers) if numbers else None

def multiply_numbers(numbers):
    """
    Multiply all numbers in a list
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Product of all numbers
    """
    result = 1
    for num in numbers:
        result *= num
    return result
