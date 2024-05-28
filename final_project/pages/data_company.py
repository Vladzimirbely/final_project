from dataclasses import dataclass

@dataclass
class DataCompany:
    main: str
    goal: str
    relationship: str
    values: str
    achievements: str
    offer: str

@dataclass
class DataSearchWithFilter:
    python: str
    