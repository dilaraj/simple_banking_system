from bank_user import Bank_User
import random

class Banking_System:
    """Main class to run banking system"""
    def __init__(self):
        pass

    def run_system(self):
        while True:
            option = self.display_bank_menu()
            if option == '1':
                self.create_new_user()
            elif option == '2':
                self.create_debit_account()
            elif option == '3':
                pass
            elif option == '4':
                break
        

    
    def display_bank_menu(self):
        """Display bank menu"""
        print('\nWelcome to the Bank')
        print('Please select an option using the corresponding number:')
        print('1. Create an Account')
        print('2. Create a Debit Account')
        print('3. Login to your Account')
        print('4. Quit')
        option = input('Please enter an option: ')

        return option
        
    
    def create_new_user(self):
        """Create a dictonary and store user object as json"""
        new_user = self._new_user_object()        
        user_dict = {
            'fname': new_user.first_name,
            'lname': new_user.last_name,
            'uname': new_user.username,
            'dob':new_user.DOB,
            'email': new_user.email,
            'phonenum': new_user.phone_num,
            'password': new_user.password,
            }
        
        self._store_user_information(new_user, user_dict)

    def _collect_user_information(self):
        """Collect user information and return an array"""
        print('Create an account:')
        fname = input(f'First Name: ')
        lname = input (f'Last Name: ')
        dob = input(f'DOB: ')
        email = input(f'Email: ')
        phonenum = input(f'Phone number: ')
        password = input(f'Password: ')


        return [fname, lname, dob, email, phonenum, password]                                                                  

    def _new_user_object(self):
        """Create a new user object"""
        new_user = self._collect_user_information()
        fname = new_user[0]
        lname = new_user[1]
        dob = new_user[2]
        email = new_user[3]
        phone_num = new_user[4]
        password = new_user[5]

        #create a new user object
        return Bank_User(fname, lname, dob, email, phone_num, password)
    
    
    def _store_user_information(self, new_user, user_dict):
        """Store new user in custom file"""
        new_user.store_user(user_dict, new_user.username)
        print(f'Account successfully created!\nYour username is: {new_user.username}\nPlease use this username when signing in')
                                

    def create_debit_account(self):
        username = input('Enter username: ')
        user_exists = Bank_User.confirm_user_exists(username)
        if user_exists:
            #confirm password
            user = Bank_User.load_user_file(username)
            entered_password = input('Enter Password: ')

            if entered_password == user['password']:
                print('Welcome to Debit Card Creation Centre')
                #create debit account
                self._create_debit_card_info(user, username)
            else:
                print('Password Incorrect!')
        else: 
            print('Username does not exist')


    def _create_debit_card_info(self, user, username):
        debit_number = random.randint(1000000000000000, 9999999999999999)
        debit_pin = input('Enter 4 digit pin: ')

        debit_info = {'debit_num':debit_number, 'debit_pin':debit_pin}
        user.update({'debit_info':debit_info})
        Bank_User.update_user(username, user)
        print('Card was created successfully')

         

#running banking system
bs = Banking_System()
bs.run_system()