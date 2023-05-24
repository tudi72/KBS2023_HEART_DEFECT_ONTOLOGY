from pracer.racer_result import RacerResult


class RacerListResult(RacerResult):
    """
    TODO: RacerResult class for parsing list results

    """
    value: []

    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value

    def get_value(self):
        return str(self.value)
