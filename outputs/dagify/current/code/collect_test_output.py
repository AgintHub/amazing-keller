from pydantic import BaseModel, Field


class ExecuteTestOutput(BaseModel):
    """Pydantic model for execute_test node outputs."""
    raw_output: str = (
        Field(..., description="The command\u2019s standard output, including any trailing newline.")
    )
    passed: bool = (
        Field(..., description="Whether the output matched the expectation.")
    )


class CollectTestOutputOutput(BaseModel):
    """Pydantic model for collect_test_output node outputs."""
    test_status: str = (
        Field(..., description="Literal string indicating the test status, either \"PASSED\" or \"FAILED\"")
    )
    raw_output: str = (
        Field(..., description="Original captured output string, preserved exactly as received")
    )


def collect_test_output(execute_test_input: ExecuteTestOutput, **kwargs) -> CollectTestOutputOutput:
    """
    Collects test output and sets test status.

    Parameters
    ----------
    raw_output : str
        String supplied by the execute_test node.

    Returns
    -------
    dict
        Dictionary with test_status and raw_output matching the declared
        output_structure.

    Raises
    ------
    ValueError
        If the input string is empty or contains only whitespace.

    Examples
    --------
    >>> parse_test_output('TEST_PASSED
Test Output')
    {'test_status': 'PASSED', 'raw_output': 'TEST_PASSED\nTest Output'}

    >>> parse_test_output('Test Output')
    {'test_status': 'FAILED', 'raw_output': 'Test Output'}

    """
    return CollectTestOutputOutput(
        test_status="",
        raw_output="",
    )