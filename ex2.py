class Clock:
    __DAY = 86400  # число сек в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, value):
        if not isinstance(value, (int, Clock)):
            raise TypeError("ОПеранд справа должен иметь тип int или Clock")

        return value if isinstance(value, int) else value.seconds

    def __eq__(self, value):
        sc = Clock.__verify_data(value)
        return self.seconds == sc

    def __lt__(self, value):
        sc = Clock.__verify_data(value)
        return self.seconds < sc

    def __gt__(self, value):
        sc = Clock.__verify_data(value)
        return self.seconds > sc


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 > 5000)
