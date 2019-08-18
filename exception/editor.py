import exception as auth

# set up test user and permission
auth.authenticator.signup('joe', 'joepass')
auth.authorizor.add_permission('paint')
auth.authorizor.add_permission('draw')
auth.authorizor.check_permission('paint', 'joe')

class Editor:

    def __init__(self):
        self.username = None
        self.menu_map = {
                            'login' : self.login,
                            'test' : self.test,
                            'change' : self.change,
                            'quit' : self.quit
                        }

    def login(self):
        logged_in = False

        while not logged_in:
            username = input('username : ')
            password = input('password : ')
            try:
                logged_in = exception.authenticator.login(
                    username, password)
            except auth.InvalidUsername:
                print("Sorry, the username does not exist")
            except auth.InvalidPassword:
                print("Sorry, the password is incorrect")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            auth.authorizor(permission, self.username)
        except auth.NotLoggedInError as e:
            print('{} is not logged in'.format(e.username))
            return False
        except auth.NotPermittedError as e:
            print('{0} permission is denied to {}'.format(permission,
                                                          e.username))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("testing program")

    def change(self):
        if self.is_permitted("change program"):
            print('Changing program')

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''

            while True:
                print("""
    Please Enter a command:
    login\tLogin
    test\tTest the program
    change\tChange the program
    quit\tQuit""")
                answer = input('enter a command').lower()

                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print('command : {} does not exist'.format(answer))

                else:
                    func()
                finally:
                    print('thankyou for using the editor')

def main():
    Editor().menu()

main()
