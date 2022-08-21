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
import random
import time
import io

cli_prompt = "$"
cli_separator = "============================================="

def get_input(text=None):
  if text is not None:
    _in = raw_input("{0}:\n{1} ".format(text, cli_prompt))
    return _in.lower()
  else:
    _in = raw_input("{0} ".format(cli_prompt))
    return _in.lower()

def call_main():
  # call the main script
  os.system("python main.py")

def print_cwd():
  print ""
  print cli_separator
  print "DEBUG: CURRENT WORKING DIRECTORY:"
  print os.getcwd()
  print cli_separator
  print ""

def gen_unix_timestamp():
  # gets the current unix timestamp, truncated (convert to int to remove millisecond decimals), and returns it
  return int(time.time())

def get_human_timestamp(unix_timestamp):
  # converts a unix timestamp to a human readable datetime and returns it
  return datetime.fromtimestamp(int(unix_timestamp).strftime('%d/%m/%Y %H:%M:%S'))

def gen_hex():
  # generates a random hexadecimal string of length 6
  # see references for more info:
  # https://stackoverflow.com/a/2511238
  return "".join(random.choice("0123456789ABCDEF") for i in range(6))

def gen_uid():
  # concatenates the timestamp and the hex string together to get a UID
  _timestamp = gen_unix_timestamp()
  _hex = gen_hex()
  return str(_timestamp) + _hex

def show_tx_schema():
  # in case we want to see the schema
  print """\nTransaction Schema
==================================
property: <data type or description>
==================================
uid: [Custom UID Type] ex: 1659562753141D91 (truncated unix timestamp + 6 random hex chars)
datetime: [Int] ex: 1659562753 (truncated unix timestamp)
description: [String] ex: Debit
credit: [Float] ex: 0.00
debit: [Float] ex: 4.00
balance: [Float] ex: 56.54"""
  print "\nPress ENTER to return to main menu"
  get_input()
  call_main()

def validate_tx(tx):
  # basic type checking and some string length checking for rudimentary schema validation
  _valid = True
  _error = ""
  if not isinstance(tx.uid, str):
    _valid = False
    _error = "uid is not a string"
  elif not isinstance(tx.datetime, int):
    _valid = False
    _error = "datetime is not an int"
  elif not isinstance(tx.description, str):
    _valid = False
    _error = "description is not a string"
  elif len(tx.description) > 100:
    _valid = False
    _error = "description is too long"
  elif not isinstance(tx.credit, float):
    _valid = False
    _error = "credit is not a float"
  elif not isinstance(tx.debit, float):
    _valid = False
    _error = "debit is not a float"
  elif not isinstance(tx.balance, float):
    _valid = False
    _error = "balance is not a float"
  return {"valid": _valid, "error": _error}

def get_balance():
  if len(io.database) == 0:
    return 0
  else:
    return io.database[len(io.database) - 1]["balance"]

def recalculate_balances(index):
  # recalc balance of all txs at and after the given index
  for i in range(index, len(io.database)):
    if i == 0:
      io.database[i]["balance"] = io.database[i]["credit"]
    else:
      io.database[i]["balance"] = io.database[i - 1]["balance"] + io.database[i]["credit"] - io.database[i]["debit"]
  return

def calculate_new_tx_balance(tx_obj):
  _db_length = len(io.database)
  _bal = tx_obj.balance
  # calculate the balance
  if _db_length == 0:
    _bal = float(tx_obj.credit) if tx_obj.credit > 0 else float(tx_obj.debit)
  else:
    _prev_bal = io.database[_db_length - 1]["balance"]
    _bal = float(_prev_bal + tx_obj.credit - tx_obj.debit)
  return _bal

def pretty_print_tx(tx, dict=False):
  # dict dot notation not supported in Python 2.x?
  if dict:
    # prints a transaction from a dict
    print """uid: {0}
datetime: {1}
description: {2}
credit: {3}
debit: {4}
balance: {5}""".format(tx["uid"], tx["datetime"], tx["description"], tx["credit"], tx["debit"], tx["balance"])
  else:
    # prints a transaction from a Transaction object
    print """uid: {0}
datetime: {1}
description: {2}
credit: {3}
debit: {4}
balance: {5}""".format(tx.uid, tx.datetime, tx.description, tx.credit, tx.debit, tx.balance)

def get_index_by_tx_uid(uid):
  # finds the index of a transaction by its uid
  for i, tx in enumerate(io.database):
    if tx["uid"] == uid:
      return i
  return -1

def get_tx_by_uid(uid):
  # finds the transaction by its uid
  _index = get_index_by_tx_uid(uid)
  if _index == -1:
    return None
  else:
    return io.database[_index]

def gen_test_result(text, result):
  _r = "Passed" if result == True else "Failed"
  return "{0}: {1}".format(text, _r)
