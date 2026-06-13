# summarize_test_results PRD

## Description
Creates a human-readable summary of test execution results, preserving formatting, by including the exact raw output wrapped in backticks.


## Conceptual Info

Process raw output from the collect_test_output node to produce a human-readable summary with the exact raw_output value.

## Docstring

### Summary
Generate a concise summary of test execution results.

### Parameters

- **raw_output** (str): Raw output string from the collect_test_output node, including test status and any output content.

### Returns

str: Human-readable summary of test execution results, including the exact raw_output value wrapped in backticks.

### Raises

- ValueError: If raw_output is not a valid JSON string or test_status is neither 'PASSED' nor 'FAILED'.

### Examples

```python
>>> summarize_test_results('TEST_PASSED
This is a test report.')
Pass: 'TEST_PASSED
This is a test report.'
```
