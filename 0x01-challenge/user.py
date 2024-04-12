#!/usr/bin/python3
""" 
Class User to manage user email properties.
"""

class User:
    """
    A class to represent a User with an email attribute.
    """

    def __init__(self):
        """
        Initializes the User object with email set to None.
        """
        self.__email = None

    @property
    def email(self):
        """
        Returns the email of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Sets the email of the user, raising an error if the value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"  # Set the email
    print(u.email)  # Retrieve and print the email
