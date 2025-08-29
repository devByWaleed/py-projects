# 🔁 Loop Calculator 🧮

## 📖 Overview

Loop Calculator is a simple **console-based calculator** application written in **Python 🐍**.
It allows users to perform **basic arithmetic operations** — ➕ addition, ➖ subtraction, ✖ multiplication, and ➗ division — on multiple numbers.

The calculator runs in a **loop 🔄**, enabling users to perform multiple calculations consecutively or exit the program when desired.

---

## ✨ Features

* ⚡ Performs arithmetic operations on multiple numbers:

  * ➕ Addition
  * ➖ Subtraction
  * ✖ Multiplication
  * ➗ Division (with division-by-zero handling 🚫0️⃣)
* 🔢 Allows the user to define how many numbers to include in the operation.
* 🛡 Division handles division-by-zero safely (asks again until valid input).
* 🔄 Users can continue performing new calculations or exit gracefully.

---

## 🖥 Usage

1️⃣ Run the application.
2️⃣ Choose an operation by entering a number from the menu (1️⃣ to 5️⃣).
3️⃣ Enter the number of values you want to use for the operation.
4️⃣ Enter each number as prompted.
5️⃣ ✅ View the result of the calculation.
6️⃣ 🔄 Choose whether to continue with another calculation or 🚪 exit.

---

## 📌 Example

```
********** Welcome To Loop calculator **********

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice: 1
How many Numbers You want to add? 3
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Result of addition: 60.0
Do you want to continue (y/n)? n
********** Exiting The Loop Calculator **********
```

---

## ⚠ Division Operation Special Handling

* 🚫 The calculator will not allow **division by zero**.
* 🔁 If a zero is entered during division, it will **prompt again until a valid non-zero divisor** is provided.

---

## 🚪 Exit Options

* Choose **option 5️⃣** at the main menu.
* Or select **'n'** when asked to continue.

---

## 🛠 Requirements

* 🐍 Python **3.x**

---

## ▶️ How to Run

Run the script using the Python interpreter:

```bash
python loop_calculator.py
```

> You can also use `.exe` file by reaching `build/exe.win-amd64-3.11/loop_calculator.exe`

> ⚠ But you can't use `.exe` file outside this folder


## 🌐 Visit

- Access the code through link:
https://github.com/devByWaleed/py-projects/tree/main/Loop%20Calculator/cloop_calculator.py


## 👨‍💻 Author

Developed by [Waleed](https://github.com/devByWaleed)
 as a simple **demonstration calculator** with loops 🔁 and error handling ⚡.

---

## 📜 License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).