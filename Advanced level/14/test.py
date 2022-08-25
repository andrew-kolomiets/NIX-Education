# Создайте несколько классов конструктора автомобиля:
# Engine -> Car -> Honda

# Реализуйте наследование этих классов и базовые методы 
# для каждого из них, например start/stop для engine, 
# open/close doors для Car и т.д.
# Используйте __init__ для инициализации необходимых 
# параметров (максимальная скорость, объем двигателя, и т.п.)
# Примените инкапсуляцию для сокрытия вспомогательных методов
# По необходимости используйте staticmethod / classmethod / property



class Engine:
    
    @classmethod
    def start_engine(self):
        return 'Engine start!'
    
    @classmethod
    def stop_engine(self):
        return 'Engine stop!'
        
    
class Car(Engine):
    
    def __init__(self,speed,volume,colour,fuel):
        self._colour=colour
        self._speed=speed
        self._volume=volume
        self._fuel=fuel
    
    @classmethod
    def open_door(self):
        return 'Dor is open!'
    
    @classmethod
    def close_door(self):
        return 'Dor is close!'
        
        

class Honda(Car):
    
    def __init__(self, speed, volume, colour, fuel):
        super().__init__(speed, volume, colour, fuel)
    
    
    def  get_colour(self):
        return self._colour
    
    
    def  get_fuel(self):
        return self._fuel
    
    
    def  get_volume(self):
        return self._volume
    

    def  get_speed(self):
        return self._speed
    
        
obj=Honda(12,24,'Blue','Disel')

print(obj.stop_engine())
    
    

    
    
    
