# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from .. import io
from .. import utility

# returns a list or None
def search_tx(prop, value, all_txs=False):
  _tx_list = io.database
  _tx_list_filtered = []
  if len(_tx_list) == 0:
    return None
  elif all_txs:
    _tx_list_filtered = _tx_list
  else:
    for _tx in _tx_list:
      if str(_tx[prop]) == str(value):
        _tx_list_filtered.append(_tx)
  return _tx_list_filtered
