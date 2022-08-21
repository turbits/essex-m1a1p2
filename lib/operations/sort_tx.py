# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from operator import itemgetter

def sort_tx(list, prop, rev):
  _sorted_data = []
  if rev is None:
    _sorted_data = list
  else:
    # sort transactions
    _sorted_data = sorted(list, key=itemgetter(str(prop)), reverse=rev)

  return _sorted_data
