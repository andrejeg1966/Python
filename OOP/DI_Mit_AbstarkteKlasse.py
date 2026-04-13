'''
Dependency Injection mit Abstrakte Klasse 
'''

from abc import ABC, abstractmethod

class Motor(ABC):
    @abstractmethod
    def start(self):
        print("Motor start")
        
class Auto:
    def __init__(self, engine: Motor):
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
auto.engine.start()  #ermöglicht durch type Annotation in init von Auto Klasse

elektro_motor = Elektromotor()
auto_elektro = Auto(elektro_motor)
auto_elektro.start()