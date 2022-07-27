import utility

class Transaction:
  def __init__(self, description, credit, debit, balance, datetime="", uid=""):
    self.uid = utility.gen_uid()
    self.datetime = utility.gen_unix_timestamp()
    self.description = description
    self.credit = credit
    self.debit = debit
    self.balance = balance
