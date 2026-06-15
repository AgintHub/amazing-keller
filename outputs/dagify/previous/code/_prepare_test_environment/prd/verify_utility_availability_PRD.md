# verify_utility_availability PRD

## Description
Verifies the availability of a utility on the system by checking its absolute path.


## Conceptual Info

The shim verifies the presence of a system utility by checking its absolute path.

## Docstring

### Summary
Verifies a system utility by checking its existence at a specific path.

### Parameters

- **utility** (str): The name of the utility to verify (e.g., `echo`, `ls`, `mkdir`).

### Returns

dict: A dictionary containing the utility name and its absolute path if found, otherwise `None` for the utility.

### Raises

- ValueError: When the utility is not found or an error occurs while checking its presence.
- TypeError: When the input type is incorrect or the utility name is invalid.

### Examples

```python
>>> verify_utility_availability(utility='echo')
>>> verify_utility_availability(utility='non-existent-utility')
{'output': '/bin/echo', 'utility': 'echo'}
None
```
