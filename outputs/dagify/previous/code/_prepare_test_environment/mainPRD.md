# _prepare_test_environment - Complete PRD Documentation

## Overview
PRDs for nodes in the '_prepare_test_environment' module.

## Table of Contents

- [create_unique_temp_directory](#create_unique_temp_directory)

- [get_absolute_path](#get_absolute_path)

- [verify_utility_availability](#verify_utility_availability)

- [check_directory_permissions](#check_directory_permissions)

- [verify_directory_isolation](#verify_directory_isolation)

- [check_for_symlinks](#check_for_symlinks)

- [get_relevant_environment_variables](#get_relevant_environment_variables)

- [generate_environment_summary](#generate_environment_summary)



---

## create_unique_temp_directory

### Description
Creates a typed node for generating a unique temporary directory

### Conceptual Info

This shim node creates a unique temporary directory for preparation of the test environment.

### Docstring

**Summary:** Creates a unique temporary directory

**Parameters:**

- input_params (dict): Input parameters for the shim
**Returns:** str - The path to the created unique temporary directory

**Raises:**

- ValueError: When input validation fails
- TypeError: When input types are incorrect
**Examples:**

```python
>>> temp_dir_path = create_unique_temp_directory()
Absolute path of a unique temporary directory
```

```python
>>> temp_dir_path = create_unique_temp_directory(input_params={'foo': 'bar'})
Absolute path of a unique temporary directory with 'bar'
```



---

## get_absolute_path

### Description
Retrieve the absolute path of a given directory or file.

### Conceptual Info

A shim responsible for obtaining the absolute path of a given directory or file.

### Docstring

**Summary:** Obtain the absolute path of a directory or file.

**Parameters:**

- path (str): The path for which the absolute path is to be retrieved.
**Returns:** STR - The absolute path of the directory or file.

**Raises:**

- ValueError: When the input path does not exist or is invalid.
- TypeError: When the input path is not a string.
**Examples:**

```python
>>> get_absolute_path('/home/user')
/home/user
```

```python
>>> get_absolute_path('./current_directory')
/current_directory
```



---

## verify_utility_availability

### Description
Verifies the availability of a utility on the system by checking its absolute path.

### Conceptual Info

The shim verifies the presence of a system utility by checking its absolute path.

### Docstring

**Summary:** Verifies a system utility by checking its existence at a specific path.

**Parameters:**

- utility (str): The name of the utility to verify (e.g., `echo`, `ls`, `mkdir`).
**Returns:** dict - A dictionary containing the utility name and its absolute path if found, otherwise `None` for the utility.

**Raises:**

- ValueError: When the utility is not found or an error occurs while checking its presence.
- TypeError: When the input type is incorrect or the utility name is invalid.
**Examples:**

```python
>>> verify_utility_availability(utility='echo')
>>> verify_utility_availability(utility='non-existent-utility')
{'output': '/bin/echo', 'utility': 'echo'}
None
```



---

## check_directory_permissions

### Description
Verifies the mode of a given directory and returns its mode as a string.

### Conceptual Info

The shim `check_directory_permissions` is used to validate directory permissions and provide its mode as a string.

### Docstring

**Summary:** Checks the directory permissions of a given directory.

**Parameters:**

- directory (str): Path to the directory to check.
**Returns:** str - Mode of the directory as a string.

**Raises:**

- ValueError: When the directory path is invalid.
- TypeError: When the input type is incorrect.
**Examples:**

```python
>>> check_directory_permissions('/path/to/directory')
'0700'
```

```python
>>> check_directory_permissions('/another/directory')
'another_mode'
```



---

## verify_directory_isolation

### Description
Verifies whether the directory is properly isolated to prevent unauthorized access.

### Conceptual Info

This shim verifies directory isolation to ensure the directory is accessible only by its owner.

### Docstring

**Summary:** Verifies whether a directory is properly isolated to prevent unauthorized access.

**Parameters:**

- directory (STR): Path to the directory being checked for isolation.
**Returns:** dict - A dictionary containing a boolean indicating whether the isolated directory is accessible only by the owner, and the directory path being checked.

**Raises:**

- ValueError: Raised when the input directory path is invalid or the directory does not exist.
- PermissionError: Raised when the shim lacks permission to access the directory being checked for isolation.
**Examples:**

```python
>>> print(verify_directory_isolation('/home/user/isolated_dir'))
>>> print(verify_directory_isolation('/home/user/public_dir'))
{'output': True, 'directory': '/home/user/isolated_dir'}
{'output': False, 'directory': '/home/user/public_dir'}
```



---

## check_for_symlinks

### Description
Checks if a directory contains symlinks.

### Conceptual Info

This shim checks whether a given directory contains symlinks, enabling comprehensive preparation of isolated environments for testing and development purposes.

### Docstring

**Summary:** Checks if a directory contains symlinks.

**Parameters:**

- directory (STR): The absolute path of the directory to check for symlinks.
**Returns:** dict - A dictionary containing the output and directory, where output is a boolean indicating the presence of symlinks and directory is the input path.

**Raises:**

- ValueError: Raised when the input directory path is invalid or not a string.
- TypeError: Raised when the input directory path is not a string.
**Examples:**

```python
>>> check_for_symlinks(directory='/path/to/valid/directory')
{'output': False, 'directory': '/path/to/valid/directory'}
```

```python
>>> check_for_symlinks(directory='/path/to/directory/with/symlinks')
{'output': True, 'directory': '/path/to/directory/with/symlinks'}
```



---

## get_relevant_environment_variables

### Description
Returns a dictionary of relevant environment variables used in the prepare test environment node.

### Conceptual Info

This shim is a typed node for extracting relevant environment variables used in the prepare test environment node.

### Docstring

**Summary:** Extracts relevant environment variables used in the prepare test environment node.

**Parameters:**

- input_param (str): Not applicable, as this is a shim.
**Returns:** str - A dictionary of relevant environment variables used in the prepare test environment node. It should be in the format of 'key-value' pairs, where keys are variable names and values are the corresponding values.

**Raises:**

- TypeError: If input is not a string or if the input string is malformed.
**Examples:**

```python
>>> environment_vars = get_relevant_environment_variables()
'{key1: value1, key2: value2}'
```



---

## generate_environment_summary

### Description
Generates a summary of the environment setup, including success/failure status for each check and relevant environment variables.

### Conceptual Info

This shim generates a summary of the environment setup, including success/failure status for each check and relevant environment variables.

### Docstring

**Summary:** Generates a summary of the environment setup.

**Parameters:**

- env_dir (str): The absolute path of the isolated temporary directory.
- utils_ok (str): Whether the essential system utilities are verified and available.
- permissions_ok (str): Whether the new directory has mode `0700` and is isolated.
- symlinks_ok (str): Whether the new directory contains no symlinks.
- env_vars (str): Relevant environment variables.
**Returns:** str - A string containing the environment summary, including success/failure status for each check and relevant environment variables.

**Raises:**

- ValueError: When the input parameters do not match the expected format.
- TypeError: When the input parameters are of the wrong type.
**Examples:**

```python
>>> env_dir_absolute = get_absolute_path(temp_dir_path)
>>> utils_available = verify_utility_availability('echo')
>>> permissions_valid = check_directory_permissions(directory=env_dir_absolute)
>>> symlinks_valid = not has_symlinks
>>> environment_vars = get_relevant_environment_variables()
>>> generate_environment_summary(env_dir=env_dir_absolute, "
              "utils_ok=bool(utils_available), permissions_ok=permissions_valid, "
              "symlinks_ok=symlinks_valid, env_vars=environment_vars)
A string containing the environment summary.
```

