class Car:
    # ~ Конструктор класса при помощи метода __init__,
    # ~ с помощью которого назначаем собственные свойства класса сразу
	def __init__(self, model, speed):
        # ~ Инициализация атрибутов авто
		self.model = model
		self.speed = speed
	# ~ Далее пойдут 2 метода, посвященные инкапсуляции
	def _secret(self):
		print("Данный метод защищенный " +
		"согласно соглашению, но его можно вызвать")
	def __topsecret(self):
		print("Данный метод запривачен согласно соглашению,\n" + 
		"чтобы вызвать его используется связка _Класс___Метод") 
	#Метод для показа скорости       
	def sp_speed(self):
		print("Скорость автомобиля составляет " + self.speed + " км/ч.")
		
class Boat:
	def __init__(self, speed):
		self.speed = speed
	def sp_speed(self):
		print("Скорость лодки составляет " + self.speed + " км/ч.")

# ~ Простой пример наследование
class SuperCar(Car):
	def super_speed(self):
		print("Скорость супер авто " + self.speed + str(0) + " км/ч.")

	# ~ Паттерн "одиночка" - это простой шаблон, когда мы создаем 
	# ~ экземпляр только один раз, при повторном создании, происходит 
	# ~ не повторное создание экземпляра, а отсылка к первому созданному
class PatSingl:
    def __new__(r):
        if not hasattr(r, ' '):
            r.name_in = super(PatSingl, r).__new__(r)
        return r.name_in

# ~ Присваиваем переменным классы с определенными атрибутами  
mboat = Boat(str(12))
mcar = Car('audi', str(40))
scar = SuperCar('BMW', str(53))

# ~ Реализация паттерна "Фабричный метод"
# ~ Класс FabMethod на основании класса средства передвижения,
# ~ реализованных с помощью классов Car, Boat, SuperCar
# ~ выдает название данного средства передвижения
class FabMethod:
	def transport(self, nam):
		if nam == mcar:
			print( "Это машина")
		elif nam == mboat:
			print( "Это катер")
		elif nam == scar:
			print( "Это супер машина")
		else:
			print( "Ошибка")

# ~ Вызов фабричного метода			
z = FabMethod()
print(z.transport(mboat)) 
print(z.transport(mcar))
print(z.transport(scar))
   

# ~ Метод с одним подчеркиваем можно вызвать как и другие методы:
mcar._secret()
print(mcar._secret())
# ~ Метод с двумя подчеркиваниями вызывается только с помощью
# ~ связки _Класс___Метод, в остальных случаях вызовет ошибку
mcar._Car__topsecret()

# ~ Вызов методов разных классов с одинаковыми названиями(полиморфизм) 
mcar.sp_speed()
mboat.sp_speed()
# ~ Реализация примера наследования, где используется атрибут родителя
scar.super_speed()
