from domain.TicketBooking import TicketBooking
from repository.client_repo import ClientRepo
from repository.movie_repo import MovieRepo
from repository.ticket_repo import TicketRepo


class TicketService:
    def __init__(self, ticket_repo: TicketRepo, repo_movie: MovieRepo, repo_client: ClientRepo):
        self.__ticket_repo = ticket_repo
        self.__repo_movie = repo_movie
        self.__client_repo = repo_client

    def get_all(self):
        """
        Get all tickets
        :return: all tickets
        """
        self.__ticket_repo.get_all()

    def get_ticket_by_id(self, t_id):
        """
        Get a ticket by a given id
        :param t_id: ticket id
        :return: the ticket
        """
        return self.__ticket_repo.get_ticket_by_id(t_id)

    def add_ticket(self, id_ticket, id_movie, cnp_client):
        """
        Add a new ticket to the ticket list
        :param id_ticket: id ticket
        :param id_movie: id movie
        :param cnp_client: id client
        :return: -
        """
        ticket_to_add = TicketBooking(id_ticket, id_movie, id_client)
        if self.__repo_movie.get_movie_by_id(id_movie) is None:
            raise ValueError("There is no movie with the given id in the ticket")
        if self.__client_repo.get_client_by_cnp(cnp_client) is None:
            raise ValueError("There is no client with ")
        self.__ticket_repo.add_ticket(ticket_to_add)