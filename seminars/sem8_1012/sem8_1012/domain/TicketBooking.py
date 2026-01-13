# TO DO
# A client can book a ticket for a movie, and the application should
# keep track of the date and time the booking was made

import datetime


class TicketBooking:
    def __init__(self, id_ticket, id_movie, id_client):
        self.__id_ticket = id_ticket
        self.__id_movie = id_movie
        self.__id_client = id_client
        self.__booking_datetime = datetime.datetime.now()

    def get_id_ticket(self):
        return self.__id_ticket

    def get_id_movie(self):
        return self.__id_movie

    def get_id_client(self):
        return self.__id_client

    def get_booking_datetime(self):
        return self.__booking_datetime

    def __str__(self):
        return f"Ticket id {self.__id_ticket}, movie:{self.__id_movie}, client:{self.__id_client}"