# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

import utility

class Transaction:
  def __init__(self, uid, datetime, description, credit, debit, balance):
    self.uid = utility.gen_uid()
    self.datetime = utility.gen_unix_timestamp()
    self.description = description
    self.credit = float(credit)
    self.debit = float(debit)
    self.balance = float(balance)

  def as_dict(self):
    return {
      "uid": self.uid,
      "datetime": self.datetime,
      "description": self.description,
      "credit": float(self.credit),
      "debit": float(self.debit),
      "balance": float(self.balance)
    }
