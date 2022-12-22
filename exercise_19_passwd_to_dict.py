"""Write a function passwd_to_dict, that reads from a UNix-style "password file",
commonly stored as /etc/passwd, and returns a dict based on it.
Each line is one user record, divided into colon-separated fields. The first field
(index 0) is the username, and the third field (index 2) is the user's unique ID number.
The function should return a dict based on /etc/passwd in which the dict's keys are
usernames and the values are the users IDs
Ignore empty lines or starting from #"""


# option 1 my solution
def passwd_to_dict(file_name: str) -> dict:
    user_id: dict = {}
    with open(file_name, 'r') as f:
        passwd = f.readlines()
        for line in passwd:
            line = line.split(':')
            if line[0] == '' or '#' in line[0]:
                continue
            else:
                user_id[line[0]] = line[2]
    return user_id

print(passwd_to_dict('exercise_19_file.txt'))

# option 2 my solution
def passwd_to_dict_2(file_name: str) -> dict:
    user_id: dict = {}
    with open(file_name, 'r') as f:
        passwd = f.readlines()
        for line in passwd:
            line = line.split(':')
            if not (line[0] == '' or '#' in line[0]):
                user_id[line[0]] = line[2]
    return user_id

print(passwd_to_dict_2('exercise_19_file.txt'))


# solution from book:
def passwd_to_dict_3(file_name):
    users = {}
    with open(file_name) as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users

print(passwd_to_dict_3('exercise_19_file.txt'))

# Beyond the exercise
"""Read though /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for whom
that shell is defined as their login shell"""
import re
print(re.split(':|/','root:*:0:0::0:0:System Administrator:/var/root:/bin/sh'))

# option 1 - iteration t
def shell_login(file_name: str) -> dict:
    shell_log: dict = {}
    key_tracker: list = []
    with open(file_name) as passwd:
        for line in passwd:
            print('TO:',line)
            if not line.startswith(('#', '\n')):
                user_info = re.split(':|/', line)
                if shell_log.get(user_info[-1].strip(), 0):
                    shell_log[user_info[-1].strip()].append(user_info[0])
                else:
                    shell_log[user_info[-1].strip()] = [user_info[0]]

    return shell_log

print(shell_login('exercise_19_file.txt'))

