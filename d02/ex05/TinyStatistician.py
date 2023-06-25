import math

class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, obj):
        return sum(obj) / len(obj)

    def median(self, obj):
        obj = sorted(obj)
        size = len(obj)
        result = 0.0
        if size % 2 != 0:
            return float(obj[int(size / 2)])
        else:
            return float((obj[int((size - 1) / 2)] + obj[int(((size - 1) / 2) + 1)]) / 2)

    def quartile(self, obj):
        if len(obj) == 0:
            return None
        obj = sorted(obj)
        middle = len(obj) // 2
        q1 = self.median(obj[:middle + 1])
        q2 = self.median(obj[middle:])
        return [q1, q2]

    def var(self, obj):
        if len(obj) == 0:
            return None
        result = self.mean(obj)
        result = sum((x - result)**2 for x in obj) / len(obj)
        return result

    def std(self, obj):
        if len(obj) == 0:
            return None
        result = self.mean(obj)
        result  = sum(pow(x - result, 2) for x in obj) / len(obj)
        result  = math.sqrt(result)
        return result


if __name__ == '__main__':
    obj = TinyStatistician()
    print("\nMean test:")
    print(obj.mean([1, 2, 3, 4, 5]))
    print("\nMedian test:")
    print(obj.median([1, 3, 2, 4, 5]))
    print("\nQuartiles test:")
    print(obj.quartile([1, 42, 300, 10, 59]))
    print("\nVariance test:")
    print(obj.var([1, 42, 300, 10, 59]))
    print("\nStandart deviation test:")
    print(obj.std([1, 42, 300, 10, 59]))
