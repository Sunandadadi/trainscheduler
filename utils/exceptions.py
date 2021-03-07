
class ExpectedArguments(Exception):
    def __init__(self, expected, missing):
        self.expected = expected
        self.missing = missing

    def __str__(self):
        return f"Expected {', '.join(self.expected)} as arguments. Missing keys: {', '.join(self.missing)}"

class InvalidTypeArguments(Exception):
    def __init__(self, invalid_type):
        self.invalid_type = invalid_type

    def __str__(self):
        return f"TypeError: Expected paramerter {', '.join(self.invalid_type)}"

class UnExpectedParamLength(Exception):
    def __init__(self, param, expected, actual):
        self.param = param
        self.expected = expected
        self.actual = actual

    def __str__(self):
        return f"Expected Parameter: '{self.param}' of length: {self.expected}, recieved: {self.actual}"

class TypeError(Exception):
    def __init__(self, expected, param = None):
        self.expected = expected
        self.param = param

    def __str__(self):
        if self.param:
            return f"Expected Parameter: '{self.param}' of type: {self.expected}"
        return f"Expected Type: {self.expected}"
