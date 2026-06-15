# verify_directory_isolation PRD

## Description
Verifies whether the directory is properly isolated to prevent unauthorized access.


## Conceptual Info

This shim verifies directory isolation to ensure the directory is accessible only by its owner.

## Docstring

### Summary
Verifies whether a directory is properly isolated to prevent unauthorized access.

### Parameters

- **directory** (STR): Path to the directory being checked for isolation.

### Returns

dict: A dictionary containing a boolean indicating whether the isolated directory is accessible only by the owner, and the directory path being checked.

### Raises

- ValueError: Raised when the input directory path is invalid or the directory does not exist.
- PermissionError: Raised when the shim lacks permission to access the directory being checked for isolation.

### Examples

```python
>>> print(verify_directory_isolation('/home/user/isolated_dir'))
>>> print(verify_directory_isolation('/home/user/public_dir'))
{'output': True, 'directory': '/home/user/isolated_dir'}
{'output': False, 'directory': '/home/user/public_dir'}
```
