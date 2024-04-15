# DO NOT MODIFY THIS CODE
# DO NOT DELETE THIS main.py FILE
# KEEP main.py CLOSED

import os

# get list of files and put into list
file_list = os.listdir()

# create new list of just .py files (not including main.py)
program_list = [f for f in file_list if (f.endswith(".py") and f != "main.py")]

# main menu (list of programs to run)
keep_going = True
while keep_going:
  print("--- Which file would you like to run? (Enter Option) ---")
  print(0,"-", "EXIT")
  menu_option = 1
  for f in program_list:
      print(menu_option,"-", f)
      menu_option += 1
# get user input  
  selection = input("Enter Option: ")
#validate input
  if selection.isnumeric() and int(selection) <= len(program_list) and int(selection) >= 0:
      keep_going = False
  else:
    print("*** Invalid Option ***")

# run selected program (or exit if user enters 0)
if int(selection) == 0:
  print("Goodbye")
else:
  print("--- Running", program_list[int(selection)-1], "---")
  file_name = program_list[int(selection)-1]
  with open(file_name) as file:
    exec(file.read())