class Newspaper:
    def __init__(self, name, year, month, day_of_month, is_finnish):
        self.__name = name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.get_name()} {self.day_of_month}.{self.month}.{self.year}{" (Finnish)" if self.is_finnish else ""}"

news = Newspaper("Kaleva", 2019, 12, 25, True)
print(news)