# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

import os
from lib.operations.create_tx import create_tx
from lib.operations.display_all_tx import display_all_tx
from lib.operations.read_tx import read_tx
from lib.operations.update_tx import update_tx
from lib import ascii_art
from lib import utility
from lib import io

database = None

def show_title():
  print ascii_art.title

def main_menu():
  print ""
  show_title()
  # check for existing db. if none, create new
  db_exist = io.check_db()
  if db_exist:
    io.load_db()
  else:
    io.create_db()
  print utility.cli_separator
  _bal = utility.get_balance()
  print "Current account balance: ${:,.2f}".format(_bal)
  print utility.cli_separator
  print "Please select an option:"
  print """1: Create transaction
2: Find (read) transaction
3: Update transaction
4: Delete transaction
5: Display all transactions
6: Sort and display all transactions
7: Display transaction schema
8: Delete and recreate database
w: Show current db var (for debugging)
e: Show current db.json (for debugging)
r: Show current balance (for debugging)
q: Exit program"""
  print utility.cli_separator
  choice = utility.get_input()

  if choice == "q":
    exit()
  elif choice == "1":
    # create_tx()
    create_tx()
  elif choice == "2":
    # read_tx()
    read_tx(True)
  elif choice == "3":
    # update_tx()
    update_tx()
  elif choice == "4":
    # delete_tx()
    main_menu()
  elif choice == "5":
    # display_all_tx()
    display_all_tx()
  elif choice == "6":
    # sort_display_all_tx()
    main_menu()
  elif choice == "7":
    # show_tx_schema()
    main_menu()
  elif choice == "8":
    print ""
    print "Database Deletion"
    print utility.cli_separator
    print "This will delete the current database and create a new one"
    print "All transactions will be permanently deleted"
    print "Are you sure you want to recreate the database? (y/n)"
    _confirm_delete = utility.get_input()
    if _confirm_delete == "y":
      # second confirm
      print "Are you absolutely sure you want to recreate the database? (y/n)"
      _confirm_delete = utility.get_input()
    if _confirm_delete == "y":
      # recreate db
      io.delete_db()
      io.create_db()
      print "Press ENTER to return to main menu"
      utility.get_input()
      main_menu()
    else:
      print "Press ENTER to return to main menu"
      utility.get_input()
      main_menu()
  elif choice == "w":
    # get db var
    io.get_db_var()
    print "Press ENTER to return to main menu"
    utility.get_input()
    main_menu()
  elif choice == "e":
    # get db json
    io.get_db_json()
    print "Press ENTER to return to main menu"
    utility.get_input()
    main_menu()
  elif choice == "r":
    # get balance
    bal = utility.get_balance()
    print "Current account balance: ${:,.2f}".format(_bal)
    print "Press ENTER to return to main menu"
    utility.get_input()
    main_menu()
  else:
    print "Invalid selection"
    main_menu()

def __main__():
  main_menu()

__main__()
