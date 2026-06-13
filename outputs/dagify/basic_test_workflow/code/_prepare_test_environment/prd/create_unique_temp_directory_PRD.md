# create_unique_temp_directory PRD

## Description
Creates a typed node for generating a unique temporary directory


## Conceptual Info

This shim node creates a unique temporary directory for preparation of the test environment.

## Docstring

### Summary
Creates a unique temporary directory

### Parameters

- **input_params** (dict): Input parameters for the shim

### Returns

str: The path to the created unique temporary directory

### Raises

- ValueError: When input validation fails
- TypeError: When input types are incorrect

### Examples

```python
>>> temp_dir_path = create_unique_temp_directory()
Absolute path of a unique temporary directory
```

```python
>>> temp_dir_path = create_unique_temp_directory(input_params={'foo': 'bar'})
Absolute path of a unique temporary directory with 'bar'
```
