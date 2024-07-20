#!/usr/bin/python3

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string")
        self.__username = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address")
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")
        self.__password = value

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"
