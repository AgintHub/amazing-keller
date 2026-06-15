# generate_environment_summary PRD

## Description
Generates a summary of the environment setup, including success/failure status for each check and relevant environment variables.


## Conceptual Info

This shim generates a summary of the environment setup, including success/failure status for each check and relevant environment variables.

## Docstring

### Summary
Generates a summary of the environment setup.

### Parameters

- **env_dir** (str): The absolute path of the isolated temporary directory.
- **utils_ok** (str): Whether the essential system utilities are verified and available.
- **permissions_ok** (str): Whether the new directory has mode `0700` and is isolated.
- **symlinks_ok** (str): Whether the new directory contains no symlinks.
- **env_vars** (str): Relevant environment variables.

### Returns

str: A string containing the environment summary, including success/failure status for each check and relevant environment variables.

### Raises

- ValueError: When the input parameters do not match the expected format.
- TypeError: When the input parameters are of the wrong type.

### Examples

```python
>>> env_dir_absolute = get_absolute_path(temp_dir_path)
>>> utils_available = verify_utility_availability('echo')
>>> permissions_valid = check_directory_permissions(directory=env_dir_absolute)
>>> symlinks_valid = not has_symlinks
>>> environment_vars = get_relevant_environment_variables()
>>> generate_environment_summary(env_dir=env_dir_absolute, "
              "utils_ok=bool(utils_available), permissions_ok=permissions_valid, "
              "symlinks_ok=symlinks_valid, env_vars=environment_vars)
A string containing the environment summary.
```
