from service.movie_service import MovieService

# TO DO: add client and ticket handling
class Console:
    def __init__(self, movie_service: MovieService, client_service):
        self.__movie_service = movie_service
        self.__client_service = client_service

    @staticmethod
    def print_menu():
        print("1. Add movie")
        print("2. Get all movies")
        print("3. Get movie by id")
        print("4. Add client")
        print("5. Get all clients")
        print("6. Get client by id")
        print("x. Exit")

    def handle_get_all_movies(self):
        for movie in self.__movie_service.get_all_movies():
            print(movie)

    def handle_get_movie_by_id(self):
        id = input("Enter movie id: ")
        movie = self.__movie_service.get_movie_by_id(id)
        if movie:
            print(movie)
        else:
            print("No movie has been found with the given id")

    def handle_add_movie(self):
        id = input("Enter id: ")
        name = input("Enter movie name: ")
        genre = input("Enter movie genre: ")
        try:
            self.__movie_service.add_movie(id, name, genre)
        except ValueError as ve:
            print(ve)

    def run(self):
        while True:
            option = input("give option: ")
            match option:
                case "1":
                    self.handle_get_all_movies()
                case "2":
                    self.handle_get_movie_by_id()
                case "3":
                    self.handle_add_movie()
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "x":
                    break
