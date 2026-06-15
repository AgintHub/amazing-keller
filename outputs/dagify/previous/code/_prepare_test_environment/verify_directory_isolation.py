import os
import stat


def verify_directory_isolation(directory: str) -> bool:
    """
    Verifies whether a directory is properly isolated to prevent unauthorized
    access.

    Parameters
    ----------
    directory : STR
        Path to the directory being checked for isolation.

    Returns
    -------
    dict
        A dictionary containing a boolean indicating whether the isolated
        directory is accessible only by the owner, and the directory path
        being checked.

    Raises
    ------
    ValueError
        Raised when the input directory path is invalid or the directory
        does not exist.
    PermissionError
        Raised when the shim lacks permission to access the directory being
        checked for isolation.

    Examples
    --------
    >>> print(verify_directory_isolation('/home/user/isolated_dir'))
    >>> print(verify_directory_isolation('/home/user/public_dir'))
    {'output': True, 'directory': '/home/user/isolated_dir'}
    {'output': False, 'directory': '/home/user/public_dir'}

    """
    
    if not directory or not isinstance(directory, str):
        raise ValueError("Invalid directory path provided")
    
    if not os.path.exists(directory):
        raise ValueError("Directory does not exist")
    
    if not os.path.isdir(directory):
        raise ValueError("Path is not a directory")
    
    try:
        dir_stat = os.stat(directory)
        file_mode = dir_stat.st_mode
        
        owner_perms = (file_mode & stat.S_IRWXU) >> 6
        group_perms = (file_mode & stat.S_IRWXG) >> 3
        other_perms = file_mode & stat.S_IRWXO
        
        is_isolated = (group_perms == 0 and other_perms == 0)
        
        return is_isolated
        
    except (OSError, IOError) as e:
        raise PermissionError(f"Permission denied accessing directory: {directory}") from e