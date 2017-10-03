import os
from nick import create_nick

# remove usernicks.csv if it exist
os.remove('usernicks.csv')

# open user csv file
with open('users.csv') as userfile:
    # read the lines
    for row in userfile.readlines():
        # split line on ","
        user = row.strip().split(',')
        # assign values
        firstname = user[0]
        lastname = user[1]

        # call create_nick to build a username
        nickname = create_nick(firstname, lastname)

        # write user and nickname to file,

        with open('usernicks.csv', 'a') as usernicksfile:
            line = firstname + ',' + lastname + ',' + nickname + '\n'
            usernicksfile.write(line)
