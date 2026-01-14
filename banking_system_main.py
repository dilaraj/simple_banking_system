from bank_user import Bank_User

class Banking_System:
    """Main class to run banking system"""
    def __init__(self):
        pass

    def run_system(self):
        print('Bank is running')
        self._store_user_information()

    
    def display_bank_menu(self):
        print('Welcome to the Bank')
        print('Please select an option using the corresponding number:')
        print('1. Create an Account')
        print('2. Credit a debit account')
        print('3. Quit')
        option = input('Please enter an option: ')

        return option
        
    
    def create_new_user(self):
        """gather information to create a new user"""
        
        print('Create an account:')
        fname = input(f'First Name: ')
        lname = input (f'Last Name: ')
        dob = input(f'DOB: ')
        email = input(f'Email: ')
        phonenum = input(f'Phone number: ')
        password = input(f'Password: ')

        #create a new user object
        new_user = Bank_User(fname, lname, dob, email, phonenum, password)
        username = (fname[0:3] + lname[0:3]).lower()
        user_dict = {
            'fname': fname,
            'lname': lname,
            'uname': username,
            'dob':dob,
            'email': email,
            'phonenum': phonenum,
            'password': password,
            }

        #return an array of needed information
        return [new_user, user_dict, username]
    
    
    def _store_user_information(self):
        """Store new user in custom file"""
        new_user = self.create_new_user()

        new_user[0].store_user(new_user[1], new_user[2])
        print(f'Account successfully created!\nYour username is: {new_user[2]}\nPlease use this username when signing in')
                                


#running banking system
bs = Banking_System()
bs.run_system()