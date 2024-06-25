from dataclasses import dataclass
@dataclass
class FonteRinnovabile:
    id: int
    tipo: str

    def __str__(self):
        return f"FonteRinnovabile({self.id}, {self.tipo})"

    def __hash__(self):
        return hash(self.id)
