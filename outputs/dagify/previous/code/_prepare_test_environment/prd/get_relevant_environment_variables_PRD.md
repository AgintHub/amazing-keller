# get_relevant_environment_variables PRD

## Description
Returns a dictionary of relevant environment variables used in the prepare test environment node.


## Conceptual Info

This shim is a typed node for extracting relevant environment variables used in the prepare test environment node.

## Docstring

### Summary
Extracts relevant environment variables used in the prepare test environment node.

### Parameters

- **input_param** (str): Not applicable, as this is a shim.

### Returns

str: A dictionary of relevant environment variables used in the prepare test environment node. It should be in the format of 'key-value' pairs, where keys are variable names and values are the corresponding values.

### Raises

- TypeError: If input is not a string or if the input string is malformed.

### Examples

```python
>>> environment_vars = get_relevant_environment_variables()
'{key1: value1, key2: value2}'
```
