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
from ..operations.delete_tx import delete_tx

def delete_tx_menu():
  print "Delete Transaction"
  print utility.cli_separator
  
  # get uid
  _uid = utility.get_input("Please provide the UID of the transaction you wish to delete")
  if _uid == "q":
    exit()
  
  # check if uid exists
  if not utility.get_index_by_tx_uid(_uid):
    print "ERROR: Transaction with UID {0} does not exist".format(_uid)
    return False

  # delete transaction
  _success = delete_tx(_uid)
  if _success:
    print "Transaction deleted"
    return True
  else:
    print "ERROR: Transaction could not be deleted"
    return False
