# Python program to demonstrate
# multilevel inheritance

# Base class
class Animal:

	def __init__(self, animalname):
		self.animalname = animalname

# Intermediate class


class Mammals(Animal):
	def __init__(self, mammalname, animalname):
		self.mammalname = mammalname

		# invoking constructor of Grandfather class
		Animal.__init__(self, animalname)

# Derived class


class Reptiles(Mammals):
	def __init__(self, reptilename, mammalname, animalname):
		self.reptilename = reptilename

		# invoking constructor of Father class
		Mammals.__init__(self, mammalname, animalname)

	def print_name(self):
		print('Animal name :', self.animalname)
		print("Mammals name :", self.mammalname)
		print("Reptile name :", self.reptilename)


# Driver code
s1 = Reptiles('cobra', 'elephant', 'cow')
print(s1.animalname)
s1.print_name()
