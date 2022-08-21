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
from lib.operations.sort_tx import sort_tx

test_results = {
  "insert": False,
  "search": False,
  "delete": False,
  "sort": False,
}

def test_insert_tx():
  # create a test tx
  _tx_obj = Transaction(uid="", datetime=0, description="test-insert", debit=0, credit=200, balance=0)
  # insert the tx
  _passed = insert_tx(_tx_obj)
  # result
  test_results["insert"] = _passed
  return _passed

def test_search_tx():
  # create test tx with specific description
  _tx_obj = Transaction(uid="", datetime=0, description="test-search", debit=0, credit=200, balance=0)
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

def test_delete_tx():
  # create test tx with specific description
  _tx_obj = Transaction(uid="", datetime=0, description="test-delete", debit=0, credit=10, balance=200)

  try:
    # insert the tx
    insert_tx(_tx_obj)
    # search for the tx by description
    _search_result = search_tx("description", "test-delete")
    if _search_result not in [None, "", []] and _search_result[0]["description"] == "test-delete":
      # remove test tx
      _passed = delete_tx(_search_result[0]["uid"])
  except:
    _passed = False
  # result
  test_results["delete"] = _passed
  return _passed

def test_sort_tx():
  # create first test tx
  _tx_obj_1 = Transaction(uid="", datetime=0, description="b_test-sort1", debit=0, credit=200, balance=0)
  # create second test tx
  _tx_obj_2 = Transaction(uid="", datetime=0, description="a_test-sort2", debit=44, credit=0, balance=0)

  _passed = False
  _passed_1 = False
  _passed_2 = False

  # insert both transactions
  insert_tx(_tx_obj_1)
  insert_tx(_tx_obj_2)

  # search for the first tx by description
  _search_result_1 = search_tx("description", "b_test-sort1")
  # search for the second tx by description
  _search_result_2 = search_tx("description", "a_test-sort2")

  # add results to a list
  _search_results = [_search_result_1[0], _search_result_2[0]]

  # Test 1: Sort by balance descending
  # sort the transactions by balance (descending)
  _sorted_txs = sort_tx(_search_results, "balance", True)
  # check that the first tx is the highest balance
  if _sorted_txs[0]["balance"] > _sorted_txs[1]["balance"]:
    _passed_1 = True
  else:
    print "ERROR: First tx not highest balance"
    _passed_1 = False
  
  # Test 2: Sort by description ascending
  # sort the transactions by description (ascending)
  _sorted_txs = sort_tx(_search_results, "description", False)
  # check that the last tx is the highest description(alphabetically)
  if _sorted_txs[1]["description"] > _sorted_txs[0]["description"]:
    _passed_2 = True
  else:
    print "ERROR: Last tx not highest description"
    _passed_2 = False

  # remove test transactions
  delete_tx(_search_result_1[0]["uid"])
  delete_tx(_search_result_2[0]["uid"])

  # determine pass
  if _passed_1 and _passed_2:
    _passed = True
  else:
    _passed = False
  
  # return result
  test_results["sort"] = _passed
  return _passed

def test_all():
  test_insert_tx()
  test_search_tx()
  test_delete_tx()
  test_sort_tx()

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
    test_delete_tx()
    print gen_test_result("Delete Test Result", test_results["delete"])
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  elif choice == "5":
    test_sort_tx()
    print gen_test_result("Sort Test Result", test_results["sort"])
    raw_input("Press ENTER to return to testing menu")
    return test_menu()
  else:
    print "Invalid option"
    return test_menu()

test_menu()
