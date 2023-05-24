

class RacerResult:

    message_code = ''
    message_type = ''
    message_content = ''

    def __init__(self, value) -> None:
        self.value = value
        values_ = value.split(' ')
        self.message_type = values_[0][1:]
        self.message_code = values_[1]
        self.message_content = ' '.join([el for el in values_[2:]])

    def get_value(self):
        return self.value

    def __str__(self) -> str:
        return str(self.get_value())
