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
import json

db_path = "db.json"
database = []

# check db file exist
def check_db():
  return os.path.exists(db_path)

# load db file
def load_db():
  with open(db_path, "r") as dat:
    try:
      _dat = json.load(dat)
      global database
      database = _dat
      print "Database loaded from file: ./db.json"
      print "Items in database: {0}".format(len(database))
    except:
      print "Error reading database file: ./db.json"

# create new db file
def create_db():
  with open(db_path, "w") as dat:
    try:
      dat.write("[]")
      print "New database file created: ./db.json"
    except:
      print "Error creating database file, check file permissions"

# save to existing db file
def save_db():
  _json = json.dumps(database, indent=2)
  with open(db_path, "w") as dat:
    try:
      dat.write(_json)
      return
    except:
      print "Error saving to database, check file permissions"
      return

def delete_db():
  os.remove(db_path)
  print "Database file deleted: ./db.json"

def get_db_var():
  print database

def get_db_json():
  with open(db_path, "r") as dat:
    try:
      _dat = json.load(dat)
      print _dat
    except:
      print "Error reading database file: ./db.json"
