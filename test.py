# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

from lib import utility
from lib.utility import gen_test_result
from lib.transaction import Transaction
from lib.operations.insert_tx import insert_tx
from lib.operations.search_tx import search_tx
from lib.operations.delete_tx import delete_tx

test_results = {
  "insert": False,
  "search": False,
  "update": False,
  "delete": False,
  "sort": False,
}

def test_insert_tx():
  # create a test tx
  _tx_obj = Transaction(uid="", datetime=0, description="test-insert", debit=0, credit=10, balance=200)
  # insert the tx
  _passed = insert_tx(_tx_obj)
  # result
  test_results["insert"] = _passed
  return _passed

def test_search_tx():
  # create test tx with specific description
  _tx_obj = Transaction(uid="", datetime=0, description="test-search", debit=0, credit=10, balance=200)
  try:
    # insert the tx
    insert_tx(_tx_obj)
    # search for the tx by description
    _search_result = search_tx("description", "test-search")
    if _search_result not in [None, "", []] and _search_result[0]["description"] == "test-search":
      _passed = True
      # remove test tx
      delete_tx(_search_result[0]["uid"])
  except:
    _passed = False
  # result
  test_results["search"] = _passed
  return _passed


def test_all():
  test_insert_tx()
  
  # other tests

  for test in test_results:
    if test_results[test] is False:
      print "{0} test failed".format(test)
    else:
      print "{0} test passed".format(test)
  
  if all(test_results.values()):
    print "All tests passed"
  else:
    print "Some tests failed"

  utility.get_input("Press ENTER to return to the main menu")
  return utility.call_main()

def test_menu():
  print "\nBankbook Test Suite"
  print utility.cli_separator
  print "Please select a testing option:"
  print """1: All tests
2: Insert transaction
3: Search transaction
4: Delete transaction
5: Sort transactions
q: Exit to Main Menu"""

  choice = utility.get_input()
  if choice == "q":
    return utility.call_main()
  elif choice == "1":
    test_all()
  elif choice == "2":
    test_insert_tx()
    print gen_test_result("Insert Test Result", test_results["insert"])
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  elif choice == "3":
    test_search_tx()
    print gen_test_result("Search Test Result", test_results["search"])
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  elif choice == "4":
    # delete
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  elif choice == "5":
    # sort
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  else:
    print "Invalid option"
    return test_menu()

test_menu()
