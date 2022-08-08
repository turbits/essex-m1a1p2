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


def sort_display_all_tx(order = "none"):
  _temp_tx = Transaction("", 0, 0, 0, "", "")

  # list empty = print & main
  if len(io.database) == 0:
    print "\nNo transactions to display"
    print "Press ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()

  # entry
  print "\nSort Transactions"
  print utility.cli_separator
  print "Choose a property from the list to sort by"
  print "Input q to return to the main menu"
  
  # get property
  print """1: datetime
2: credit
3: debit
4: balance
  """

  _choice = utility.get_input()
  _prop = ""
  if _choice == "q":
    return utility.call_main()
  elif _choice == "1":
    _prop = "datetime"
  elif _choice == "2":
    _prop = "credit"
  elif _choice == "3":
    _prop = "debit"
  elif _choice == "4":
    _prop = "balance"

  
  # check property exists in schema, err = print & recall
  if not getattr(_temp_tx, str(_prop)):
    print "'{0}' is not a valid property on Transaction object".format(_prop)
    print "Press ENTER to retry operation"
    utility.get_input()
    return sort_display_all_tx()

  # get order; on invalid order recall func (none, dec, inc)
  _choice = utility.get_input()
  _order = order
  print "Choose a sort order; if none is provided this operation"
  print "will use the passed in value, by default 'none'"
  print "Sort order: {0}".format(order)
  print """1: None; will not sort the dataset
2: Dec : will sort the dataset DECREMENTING
3: Inc : will sort the dataset INCREMENTING
q: Exit to main menu"""

  if _choice == "q":
    return utility.call_main()
  elif _choice == "1":
    _order = "none"
  elif _choice == "2":
    _order = "dec"
  elif _choice == "3":
    _order = "inc"
  else:
    print "Invalid choice"
    return sort_display_all_tx()
  
  # if order = none, display data as-is (call display_all_tx())
  display_all_tx()
  print "Press ENTER to return to main menu"
  utility.get_input()
  utility.call_main()

  # get data

  # sort data by prop/order and store in new dict/arr

  # display sorted data

