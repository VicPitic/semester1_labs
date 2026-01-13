from domain.client import Client

# in the repository you have to define all CRUD operations
# and only the CRUD operations


class ClientRepo:
    def __init__(self):
        self.__clients = []

    # TO DO: exception if client already exists
    def add_client(self, client: Client):
        """
        Add a new client to the clients list
        :param client: client to add
        :return: -
        """
        self.__clients.append(client)

    def get_client_by_cnp(self, cnp):
        """
        Gets a client by cnp
        :param cnp: the cnp to find
        :return: the client object with given cnp
        """
        for client in self.__clients:
            if client.get_cnp() == cnp:
                return client
        return None

    def get_all_clients(self):
        """
        Get the list with all the clients
        :return: the list of clients
        """
        return self.__clients

    # TO DO exception if client does not exist
    def delete_client_by_cnp(self, cnp):
        """
        Deletes a client with a given cnp
        :param cnp: cnp
        :return: -
        """
        client_to_delete = self.get_client_by_cnp(cnp)
        if client_to_delete is not None:
            self.__clients.remove(client_to_delete)


    # TO DO exception if client does not exist
    def update_client_by_cnp(self, cnp, new_name):
        """
        Updates a client name by given cnp
        :param cnp: cnp
        :param new_name: name to update
        :return: -
        """
        client_to_update = self.get_client_by_cnp(cnp)
        if client_to_update:
            client_to_update.set_name(new_name)



