# 🧮 CLI Calculator

A simple command-line calculator app built with Python that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nitinkumar30/python-cli-calculator/.github%2Fworkflows%2Frun_tests.yml?branch=main&style=plastic)
---

## 🚀 Features

- Command-line interface using `argparse`
- Supports:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with zero-division check)
- Test suite included using `unittest`

---

## 📁 Files used

1. [calc.py](calc.py)
2. [test_calc.py](test_calc.py)

---

## 🛠️ Requirements

- Python 3.6 or higher

---

## 📦 Installation

Clone the repository:


```bash
git clone https://github.com/nitinkumar30/python-cli-calculator.git
cd python-cli-calculator
```

---

## 🧾 Usage

Run the CLI calculator using the command below:

```bash
python calc.py <operation> <x> <y>
```

Replace `<operation>` with one of the following:

### ✅ Supported Operations

| Operation | Description     | Example                        | Output |
|-----------|-----------------|--------------------------------|--------|
| `add`     | Addition         | `python calc.py add 5 3`       | `8.0`  |
| `sub`     | Subtraction      | `python calc.py sub 10 4`      | `6.0`  |
| `mul`     | Multiplication   | `python calc.py mul 2 3`       | `6.0`  |
| `div`     | Division         | `python calc.py div 9 3`       | `3.0`  |

> ⚠️ Division by zero is handled and will output an error message: `Error: Division by zero`

---

## ✅ Running Tests

Run the test suite using:

```bash
python test_calc.py
```

Expected output:

```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.3s

OK
```

---

💻 Author 

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)
