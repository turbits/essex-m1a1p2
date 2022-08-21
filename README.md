# Bankbook Program

I coded this program as part of the **Launching into Computer Science** course, Assignment 1, Part 2, at the University of Essex in July/August 2022. This assignment was to create a program following a written assignment in Part 1 which detailed a program of the student's choosing in flowchart and/or pseudocode, including a testing table.

For Part 2 of the assignment we were required to write the program that we had detailed in Part 1, and write a testing strategy along with this README outlining the program requirements, how to run the program, and details on how the program operates.

---

# Program Requirements

This program was built and tested on Python 2.7.18 as the Codio Python labs given to students of this program used Python "2.7.15+". Ideally, labs with a modern version of Python (3.x+) would have been provided as Python 2 has been obsolete by two years at the time of this assignment (August 2022).

---

# Running the Program

The program is built to be interacted with from a single file, main.py, which includes the entry function of the program. From the main function, all of the operations can be called from a main menu, in addition to the testing suite and some extra features.

To open the program, open the main.py file with the Python interpreter: `python main.py`

Opening the main file will present a list of operations as described in detail in my paper "Data Structures and Algorithm Design", also in this repository in the Bankbook Design Document PDF file. For posterity, I will include an explanation of each operation, the test suite, and additional features of this program below.

## Insert Operation

The insert operation accepts a transaction object and attempts to insert it into the database. It appends it to an in-memory database variable, then saves the variable which contains all current transactions to a JSON file for persistent data storage.

For this particular operation choice, the user is first stepped through the "create" part of a transaction, as it is the most user-friendly way to do it. Simply requiring a transaction object would not be good practice, user-experience-wise. After the user is run through creating a transaction, the insert operation is called.

## Search Operation

The search operation accepts a property and a value pair to search the database by. It collects all matching transactions and adds them to a list, which it then returns.

## Delete Operation

The delete operation accepts a UID as described in the schema. It uses the search operation to find the matching transaction, if any, and removes it from the database. This operation then recalculates the balances of transactions that appear at and after the index of the transaction removed so the balances are properly calculated.

## Sort Operation

The sort operation accepts a list, a property to sort by, and the order in which to sort the list. It returns a sorted list of transactions based on the property and order given.

## Test Suite

The test suite contains several options. One can test all of the operations in a single option, or test them individually. For the full test strategy and data, please see the final section of the included paper, "Bankbook Design Document". The Testing section in the paper details the strategy and data I used to come up with a test suite that would adequately define the relevant tests in this program.

Each test that creates one or more transactions in the database to use for testing, then removes the transactions afterwards.

## Additional Features

The program also contains several additional, quality-of-life features.

One of the earliest features implemented was persistent data storage in the form of a JSON file. Simple database input/output functions were written to accommodate this as a core function of any database is persistence.

For convenience, a show all transactions function was implemented. This displays all of the transactions as they appear in the in-memory database variable. A show schema function has also been written to provide the user with reference if they want to know what the structure of a transaction object looks like.

In case of database errors or if the user simply wants to easily get rid of the database, there is also a recreate database function available, which wipes the in-memory database variable, and overwrites the JSON database file with an empty array: "[]".

---

# References

Robinson, S (2022) Reading and Writing JSON to a File in Python. Available at: [https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/](https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/) (Accessed: 21 Aug 2022).

Sturtz, J (no date) Python Modules and Packages - An Introduction. Available at: [https://realpython.com/python-modules-packages/](https://realpython.com/python-modules-packages/) (Accessed: 15 Aug 2022)

Byers, M (2010) Efficiently generate a 16-character, aphanumeric string. Available at: [https://stackoverflow.com/a/2511238](https://stackoverflow.com/a/2511238) (Accessed: 15 Aug 2022)

patorjk.com (no date) Text to ASCII Art Generator (TAAG). Available at: [https://patorjk.com/software/taag](https://patorjk.com/software/taag) (Accessed: 13 Aug 2022)
