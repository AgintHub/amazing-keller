# basic_test_workflow - Complete PRD Documentation

## Overview
PRDs for nodes in the 'basic_test_workflow' module.

## Table of Contents

- [prepare_test_environment](#prepare_test_environment)

- [execute_test](#execute_test)

- [collect_test_output](#collect_test_output)

- [summarize_test_results](#summarize_test_results)



---

## prepare_test_environment

### Description
Creates an isolated temporary directory for testing, verifies that essential system utilities are available, and records all necessary information to enable safe cleanup. Returns a JSON object with fields `env_dir`, `utils_ok`, `permissions_ok`, `symlinks_ok`, `cleanup_command`, and a summary of the environment setup.

### Conceptual Info

This node sets up an isolated temporary directory for testing by creating a unique directory, verifying the availability and executability of essential system utilities, checking directory permissions and symlinks, and recording the results. It then generates a cleanup command and returns a structured summary of the environment setup.

### Docstring

**Summary:** Setup isolated temporary directory and verify utilities for testing.

**Parameters:**

- current_working_directory (str): The current working directory where the temporary directory will be created.
**Returns:** dict - Dictionary containing the declared output fields.

**Raises:**

- ValueError: If an input is invalid or cannot be resolved.
**Examples:**

```python
>>> import os
>>> import tempfile
>>> import which
>>> import pwd
>>> import grp
>>> import stat
{'env_dir': '/tmp/test_env.XXXXXX', 'utils_ok': True, 'permissions_ok': True, 'symlinks_ok': True, 'cleanup_command': 'rm -rf /tmp/test_env.XXXXXX', 'summary': 'Environment setup successful.'}
```



---

## execute_test

### Description
Runs a deterministic echo command inside the isolated test environment, captures its exact standard output—including the trailing newline—and validates it against the predefined expected string.

### Conceptual Info

Validate the exact output of a deterministic echo command inside a prepared isolated environment against a predefined expected string.

### Docstring

**Summary:** Run a deterministic echo command and validate its output.

**Parameters:**

- env_dir (str): AbsolutePath to the isolated test environment directory.
- expected_string (str): Predefined expected string to be validated against the command’s standard output.
**Returns:** dict - Dictionary containing the declared output fields: `raw_output` and `passed`.

**Raises:**

- ValueError: If the environment directory is unavailable or the expected string is empty.
**Examples:**

```python
>>> execute_test(env_dir='/test/env', expected_string='TEST_PASSED')
{'raw_output': 'TEST_PASSED\n', 'passed': True}
```



---

## collect_test_output

### Description
Collects test output and sets test status based on 'TEST_PASSED' presence.

### Conceptual Info

This node parses the test execution output from the execute_test node and assigns a pass/fail status based on whether the 'TEST_PASSED' substring is present. It returns a clean JSON object with test_status and raw_output preserved from the original output.

### Docstring

**Summary:** Collects test output and sets test status.

**Parameters:**

- raw_output (str): String supplied by the execute_test node.
**Returns:** dict - Dictionary with test_status and raw_output matching the declared output_structure.

**Raises:**

- ValueError: If the input string is empty or contains only whitespace.
**Examples:**

```python
>>> parse_test_output('TEST_PASSED
Test Output')
{'test_status': 'PASSED', 'raw_output': 'TEST_PASSED\nTest Output'}
```

```python
>>> parse_test_output('Test Output')
{'test_status': 'FAILED', 'raw_output': 'Test Output'}
```



---

## summarize_test_results

### Description
Creates a human-readable summary of test execution results, preserving formatting, by including the exact raw output wrapped in backticks.

### Conceptual Info

Process raw output from the collect_test_output node to produce a human-readable summary with the exact raw_output value.

### Docstring

**Summary:** Generate a concise summary of test execution results.

**Parameters:**

- raw_output (str): Raw output string from the collect_test_output node, including test status and any output content.
**Returns:** str - Human-readable summary of test execution results, including the exact raw_output value wrapped in backticks.

**Raises:**

- ValueError: If raw_output is not a valid JSON string or test_status is neither 'PASSED' nor 'FAILED'.
**Examples:**

```python
>>> summarize_test_results('TEST_PASSED
This is a test report.')
Pass: 'TEST_PASSED
This is a test report.'
```

