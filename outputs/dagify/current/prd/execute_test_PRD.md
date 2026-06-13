# execute_test PRD

## Description
Runs a deterministic echo command inside the isolated test environment, captures its exact standard output—including the trailing newline—and validates it against the predefined expected string.


## Conceptual Info

Validate the exact output of a deterministic echo command inside a prepared isolated environment against a predefined expected string.

## Docstring

### Summary
Run a deterministic echo command and validate its output.

### Parameters

- **env_dir** (str): AbsolutePath to the isolated test environment directory.
- **expected_string** (str): Predefined expected string to be validated against the command’s standard output.

### Returns

dict: Dictionary containing the declared output fields: `raw_output` and `passed`.

### Raises

- ValueError: If the environment directory is unavailable or the expected string is empty.

### Examples

```python
>>> execute_test(env_dir='/test/env', expected_string='TEST_PASSED')
{'raw_output': 'TEST_PASSED\n', 'passed': True}
```
