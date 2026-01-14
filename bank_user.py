import json
from pathlib import Path

class Bank_User():
    """Class to create and store information about each bank user"""
    def __init__(self, fname, lname, dob, email, phonenum, passw):
        self.first_name = fname
        self.last_name = lname
        self.DOB = dob
        self.email = email
        self.phone_num = phonenum
        self.password = passw

    
    def store_user(self, new_user, userName):
        try:
            path = f'bank_users/{userName}_account.json'
            content = json.dumps(new_user, indent=4)
            with open(path, 'w') as f:
                f.write(content)
        except FileNotFoundError:
            pass
