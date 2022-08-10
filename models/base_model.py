#!/usr/bin/python3
"""Base Model Module
"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """base_model that defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """init method for BaseModel class

        Args: 
            id : string - assign with an uuid when an instance is created
            created_at : datetime - assign with the current datetime when an instance is created
		    updated_at : datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
        """  
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """str method for BaseModel class

        Return: 
            string(str): string descriptor for BaseModel Class
        """        

        return ("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """updates the public instances attribute 
        updated_at with current time and date
        """
        self.updated_at = datetime.now() 

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """              
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary