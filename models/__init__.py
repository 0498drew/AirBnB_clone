#!/usr/bin/python3

"""
creating a unique Filestorage instance
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
