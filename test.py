# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from lib import utility
from lib.transaction import Transaction
from lib.operations.create_tx import create_tx

test_results = {
  "create": False,
  "read": False,
  "update": False,
  "delete": False,
  "sort": False,
}

def test_create_tx():
  _tx_obj = Transaction(uid="", datetime=0, description="Fee", debit=0, credit=10, balance=200)
  _passed = create_tx(_tx_obj)
  test_results.create = _passed

def test_all():
  test_create_tx()

def test_menu():
  print "\nBankbook Test Suite"
  print utility.cli_separator
  print "This will run a suite of tests against the defined operations used by the bankbook program"
  print "Please select an option:"
  print """1: All tests
2: Create transaction
3: Read transaction
4: Update transaction
5: Delete transaction
6: Sort and display all transactions
q: Exit script"""

  choice = utility.get_input()
  if choice == "q":
    exit()
  elif choice == "1":
    test_all()
  elif choice == "2":
    test_create_tx()
    print "Create TX Test Result: {0}".format("Passed" if test_results.create == True else "Failed")
  elif choice == "3":
    # read
    pass
  elif choice == "4":
    # update
    pass
  elif choice == "5":
    # delete
    pass
  elif choice == "6":
    # sort
    pass
  else:
    print "Invalid option"
    return test_menu()

test_menu()
