# from abc import ABC, abstractmethod

# class animal(ABC):
#     def speak(self):
#         pass
#     def foot(self):
#         pass

# class dog(animal):
#     def speak(self):
#         return "bark!"
#     def foot(self):
#         return 4
    
# class chicken(animal):
#     def speak(self):
#         return "chick-chick!"
#     def foot(self):
#         return 2
    
# def animal_behavior(animal: animal):
#     print(f"the animal says: {animal.speak()}")
#     print(f"the animal has: " + str(animal.foot()) + "legs")

# dog = dog();
# chicken = chicken();

# animal_behavior(dog);
# animal_behavior(chicken);


from abc import ABC, abstractmethod

class mobil(ABC):
    def fasilitas(self):
        pass
    def kecepatan(self):
        pass
    def harga(self):
        pass
    def kekuatan(self):
        pass

class BMW(mobil):
    def fasilitas(self):
        return ("F Crash sensor, Aribags, Brake Assist")
    def kecepatan(self):
        return (" 286Hp")
    def harga(self):
        return("2,5 Milyar")
    def kekuatan(self):
        return(" 400Nm")

class Avanza(mobil):
    def fasilitas(self):
          return ("Crash sensor, Aribags depan, Brake Assist")
    def kecepatan(self):
        return("105Hp")
    def harga(self):
        return("288 Juta")
    def kekuatan(self):
        return("137Nm")

class Ferrari(mobil):
    def fasilitas(self):
           return ("Crash sensor, Engine Check Warning, Brake Assist")
    def kecepatan(self):
        return ("340/km")
    def harga(self):
        return ("7 Milyar")
    def kekuatan(self):
        return(" 800Nm")
    

def Kelebihan_mobil(mobil:mobil):
    print(f"Fasilitas: {mobil.fasilitas()}")
    print(f"Kecepatan: {mobil.kecepatan()}")
    print(f"Harga: {mobil.harga()}")
    print(f"Kekuatan: {mobil.kekuatan()}")

BMW= BMW();
Avanza= Avanza();
Ferrari = Ferrari();


Kelebihan_mobil(BMW);
print("Avanza")
Kelebihan_mobil(Avanza);
print("Ferrari")
Kelebihan_mobil(Ferrari);