# Scientific Calculator Design Guide

## 1. Recommended File Structure

```text
Scientific_Calculator/
├── README.md
├── DESIGN_GUIDE.md
├── calculator/
│   ├── __init__.py
│   ├── core.py
│   ├── expression.py
│   ├── equation.py
│   ├── parser.py
│   └── utils.py
├── main.py
├── requirements.txt
└── tests/
    ├── test_core.py
    ├── test_expression.py
    ├── test_equation.py
    └── test_parser.py
```

## 2. Purpose of Each File

- `README.md`
  - Project overview, install/run instructions, examples.
- `DESIGN_GUIDE.md`
  - Architecture, file structure, and class responsibilities.
- `calculator/__init__.py`
  - Exposes the public calculator API.
- `calculator/core.py`
  - Implements basic arithmetic and scientific operations.
- `calculator/expression.py`
  - Defines expression-related objects and evaluation logic.
- `calculator/equation.py`
  - Defines equation solving workflows and related classes.
- `calculator/parser.py`
  - Parses text input into expression and equation objects.
- `calculator/utils.py`
  - Shared helper functions and constants.
- `main.py`
  - CLI or REPL entry point for interactive usage.
- `requirements.txt`
  - Third-party dependencies, if any.
- `tests/`
  - Unit tests for core logic, expression handling, equation solving, and parsing.

## 3. Core Classes

### 3.1 `ScientificCalculator`

This class ties the whole calculator together and exposes convenience methods.

```python
class ScientificCalculator:
    def __init__(self):
        self.core = CalculatorCore()
        self.parser = ExpressionParser()
        self.equation_solver = EquationSolver()

    def evaluate(self, input_text: str):
        node = self.parser.parse(input_text)
        return node.evaluate(self.core)

    def solve(self, input_text: str):
        equation = self.parser.parse_equation(input_text)
        return self.equation_solver.solve(equation, self.core)
```

### 3.2 `CalculatorCore`

Contains actual numeric and scientific operations.

```python
class CalculatorCore:
    def add(self, a, b):
        pass

    def subtract(self, a, b):
        pass

    def multiply(self, a, b):
        pass

    def divide(self, a, b):
        pass

    def power(self, base, exponent):
        pass

    def sqrt(self, x):
        pass

    def factorial(self, n):
        pass

    def logarithm(self, x, base=10):
        pass

    def natural_log(self, x):
        pass

    def sine(self, x, degrees=False):
        pass

    def cosine(self, x, degrees=False):
        pass

    def tangent(self, x, degrees=False):
        pass
```

### 3.3 `Expression`

Represents a mathematical expression tree.

```python
class Expression:
    def evaluate(self, core: CalculatorCore):
        raise NotImplementedError
```

Subclasses include:

- `NumberExpression`
- `BinaryExpression`
- `UnaryExpression`
- `FunctionExpression`
- `VariableExpression`

Example:

```python
class BinaryExpression(Expression):
    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self, core: CalculatorCore):
        left_value = self.left.evaluate(core)
        right_value = self.right.evaluate(core)
        if self.operator == '+':
            return core.add(left_value, right_value)
        if self.operator == '-':
            return core.subtract(left_value, right_value)
        if self.operator == '*':
            return core.multiply(left_value, right_value)
        if self.operator == '/':
            return core.divide(left_value, right_value)
        if self.operator == '^':
            return core.power(left_value, right_value)
        raise ValueError(f"Unknown operator: {self.operator}")
```

### 3.4 `Equation`

Models equations for solving.

```python
class Equation:
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def residual(self, core: CalculatorCore, x_value):
        return self.left.evaluate(core, x_value) - self.right.evaluate(core, x_value)
```

Possible equation subclasses:

- `LinearEquation`
- `QuadraticEquation`
- `NonlinearEquation`

### 3.5 `EquationSolver`

Solves equations using appropriate methods.

```python
class EquationSolver:
    def solve(self, equation: Equation, core: CalculatorCore):
        pass
```

Possible solver methods:

- `solve_linear(equation)`
- `solve_quadratic(equation)`
- `solve_nonlinear(equation)`

## 4. Supporting Classes and Functions

### 4.1 `ExpressionParser`

Parses text into expression trees or equation objects.

```python
class ExpressionParser:
    def parse(self, text: str) -> Expression:
        pass

    def parse_equation(self, text: str) -> Equation:
        pass
```

### 4.2 `Token` and `Tokenizer`

If you build a parser, define token objects for numbers, operators, functions, parentheses, variables, and equality signs.

### 4.3 Utility Functions in `utils.py`

- `is_number(value)`
- `to_radians(value, degrees)`
- `safe_divide(a, b)`
- `format_number(value)`
- `validate_integer(n)`

## 5. Example Class Responsibilities

### `calculator/core.py`
- arithmetic and scientific operations
- angle mode conversion
- constants like `PI` and `E`

### `calculator/expression.py`
- expression tree node classes
- evaluation logic for operators and functions
- variable handling for expressions like `x^2 + 3x`

### `calculator/equation.py`
- equation representation
- solver selection logic
- specialized solvers for linear, quadratic, and numeric methods

### `calculator/parser.py`
- tokenization of input text
- converting tokens into expression/equation objects
- support for parentheses, unary minus, and function calls

### `calculator/utils.py`
- reusable helpers and validation
- error formatting and safe numeric conversion

## 6. Example Usage Scenarios

- Evaluate an expression:
  - `2 + 3 * 4`
  - `sin(30) + log(100)`
- Solve an equation:
  - `2*x + 5 = 13`
  - `x^2 - 5*x + 6 = 0`
- Evaluate a function expression:
  - `sqrt(25) + 2^3`

## 7. Suggested Test Coverage

- `test_core.py`
  - arithmetic and scientific operation correctness
  - divide-by-zero and invalid input handling
- `test_expression.py`
  - expression parsing and evaluation
  - operator precedence and associativity
- `test_equation.py`
  - solving linear and quadratic equations
  - checking numeric solver results
- `test_parser.py`
  - tokenization and parse tree structure
  - invalid syntax detection

## 8. Starting Implementation Plan

1. Create `calculator/core.py` and implement `CalculatorCore`.
2. Define expression node classes in `calculator/expression.py`.
3. Add parser scaffolding in `calculator/parser.py`.
4. Implement equation modeling and solvers in `calculator/equation.py`.
5. Build `main.py` for CLI input, evaluation, and solving.
6. Add tests in `tests/` and validate behavior.

## 9. Notes

- Keep expression evaluation separate from numeric operations so the calculator is easier to extend.
- Use equation classes only when you need solveable forms like `left = right`.
- Use a parser to convert user text into structured objects instead of evaluating raw strings directly.
