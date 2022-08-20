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

def delete_tx_menu():
  print "Delete Transaction"
  print utility.cli_separator
  
  # get uid
  _uid = utility.get_input("Please provide the UID of the transaction you wish to delete")
  if _uid == "q":
    exit()
  else:
    _success = delete_tx(_uid)
    if _success:
      print "Transaction deleted"
    else:
      print "Transaction not found"
    raw_input("")
    return __main__()
