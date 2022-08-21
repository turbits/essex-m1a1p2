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
from ..transaction import Transaction
from ..operations.insert_tx import insert_tx

def create_tx_menu():
  _tx_obj = Transaction("", 0, "", 0, 0, 0)
  print "Create Transaction"
  print utility.cli_separator
  
  # get description
  _tx_obj.description = utility.get_input("Please provide a description of the transaction")
  if _tx_obj.description == "q":
    return utility.call_main()
  
  # determine credit or debit and amount
  _credit_or_debit = utility.get_input("Is this a credit or a debit transaction? (c/d)")
  if _credit_or_debit == "q":
    return utility.call_main()

  _amount = utility.get_input("Please provide the amount of the transaction")
  if _amount == "q":
    return utility.call_main()
    
  if _credit_or_debit == "c":
    _tx_obj.credit = float(_amount)
    _tx_obj.debit = 0
  elif _credit_or_debit == "d":
    _tx_obj.debit = float(_amount)
    _tx_obj.credit = 0
  else:
    print "Invalid selection"
    return create_tx_menu()
  
  # get balance
  _tx_obj.balance = utility.calculate_new_tx_balance(_tx_obj)

  # confirm create
  print utility.cli_separator
  print "Confirm create transaction:"
  utility.pretty_print_tx(_tx_obj)
  print utility.cli_separator
  _confirm_create = utility.get_input("Are you sure you want to create this transaction? (y/n)")
  if _confirm_create == "y":
    # insert transaction
    # returns True or False
    return insert_tx(_tx_obj)
  else:
    return False
