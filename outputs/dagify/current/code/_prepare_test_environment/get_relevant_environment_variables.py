import os
import json


def get_relevant_environment_variables() -> str:
    """
    Extracts relevant environment variables used in the prepare test environment
    node.

    Parameters
    ----------
    input_param : str
        Not applicable, as this is a shim.

    Returns
    -------
    str
        A dictionary of relevant environment variables used in the prepare
        test environment node. It should be in the format of 'key-value'
        pairs, where keys are variable names and values are the
        corresponding values.

    Raises
    ------
    TypeError
        If input is not a string or if the input string is malformed.

    Examples
    --------
    >>> environment_vars = get_relevant_environment_variables()
    '{key1: value1, key2: value2}'

    """
    
    test_relevant_vars = [
        'PATH',
        'PYTHONPATH', 
        'HOME',
        'USER',
        'LANG',
        'LC_ALL',
        'TMPDIR',
        'TMP',
        'TEMP',
        'TEST_ENV',
        'CI',
        'GITHUB_ACTIONS',
        'JENKINS_URL',
        'BUILD_NUMBER',
        'JOB_NAME'
    ]
    
    environment_dict = {}
    
    for var in test_relevant_vars:
        value = os.environ.get(var)
        if value is not None:
            environment_dict[var] = value
    
    for key, value in os.environ.items():
        if ('TEST' in key.upper() or 
            'BUILD' in key.upper() or 
            'CI' in key.upper() or
            key.startswith('PYTEST_') or
            key.startswith('UNITTEST_')):
            environment_dict[key] = value
    
    return json.dumps(environment_dict)