class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        output = [celsius + 273.15, celsius*1.80 +32]
        return output