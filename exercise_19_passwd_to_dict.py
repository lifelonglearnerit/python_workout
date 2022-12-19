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