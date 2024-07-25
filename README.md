# texttransform

`texttransform` is a simple Python tool designed to:
- Convert sentences to uppercase or lowercase.
- Properly format sentences by capitalizing the first letter of each sentence and handling ellipses correctly.

This tool was developed as a learning exercise to explore how to package Python scripts into downloadable executables that others can use. Additionally, it’s a handy solution for those times when I accidentally type entire paragraphs in uppercase before realizing I've made a major text blunder.


## Features
- **Convert**: Change text to uppercase or lowercase.
- **Format**: Properly capitalize sentences and handle ellipses.

## Installation
You can install `texttransform` in two ways:

### From PyPI

To install the latest version of `texttransform` from PyPI, use the following command:

```bash
pip install texttransform
```

You can find the package on PyPI [here](https://pypi.org/project/texttransform/).

### From Local Source

To install texttransform from the local source, follow these steps:

1. Navigate to the directory containing the setup.py file:

```bash
cd path/to/directory
```

2. Run the following command to install the package:

```bash
pip install .
```

This will install the package from the local source directory.

## Usage
After installation, you can use the texttransform command-line tool to perform various text transformations.

### Convert to Uppercase
```bash
texttransform -upper "your text here"
```

### Convert to Lowercase
```bash
texttransform -lower "YOUR TEXT HERE"
```

### Format Sentences
```bash
texttransform -sentence "your text here. another sentence here."
```

### Example
```bash
texttransform -sentence "hello. world. this is an example..."
```

#### Output:
```bash
Hello. World. This is an example...
```

## Running Tests
To run the tests for texttransform, use:

```bash
python -m unittest text_transform_test.py
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Genevieve - [GitHub Profile](https://github.com/Genevieveok/)

