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
            """using *args to create attributes for instances without knowing the intended
            number of arguments to be passed a passed"""

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """some certain attributes at initialization of instance"""

            """if dictionary passed as arguments,attributes of the instance is created.
            string time format changed to object for the instance atribute"""
            if kwargs:
                  for key, value in kwargs.items():
                    if key == "created_at" or key == "updated_at":
                          self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = value
            else:
                 models.storage.new(self)

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
              models.storage.save(self)
