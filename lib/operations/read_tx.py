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

  print ""
  print "Reading a transaction"
  print utility.cli_separator
  print "Follow the prompts to find a transaction"
  print "UID: <unix timestamp><6 character hexadecimal string>"
  print "UID Example: 16589476959D3DD8"
  print "Input q to return to the main menu"
  
  # get uid
  print "Please provide the UID of the transaction you wish to read"
  _uid = utility.get_input()
  if _uid == "q":
    return utility.call_main()

  # find tx by uid, none = print & recall
  try:
    _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
    if pretty:
      utility.pretty_print_tx(_tx_dict, True)
    else:
      print _tx_dict
  except StopIteration:
    print "Transaction not found, please try again"
    read_tx()
    print "Press ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()
  else:
    try:
      _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
      return _tx_dict
    except StopIteration:
      print "Transaction not found, please try again"
      return None
