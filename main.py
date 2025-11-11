#Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.

class rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self): 
        return self.lenght*self.width  

obj1=rectangle(100,10)

print(f"The area is {obj1.area()}")




         
  
        
