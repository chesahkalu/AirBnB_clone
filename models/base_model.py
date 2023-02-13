#!/usr/bin/python3
"""contains the base model class that defines
all common attributes/methods for other classes:"""

import models
import uuid
from datetime import datetime


class Basemodel:
        """contains the base model class that defines
        all common attributes/methods for other classes:"""

        def __init__(self, *args, **kwargs):
            """using *args and **kwargs to create an instance with a passed
            dictionary values"""

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """normal creation of instance value with initialization"""

            """if dictionary passed as argument,attributes of the instance is created.
            string time format changed to object for the instance atribute"""
            if kwargs:
                  for k, v in kwargs.items():
                    if k == "created_at" or k == "updated_at":
                          self.__dict__[k] = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[k] = v

        def __str__(self):
              """String printable representation of Basemodel instance"""

              return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
        def to_dict(self):
              """Returns dictionary format of all instances attribute,
              class name, created_at and updated_at made readable as it
              is in a data structure."""

              all_dict = self.__dict__.copy()
              all_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
              all_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
              all_dict["__class__"] = self.__class__.__name__
              return all_dict
        
        def save(self):
              """Updates the attribute updated at with the current date and time"""

              self.updated_at = datetime.now()
