#%%
class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity


    def __str__(self):
        return f"Book(id = {self.id}, name={self.name}, quantity={self.quantity})"
    

#%%

class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name


    def __str__(self):
        return f"User(id= {self.id}, name= {self.name})"