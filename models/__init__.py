#!/usr/bin/python3
""" __init__ method that inisialize models directory. """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
