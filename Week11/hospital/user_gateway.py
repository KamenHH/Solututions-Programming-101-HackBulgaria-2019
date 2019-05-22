import sys


class UserGateway(Gateway):
    def create_new_user(self, **kwargs):;
        try:
            self.db.create('User', username, password, **kwargs)
        except DatabaseConnectionError:
            sys.exit(1)

    def find_existing_user(self, username):
        self.db.find('User', username)
# create 
# find
# delete
# update