from dataclasses import dataclass

@dataclass
class Ab():
    name : str
    age : int
    salary: int 

s= Ab("mohit",21,200000)
print(s.name)