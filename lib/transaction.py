# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

import utility

class Transaction:
  def __init__(self, description, credit, debit, balance, datetime="", uid=""):
    self.uid = utility.gen_uid()
    self.datetime = utility.gen_unix_timestamp()
    self.description = description
    self.credit = credit
    self.debit = debit
    self.balance = balance

  def as_dict(self):
    return {
      "uid": self.uid,
      "datetime": self.datetime,
      "description": self.description,
      "credit": self.credit,
      "debit": self.debit,
      "balance": self.balance
    }
