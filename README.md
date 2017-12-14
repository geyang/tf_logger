# TF_Logger, A Logging Utility for Python Debugging

## Todo

### Done

## Installation

```bash
pip install loggers
```

## Usage

```python
from tf_logger import TF_Logger

logger = TF_Logger(log_directory="/tmp/logs/tf_logger_test/")

logger.log(index=3, note='this is a log entry!')
logger.flush()
```
