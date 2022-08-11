# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

import os
from lib.transaction import Transaction
from lib.operations.create_tx import create_tx
from lib import ascii_art
from lib import utility
from lib import io

def show_title():
  print ascii_art.title

def create_tx_menu():
  _tx_obj = Transaction("", 0, "", 0, 0, 0)
  print "Create Transaction"
  print utility.cli_separator
  
  # get description
  _tx_obj.description = utility.get_input("Please provide a description of the transaction")
  
  # determine credit or debit and amount
  _credit_or_debit = utility.get_input("Is this a credit or a debit transaction? (c/d)")
  _amount = utility.get_input("Please provide the amount of the transaction")
  if _credit_or_debit == "c":
    _credit = float(_amount)
    _debit = float(0.00)
  elif _credit_or_debit == "d":
    _debit = float(_amount)
    _credit = float(0.00)
  else:
    print "Invalid selection"
    create_tx_menu()

  # confirm create
  print utility.cli_separator
  print "Confirm create transaction:"
  utility.pretty_print_tx(_tx_obj)
  print utility.cli_separator
  _confirm_create = utility.get_input("Are you sure you want to create this transaction? (y/n)")
  if _confirm_create == "y":
    # create transaction
    return create_tx(_tx_obj)
  else:
    print "Transaction creation cancelled"
    utility.get_input("Press ENTER to return to main menu")
    __main__()

def __main__():
  print "\n{0}".format(ascii_art.title)

  # check for existing db. if none, create new
  db_exist = io.check_db()
  if db_exist:
    io.load_db()
  else:
    io.create_db()
  
  # get balance
  _balance = utility.get_balance()
  print _balance

  # main menu
  print utility.cli_separator
  print "Current account balance: ${:,.2f}".format(_balance)
  print utility.cli_separator
  print "Please select an option:"
  print """1: Create transaction
2: Read/find transaction(s)
3: Update transaction
4: Delete transaction
6: Sort transactions
7: Display transaction schema
8: Delete and recreate database
q: Exit program"""
  print utility.cli_separator
  choice = utility.get_input()

  if choice == "q":
    exit()
  elif choice == "1":
    _success = create_tx_menu()
    print _success
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "4":
    pass
  elif choice == "5":
    pass
  elif choice == "6":
    pass
    pass
  elif choice == "7":
    pass
  elif choice == "8":
    print ""
    print "Database Deletion"
    print utility.cli_separator
    print "This will delete the current database and create a new one"
    print "All transactions will be permanently deleted"
    _confirm_delete = utility.get_input("Are you sure you want to recreate the database? (y/n)")
    if _confirm_delete == "y":
      # second confirm
      _confirm_delete = utility.get_input("Are you absolutely sure you want to recreate the database? (y/n)")
    if _confirm_delete == "y":
      # recreate db
      io.delete_db()
      io.create_db()
      utility.get_input("Press ENTER to return to main menu")
      __main__()
    else:
      utility.get_input("Press ENTER to return to main menu")
      __main__()
  else:
    print "Invalid selection"
    __main__()

# enter main
__main__()
