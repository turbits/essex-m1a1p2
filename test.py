# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from lib.operations.create_tx import create_tx

test_results = {
  create: False,
  read: False,
  update: False,
  delete: False,
  sort: False,
}

def test_create_tx():
  _tx_obj = Transaction("", 0, "Fee", 0, 10, 200)
  _passed = create_tx(_tx_obj)

  test_results.create = _passed


