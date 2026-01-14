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
        self.username = (fname[0:3] + lname[0:3]).lower()

    
    def store_user(self, new_user, userName):
        try:
            path = f'bank_users/{userName}_account.json'
            content = json.dumps(new_user, indent=4)
            with open(path, 'w') as f:
                f.write(content)
        except FileNotFoundError:
            pass

    
    def confirm_user_exists(userName):
        user_path = Path(f'bank_users/{userName}_account.json')
        if user_path.is_file():
            return True
        else:
            return False
        
    
    def load_user_file(username):
        path = Path(f'bank_users/{username}_account.json')
        content = path.read_text()
        user = json.loads(content)

        return user
        
        
    
    def update_user(username, new_user):
        try:
            path = f'bank_users/{username}_account.json'
            content = json.dumps(new_user, indent=6)
            with open(path, 'w') as f:
                f.write(content)
        except FileNotFoundError:
            pass
        
