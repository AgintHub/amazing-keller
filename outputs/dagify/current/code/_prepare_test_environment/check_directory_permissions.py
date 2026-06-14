import os
import stat


def check_directory_permissions(directory: str) -> str:
    """
    Checks the directory permissions of a given directory.

    Parameters
    ----------
    directory : str
        Path to the directory to check.

    Returns
    -------
    str
        Mode of the directory as a string.

    Raises
    ------
    ValueError
        When the directory path is invalid.
    TypeError
        When the input type is incorrect.

    Examples
    --------
    >>> check_directory_permissions('/path/to/directory')
    '0700'

    >>> check_directory_permissions('/another/directory')
    'another_mode'

    """
    
    if not isinstance(directory, str):
        raise TypeError("Input must be a string")
    
    if not directory or not directory.strip():
        raise ValueError("Directory path cannot be empty")
    
    try:
        if not os.path.exists(directory):
            raise ValueError(f"Directory path does not exist: {directory}")
        
        if not os.path.isdir(directory):
            raise ValueError(f"Path is not a directory: {directory}")
        
        dir_stat = os.stat(directory)
        mode = stat.S_IMODE(dir_stat.st_mode)
        mode_string = oct(mode)[2:]
        
        return mode_string
    except OSError as e:
        raise ValueError(f"Cannot access directory: {directory}") from e