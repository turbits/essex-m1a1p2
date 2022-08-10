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
from ..transaction import Transaction
from .. import io
from display_all_tx import display_all_tx

def sort_display_all_tx():
  _temp_tx = Transaction("", 0, 0, 0, "", "")
  _original_data = io.database
  _sorted_data = []
  _order = None
  # this (_reverse) is an extra var just to keep the initial flowcharts relevant,
  # probably a good reason to write a prototype along with flowcharts :^)
  _reverse = False

  # list empty = print & main
  if len(io.database) == 0:
    print "\nNo transactions to display"
    print "Press ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()

  # get property to sort by
  print "\nSort Transactions"
  print utility.cli_separator
  print "Choose a property from the list to sort by:"
  print "datetime, credit, debit, balance"
  print "Input q to return to the main menu"

  _prop = utility.get_input()
  if _prop == "q":
    return utility.call_main()
  if _prop not in ["datetime", "credit", "debit", "balance"]:
    print "\nNot a valid property, please try again"
    print "Press ENTER to retry operation"
    utility.get_input()
    return sort_display_all_tx()

  # get order to sort by; on invalid order recall func (none, dec, inc)
  print "\nChoose a sort order"
  print """1: None: No sort order, will return tx database as-is
2: Dec : Will sort the dataset DECREMENTING/DESCENDING
3: Inc : Will sort the dataset INCREMENTING/ASCENDING
q: Exit to main menu"""

  _choice = utility.get_input()

  if _choice == "q":
    return utility.call_main()
  elif _choice == "1":
    # order is none, just display all tx in db
    return display_all_tx()
  elif _choice == "2":
    # choice is descending, in Python sorted() func this is True
    _order = "dec"
    _reverse = True
  elif _choice == "3":
    # choice is ascending, in Python sorted() func this is False
    _order = "inc"
    _reverse = False
  else:
    print "Invalid choice"
    print "Press ENTER to retry operation"
    utility.get_input()
    return sort_display_all_tx()

  # sort data by prop/order
  _sorted_data = sorted(_original_data, key=lambda p: p[str(_prop)], reverse=_reverse)

  # display sorted data
  print ""
  print "Sorted Transactions"
  print utility.cli_separator
  print "Sorted by: {0}".format(_prop)
  print "Order: {0}".format(_order)
  print utility.cli_separator
  for tx in _sorted_data:
    utility.pretty_print_tx(tx, True)
    print utility.cli_separator
  
  # end
  print "\nPress ENTER to return to main menu"
  utility.get_input()
  return utility.call_main()
