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

# this is just a find by property
# find by predicate a little out of scope
# function returns the first match
def read_tx(pretty=False, uid=None):
  _uid = uid
  _prop = None
  _value = None

  # if a UID is passed just return the tx if found
  if _uid is not None:
    return next(tx for tx in io.database if tx["uid"] == _uid)

  print "\nReading a transaction"
  print utility.cli_separator
  print "Follow the prompts to find a transaction"
  print "This operation will return the first match"
  print utility.cli_separator

  # get prop
  print "\nPlease provide the property you wish to find a transaction by:"
  print "uid, datetime, description, credit, debit, balance"
  print "Enter q to return to main menu"

  _prop = utility.get_input()
  if _prop == "q":
    return utility.call_main()
  if _prop not in ["uid", "datetime", "description", "credit", "debit", "balance"]:
    print "\nNot a valid property, please try again"
    print "Press ENTER to retry operation"
    utility.get_input()
    return read_tx()

  # get value
  print "\nPlease provide the value of the property"
  print "Must be exact value; I didn't implement fuzzy search"
  print "Enter q to return to main menu"

  _value = utility.get_input()
  if _value == "q":
    return utility.call_main()
  
  # converting to match value types
  if _prop in ["datetime"]:
    _value = int(_value)
  if _prop in ["credit", "debit", "balance"]:
    _value = float(_value)

  # find tx by property and value
  try:
    _tx_dict = next(tx for tx in io.database if tx[str(_prop)] == _value)
    # pretty print the transaction
    print ""
    print utility.cli_separator
    utility.pretty_print_tx(_tx_dict, True)
    print utility.cli_separator

    print "\nPress ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()
  except StopIteration:
    print "\nTransaction not found, please try again"
    print "Press ENTER to retry operation"
    utility.get_input()
    read_tx()

  print "\nPress ENTER to return to main menu"
  utility.get_input()
  return utility.call_main()
