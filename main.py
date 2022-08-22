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
from lib import io
from lib import utility
from lib import ascii_art
from lib.operations.search_tx import search_tx
from lib.menus.create_tx_menu import create_tx_menu
from lib.menus.delete_tx_menu import delete_tx_menu
from lib.menus.search_tx_menu import search_tx_menu
from lib.menus.sort_tx_menu import sort_tx_menu


def show_title():
  print ascii_art.title

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
  print """1: Create/insert transaction
2: Search transaction(s)
3: Delete transaction
4: Sort transactions
5: Display all transactions
6: Display transaction schema
7: Delete and recreate database
t: Run test suite
q: Exit program"""
  print utility.cli_separator
  choice = utility.get_input()

  if choice == "q":
    return exit()
  elif choice == "1":
    _success = create_tx_menu()
  elif choice == "2":
    _tx_list = search_tx_menu()
    if _tx_list == [] or _tx_list == False:
      _success = False
    else:
      _success = True
      print _tx_list
  elif choice == "3":
    _success = delete_tx_menu()
  elif choice == "4":
    _success = sort_tx_menu()
  elif choice == "5":
    # show all transactions
    _transactions = search_tx("", "", True)
    for _tx in _transactions:
      print utility.cli_separator
      utility.pretty_print_tx(_tx, True)
      print utility.cli_separator
    _success = True
  elif choice == "6":
    utility.show_tx_schema()
    _success = True
  elif choice == "7":
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
      try:
        # recreate db
        io.delete_db()
        io.create_db()
        _success = True
      except:
        _success = False
    else:
      _success = False
  elif choice == "t":
    # test suite
    return os.system("python test.py")
  else:
    print "Invalid selection"
    return __main__()
  
  # return to main menu
  print "Operation complete" if _success else "ERROR: Operation cancelled"
  raw_input("Press ENTER to return to main menu")
  return __main__()

# enter main
__main__()
