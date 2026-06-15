import shutil
import os


def verify_utility_availability(utility: str) -> str:
    """
    Verifies a system utility by checking its existence at a specific path.

    Parameters
    ----------
    utility : str
        The name of the utility to verify (e.g., `echo`, `ls`, `mkdir`).

    Returns
    -------
    dict
        A dictionary containing the utility name and its absolute path if
        found, otherwise `None` for the utility.

    Raises
    ------
    ValueError
        When the utility is not found or an error occurs while checking its
        presence.
    TypeError
        When the input type is incorrect or the utility name is invalid.

    Examples
    --------
    >>> verify_utility_availability(utility='echo')
    >>> verify_utility_availability(utility='non-existent-utility')
    {'output': '/bin/echo', 'utility': 'echo'}
    None

    """
    
    if not isinstance(utility, str):
        raise TypeError("Input utility must be a string")
    
    if not utility or not utility.strip():
        raise TypeError("Utility name is invalid or empty")
    
    utility = utility.strip()
    
    try:
        absolute_path = shutil.which(utility)
        if absolute_path is None:
            raise ValueError(f"Utility '{utility}' not found on the system")
        
        if not os.path.exists(absolute_path):
            raise ValueError(f"Utility '{utility}' path exists but file is not accessible")
        
        return absolute_path
    except Exception as e:
        if isinstance(e, (ValueError, TypeError)):
            raise
        raise ValueError(f"Error occurred while checking utility '{utility}': {str(e)}")