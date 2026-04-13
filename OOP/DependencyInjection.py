'''
Dependency Injection: Objekt erhält seine Abhängigkeiten von außen.
Auto Klasse soll Motor Klasse nicht selbst erstellen. 
Wird von außen erstellt und im Konstruktor an der unabhängige Klasse übergeben
Vorteil. Vererbung von unabhängige Klasse wird ermöglicht
'''


class Motor:
    def start(self):
        print("Motor start")
        
class Auto:
    def __init__(self, engine):
        self.engine = engine
    def start(self):
        print("Auto start")
        self.engine.start()

class Verbreungsmotor(Motor):
    def start(self):
        print("Verbreungsmotor wurde gestartet")

class Elektromotor(Motor):
    def start(self):
        print("Elektromotor wurde gestartet")

engine = Verbreungsmotor()
auto = Auto(engine)
auto.start() 


elektro_motor = Elektromotor()
auto_elektro = Auto(elektro_motor)
auto_elektro.start()