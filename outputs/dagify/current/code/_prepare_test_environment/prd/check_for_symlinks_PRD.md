# check_for_symlinks PRD

## Description
Checks if a directory contains symlinks.


## Conceptual Info

This shim checks whether a given directory contains symlinks, enabling comprehensive preparation of isolated environments for testing and development purposes.

## Docstring

### Summary
Checks if a directory contains symlinks.

### Parameters

- **directory** (STR): The absolute path of the directory to check for symlinks.

### Returns

dict: A dictionary containing the output and directory, where output is a boolean indicating the presence of symlinks and directory is the input path.

### Raises

- ValueError: Raised when the input directory path is invalid or not a string.
- TypeError: Raised when the input directory path is not a string.

### Examples

```python
>>> check_for_symlinks(directory='/path/to/valid/directory')
{'output': False, 'directory': '/path/to/valid/directory'}
```

```python
>>> check_for_symlinks(directory='/path/to/directory/with/symlinks')
{'output': True, 'directory': '/path/to/directory/with/symlinks'}
```
