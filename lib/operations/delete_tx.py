# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

from .. import utility

def delete_tx(uid):
  print ""
  print "Delete a transaction"
  print utility.cli_separator
  print "Follow the prompts to delete a transaction"
  print "This is a PERMANENT delete"
  print "UID: <unix timestamp><6 character hexadecimal string>"
  print "UID Example: 16589476959D3DD8"
  print "Input q to return to the main menu"

  # get uid of tx to delete
  print "Please provide the UID of the transaction you wish to read"
  _uid = utility.get_input()
  if _uid == "q":
    return utility.call_main()

  # confirm deletion, no = recall
  print "Are you sure you want to delete this transaction? (y/n)"
  _confirm = utility.get_input()

  if _confirm == "y":
    print "Are you absolutely sure you want to delete this transaction? (y/n)"
    _confirm = utility.get_input()

  # delete tx
  if _confirm == "y":
    try:
      _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
      io.database.remove(_tx_dict)
      print "Transaction deleted"
    except StopIteration:
      print "Transaction not found, please try again"
      delete_tx()
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
