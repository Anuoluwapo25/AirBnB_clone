#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
"""


from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """_summary_
    """
    def __init__(self, *args, **kwargs):
        """_summary_
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid4())
            if not any(key in kwargs for key in ["created_at", "updated_at"]):
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            models.storage.new(self)
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
    def __str__(self):
        """_summary_

        Returns:
            str: _description_
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"
    
    def save(self):
        """_summary_
        """
        self.updated_at = self.updated_at.now()
        storage.save()
        
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        dics = self.__dict__
        dics["__class__"] = self.__class__.__name__
        dics["created_at"] = self.created_at.isoformat()
        dics["updated_at"] = self.updated_at.isoformat()
        return dics
