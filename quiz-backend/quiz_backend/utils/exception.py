


class InvalidInputException(Exception):
    # this fuction is initializer like constructor
    def __init__(self, args:object):
        self.invalid_input = args



class NotfoundException(Exception):
    def __init__(self, args:object):
        self.not_found = args


class ConflictException(Exception):
    def __init__(self, args:object):
        self.conflict_input = args

