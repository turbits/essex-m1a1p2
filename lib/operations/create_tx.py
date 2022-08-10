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

# This function walks the user through creating a valid tx object,
# validates it, then adds it to the database
def create_tx(tx_obj=None):
  _tx_obj = Transaction("", 0, 0, 0, "", "")
  _prev_balance = None
  _bal_change_op = None

  # confirm create, no = print & recall
  def confirm_create():
    print "Is this correct? (y/n)"
    _confirm_create = utility.get_input()
    if _confirm_create == "y":
      # add to database
      io.database.append(_tx_obj.as_dict())
      # save current database var to db.json file (overwrite)
      io.save_db()

      print "Transaction creation successful"
      print "Press ENTER to return to main menu"
      utility.get_input()
      return utility.call_main()
    elif _confirm_create == "n":
      print "Press ENTER to return to main menu"
      utility.get_input()
      return utility.call_main()
    else:
      print "Invalid input"
      confirm_create()

  # bypass creation if tx_obj passed in
  if tx_obj is not None:
    print "Transaction to be created:"
    print utility.cli_seperator
    utility.pretty_print_tx(tx_obj)
    print utility.cli_seperator
    confirm_create()

  print ""
  print "Creating a new transaction"
  print utility.cli_separator
  print "Follow the prompts to create a new transaction."
  print "To return to the main menu, enter q"

  # generate uid (unix ts + 6 random hex char)
  _tx_obj.uid = utility.gen_uid()

  # generate datetime (unix timestamp)
  _tx_obj.datetime = utility.gen_unix_timestamp()

  # get the description
  print "Enter a description or press ENTER to use defaults"
  _tx_obj.description = utility.get_input()
  if _tx_obj.description.lower() == "q":
    return utility.call_main()

  # check the transaction type (credit or debit)
  def tx_type_menu():
    print ""
    print "Is this a credit or a debit?"
    print "1: Credit"
    print "2: Debit"
    _credit_or_debit = utility.get_input()
    if _credit_or_debit == "1":
      return "credit"
    elif _credit_or_debit == "2":
      return "debit"
    else:
      print "Invalid input"
      tx_type_menu()
  _credit_or_debit = tx_type_menu()

  # get transaction amount
  def tx_amount():
    print ""
    if _credit_or_debit == "credit":
      print "Enter credit amount: "
      _input = utility.get_input()
      try:
        _tx_obj.credit = float(_input)
        _tx_obj.debit = float(0)
      except ValueError:
        print "Invalid input"
        tx_amount()
    elif _credit_or_debit == "debit":
      print "Enter debit amount: "
      _input = utility.get_input()
      try:
        _tx_obj.debit = float(_input)
        _tx_obj.credit = float(0)
      except ValueError:
        print "Invalid input"
        tx_amount()
    else:
      print "Invalid input"
      tx_amount()
  tx_amount()

  # calculate the balance
  # if there is no previous tx, set balance to credit amount
  if len(io.database) == 0:
    _tx_obj.balance = _tx_obj.credit
  # if there is a previous tx, set balance to previous balance +/- credit and debit amounts
  else:
    _db_len = len(io.database)
    _prev_balance = io.database[_db_len - 1]["balance"]
    _tx_obj.balance = _prev_balance + float(_tx_obj.credit) - float(_tx_obj.debit)

  # create a description using tx type if no description given
  if _tx_obj.description == "":
    if _tx_obj.credit > 0:
      _tx_obj.description = "Credit"
    elif _tx_obj.debit > 0:
      _tx_obj.description = "Debit"
    else:
      _tx_obj.description = "Other"
  
  # check against schema, err = print & recall create
  _tx_validation = utility.validate_tx(_tx_obj)
  if not _tx_validation["valid"]:
    print ""
    print "Transaction is not valid, please try again:"
    print _tx_validation["error"]
    print "\nPress ENTER to restart transaction creation process"
    utility.get_input()
    create_tx()

  # display new tx for visual confirmation
  print ""
  print "Transaction to be created:"
  print utility.cli_separator
  utility.pretty_print_tx(_tx_obj)
  print utility.cli_separator

  confirm_create()

  return True
