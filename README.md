# Django Expense Tracker

This is a web-based application built with **Django** designed to help users track and manage their personal expenses. It provides a user-friendly interface for logging new expenses, viewing spending history, filtering by category, and displaying total expenditure. All expense data is persistently stored in a relational database using Django’s ORM, with built-in multi-user support and authentication.

---

## Features

-   **Multi-User Support**: Each user can manage their own expenses securely.
-   **User Authentication**: Built-in login, signup, and logout using Django’s robust authentication system.
-   **Add Expenses**: Easily record new expenses with details like amount, category, and description.
-   **Edit Expenses**: Modify existing expense entries.
-   **Delete Expenses**: Remove unwanted expense records.
-   **View History**: Display a comprehensive list of all logged expenses for the authenticated user.
-   **Filter by Category**: Search and view expenses based on a specific category.
-   **Total Spending**: Get a quick overview of your overall expenditure.
-   **Category-Wise Spending**: See a breakdown of expenses by category.
-   **Dynamic Filtering**: Implemented with JavaScript `fetch()` for instant updates when selecting categories without a page reload.

---

## How to Run

### Prerequisites

-   Python 3.x installed on your system.
-   Django installed (`pip install django`).
-   No external dependencies are required (`requirements.txt` is not included as this is a learning/demo project).

### File Setup

1.  Clone or download this repository.
2.  Navigate into the project directory:
    ```bash
    cd Expense_Tracker
    ```
3.  Run database migrations to set up your tables:
    ```bash
    python manage.py migrate
    ```
4.  Create a superuser (admin account) to manage your site:
    ```bash
    python manage.py createsuperuser
    ```

### Execution

1.  Start the Django development server:
    ```bash
    python manage.py runserver
    ```
2.  Open your browser and navigate to: `http://127.0.0.1:8000/`
3.  Sign up or log in as a user.
4.  Add expenses with details like amount, category, and description.
5.  View and manage your expenses directly from the web interface, using category filters and viewing totals.

---

## Code Structure

The project is organized using Django’s **MTV (Model-Template-View)** architecture for a clean and scalable design.

-   **Expense Model**: Represents a single expense entry with fields for:
    -   `amount`, `category`, `description`
    -   `created_at`, `updated_at`
    -   `user` (A `ForeignKey` to Django’s built-in `User` model).
-   **Views**: Handle expense CRUD operations, category filtering via AJAX, and user authentication.
-   **Templates**: Provide the HTML pages for the user interface, including forms and data displays.
-   **Static Files**: Contain the CSS and JavaScript assets for styling and dynamic UI behavior.
-   **URLs**: Route web requests to the appropriate views.

### Project Directory Layout
The structure of your project is clean and well-organized:
Expense_Tracker/
│
├── Expense_Tracker/          # Main project folder (settings, URLs, WSGI/ASGI)
│
├── expense/                  # The main app handling all expense logic
│   ├── models.py             # Expense model definition
│   ├── views.py              # CRUD & filtering logic
│   ├── urls.py               # App-level URL routing
│   ├── templates/            # HTML templates
│   └── static/               # CSS and JS files
│
├── db.sqlite3                # The default database file
└── manage.py                 # Django project manager
---


## Future Improvements

-   Export expenses to CSV/Excel.
-   Responsive UI design with a framework like Bootstrap or Tailwind CSS.
-   Add graphical reports (e.g., charts) for better insights into spending habits.
-   Implement expense reports.