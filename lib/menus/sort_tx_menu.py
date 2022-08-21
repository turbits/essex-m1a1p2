# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from .. import utility
from .. import io
from ..operations.sort_tx import sort_tx

def sort_tx_menu():
  _original_data = io.database
  _sorted_data = []

  if len(io.database) == 0:
    print "\nNo transactions to display"
    raw_input("Press ENTER to return to main menu")
    return utility.call_main()

  # get sort property
  print "Sort Transactions"
  print utility.cli_separator
  _prop = utility.get_input("Choose a property to sort by: uid, datetime, description, credit, debit, balance")

  if _prop == "q":
    return utility.call_main()

  if _prop not in ["uid", "datetime", "description", "credit", "debit", "balance"]:
    print "\nNot a valid property, please try again"
    raw_input("Press ENTER to return to main menu")
    return sort_tx_menu()

  # get order
  print "\nSort order:"
  _choice = utility.get_input("1. Ascending\n2. Descending\n3. None\nq. Return to main menu")
  if _choice == "q":
    return utility.call_main()
  elif _choice == "1":
    # ascending in python is reverse=False
    _choice = False
  elif _choice == "2":
    # descending in python is reverse=True
    _choice = True
  elif _choice == "3":
    _choice = None
  else:
    print "\nNot a valid sort order, please try again"
    raw_input("Press ENTER to return to main menu")
    return sort_tx_menu()

  # sort transactions
  _sorted_data = sort_tx(_original_data, _prop, _choice)

  # display sorted data
  for _tx in _sorted_data:
    print utility.cli_separator
    utility.pretty_print_tx(_tx, True)
    print utility.cli_separator
  
  return True
