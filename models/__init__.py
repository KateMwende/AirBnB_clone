#!/usr/bin/env python3
"""create a unique FileStorage instance for your application"""

from models.engine.filestorage import FileStorage

storage = FileStorage()
storage.reload()
