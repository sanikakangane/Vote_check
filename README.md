# 🗳️ Vote Eligibility Checker

A simple Python program that calculates a user's age based on their birth year and determines whether they are eligible to vote. The program automatically detects the current year, ensuring accurate results every time it is run.

---

## 📌 Features

- Accepts the user's birth year as input.
- Automatically detects the current year.
- Calculates the user's age.
- Checks whether the user is eligible to vote.
- Displays a clear eligibility message.

---

## 📂 File Structure

```text
vote.py
```

---

## 💻 Technologies Used

- Python 3
- `datetime` module

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python vote.py
```

---

## 📜 How It Works

1. The user enters their birth year.
2. The program retrieves the current year using Python's `datetime` module.
3. The age is calculated using:

```text
Age = Current Year - Birth Year
```

4. If the calculated age is **18 years or older**, the user is eligible to vote.
5. Otherwise, the user is not eligible to vote.

---

## 🖥️ Sample Output

### Example 1

```text
Enter your Birth year: 2002
Your age is: 24
Hey! You are eligible to vote.
```

### Example 2

```text
Enter your Birth year: 2010
Your age is: 16
Hey! You are NOT eligible to vote.
```

> **Note:** The sample outputs above assume the program is run in **2026**. Since the current year is detected automatically, the displayed age will change depending on the year the program is executed.

---

## 📖 Example Code

```python
from datetime import datetime

DOB = int(input("Enter your Birth year: "))

Current_year = datetime.now().year
age = Current_year - DOB

print("Your age is:", age)

if age >= 18:
    print("Hey! You are eligible to vote.")
else:
    print("Hey! You are NOT eligible to vote.")
```

---

## 🚀 Future Improvements

- Validate invalid or future birth years.
- Handle non-numeric input using exception handling.
- Allow users to check eligibility multiple times without restarting the program.
- Display the user's exact age based on their full date of birth.

---

## 👩‍💻 Author

**Sanika Kangane**

---

If you like this project, consider giving it a ⭐ on GitHub!
