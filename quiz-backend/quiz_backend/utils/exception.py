
class InvalidInputException(Exception):
    # this fuction is initializer like constructor
    def __init__(self):
        self.invalid_input = "Email"

class NotfoundException(Exception):
    def __init__(self, args:object):
        self.not_found = args
class ConflictException(Exception):
    def __init__(self):
        self.conflict_input = "Quiz"

