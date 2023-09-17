#!.venv/bin/python
#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

storage_determiner = getenv("HBNB_TYPE_STORAGE")
if storage_determiner == "db":
    from .engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
