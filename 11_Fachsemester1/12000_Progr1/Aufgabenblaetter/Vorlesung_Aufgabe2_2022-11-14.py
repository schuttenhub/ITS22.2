class Auto:
    def __init__(self):
        self.fahren_counter = 0
        pass

    def faehrt(self):
        self.fahren_counter += 1
        if self.fahren_counter <=3:
            return "Auto faehrt"
        return "Auto ist kaputt"

    def reparieren(self):
        pass

    def kaputt(self):


