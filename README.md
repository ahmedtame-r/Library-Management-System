# **Library Management System**

## **Overview**

The **Library Management System (LMS)** is a desktop application built with **Python** and **Tkinter**. It is designed to help libraries manage books efficiently and facilitate interactions between users and administrators. Users can perform operations like logging in, adding books, borrowing, searching, and displaying available books. Administrators can manage the system and ensure that all library operations run smoothly.

## **Table of Contents**

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Installation Guide](#installation-guide)
4. [Usage Instructions](#usage-instructions)
5. [Code Structure](#code-structure)

## **Features**

- **User Authentication**: 
  - Sign up and login functionality for both users and administrators.
  - Secure password storage and validation.
  
- **Book Management**:
  - Add new books to the library system.
  - Update or remove book details.
  
- **Borrowing System**:
  - Borrow books, with a real-time update on the number of available copies.
  - Track borrowed books.

- **Search Functionality**:
  - Search for books based on title, author, or other keywords.

- **Admin Control**:
  - Admins have special privileges to manage books and user accounts.
  - View all books and check availability.

- **User Interface**:
  - A clean, user-friendly interface developed with **Tkinter**.
  - Responsive design with interactive elements.

## **Technologies Used**

- **Programming Language**: Python
- **GUI Framework**: Tkinter
- **Data Storage**: Local dictionary-based storage (to be extended to a database in future versions)
- **Platform**: Cross-platform (Windows, Linux, macOS)

## **Installation Guide**

### Prerequisites

- Ensure Python 3.x is installed on your system.
- Tkinter comes pre-installed with Python, so no additional installation is needed for it.

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
2. **Navigate to Project Directory**:
   ```bash
   cd library-management-system
3. **Run the Application**:
   ```bash
   python main.py
4. **The application will launch a login window where users can sign up or log in to the system**

---
## **Usage Instructions**

### User Login:
- Upon opening the application, users will be presented with a login screen.
- Users can either log in with their credentials or sign up for a new account.

### Admin Panel:
- Once logged in, users with admin privileges can access the full library management functionality.
- Admins can add new books, update existing ones, and manage book availability.

### Borrowing Books:
- Users can search for books and borrow them if available.
- Once borrowed, the number of copies is updated automatically.

### Book Search:
- Users can search for books by title, author, or keyword.

---

## **Code Structure**

The project follows a modular structure to separate concerns and maintain readability. The core components of the project are:

### 1. **LoginPage** (class `LoginPage`):
- Handles user authentication (login and sign-up functionality).

### 2. **Library** (class `Library`):
- Manages the collection of books and handles operations like adding, borrowing, and searching.

### 3. **LibraryGUI** (class `LibraryGUI`):
- Implements the graphical interface for managing books, borrowing books, and displaying book information.

### 4. **Book** (class `Book`):
- Represents individual books with properties like ID, title, author, and number of copies.

### 5. **Admin Management**:
- Admins can manage the system from the Library GUI, adding and updating books as needed.
