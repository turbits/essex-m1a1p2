# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July 27th, 2022
# +===================================================================+

import os
from .. import utility
from .. import io

def display_all_tx(pretty=True):
  if len(io.database) == 0:
    print ""
    print "No transactions to display"
    print "Press ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()
  ascii_db = [str(tx) for tx in io.database]
  print ""
  for tx in io.database:
    utility.pretty_print_tx(tx, True)
    print utility.cli_separator
  print ""
  print "Press enter to return to main menu"
  utility.get_input()
  return utility.call_main()
