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
from ..transaction import Transaction
from read_tx import read_tx

def update_tx():
  _old_tx = None
  _old_tx_index = None
  _new_tx = Transaction("", 0, 0, 0)

  print ""
  print "Updating a transaction"
  print utility.cli_separator
  print "Please provide the UID of the transaction you wish to update"
  print "UID: <unix timestamp><6 character hexadecimal string>"
  print "UID Example: 16589476959D3DD8"
  print "Input q to return to the main menu"
  # get uid
  _uid = raw_input("{0} ".format(utility.cli_prompt)).lower()
  if _uid == "q":
    return utility.call_main()
  
  # find tx by uid, none = print & recall
  try:
    _old_tx = read_tx(False, _uid)
    _old_tx_index = utility.find_index_by_uid(_old_tx["uid"])
  except:
    print "Transaction not found, please try again"
    update_tx()
  
  # build new tx object
  print ""
  print "Please provide the new transaction details"
  print utility.cli_separator
  print "If you do not wish to change a field, leave it blank and press ENTER"
  print "UID will not change on updates; datetime is automatically generated"
  _new_tx.uid = _uid
  _new_tx.datetime = utility.gen_unix_timestamp()
  
  print ""
  print "Description"
  print "Current description: {0}".format(_old_tx["description"])
  print utility.cli_separator
  _new_tx_desc_input = raw_input("{0} ".format(utility.cli_prompt))
  if _new_tx_desc_input == "":
    _new_tx.description = str(_old_tx["description"])
  else:
    _new_tx.description = _new_tx_desc_input
  
  # check if credit or debit tx type
  if _old_tx["credit"] > 0:
    # if credit, only allow credit changes
    print ""
    print "Credit"
    print "Current credit: {0}".format(_old_tx["credit"])
    print utility.cli_separator
    _new_tx_credit_amt = raw_input("{0} ".format(utility.cli_prompt))
    _new_tx.debit = float(0)
    if _new_tx_credit_amt == "":
      _new_tx.credit = float(_old_tx["credit"])
    else:
      _new_tx.credit = float(_new_tx_credit_amt)
  else:
    # if debit, only allow debit changes
    print ""
    print "Debit"
    print "Current debit: {0}".format(_old_tx["debit"])
    print utility.cli_separator
    _new_tx_debit_amt = float(raw_input("{0} ".format(utility.cli_prompt)))
    _new_tx.credit = float(0)
    if _new_tx_debit_amt == "":
      _new_tx.debit = float(_old_tx["debit"])
    else:
      _new_tx.debit = float(_new_tx_debit_amt)
  
  # calculate old balance if credit or debit tx changes made
  # here were reversing the sequence, adding debits and removing credits
  _old_balance_before_tx = float(_old_tx["balance"]) + float(_old_tx["debit"] - float(_old_tx["credit"]))

  # calculate new balance
  _new_balance = float(_old_balance_before_tx) + float(_new_tx.credit) - float(_new_tx.debit)
  print ""
  print "Balance; This will be recalculated based on altered transaction debits or credits"
  print "New balance: {0}".format(_new_balance)
  print utility.cli_separator
  _new_tx.balance = float(_new_balance)

  # check against schema, err = print & recall
  _tx_validation = utility.validate_tx(_new_tx)
  if not _tx_validation["valid"]:
    print ""
    print "Transaction is not valid, please try again:"
    print _tx_validation["error"]
    raw_input("Press ENTER to restart transaction update process")
    create_tx()

  # confirm overwrite
  print ""
  print ">> Are you sure you want to overwrite this original transaction:"
  print utility.cli_separator
  utility.pretty_print_tx(_old_tx, True)
  print ">> with the following new transaction:"
  print utility.cli_separator
  utility.pretty_print_tx(_new_tx, False)
  print "IMPORTANT: This will recalculate the balances of all transactions that come after the updated transaction"
  print "Are you sure you wish to continue? (y/n)"
  _confirm_create = raw_input("{0} ".format(utility.cli_prompt)).lower()
  if _confirm_create == "y":
    # overwrite tx
    io.database[_old_tx_index] = _new_tx.as_dict()
    # recalculate balances
    utility.recalculate_balances(_old_tx_index)
    # save current database var to db.json file (overwrite)
    io.save_db()

    print "Transaction update successful"
    raw_input("Press ENTER to return to main menu")
    return utility.call_main()
  elif _confirm_create == "n":
    raw_input("Press ENTER to return to main menu")
    return utility.call_main()
  else:
    print "Invalid input"
    confirm_create()
