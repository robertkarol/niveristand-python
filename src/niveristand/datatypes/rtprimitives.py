from niveristand import errormessages
from niveristand import exceptions as nivsexceptions


class DataType:
    def __init__(self, value, description="", units=""):
        self._validate(value)
        self.__value = value

    def __str__(self):
        return str(self.value)

    def _validate(self, value):
        return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Double(DataType):
    def _validate(self, value):
        try:
            return float(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


class Int32(DataType):
    def _validate(self, value):
        try:
            return int(value)
        except TypeError:
            raise nivsexceptions.TranslateError(errormessages.init_var_invalid_type)


VALID_TYPES = {
    Double.__name__: Double,
    Int32.__name__: Int32
}