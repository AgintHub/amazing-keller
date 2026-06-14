import os


def get_absolute_path(path: str) -> str:
    """
    Obtain the absolute path of a directory or file.

    Parameters
    ----------
    path : str
        The path for which the absolute path is to be retrieved.

    Returns
    -------
    STR
        The absolute path of the directory or file.

    Raises
    ------
    ValueError
        When the input path does not exist or is invalid.
    TypeError
        When the input path is not a string.

    Examples
    --------
    >>> get_absolute_path('/home/user')
    /home/user

    >>> get_absolute_path('./current_directory')
    /current_directory

    """
    
    if not isinstance(path, str):
        raise TypeError("The input path is not a string")
    
    if not path:
        raise ValueError("The input path does not exist or is invalid")
    
    try:
        absolute_path = os.path.abspath(path)
        return absolute_path
    except Exception:
        raise ValueError("When the input path does not exist or is invalid")