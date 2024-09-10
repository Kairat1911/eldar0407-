class Car:
    def __init__(self, the_year, the_model, the_color, the_penalties=0):
        # frelds / arrtibutes
        self.year = the_year
        self.model = the_model
        self.color = the_color
        self.penalties = the_penalties


number = 7
print(number)

bmw_car = Car(2020, 'BMW X6', 'Blue')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color}')
bmw_car.color = 'green'
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year}  NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(2020, 'Honda fit', 'Yellow' )
print(f'MODEL: {honda_car.model} YEAR {honda_car.year} COLOR: {honda_car.color}'
      f' PENALTIES: {honda_car.penalties}')

ford_car = Car(the_model='Ford Focus', the_color='sikver', penalties=100, the_penalties=2009)
print(f'MODEL: {ford_car.model} YEAR: {ford_car.year} COLOR: {ford_car.color}'
      f' PENALTIES: {ford_car.penalties}')
