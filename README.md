# Python Learning and Practice

A comprehensive collection of Python programs covering fundamental to advanced concepts. This repository documents my learning journey through Python, including core language features, object-oriented programming, GUI development, and multi-threading.

## Overview

This repository contains extensive Python practice code organized by learning progression. It includes practical examples, utilities, games, and small projects that demonstrate various Python concepts and libraries.

## Tech Stack

- **Language**: Python 3.6+
- **Testing Framework**: pytest
- **Linting**: flake8
- **GUI Framework**: tkinter
- **Package Manager**: pip

## Repository Structure

### Core Python Fundamentals
- **Basic I/O and Data Types**: Input/output operations, variables, type conversion
- **Control Flow**: Conditionals, loops, break/continue statements
- **Functions**: Function definition, parameters, return values, decorators
- **Data Structures**: Lists, tuples, dictionaries, sets, comprehensions
- **String Operations**: String manipulation, formatting, regex operations
- **File Handling**: Reading, writing, processing text and data files
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, special methods

### Advanced Topics
- **GUI Development** (`GUI/`): Tkinter applications, event handling, widgets
  - Simple GUI programs
  - Form applications
  - Interactive tools
- **Concurrency** (`Python/`): Threading, multiprocessing examples
- **Utilities**: Helper scripts, tools, utilities

### Nested Learning Structure
- **Python/** - Additional nested practice exercises and experimental code
  - Mirror of core concepts with alternative implementations
  - Additional challenge problems

## Topics Covered

### Fundamental Concepts
- Variables and data types (int, float, str, bool)
- Operators (arithmetic, comparison, logical)
- Control flow (if-elif-else, loops)
- Lists, tuples, dictionaries, sets
- String operations and formatting

### Intermediate Topics
- Functions and scope
- List comprehensions and generators
- Decorators and functional programming
- Exception handling and error management
- File I/O and data persistence

### Advanced Topics
- Object-oriented programming
- Class inheritance and polymorphism
- Magic methods and operator overloading
- Abstract base classes
- Design patterns

### Libraries and Frameworks
- **tkinter**: GUI development and event-driven programming
- **threading/multiprocessing**: Concurrent programming
- **regular expressions**: Pattern matching and text processing
- **collections**: Specialized container data types

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

Clone the repository:
```bash
git clone https://github.com/fizaan-ali/Python.git
cd Python
```

Install dependencies (if needed):
```bash
pip install -r requirements.txt
```

### Running Programs

#### Basic Python Scripts
```bash
python filename.py
```

#### GUI Applications
```bash
python GUI/application_name.py
```

#### Running with Python 3 explicitly
```bash
python3 filename.py
```

## Code Organization

### Root Level
- General Python exercises and fundamental concepts
- Basic programs demonstrating core language features

### GUI Directory
- Tkinter-based GUI applications
- Event handling and widget demonstrations
- Form and dialog examples

### Python Directory
- Nested practice exercises
- Alternative implementations
- Additional challenge problems

## Key Programs

### Fundamental Examples
- Variables and type conversion
- List and dictionary operations
- Loop patterns and control flow
- File I/O operations
- String manipulation

### Object-Oriented Examples
- Class definitions and instantiation
- Inheritance and method overriding
- Encapsulation and data hiding
- Special methods (__init__, __str__, etc.)

### GUI Examples
- Window creation and widgets
- Event handling and callbacks
- Form validation
- File dialogs

## Running Tests

Run all tests with pytest:
```bash
pytest
```

Run tests for a specific directory:
```bash
pytest GUI/
```

Run with verbose output:
```bash
pytest -v
```

## Code Quality

Check code style with flake8:
```bash
flake8 .
```

## Learning Path Recommendation

1. Start with fundamental Python concepts
2. Practice with data structures and built-in functions
3. Learn object-oriented programming principles
4. Explore GUI development with tkinter
5. Experiment with concurrent programming
6. Build small projects combining multiple concepts

## Common Python Patterns

### File Operations
```python
with open('file.txt', 'r') as f:
    content = f.read()
```

### List Comprehensions
```python
squares = [x**2 for x in range(10)]
```

### Class Definition
```python
class MyClass:
    def __init__(self, value):
        self.value = value
```

### Exception Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## License

MIT License - See LICENSE file for details

## Author

Fizaan Ali

