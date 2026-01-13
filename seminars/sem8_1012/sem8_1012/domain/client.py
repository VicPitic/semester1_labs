class Client:
    def __init__(self, cnp, name):
        self.__cnp = cnp
        self.__name = name

    def get_name(self):
        return self.__name

    def get_cnp(self):
        return self.__cnp

    def set_cnp(self, new_cnp):
        self.__cnp = new_cnp

    def set_name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return F"Name: {self.__name}, CNP: {self.__cnp}"

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.__cnp == other.__cnp