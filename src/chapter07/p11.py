"""
**File System: **

Explain the data structures and algorithms that you would use to design an in-memory file system.
Illustrate with an example in code where possible.
"""

# Objects:
# File (Name, Size, Created Date)
# Directory (Name, Created Date(

# Datastructures:
# File -> String
# Directory -> Dictionary that points to file or other Directories
# Root Directory -> that points to other Directories

# Actions:
# * Create File at (Directory)
# * Delete File at (Directory)
# * Delete Directory (raise error or delete recursively)
import datetime
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Owner:
    name: str


@dataclass
class File:
    name: str
    content: str
    owner: Owner

    @property
    def size(self):
        return len(self.content.encode("utf-8"))


class DirectoryNotFound(Exception):
    """Raised on missing directory."""


@dataclass
class Directory:
    name: str
    parent: "Directory" = field(default=None)
    links: Dict[str, "Directory" | File] = field(default_factory=dict)
    created_at: int = field(default_factory=datetime.datetime.utcnow().timestamp)

    def create_file(self, file_name: str, content: str, owner: Owner):
        file = File(file_name, content, owner)
        self.links[file_name] = file

    def __getitem__(self, item):
        return self.links[item]

    def __setitem__(self, key, value):
        self.links[key] = value

    @property
    def fully_qualified_name(self):
        arr = []
        parent = self.parent
        while parent != Directory("/"):
            arr.append(parent.name)
            parent = parent.parent
        arr.append("/")
        return arr[::-1]

@dataclass
class FileSystem:
    root = Directory("/")

    def create_file(self, name: str, owner: Owner, content: str, directory_name: str):
        if directory_name not in self.root:
            raise DirectoryNotFound(f"{directory_name}")
        directory = self.root[directory_name]
        directory.create_file(name, content, owner)

    def create_directory(self, name: str):
        self.root[name] = Directory(name, self.root)

    def delete_directory(self, name: str):
        pass
        