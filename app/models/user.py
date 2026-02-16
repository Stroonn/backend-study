from dataclasses import dataclass

@dataclass
class User:

    name : str
    email : str

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty")