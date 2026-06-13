from pydantic import BaseModel, Field


class PrepareTestEnvironmentOutput(BaseModel):
    """Pydantic model for prepare_test_environment node outputs."""
    env_dir: str = (
        Field(..., description="Absolute path of the isolated temporary directory")
    )
    utils_ok: bool = (
        Field(..., description="Whether the essential system utilities are verified and available")
    )
    permissions_ok: bool = (
        Field(..., description="Whether the new directory has mode `0700` and is isolated")
    )
    symlinks_ok: bool = (
        Field(..., description="Whether the new directory contains no symlinks")
    )
    cleanup_command: str = (
        Field(..., description="Shell command to safely remove the directory after tests complete")
    )
    summary: str = (
        Field(..., description="Summary of the environment setup, including success/failure status for each check and relevant environment variables")
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
    return PrepareTestEnvironmentOutput(
        env_dir="",
        utils_ok=False,
        permissions_ok=False,
        symlinks_ok=False,
        cleanup_command="",
        summary="",
    )