def generate_environment_summary(env_dir: str, utils_ok: str, permissions_ok: str, symlinks_ok: str, env_vars: str) -> str:
    """
    Generates a summary of the environment setup.

    Parameters
    ----------
    env_dir : str
        The absolute path of the isolated temporary directory.
    utils_ok : str
        Whether the essential system utilities are verified and available.
    permissions_ok : str
        Whether the new directory has mode `0700` and is isolated.
    symlinks_ok : str
        Whether the new directory contains no symlinks.
    env_vars : str
        Relevant environment variables.

    Returns
    -------
    str
        A string containing the environment summary, including
        success/failure status for each check and relevant environment
        variables.

    Raises
    ------
    ValueError
        When the input parameters do not match the expected format.
    TypeError
        When the input parameters are of the wrong type.

    Examples
    --------
    >>> env_dir_absolute = get_absolute_path(temp_dir_path)
    >>> utils_available = verify_utility_availability('echo')
    >>> permissions_valid =
    check_directory_permissions(directory=env_dir_absolute)
    >>> symlinks_valid = not has_symlinks
    >>> environment_vars = get_relevant_environment_variables()
    >>> generate_environment_summary(env_dir=env_dir_absolute, "
    "utils_ok=bool(utils_available), permissions_ok=permissions_valid, "
    "symlinks_ok=symlinks_valid, env_vars=environment_vars)
    A string containing the environment summary.

    """
    if not isinstance(env_dir, str):
        raise TypeError("env_dir must be of type str")
    if not isinstance(utils_ok, str):
        raise TypeError("utils_ok must be of type str")
    if not isinstance(permissions_ok, str):
        raise TypeError("permissions_ok must be of type str")
    if not isinstance(symlinks_ok, str):
        raise TypeError("symlinks_ok must be of type str")
    if not isinstance(env_vars, str):
        raise TypeError("env_vars must be of type str")
    
    summary_lines = []
    summary_lines.append("Environment Setup Summary")
    summary_lines.append("=" * 28)
    summary_lines.append("")
    
    summary_lines.append(f"Environment Directory: {env_dir}")
    summary_lines.append("")
    
    summary_lines.append("Status Checks:")
    
    utils_status = "PASS" if utils_ok.lower() in ['true', 'yes', '1', 'pass', 'ok'] else "FAIL"
    summary_lines.append(f"  - System utilities available: {utils_status}")
    
    permissions_status = "PASS" if permissions_ok.lower() in ['true', 'yes', '1', 'pass', 'ok'] else "FAIL"
    summary_lines.append(f"  - Directory permissions (0700): {permissions_status}")
    
    symlinks_status = "PASS" if symlinks_ok.lower() in ['true', 'yes', '1', 'pass', 'ok'] else "FAIL"
    summary_lines.append(f"  - No symlinks present: {symlinks_status}")
    
    summary_lines.append("")
    summary_lines.append("Environment Variables:")
    if env_vars.strip():
        for line in env_vars.strip().split('\n'):
            if line.strip():
                summary_lines.append(f"  {line.strip()}")
    else:
        summary_lines.append("  (None specified)")
    
    return "\n".join(summary_lines)