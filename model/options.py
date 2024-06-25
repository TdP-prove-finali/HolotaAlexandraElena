from dataclasses import dataclass
@dataclass
class Options:
    attributes: str
    attributi: str

    def __str__(self):
        return f"{self.attributes} - {self.attributi}"

    def __eq__(self, other):
        return self.attributes == other.attributes and self.attributi == other.attributo

    def __hash__(self):
        return hash(self.attributes)
