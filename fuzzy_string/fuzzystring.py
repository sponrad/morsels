class FuzzyString():
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return str(self.s)

    def __repr__(self):
        return("'{}'".format(self.s))

    def __eq__(self, s):
        return str(self).lower() == s.lower()

    def __ne__(self, s):
        return str(self).lower() != s.lower()

    def __lt__(self, s):
        return str(self).lower() < s.lower()

    def __gt__(self, s):
        return str(self).lower() > s.lower()

    def __ge__(self, s):
        return str(self).lower() >= s.lower()

    def __gt__(self, s):
        return str(self).lower() <= s.lower()

if __name__ == "__main__":
    apple = FuzzyString("Apple")
    print(apple < "animal")
