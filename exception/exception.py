import hashlib

# defining exceptions
class AuthException(Exception):
    ''' authenticate the login.'''

    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExist(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

class NotLoggedInError(AuthException):
    pass


class User:

    def __init__(self, username, password):
        ''' Initialise the username and password
    encrypt the password before storing
    declare that logged in info.'''

        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged_in = False

    def _encrypt_password(self, password):
        ''' Encrypt the password with the username.'''

        hash_string = self.username + password
        hash_string = hash_string.encode('utf')
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        ''' check if the input password matches the
    correct input.'''

        password = self._encrypt_password(password)
        return self.password == password

class Authenticator:
    ''' Map username to the user.'''

    def __init__(self):
        self.users = {}

    def signup(self, username, password):
        ''' Add a user with username and password
    check if the username already exist
    check for the length of password.'''

        if username in self.users:
            raise UserAlreadyExist(username)
        if len(password) < 6:
            raise PasswordTooShort(usename)

        self.users[username] = User(username, password)

    def login(self, username, password):
        ''' login an already existing user
    check for invalid login information.'''

        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True

        return True

    def is_logged_in(self, username):
        ''' To check if ap articular username is logged in'''

        if username in self.users:
            return self.users[username].is_logged_in
        return False


# adding default authenticator to client can access easily
authenticator = Authenticator()


class Authorizor:

    def __init__(self, authenticator=authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, permission):
        ''' create a new permission that
    user can be added to'''

        try:
            perm_set = self.permissions[permission]
        except KeyError:
            self.permissions[permission] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, permission, username):
        '''grant the given permission to the user'''

        try:
            perm_set = self.permissions[permission]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

# default authorizor
authorizor = Authorizor()
        
            


























