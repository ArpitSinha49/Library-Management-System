# CLI Library Management System

A command-line Library Management System built in Python. It allows an administrator to add new books, manage subjects, issue and return books, and track due dates.

## Prerequisites
* **Python 3.10 or higher** is strictly required (the code utilizes `match...case` structural pattern matching).
* No external libraries or dependencies are required.

## Environment Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArpitSinha49/Library-Management-System
   cd Library-Management-System
   ```

2. **Run the application:**
   Execute the script directly from your terminal:
   ```bash
   python lib2.py
   ```
   *(Note: If your system defaults to an older Python 3 version, you may need to use `python3 lib2.py` or `python3.10 lib2.py`)*

## Usage Instructions

Upon running the script, you will be prompted to log in. Use the following default administrator credentials to access the system:
* **Username:** `admin`
* **Password:** `library123`

Once logged in, type the number corresponding to the menu options to navigate the system:
1. **Add a new book:** Automatically generates a unique book number based on the subject category.
2. **Issue a book:** Assigns a book to a student (requires student name and registration number) and sets a 14-day due date.
3. **Return a book:** Marks a previously issued book as available again.
4. **Display all available books:** Shows books currently on the shelf.
5. **Display all issued books:** Shows books currently checked out and to whom.
6. **Display books due today:** Checks active issues against the current system date.
7. **Logout:** Exits the admin session.