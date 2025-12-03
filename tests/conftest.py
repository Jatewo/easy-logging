import logging
import pytest
from easy_logging_formatter.config import FormatterConfig


@pytest.fixture
def base_config() -> FormatterConfig:
    """Create a fresh configuration object for each test.

    Returns:
        FormatterConfig: A new configuration object.

    """
    return FormatterConfig()


@pytest.fixture
def log_record() -> logging.LogRecord:
    """Create a standard Python LogRecord.

    This simulates what the logging system generates when you call logger.info(...)

    Returns:
        logging.LogRecord: A LogRecord object.

    """
    record = logging.LogRecord(
        name="test_logger",
        level=logging.INFO,
        pathname="/path/to/project/src/main.py",
        lineno=42,
        msg="This is a test message",
        args=(),
        exc_info=None,
    )
    return record
