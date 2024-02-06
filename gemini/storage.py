from __future__ import annotations

import json
import os


class Storage:
    def __init__(self, file: str):
        self.filepath = file
        self.data = None
        self._structure = {
            "config": {},
            "session": {
                "tabs": [
                    "a.b/c.gmi"
                ]
            }
        }
        self.read()

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def _sanitize(self, data: dict, structure: dict) -> None:
        for item in structure.keys():
            if item not in data:
                data[item] = structure[item]
            elif isinstance(data[item], dict):
                self._sanitize(data[item], structure[item])

    def read(self) -> None:
        if not os.path.exists(self.filepath):
            open(self.filepath, 'x').close()
        with open(self.filepath, 'r') as file:
            if not file.read():
                self.data = {}
            else:
                file.seek(0)
                self.data = json.loads(file.read())
            file.close()
        self._sanitize(self.data, self._structure)
        self.write()

    def write(self) -> None:
        with open(self.filepath, 'w') as file:
            file.write(json.dumps(self.data))
            file.close()

    def close(self, *, write=True) -> None:
        if write:
            self.write()
        del self
