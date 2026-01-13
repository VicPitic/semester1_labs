class Movie:
    # counter = 0
    def __init__(self, id, name, genre):
        # self.__id = Movie.counter
        self.__id = id
        self.__name = name
        self.__genre = genre
        # Movie.counter += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_genre(self):
        return self.__genre

    def set_name(self, new_name):
        self.__name = new_name

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def __str__(self):
        return f"Movie: {self.__id}, name: {self.__name}, genre:{self.__genre}"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.__name == other.__name and self.__genre == other.__genre