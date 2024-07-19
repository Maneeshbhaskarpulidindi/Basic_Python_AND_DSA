#POP
#OOPS
#FunctionalPrograming


#what is an object??
#in real world every thing is an object
#what is an Attributes??
#what is Behaviour?? to be implemented by using Methods (are the functions in class )

#object has attributes and Behaviour

class first_class:
    #Attributes
    #Method
    def __init__(self,cpu,ram):
        #it will automatically run without call the function 
        #here self is an object 
        self.cpu=cpu
        self.ram=ram
        print("Hello from the constructor")
    def config(self):
        print("hello world")
        print("CPU:",self.cpu, "ram:",self.ram)



#__init__ method
#self and comstructor methods

class second_class:
    def __init__(self) -> None:
        self.name="John Doe"
        self.age=30
        self.city="New York"
    def compare_age(orther):
        if self.age==orther.age:
            print("yes they are same ")
        else:
            print("no they are not same")

#Variable
#class Variable and intenance Variable  
#if we define the var out side the init function it will  class Var other wise it wil be intenance var
#https://www.youtube.com/watch?v=RSQjxL5WRNM&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=57





if __name__ == "__main__":
    a=first_class("i",64)
    b=first_class("rysan",32)
    #EVERY time you create a object it will create a new object.
    print(id(a),id(b))
    a.config()
    print(type(a))














