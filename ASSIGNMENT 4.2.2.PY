class UserProfile:
    def __init__(self, username, email, password, security_question):
        self._username = username
        self._email = email
        self.__password = password
        self.__security_question = security_question

    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email

    def set_password(self, new_password):
        self.__password = new_password

    def validate_password(self, entered_password):
        return entered_password == self.__password

    def reset_password(self, new_password):
        self.__password = new_password
        print("Password reset successful.")

    def get_security_question(self):
        return self.__security_question

    def set_security_question(self, new_security_question):
        self.__security_question = new_security_question
