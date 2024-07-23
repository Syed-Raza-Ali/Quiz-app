class InvalidInputException(Exception):
    # this fuction is initializer like constructor
    def __init__(self, args:object) -> None:
        self.invalid_input = args



class NotfoundException(Exception):
    def __init__(self, args:object) -> None:    
        self.not_found = args


class ConflictException(Exception):
    def __init__(self, args:object) -> None:
        self.conflict_input = args

