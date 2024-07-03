from dataclasses import dataclass
@dataclass()
class SistemaEnergeticoRinnovabile:
    id: int
    Type_of_Renewable_Energy: int
    Installed_Capacity_MW: float
    Energy_Production_MWh: float
    Energy_Consumption_MWh: float
    Energy_Storage_Capacity_MWh: float
    Storage_Efficiency_Percentage: float
    Grid_Integration_Level : int
    Initial_Investment_USD: float
    Funding_Sources: int
    Financial_Incentives_USD: float
    GHG_Emission_Reduction_tCO2e: float
    Air_Pollution_Reduction_Index: float
    Jobs_Created: int

    def __str__(self):
        return f"{self.Type_of_Renewable_Energy} - {self.Energy_Production_MWh}"

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)