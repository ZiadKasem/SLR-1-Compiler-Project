
---

# SLR(1) Parser

A Python implementation of an SLR(1) parser with a graphical user interface (GUI) using Tkinter.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

SLR(1) parser is a parsing technique used in compiler construction to parse context-free grammars. This project provides a Python implementation of an SLR(1) parser with a graphical user interface built using Tkinter.

## Features

- **SLR(1) Parsing**: Implements the SLR(1) parsing algorithm.
- **Graphical User Interface**: Provides a user-friendly interface for inputting statements, tokenizing them, drawing parse trees, and displaying the parse table.
- **Grammar Augmentation**: Augments the grammar to handle start symbols and closures.
- **Parse Table Generation**: Automatically generates the parse table for the given grammar.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/slr-parser.git
    ```

2. Navigate to the project directory:

    ```bash
    cd slr-parser
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:

    ```bash
    python main.py
    ```

2. Enter statements in the provided input field.

3. Click on the "Tokenize" button to tokenize the input.

4. Click on the "Draw parse tree" button to draw the parse tree.

5. Click on the "Show parse table" button to display the parse table.

6. Click on the "Show stack content" button to view the stack content.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
