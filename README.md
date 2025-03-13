# module5_mini_project

Library Management System
Created by: Nicholas Aranda

Overview
A command-line Library Management System built with Python and MySQL. It helps manage books, users, authors, and borrowed books.

Features
* Book Operations: Add, display, search books
* User Operations: Add, display users
* Author Operations: Add, display authors
* Borrow/Return Books: Borrow and return books

Database Schema
Uses the following MySQL tables:
* authors: Author details
* books: Book details and availability
* users: Library user details
* borrowed_books: Tracks borrowed books

Getting Started:

Install (with the below command):
pip install mysql-connector-python

Set Up Database
1. Run the provided SQL schema to create the tables (authors, books, users, borrowed_books).
2. Ensure MySQL is running.

Run the Program (with the below command):
python library_system.py
(This will launch the system where you can manage books, users, and authors via the command line.)
