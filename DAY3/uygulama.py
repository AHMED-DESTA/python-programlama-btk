class movie:
    def __init__(self, name, year, genre):
        self.name = name
        self.year = year
        self.genre = genre
    def __eq__(self, other):
        return self.name == other.name and self.year == other.year and self.genre == other.genre
m1=movie("The Matrix", 1999, "Action")
m2=movie("The Matrix", 1999, "Action")
print(m1==m2)
   