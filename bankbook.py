import os.path
from lib.operations.create_tx import create_tx
from lib import ascii_art
from lib.utility import cli_prompt, cli_separator

def show_title():
  print ascii_art.title

def main_menu():
  show_title()
  print("""1: Create transaction
2: Read transaction
3: Update transaction
4: Delete transaction
5: Display all transactions
6: Sort and display all transactions
7: Display transaction schema
q: Exit program""")
  print cli_separator
  choice = raw_input('%s ' % cli_prompt)

  if choice.lower() == 'q':
    exit()
  elif choice == '1':
    # create_tx()
    create_tx()
  elif choice == '2':
    # read_tx()
    print('2')
    main_menu()
  elif choice == '3':
    # update_tx()
    print('3')
    main_menu()
  elif choice == '4':
    # delete_tx()
    print('4')
    main_menu()
  elif choice == '5':
    # display_all_tx()
    print('5')
    main_menu()
  elif choice == '6':
    # sort_display_all_tx()
    print('6')
    main_menu()
  elif choice == '7':
    # show_tx_schema()
    print('7')
    main_menu()
  else:
    print('Invalid choice')
    main_menu()

def __main__():
  main_menu()

__main__()
