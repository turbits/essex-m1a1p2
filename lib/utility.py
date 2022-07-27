import random
import time

cli_prompt = '$'
cli_separator = '============================================='

def gen_unix_timestamp():
  return str(int(time.time()))

def gen_hex():
  return ''.join(random.choice('0123456789ABCDEF') for i in range(16))

def gen_uid():
  _timestamp = gen_unix_timestamp()
  _hex = gen_hex()
  return _timestamp + _hex

def show_tx_schema():
  print("""
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
  """)

def check_tx_schema(uid, datetime, description, credit, debit, balance):
  _valid = True
  _error = ""
  if not isinstance(uid, str):
    _valid = False
    _error = "uid is not a string"
  elif not isinstance(datetime, str):
    _valid = False
    _error = "datetime is not a string"
  elif not isinstance(description, str):
    _valid = False
    _error = "description is not a string"
  elif len(description) > 100:
    _valid = False
    _error = "description is too long"
  elif not isinstance(credit, float):
    _valid = False
    _error = "credit is not a float"
  elif not isinstance(debit, float):
    _valid = False
    _error = "debit is not a float"
  elif not isinstance(balance, float):
    _valid = False
    _error = "balance is not a float"
  return {'valid': _valid, 'error': _error}
