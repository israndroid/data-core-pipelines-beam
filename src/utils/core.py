from datetime import datetime

def get_total_elapsed_time_in_seconds(start_time:float, end_time:float) -> int:
    """
    Calculate the total elapsed time in seconds between two datetime objects.
    
    Args:
        start_time (float): The start time.
        end_time (float): The end time.
    
    Returns:
        int: Total elapsed time in seconds.
    """
    if not isinstance(start_time, float) or not isinstance(end_time, float):
        raise ValueError("Both start_time and end_time must be float objects.")
    
    elapsed_time = end_time - start_time
    return int(elapsed_time)

def format_elapsed_time(seconds:int) -> str:
    """
    Format elapsed time in seconds into a human-readable string.
    
    Args:
        seconds (int): Total elapsed time in seconds.
    
    Returns:
        str: Formatted elapsed time.
    """
    if seconds < 0:
        raise ValueError("Elapsed time cannot be negative.")
    
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return f"{hours}h {minutes}m {seconds}s"

def get_elapsed_time(start_time:float, end_time:float) -> str:
    """
    Get the elapsed time between two float objects in a human-readable format.
    
    Args:
        start_time (float): The start time.
        end_time (float): The end time.
    
    Returns:
        str: Formatted elapsed time.
    """
    total_seconds = get_total_elapsed_time_in_seconds(start_time, end_time)
    return format_elapsed_time(total_seconds)