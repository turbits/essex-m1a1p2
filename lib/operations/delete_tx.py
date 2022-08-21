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
from .. import io

def delete_tx(uid):
  _tx_obj = utility.get_tx_by_uid(uid)
  print "DEBUG: tx obj\n{0}".format(_tx_obj)
  if _tx_obj is None:
    print "ERROR: Transaction not found"
    return False
  else:
    try:
      _index = utility.get_index_by_tx_uid(uid)
      io.database.remove(_tx_obj)
      # recalculate balances for all transactions at and after the index of the deleted tx
      utility.recalculate_balances(_index)
      io.save_db()
      return True
    except:
      print "ERROR: Transaction could not be deleted"
      return False
