Introduction

The Budget Calculator is a Python program designed to help users manage and allocate their budgets. It allows users to define an initial budget, assign percentages to various categories, calculate amounts for each category, and save or load budget data from an Excel file. The program features a simple menu-based interface and integrates file handling, user input validation, and error handling.

Features

Budget Management:

    Define an initial budget amount.
    Allocate percentages to various categories.
    Automatically calculate category-specific budget amounts.
    
File Handling:

    Save budgets to an Excel file.
    Load budgets from an existing Excel file.
    Avoid overwriting files by prompting the user to rename or overwrite.
    
User-Friendly Interface:

    Menu-driven navigation for ease of use.
    Input validation for budget amounts and percentages.
    
Excel Integration:

    Save data in a well-structured Excel sheet using xlsxwriter.
    Reload and manipulate data using openpyxl.

Requirements

Libraries

The following Python libraries are required:

    xlsxwriter (for creating Excel files)
    openpyxl (for reading and updating Excel files)
    
Installation
    
These libraries are automatically installed when running the program.

Usage

Run the Program: Execute the script with:

    python <script_name>.py
    
Main Menu: Upon launching the program, you'll see a menu with the following options:

    1: Create a new budget and allocate percentages.
    2: Save the current budget to an Excel file.
    3: Load an existing budget from an Excel file.
    4: Exit the program.
    
Creating a Budget:

    Enter your initial budget amount.
    Specify the number of categories and assign names and percentages to each.
    
Saving a Budget:

    Choose a file name or overwrite an existing file.
    
Loading a Budget:

    Provide the file name of an existing budget to load data.
    
Making Changes to Loaded Budget:

    Modify percentages or add new categories, then save changes if needed.
    
File Structure

Budget Data in Excel: The Excel sheet is organized as follows:

    A1: Initial Amount
    B1: After Deductions
    A4-C4: Headers for categories, percentages, and final amounts
    Row 5+: Detailed category data
    Final Row: Total of all calculated amounts
    
Default save location is the Documents directory.

Menu Options

Enter Budget Data:

    Define your budget and allocate percentages to categories.
    
Save Data:

    Save your current budget to an Excel file.
    
Load Data:

    Load an existing budget for review or modification.
    
Exit:

    Exit the application.
    
Error Handling

User Input:

    Ensures amounts and percentages are valid numbers.
    Restricts percentages between 0 and 100.

File Handling:

    Prompts before overwriting existing files.
    Detects if the file is open or inaccessible.

General Errors:

    Displays helpful error messages for unexpected issues.


Example Workflow

    Start the program.
    Choose 1 to create a new budget:
        Input: 1000 as initial budget.
        Define categories like Food, Rent, Savings.
        Enter percent for each category: 30, 20, 50
    Save the budget using 2:
        File name: my_budget.
    Load the file using 3 to review or update.
    Exit using 4.
    
Notes

Ensure the installer module and menu.py are in the same directory as the script.
Adjust file paths and permissions as necessary for your operating system.

