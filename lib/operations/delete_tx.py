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

  _tx_dict = {}

  print "\nDelete a transaction"
  print utility.cli_separator
  print "Follow the prompts to delete a transaction"
  print "This is a PERMANENT delete"
  print "UID: <unix timestamp><6 character hexadecimal string>"
  print "UID Example: 16589476959D3DD8"
  print "Input q to return to the main menu"

  # get uid of tx to delete
  print "Please provide the UID of the transaction you wish to delete"
  _uid = utility.get_input()
  if _uid == "q":
    return utility.call_main()
  
  # find the tx if exists
  try:
    _tx_dict = next(tx for tx in io.database if tx["uid"] == _uid)
  except StopIteration:
    print "\nTransaction not found, please try again"
    print "Press ENTER to retry operation"
    utility.get_input()
    delete_tx()

  # confirm deletion
  print "\nAre you sure you want to delete this transaction? (y/n)"
  _confirm = utility.get_input()

  if _confirm == "y":
    print "\nAre you absolutely sure you want to delete this transaction? (y/n)"
    _confirm = utility.get_input()

  # try delete tx
  if _confirm == "y":
    try:
      io.database.remove(_tx_dict)
      print "\nTransaction deleted"
    except:
      print "\nError removing transaction from database, please try again"
      print "Press ENTER to retry operation"
      delete_tx()
  
  print "\nPress ENTER to return to main menu"
  utility.get_input()
  return utility.call_main()
