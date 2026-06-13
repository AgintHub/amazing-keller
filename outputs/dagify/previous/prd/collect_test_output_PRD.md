# collect_test_output PRD

## Description
Collects test output and sets test status based on 'TEST_PASSED' presence.


## Conceptual Info

This node parses the test execution output from the execute_test node and assigns a pass/fail status based on whether the 'TEST_PASSED' substring is present. It returns a clean JSON object with test_status and raw_output preserved from the original output.

## Docstring

### Summary
Collects test output and sets test status.

### Parameters

- **raw_output** (str): String supplied by the execute_test node.

### Returns

dict: Dictionary with test_status and raw_output matching the declared output_structure.

### Raises

- ValueError: If the input string is empty or contains only whitespace.

### Examples

```python
>>> parse_test_output('TEST_PASSED
Test Output')
{'test_status': 'PASSED', 'raw_output': 'TEST_PASSED\nTest Output'}
```

```python
>>> parse_test_output('Test Output')
{'test_status': 'FAILED', 'raw_output': 'Test Output'}
```
