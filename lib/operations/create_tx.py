# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

import os
from .. import utility
from .. import io
from ..transaction import Transaction

# create_tx(tx)
# takes in a tx object
# generates a uid, datetime, and description if none provided
# validates the transaction
# adds the transaction to the database
def create_tx(tx_obj):
  _tx_obj = Transaction(uid=tx_obj.uid, datetime=tx_obj.datetime, description=tx_obj.description, credit=tx_obj.credit, debit=tx_obj.debit, balance=tx_obj.balance)
  _prev_balance = None
  _db_length = len(io.database)

  # generate and set the UID of the transaction
  if _tx_obj.uid is None:
    _tx_obj.uid = utility.gen_uid()
  
  # generate and set the datetime of the transaction
  if _tx_obj.datetime is None:
    _tx_obj.datetime = utility.gen_unix_timestamp()
  
  # generate and set a description for the transaction if one was not provided
  if _tx_obj.description is None or _tx_obj.description == "":
    _tx_obj.description = "credit" if _tx_obj.credit > 0 else "debit"
  
  # calculate the balance
  if _db_length == 0:
    _tx_obj.balance = _tx_obj.credit
  else:
    _prev_balance = io.database[_db_length - 1]["balance"]
    _tx_obj.balance = float(_prev_balance + _tx_obj.credit - _tx_obj.debit)

  # validate the transaction
  _tx_validation = utility.validate_tx(_tx_obj)
  if not _tx_validation["valid"]:
    print "Transaction is invalid:"
    print utility.cli_separator
    print _tx_validation["error"]
    return False

  # add the transaction to the database
  try:
    io.database.append(_tx_obj.as_dict())
    io.save_db()
    return True
  except:
    io.database.remove(_tx_obj.as_dict())
    print "Error saving transaction to database"
    return False
