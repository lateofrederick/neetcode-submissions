class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        while timestamp >= 0:
            val = self.map.get((key, timestamp))
            if val:
                return val

            timestamp -= 1
    
        return ""
