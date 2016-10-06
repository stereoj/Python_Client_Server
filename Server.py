from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import Binary
import os
import time

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True, allow_none=True)
server.register_introspection_functions()
server.register_multicall_functions()


class ExamService:
    def __init__(self):
        self.state = {}

    def _ping(self):
        hostname = "google.com"
        response = os.system("ping -c 1 " + hostname)
        return response

    def login(self, user, password, host):
        response = self._ping()
        if response == 0:
            self.state[user] = "logged in"
            return 1
        else:
            time.sleep(5)
            response = self._ping()
            if response == 0:
                self.state[user] = "logged in"
                return 1
            else:
                self.state[user] = "logged out"
                return 0;

    def logout(self, user):
        self.state[user] = "logged out"
        return "logged out"

    def discovery(self, user):
        if "logged in" not in self.state.get(user):
            return 0;

    def bidir(self, user, portA, portB):
        if "logged in" not in self.state.get(user):
            return 0;

        return True

    def unidir(self, user):

        if "logged in" not in self.state.get(user):
            return 0;

    def set_attribute(self, user):
        if "logged in" not in self.state.get(user):
            return 0;
        return True

    def get_attribute(self, user):
        if "logged in" not in self.state.get(user):
            return 0;

        return True

    def raises_exception(self, msg):
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        data = bin.data
        response = Binary(data)
        return response


server.register_instance(ExamService())

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'
