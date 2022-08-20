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
  if _tx_obj is None:
    print "Transaction not found"
    return False
  else:
    try:
      io.database.remove(_tx_obj.as_dict())
      io.save_db()
      return True
    except:
      print "Error deleting transaction from database"
      return False
