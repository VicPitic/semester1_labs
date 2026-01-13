from domain.client import Client
from domain.validation import ClientValidator
from repository.client_repo import ClientRepo


class ClientService:
    def __init__(self, client_repo: ClientRepo, client_validator: ClientValidator):
        self.__client_repo = client_repo
        self.__client_validator = client_validator

    def get_all_clients(self):
        return self.__client_repo.get_all_clients()

    def get_client_by_cnp(self, cnp):
        return self.__client_repo.get_client_by_cnp(cnp)

    def add_client(self, cnp, name):
        """
        Add a client using name and cnp attributes as parameters
        :param cnp: client cnp
        :param name: client name
        :return: -
        :raises: ValueError if client is not valid
        """
        client = Client(cnp, name)
        self.__client_validator.validate_client(client)
        self.__client_repo.add_client(client)

    def delete_client(self, cnp):
        """
        Deletes a client by a given cnp
        :param cnp: cnp
        :return: -
        :raises: ValueError if there is no client with the given cnp
        """
        self.__client_repo.delete_client_by_cnp(cnp)