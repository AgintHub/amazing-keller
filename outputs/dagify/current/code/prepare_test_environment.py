from ._prepare_test_environment.create_unique_temp_directory import create_unique_temp_directory
from ._prepare_test_environment.get_absolute_path import get_absolute_path
from ._prepare_test_environment.verify_utility_availability import verify_utility_availability
from ._prepare_test_environment.check_directory_permissions import check_directory_permissions
from ._prepare_test_environment.verify_directory_isolation import verify_directory_isolation
from ._prepare_test_environment.check_for_symlinks import check_for_symlinks
from ._prepare_test_environment.get_relevant_environment_variables import get_relevant_environment_variables
from ._prepare_test_environment.generate_environment_summary import generate_environment_summary

from ._prepare_test_environment.create_unique_temp_directory import create_unique_temp_directory
from ._prepare_test_environment.get_absolute_path import get_absolute_path
from ._prepare_test_environment.verify_utility_availability import verify_utility_availability
from ._prepare_test_environment.check_directory_permissions import check_directory_permissions
from ._prepare_test_environment.verify_directory_isolation import verify_directory_isolation
from ._prepare_test_environment.check_for_symlinks import check_for_symlinks
from ._prepare_test_environment.get_relevant_environment_variables import get_relevant_environment_variables
from ._prepare_test_environment.generate_environment_summary import generate_environment_summary

from pydantic import BaseModel, Field


class PrepareTestEnvironmentOutput(BaseModel):
    """Pydantic model for prepare_test_environment node outputs."""
    env_dir: str = (
        Field(..., description = (
            "Absolute path of the isolated temporary directory")
        )
    )
    utils_ok: bool = (
        Field(..., description = (
            "Whether the essential system utilities are verified and available")
        )
    )
    permissions_ok: bool = (
        Field(..., description = (
            "Whether the new directory has mode `0700` and is isolated")
        )
    )
    symlinks_ok: bool = (
        Field(..., description="Whether the new directory contains no symlinks")
    )
    cleanup_command: str = (
        Field(..., description = (
            "Shell command to safely remove the directory after tests complete")
        )
    )
    summary: str = (
        Field(..., description = (
            "Summary of the environment setup, including success/failure status for each check and relevant environment variables")
        )
    )


def prepare_test_environment(general_input: str, **kwargs) -> PrepareTestEnvironmentOutput:
    """
    Setup isolated temporary directory and verify utilities for testing.

    Parameters
    ----------
    current_working_directory : str
        The current working directory where the temporary directory will be
        created.

    Returns
    -------
    dict
        Dictionary containing the declared output fields.

    Raises
    ------
    ValueError
        If an input is invalid or cannot be resolved.

    Examples
    --------
    >>> import os
    >>> import tempfile
    >>> import which
    >>> import pwd
    >>> import grp
    >>> import stat
    {'env_dir': '/tmp/test_env.XXXXXX', 'utils_ok': True, 'permissions_ok':
    True, 'symlinks_ok': True, 'cleanup_command': 'rm -rf /tmp/test_env.XXXXXX',
    'summary': 'Environment setup successful.'}

    """
    temp_dir_path: str = create_unique_temp_directory()
    env_dir_absolute: str = get_absolute_path(path=temp_dir_path)
    
    echo_path: str = verify_utility_availability(utility="echo")
    ls_path: str = verify_utility_availability(utility="ls")
    mkdir_path: str = verify_utility_availability(utility="mkdir")
    utils_available: bool = bool(echo_path and ls_path and mkdir_path)
    
    directory_mode: str = check_directory_permissions(directory=env_dir_absolute)
    is_isolated: bool = verify_directory_isolation(directory=env_dir_absolute)
    permissions_valid: bool = directory_mode == "0700" and is_isolated
    
    has_symlinks: bool = check_for_symlinks(directory=env_dir_absolute)
    symlinks_valid: bool = not has_symlinks
    
    cleanup_cmd: str = f"rm -rf "{env_dir_absolute}""
    
    environment_vars: dict = get_relevant_environment_variables()
    setup_summary: str = generate_environment_summary(
        env_dir=env_dir_absolute,
        utils_ok=utils_available,
        permissions_ok=permissions_valid,
        symlinks_ok=symlinks_valid,
        env_vars=environment_vars
    )
    
    return PrepareTestEnvironmentOutput(
        env_dir=env_dir_absolute,
        utils_ok=utils_available,
        permissions_ok=permissions_valid,
        symlinks_ok=symlinks_valid,
        cleanup_command=cleanup_cmd,
        summary=setup_summary
    )