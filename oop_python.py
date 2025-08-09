#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  9 12:58:03 2025

@author: fawaz
"""

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("I don't know how to speak until I am assgined an animal class")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        print("meow")
    def show_color(self):
        print(f"my color is {self.color}")
        

class Dog(Pet):
    def speak(self):
        print("Bark")
        

p = Pet("Tim",19)
p.show()
p.speak()
c = Cat("Bill",20,"orange")
c.show()
c.show_color()

d = Dog("John",21)
d.show()
c.speak()
d.speak()
#%%
class Person:
    number_of_people = 0
    def __init__(self,name):
        self.name = name
        Person.number_of_people+=1
    
    @classmethod
    def return_number_of_people(cls):
        return cls.number_of_people
        
p1 = Person("tim")
p2 = Person("jill")

print(p1.name)
print(p2.name)

print(p1.number_of_people)
print(p2.number_of_people)
print(Person.number_of_people)

#Person.number_of_people = 10

print(p1.return_number_of_people())

#%%
import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all_things = []
    def __init__(self,name:str, price:float, quantity = 0):
        assert price >=0, f"Price {price} is not greater than 0"
        assert quantity >=0, f"Quantity {quantity} is not greater than 0"
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all_things.append(self)
        
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price*self.pay_rate
        
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('/home/fawaz/Desktop/USF/PHD/COURSES/SPRING25/projects_on_git/general_test/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('item'),
                price=int(item.get('price')),
                quantity = int(item.get('quantity'))
                )
    
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
            
            
Item.instantiate_from_csv()
print(Item.all_things)
            
        
        
    


item1 = Item('phone',100,5)
item2 = Item('laptop',1000,3)
item3 = Item('cable',100,5)
item4 = Item('mouse',1000,3)
item5 = Item('keyboard',100,5)

Item.instantiate_from_csv()