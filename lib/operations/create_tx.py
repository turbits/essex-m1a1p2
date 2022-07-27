from .. import utility

### This function walks the user through creating a valid transaction object
def create_tx():
  print ""
  print "Creating a new transaction"
  print "=========================="
  print "Follow the prompts to create a new transaction"


  # generate uid (unix + 6 random hex char)
  _uid = utility.gen_uid()

  # generate datetime (unix timestamp)
  _datetime = utility.gen_unix_timestamp()

  # get the description
  print "Enter a description or press ENTER to use defaults"
  _description = raw_input("%s " % utility.cli_prompt)

  # check the transaction type (credit or debit)
  def tx_type_menu():
    print "Is this a credit or a debit?"
    print "1: Credit"
    print "2: Debit"
    _credit_or_debit = raw_input("%s " % utility.cli_prompt)
    if _credit_or_debit == "1":
      return "credit"
    elif _credit_or_debit == "2":
      return "debit"
    else:
      print "Invalid choice"
      tx_type_menu()

  _credit_or_debit = tx_type_menu()

  def confirm_tx_type():
    if _credit_or_debit == "credit":
      print "Enter credit amount: "
      _credit = raw_input("%s " % utility.cli_prompt)
      _debit = "0"
    elif _credit_or_debit == "debit":
      print "Enter debit amount: "
      _debit = raw_input("%s " % utility.cli_prompt)
      _credit = "0"
    else:
      print "Invalid choice"
      confirm_tx_type()  
  confirm_tx_type()

  # calculate balance
  # if there is no previous tx, set balance to credit amount
  print "Calculating balance..."
  if database.length == 0:
    _balance = _credit
  # if there is a previous tx, set balance to previous balance +/- credit and debit amounts
  else:
    _balance = database[-1].balance + float(_credit) - float(_debit)
  print "Balance %s" % _balance

  # create a description using tx type if none given
  if _description == "":
    if _credit > 0:
      _description = "Credit"
    elif _debit > 0:
      _description = "Debit"
    else:
      _description = "Other"
  
  # check against schema, err = print & recall create
  print "Verifying transaction..."
  _tx_schema_check = utility.check_tx_schema(_uid, _datetime, _description, _credit, _debit, _balance)

  if not _tx_schema_check.valid:
    print "Transaction is not valid, please try again:"
    print _tx_schema_check.error
    raw_input("Press ENTER to restart transaction creation process")
    create_tx()

  # display new tx
  print utility.cli_separator
  print "Transaction:"
  print "uid: %s" % _uid
  print "datetime: %s" % _datetime
  print "description: %s" % _description
  print "credit: %s" % _credit
  print "debit: %s" % _debit
  print "balance: %s" % _balance
  raw_input("Press ENTER to continue")

  # confirm create, no = print & recall
  def confirm_create():
    print "Is this correct? (y/n)"
    _confirm_create = raw_input("%s" % utility.cli_prompt)
    if _confirm_create.lower() == "y":
      # add to database
      database.append(Transaction(_uid, _datetime, _description, _credit, _debit, _balance))
      print "Transaction added"
    elif _confirm_create.lower() == "n":
      raw_input("Press ENTER to return to main menu")
      return
    else:
      print "Invalid choice"
      confirm_create()
  confirm_create()
