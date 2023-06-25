import math

class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, obj):
        if len(obj) == 0:
            return None
        return sum(obj) / len(obj)

    def median(self, obj):
        if len(obj) == 0:
            return None
        obj.sort()
        size = len(obj)
        if size % 2 != 0:
            return float(obj[size//2])
        else:
            return float((obj[size//2 - 1] + obj[size//2]) / 2)

    def quartile(self, obj):
        if len(obj) == 0:
            return None
        obj.sort()
        middle = len(obj) // 2
        q1 = self.median(obj[:middle + 1])
        q2 = self.median(obj[middle:])
        return [q1, q2]

    def var(self, obj):
        if len(obj) == 0:
            return None
        mean = self.mean(obj)
        var = sum((x - mean) ** 2 for x in obj) / len(obj)
        return var

    def std(self, obj):
        if len(obj) == 0:
            return None
        var = self.var(obj)
        return math.sqrt(var)
