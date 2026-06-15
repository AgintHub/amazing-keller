# format_test_summary PRD

## Description
A typed node for generating a concise summary of test execution results based on raw output and test status.


## Conceptual Info

The format_test_summary node generates a concise summary of test execution results, including raw output and test status.

## Docstring

### Summary
Generate a concise summary of test execution results.

### Parameters

- **test_status** (str): Literal string indicating the test status, either 'PASSED' or 'FAILED'.
- **raw_output** (str): Raw output string from the collect_test_output node, including test status and any output content.

### Returns

str: Formatted summary of test execution results, including raw output wrapped in backticks and test status.

### Raises

- ValueError: When raw_output is not a valid JSON string or test_status is neither 'PASSED' nor 'FAILED'.

### Examples

```python
>>> formatted_summary = format_test_summary('PASSED', 'TEST_PASSED\nThis is a test report.')
>>> print(formatted_summary)
Pass: 'TEST_PASSED\nThis is a test report.'
```

```python
>>> formatted_summary = format_test_summary('FAILED', 'TEST_FAILED\nThis is a test report.')
>>> print(formatted_summary)
Fail: 'TEST_FAILED\nThis is a test report.'
```
