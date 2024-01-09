#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"
    
    def save(self):
        self.updated_at = self.updated_at.now()
        
    def to_dict(self):
        dics = self.__dict__
        dics["__class__"] = self.__class__.__name__
        dics["created_at"] = self.created_at.isoformat()
        dics["updated_at"] = self.updated_at.isoformat()
        
        
        return dics
       
new = BaseModel()
# print(new.to_dict())
print(new)