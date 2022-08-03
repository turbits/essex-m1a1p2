# +===================================================================+
# Author: Trevor Woodman
# Github: https://github.com/turbits
# Repo: https://github.com/turbits/essex-m1a1p2
# Project: Assignment 1, Part 2: Bankbook Program
# Course: Launching into Computer Science (LCS_PCOM7E June 2022)
# School: University of Essex
# Date: July/August, 2022
# +===================================================================+

import os
from .. import utility
from .. import io

def display_all_tx(pretty=True):
  if len(io.database) == 0:
    print "\nNo transactions to display"
    print "Press ENTER to return to main menu"
    utility.get_input()
    return utility.call_main()
  ascii_db = [str(tx) for tx in io.database]
  print ""
  for tx in io.database:
    utility.pretty_print_tx(tx, True)
    print utility.cli_separator
  print "\n Press ENTER to return to main menu"
  utility.get_input()
  return utility.call_main()
