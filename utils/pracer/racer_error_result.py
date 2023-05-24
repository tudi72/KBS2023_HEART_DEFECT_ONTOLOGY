from pracer.racer_result import RacerResult


class RacerErrorResult(RacerResult):

    def __init__(self, msg):
        super().__init__(msg)

    def get_value(self):
        return self.value

    def __str__(self) -> str:
        return str(self.get_value())
