class cat:
    breed = None
    gender = None
    fun_color = None
    age = None
    weight = None
    height = None
    is_pet = None
    is_tamed = None
    
    def eat(self,food = 'catfood'):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is eating {food}')
    
    def play(self):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is playing')

    def sleep(self):      # self keyword indicates that this is a method of class (instance function)
        print(f'🐈 is sleeping')

billu = cat() # constructor calling
##print(billu, type(billu))
tom = cat()
bagadbilla = cat()


billu.breed = 'persian'
billu.weight = 2
billu.age = 2 
billu.fun_color = 'white'
billu.height = 1
billu.is_tamed = True
billu.gender = "M"

tom.breed = 'street cat'
tom.weight = 1.5
tom.age = 100
tom.fun_color = 'grey'
tom.height = 1.1
tom.is_tamed = True
tom.gender = "M"

bagadbilla.breed = 'wild cat'
bagadbilla.weight = 2.5
bagadbilla.age = 10
bagadbilla.fun_color = 'brown'
bagadbilla.height = 1.1
bagadbilla.is_tamed = True
bagadbilla.gender = "M"

print("billu details")
print("breed:", billu.breed)
print("gender:", billu.gender)
print("age:", billu.age)
print("weight:", billu.weight)
print("height:", billu.height)
print("color:", billu.fun_color)
print("pet:", billu.is_tamed )
billu.eat()
billu.play()
billu.sleep()


print("tom details")
print("breed:", tom.breed)
print("gender:", tom.gender)
print("age:", tom.age)
print("weight:", tom.weight)
print("height:", tom.height)
print("color:", tom.fun_color)
print("pet:", tom.is_tamed )
tom.sleep()
tom.play()
tom.sleep()

print("bagadbilla details")
print("breed:", bagadbilla.breed)
print("gender:", bagadbilla.gender)
print("age:", bagadbilla.age)
print("weight:", bagadbilla.weight)
print("height:", bagadbilla.height)
print("color:", bagadbilla.fun_color)
print("pet:", bagadbilla.is_tamed )
bagadbilla.eat("mouse")
bagadbilla.eat("bird")
bagadbilla.sleep()
bagadbilla.eat("bird")