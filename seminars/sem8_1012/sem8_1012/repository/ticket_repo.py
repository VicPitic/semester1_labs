# TO DO
# implement find, add, get all in memory
from domain.TicketBooking import TicketBooking


class TicketRepo:
    def __init__(self):
        self.__tickets = []

    def get_all(self):
        """
        Get all tickets
        :return: a list with all tickets
        """
        return self.__tickets

    def get_ticket_by_id(self, t_id):
        """
        Get a ticket by a given ticket id
        :return: the ticket
        """
        for ticket in self.__tickets:
            if ticket.get_id_ticket() == t_id:
                return ticket
        return None

    def add_ticket(self, ticket: TicketBooking):
        """
        Add a ticket object to the tickets list
        :param ticket: the ticket to add
        :return: -
        :raises: ValueError if a ticket with the id already exists
        """
        if self.get_ticket_by_id(ticket.get_id_ticket()) is not None:
            raise ValueError("A ticket with the given id already exists. Cannot add ticket")
        self.__tickets.append(ticket)

