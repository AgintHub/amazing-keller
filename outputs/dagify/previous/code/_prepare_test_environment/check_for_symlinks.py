import os


def check_for_symlinks(directory: str) -> bool:
    """
    Checks if a directory contains symlinks.

    Parameters
    ----------
    directory : STR
        The absolute path of the directory to check for symlinks.

    Returns
    -------
    dict
        A dictionary containing the output and directory, where output is a
        boolean indicating the presence of symlinks and directory is the
        input path.

    Raises
    ------
    ValueError
        Raised when the input directory path is invalid or not a string.
    TypeError
        Raised when the input directory path is not a string.

    Examples
    --------
    >>> check_for_symlinks(directory='/path/to/valid/directory')
    {'output': False, 'directory': '/path/to/valid/directory'}

    >>> check_for_symlinks(directory='/path/to/directory/with/symlinks')
    {'output': True, 'directory': '/path/to/directory/with/symlinks'}

    """
    
    if not isinstance(directory, str):
        raise TypeError("Input directory path must be a string")
    
    if not directory or not os.path.exists(directory):
        raise ValueError("Input directory path is invalid")
    
    if not os.path.isdir(directory):
        raise ValueError("Input path is not a directory")
    
    try:
        for root, dirs, files in os.walk(directory):
            for item in dirs + files:
                item_path = os.path.join(root, item)
                if os.path.islink(item_path):
                    return True
        return False
    except (OSError, PermissionError) as e:
        raise ValueError(f"Error accessing directory: {e}") from e