# Yolo: Streamlined Python Testing and Execution

## Introduction

`yolo` is a Python module that enhances the efficiency of running and testing
Python code. With its user-friendly interface, `yolo` allows for easy
execution of test functions, customizable logging, and output formatting,
making it a valuable tool for Python developers.

## Features

- **Easy Execution:** Run your test functions with minimal setup.
- **Customizable Logging:** Direct logs to your desired filepath.
- **Flexible Output Formatting:** Define how you want to see your standard
  output.

## Installation

```
pip install yolo
```

## Usage

### Standard Use

```python
from yolo import Yolo


def main() -> None:
  """Some test code"""


with Yolo(main) as yolo:
  yolo.log('path/to/logfile')  # Optional
yolo.out(...)  # Define output format
yolo.run()
```

### Shorthand Use

```python
from yolo import Yolo


def main() -> None:
  """Function wrapping the testing code"""


outFormat = 'Normal'  # Style specification of output

with Yolo(main) as yolo:
  yolo('path/to/logfile', outFormat)
```

## Contributing

Contributions are welcome! Please read
our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
