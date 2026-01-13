"""
Custom Exception classes for the Penguin Data Application
"""


class PenguinAppException(Exception):
    """Base exception for the penguin application"""
    pass


class FileNotFoundException(PenguinAppException):
    """Raised when a file is not found"""
    def __init__(self, filename):
        self.filename = filename
        super().__init__(f"File not found: {filename}")


class NoDataLoadedException(PenguinAppException):
    """Raised when an operation is attempted without loaded data"""
    def __init__(self):
        super().__init__("No data loaded. Use 'load <filename>' first.")


class InvalidAttributeException(PenguinAppException):
    """Raised when an invalid attribute is specified"""
    def __init__(self, attribute, valid_attributes=None):
        self.attribute = attribute
        self.valid_attributes = valid_attributes
        msg = f"Invalid attribute: {attribute}"
        if valid_attributes:
            msg += f". Valid attributes are: {', '.join(valid_attributes)}"
        super().__init__(msg)


class NonNumericAttributeException(PenguinAppException):
    """Raised when a numeric operation is attempted on a non-numeric attribute"""
    def __init__(self, attribute, operation):
        self.attribute = attribute
        self.operation = operation
        super().__init__(f"Cannot perform '{operation}' on non-numeric attribute: {attribute}")


class InvalidFilterValueException(PenguinAppException):
    """Raised when an invalid filter value is provided"""
    def __init__(self, value, expected_type):
        self.value = value
        self.expected_type = expected_type
        super().__init__(f"Invalid filter value: {value}. Expected {expected_type}.")


class InvalidCommandException(PenguinAppException):
    """Raised when an invalid command is entered"""
    def __init__(self, command):
        self.command = command
        super().__init__(f"Unknown command: {command}. Type 'help' for available commands.")


class InvalidSortOrderException(PenguinAppException):
    """Raised when an invalid sort order is specified"""
    def __init__(self, order):
        self.order = order
        super().__init__(f"Invalid sort order: {order}. Use 'asc' or 'desc'.")


class InvalidPercentageException(PenguinAppException):
    """Raised when an invalid percentage is provided"""
    def __init__(self, value):
        self.value = value
        super().__init__(f"Invalid percentage: {value}. Must be a positive number.")


class InvalidAugmentModeException(PenguinAppException):
    """Raised when an invalid augment mode is specified"""
    def __init__(self, mode):
        self.mode = mode
        super().__init__(f"Invalid augment mode: {mode}. Use 'duplicate' or 'create'.")


class EmptyDatasetException(PenguinAppException):
    """Raised when an operation requires non-empty data but dataset is empty"""
    def __init__(self):
        super().__init__("Dataset is empty. Cannot perform operation.")


class ValidationException(PenguinAppException):
    """Raised when data validation fails"""
    def __init__(self, message):
        super().__init__(f"Validation error: {message}")
