# Expense_Tracker

This is a console-based application designed to help users track and manage their personal expenses. It provides a simple command-line interface for logging new expenses, viewing spending history, filtering by category, and displaying total expenditure. All expense data is persistently stored in a local JSON file.

## Features

-   **Add Expenses**: Easily record new expenses with details like amount, category, and a brief description.
-   **Total Spending**: Get a quick overview of your total expenditure.
-   **View History**: Display a comprehensive list of all logged expenses.
-   **Filter by Category**: Search and view expenses based on a specific category.
-   **Edit Expenses**: Modify existing expense entries.
-   **Delete Expenses**: Remove unwanted expense records.
-   **Data Persistence**: All expense data is automatically saved to and loaded from a local JSON file, ensuring your records are preserved across sessions.
-   **Robust Input Handling**: Includes basic input validation to prevent common errors.

## How to Run

### Prerequisites

-   Python 3.x installed on your system.
-   No external libraries are required; the project uses built-in Python modules (`datetime`, `json`).

### File Setup

1.  Create a JSON file named `expense.json` in a directory of your choice.
2.  **Important**: The code uses a hardcoded file path: `D:\Python\JSONS\expense.json`. You **must** change this path within the `load_from_file()` and `save_to_file()` functions to match the actual location of your `expense.json` file on your system.

### Execution

1.  Navigate to the directory containing the `expense_tracker.py` (or whatever you've named your main Python file) in your terminal or command prompt.
2.  Run the script using: `python expense_tracker.py`
3.  The application will then present you with the main menu options to manage your expenses.

## Code Structure

The project is organized using Object-Oriented Programming (OOP) principles to ensure a clean and scalable design:

-   **`Expense` Class**: Represents a single expense entry. It stores the `amount`, `category`, `description`, and `time` of the expense.
-   **`ExpenseTracker` Class**: Manages all expense-related functionality. It holds a list of `Expense` objects and contains methods for adding, viewing, editing, and deleting expenses. It also handles the saving and loading of data to and from the `expense.json` file.