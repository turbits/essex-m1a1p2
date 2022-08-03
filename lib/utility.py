# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

import os
import random
import time
import io

cli_prompt = "$"
cli_separator = "============================================="

def get_input(lower=True):
  if lower:
    return raw_input("{0} ".format(cli_prompt).lower())
  else:
    return raw_input("{0} ".format(cli_prompt))

def call_main():
  # call the main script
  os.system("python bankbook.py")

def print_cwd():
  print ""
  print cli_separator
  print "DEBUG: CURRENT WORKING DIRECTORY:"
  print os.getcwd()
  print cli_separator
  print ""

def gen_unix_timestamp():
  # gets the current unix timestamp, truncated
  return str(int(time.time()))

def gen_hex():
  # generates a random hexadecimal string of length 6
  return "".join(random.choice("0123456789ABCDEF") for i in range(6))

def gen_uid():
  # concatenates the timestamp and the hex string together to get a UID
  _timestamp = gen_unix_timestamp()
  _hex = gen_hex()
  return _timestamp + _hex

def show_tx_schema():
  # in case we want to see the schema
  print """
  Transaction Schema
  ==================================
  property: <data type or description>
  ==================================
  uid: int (truncated unix timestamp) + 6 random hex chars
  datetime: int (truncated unix timestamp)
  description: string
  credit: float
  debit: float
  balance: float
  """

def validate_tx(tx):
  # basic type checking and some string length checking for rudimentary schema validation
  _valid = True
  _error = ""
  if not isinstance(tx.uid, str):
    _valid = False
    _error = "uid is not a string"
  elif not isinstance(tx.datetime, str):
    _valid = False
    _error = "datetime is not a string"
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
  # recalc balance of all txs after index
  for i in range(index, len(io.database)):
    if i == 0:
      io.database[i]["balance"] = io.database[i]["credit"]
    else:
      io.database[i]["balance"] = io.database[i - 1]["balance"] + io.database[i]["credit"] - io.database[i]["debit"]
  return

def pretty_print_tx(tx, dict=False):
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

def find_index_by_uid(uid):
  # finds the index of a transaction by its uid
  for i, dict in enumerate(io.database):
    if dict["uid"] == uid:
      return i
  return -1
