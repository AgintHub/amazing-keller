from ._summarize_test_results.format_test_summary import format_test_summary

from pydantic import BaseModel, Field


class CollectTestOutputOutput(BaseModel):
    """Pydantic model for collect_test_output node outputs."""
    test_status: str = (
        Field(..., description = (
            "Literal string indicating the test status, either "PASSED" or "FAILED"")
        )
    )
    raw_output: str = (
        Field(..., description = (
            "Original captured output string, preserved exactly as received")
        )
    )


class SummarizeTestResultsOutput(BaseModel):
    """Pydantic model for summarize_test_results node outputs."""
    summary: str = (
        Field(..., description = (
            "A single paragraph that states the test outcome, includes the exact raw output wrapped in backticks, and is formatted for clear, standalone logging or display.")
        )
    )


def summarize_test_results(collect_test_output_input: CollectTestOutputOutput, **kwargs) -> SummarizeTestResultsOutput:
    """
    Generate a concise summary of test execution results.

    Parameters
    ----------
    raw_output : str
        Raw output string from the collect_test_output node, including test
        status and any output content.

    Returns
    -------
    str
        Human-readable summary of test execution results, including the
        exact raw_output value wrapped in backticks.

    Raises
    ------
    ValueError
        If raw_output is not a valid JSON string or test_status is neither
        'PASSED' nor 'FAILED'.

    Examples
    --------
    >>> summarize_test_results('TEST_PASSED
This is a test report.')
    Pass: 'TEST_PASSED
    This is a test report.'

    """
    test_status = collect_test_output_input.test_status
    raw_output = collect_test_output_input.raw_output
    
    formatted_summary: str = format_test_summary(
        test_status=test_status,
        raw_output=raw_output
    )
    
    return SummarizeTestResultsOutput(
        summary=formatted_summary
    )