# 🧮 Advanced String-Based Calculator

This is a Python-based **string expression calculator** that evaluates complex arithmetic expressions, including support for:

* Aliases (e.g., `add`, `sub`, `mul`)
* Nested expressions using parentheses
* Operator precedence
* Unary and binary operations


## 📦 Features

* ✅ Handles nested expressions like `- (2 pow (3 sub 4))`
* ✅ Supports both symbols and aliases: `+`, `add`, `^`, `pow`, etc.
* ✅ Unary operations like `-5`
* ✅ Validates input and catches errors like division by zero or mismatched parentheses
* ✅ Supports integers and floating-point numbers


## 🔧 Supported Operators

| Alias | Symbol | Operation      |
| ----- | ------ | -------------- |
| add   | `+`    | Addition       |
| sub   | `-`    | Subtraction    |
| mul   | `*`    | Multiplication |
| div   | `/`    | Division       |
| mod   | `%`    | Modulo         |
| pow   | `^`    | Exponentiation |



## 🧑‍💻 How It Works

### 1. **Parenthesis Validity**

User input is varified via `pre_parse()` through `coordinate()`.

### 2. **Input Parsing**

User input is tokenized and validated via `get_next()` and `parse()`.

### 3. **Expression Structuring**

Flat expressions are converted into nested lists using operator precedence via `struct()`.

### 4. **Evaluation**

Nested expressions are recursively evaluated using `eval()` and `calc()`.



## 🚀 Example Usage


### Sample Inputs

```bash
add 5 3
1+2mod3+4
2*(3 + 4)
- (2 pow (3 sub 4))
2 pow 3
-sub 10 4
```

### Sample Outputs

```bash
8
7
Error: Not matching parenthesis
-0.5
8
Error: Invalid operator "-sub"
```

*Important Point: It is easy for both user and code to write the experssion like `5+3*2` or `5add3mul2` as the code re-structure this*


## 🛠️ Project Structure

* `calc()`  – Performs arithmetic operations
* `eval()` – Recursively evaluates expressions
* `get_next()` – Parses next token from string
* `struct()` – Structures expression based on operator precedence
* `parse()` – Converts input string into a nested list
* `coordinate()` – Entry point that handles exceptions and coordinates parsing and evaluation



## ⚠️ Error Handling

* Division by zero
* Invalid operators or inputs
* Mismatched parentheses
* Unsupported expressions like `add(3,)` or `(div 4)`



## 🌐 Visit

- Access the code through link:
https://replit.com/@waleed-repl/python-projects#String-Based%20Calculator/


## 📜 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).