"""
Data Processing Module - Spoke 3
Handles data processing and analysis
"""

def process_student_data(students):
    """
    Process student data and return statistics
    
    Args:
        students (list): List of dictionaries with student info
                        Each dict has 'name' and 'score' keys
    
    Returns:
        dict: Dictionary with processed statistics
    """
    if not students:
        return {}
    
    scores = [student["score"] for student in students]
    names = [student["name"] for student in students]
    
    processed = {
        "total_students": len(students),
        "highest_score": max(scores),
        "lowest_score": min(scores),
        "average_score": sum(scores) / len(scores),
        "top_student": names[scores.index(max(scores))],
        "all_names": names
    }
    
    return processed

def filter_by_score(students, threshold):
    """
    Filter students by score threshold
    
    Args:
        students (list): List of student dictionaries
        threshold (int): Minimum score threshold
        
    Returns:
        list: Students meeting the threshold
    """
    return [s for s in students if s["score"] >= threshold]

def sort_by_score(students, descending=True):
    """
    Sort students by score
    
    Args:
        students (list): List of student dictionaries
        descending (bool): Sort in descending order if True
        
    Returns:
        list: Sorted list of students
    """
    return sorted(students, key=lambda x: x["score"], reverse=descending)

def group_by_range(students, range_size=10):
    """
    Group students into score ranges
    
    Args:
        students (list): List of student dictionaries
        range_size (int): Size of each range
        
    Returns:
        dict: Groups of students by score range
    """
    groups = {}
    
    for student in students:
        score = student["score"]
        range_key = f"{(score // range_size) * range_size}-{((score // range_size) + 1) * range_size}"
        
        if range_key not in groups:
            groups[range_key] = []
        groups[range_key].append(student)
    
    return groups

def create_name_score_tuple(students):
    """
    Create list of tuples with name and score
    
    Args:
        students (list): List of student dictionaries
        
    Returns:
        list: List of tuples (name, score)
    """
    return [(s["name"], s["score"]) for s in students]