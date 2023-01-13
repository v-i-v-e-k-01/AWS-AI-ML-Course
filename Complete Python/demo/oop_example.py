from oop_shirt import Shirt

shirt_one= Shirt('orange','M','short sleeve',45)
shirt_two= Shirt('red','S','short sleeve',30)

print(shirt_one.price)
print(shirt_one.color)


shirt_two.change_price(45)
print(shirt_two.price)

shirt_one.color ='yellow'
shirt_one.size='L'
shirt_one.price=43

