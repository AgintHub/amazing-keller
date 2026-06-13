# check_directory_permissions PRD

## Description
Verifies the mode of a given directory and returns its mode as a string.


## Conceptual Info

The shim `check_directory_permissions` is used to validate directory permissions and provide its mode as a string.

## Docstring

### Summary
Checks the directory permissions of a given directory.

### Parameters

- **directory** (str): Path to the directory to check.

### Returns

str: Mode of the directory as a string.

### Raises

- ValueError: When the directory path is invalid.
- TypeError: When the input type is incorrect.

### Examples

```python
>>> check_directory_permissions('/path/to/directory')
'0700'
```

```python
>>> check_directory_permissions('/another/directory')
'another_mode'
```
