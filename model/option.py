from dataclasses import dataclass
@dataclass
class Option:
    attribute: str
    attributo: str

    def __str__(self):
        return f"{self.attribute} - {self.attributo}"

    def __eq__(self, other):
        return self.attribute == other.attributes and self.attribute == other.attributo

    def __hash__(self):
        return hash(self.attribute)
