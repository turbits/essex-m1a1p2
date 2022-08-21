# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from .. import io
from .. import utility
from ..operations.search_tx import search_tx

_prop_list = ["uid", "datetime", "description", "credit", "debit", "balance"]

def search_tx_menu():
  print "Search Transactions"
  print utility.cli_separator
  
  # get prop
  _prop = utility.get_input("Choose a property to search by: uid, datetime, description, credit, debit, balance")
  if _prop == "q":
    exit()
  elif _prop not in _prop_list:
    print "Invalid selection"
    return search_tx_menu()
  
  # get value
  _value = utility.get_input("Please provide the value to search for")

  # search transactions
  _tx_list = search_tx(_prop, _value)
  
  if _tx_list is None or _tx_list == []:
    print "No transactions found"
    return False
  
  # display transactions
  for _tx in _tx_list:
    print utility.cli_separator
    utility.pretty_print_tx(_tx, True)
    print utility.cli_separator
  
  return True
  
