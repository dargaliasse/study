list_of_worker = []
departement = ["Production", "Personel", "Experience", "Equipement"]
poste = ["Drive", "Avant", "Cuisine"]
class Worker:
   def __init__(self, name):
       self.name = name
       list_of_worker.append(name)

class Gerant(Worker):
    def __init__(self, name, departement):
        super().__init__(self)
        self.departement = departement
        print(f'{name} est un gerant de {self.departement}')
class ChefDeQuart(Worker):
    def __init__(self):
        pass

class Instructeur(Worker):
    def __init__(self):
        pass

class Equipier(Worker):
    def __init__(self, section):
        pass

class Client:
    def __init__(self):
        pass
patrick = Gerant("Patrick","Cuisine")

    print("noooo")
