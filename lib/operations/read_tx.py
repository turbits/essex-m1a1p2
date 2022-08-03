# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

from .. import io
from .. import utility

def read_tx(pretty=False, uid=None):
  _uid = uid

  if _uid is not None:
    return next(tx for tx in io.database if tx["uid"] == _uid)

  print "\nReading a transaction"
  print utility.cli_separator
  print "Follow the prompts to find a transaction"
  print "UID: <unix timestamp><6 character hexadecimal string>"
  print "UID Example: 16589476959D3DD8"
  print "Input q to return to the main menu"
  
  # get uid
  print "\nPlease provide the UID of the transaction you wish to read"
  _uid = utility.get_input()
  if _uid == "q":
    return utility.call_main()

  # find tx by uid, none = print & recall
  try:
    _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
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
  else:
    try:
      _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
      return _tx_dict
    except StopIteration:
      print "\nTransaction not found, please try again"

  print "\nPress ENTER to return to main menu"
  utility.get_input()
  return utility.call_main()
