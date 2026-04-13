'''
*****************VERERBUNG**************
Tight coupiling: Änderung in einer Klasse bewirkt Änderung in andere Klasse
'''
class MotorVer:
    def start(self):
        print("Motor start")
        
class AutoVer(MotorVer):
    def start(self):
        print("Auto start")
        return super().start()
    
auto_ver = AutoVer()
auto_ver.start()

'''
*****************COMPOSITION**************
Loose coupling: Keine oder minimale Beziehung der Klassen zueinander. Bevorzugt
'''

class MotorCom:
    def start(self):
        print("Motor start")
        
class AutoCom:
    def __init__(self):
        self.engine = MotorCom()
    def start(self):
        print("Auto start")
        self.engine.start()

auto_com = AutoCom()
auto_com.start() 