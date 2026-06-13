# get_absolute_path PRD

## Description
Retrieve the absolute path of a given directory or file.


## Conceptual Info

A shim responsible for obtaining the absolute path of a given directory or file.

## Docstring

### Summary
Obtain the absolute path of a directory or file.

### Parameters

- **path** (str): The path for which the absolute path is to be retrieved.

### Returns

STR: The absolute path of the directory or file.

### Raises

- ValueError: When the input path does not exist or is invalid.
- TypeError: When the input path is not a string.

### Examples

```python
>>> get_absolute_path('/home/user')
/home/user
```

```python
>>> get_absolute_path('./current_directory')
/current_directory
```
