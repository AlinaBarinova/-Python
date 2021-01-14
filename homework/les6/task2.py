class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    weight_per_sq_meter = 25
    depth = 5

    def count_asphalt(self):
        return self._length * self._width * Road.weight_per_sq_meter * (Road.depth/100)


road = Road(20, 500)
print(road.count_asphalt())