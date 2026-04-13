class Mitarbeiter:
    def __init__(self, namen, personalnummer, grundgehalt):
        self.namen = namen
        self.personalnummer = personalnummer
        self.grundgehalt = grundgehalt

    def gehalt_berechnung(self):
        self.grundgehalt = self.grundgehalt * 13 / 12
        return self.grundgehalt
        
    def __repr__(self):
        return f"Mitarbeiter: Namen {self.namen}, Peronalnummer {self.personalnummer}, Grundgehalt {self.grundgehalt:.2f}"
    
class Arbeiter(Mitarbeiter):
    def __init__(self, namen, personalnummer, grundgehalt, ueberstunden, stundenlohn):
        super().__init__(namen, personalnummer, grundgehalt)
        self.ueberstunden = ueberstunden
        self.stundenlohn = stundenlohn

    def gehalt_berechnung(self):
        self.gehalt_arbeiter = super().gehalt_berechnung() + (self.ueberstunden * self.stundenlohn)
       
    def __str__(self):
        return f"Arbeiter: {self.namen} bekommt ein von Gehalt {self.gehalt_arbeiter:.2f}"
    
    def __repr__(self):
        return f"Arbeiter: {self.namen}, Gehalt {self.gehalt:.2f}"

class Manager(Mitarbeiter):
    def __init__(self, namen, personalnummer, grundgehalt, bonus):
        super().__init__(namen, personalnummer, grundgehalt)
        self.bonus = bonus
        
    def gehalt_berechnung(self):
        self.gehalt_manager = super().gehalt_berechnung() + self.bonus

    def __str__(self):
        return f"Manager: {self.namen} bekommt ein von Gehalt {self.gehalt_manager:.2f}"
    
    def __repr__(self):
        return f"Manager: {self.namen}, Gehalt {self.gehalt:.2f}"

mitarbeiter = Mitarbeiter("Goran",  123, 1000)
mitarbeiter.gehalt_berechnung()
print(mitarbeiter)

arbeiter = Arbeiter("Goran",  123, 1000, 10, 25.00)
arbeiter.gehalt_berechnung()
print(arbeiter)

manager = Manager("Goran",  123, 2000, 500.00)
manager.gehalt_berechnung()
print(manager)