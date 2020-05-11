import math


class VectorException(Exception):
    def __init__(self, message="VectorException"):
        self.message = message

    def __str__(self):
        return self.message


class Vector:
    def __init__(self, *args):
        for argument in args:
            if not isinstance(argument, (int, float)):
                raise VectorException("Type {} is not valid for vector".format(type(argument)))

        if len(args):
            self.coordinates = []
            for element in args:
                self.coordinates.append(element)

            self.dimension = len(self.coordinates)
        else:
            self.coordinates.append(0)
            self.dimension = 1

    def __repr__(self):
        return "Vector ({})".format(", ".join(str(coordinate) for coordinate in self.coordinates))

    def __str__(self):
        return "Vector ({})".format(", ".join(str(coordinate) for coordinate in self.coordinates))

    def __add__(self, other):
        if self.dimension == other.dimension:
            new_vector = []
            for first_vector, second_vector in zip(self.coordinates, other.coordinates):
                new_vector.append(first_vector + second_vector)
            return Vector(*new_vector)
        else:
            raise VectorException()

    def __iadd__(self, other):
        if self.dimension == other.dimension:
            for index, second_vector in enumerate(other.coordinates):
                self.coordinates[index] += second_vector
            return self
        else:
            raise VectorException()

    def __sub__(self, other):
        if self.dimension == other.dimension:
            new_vector = []
            for first_coordinate, second_coordinate in zip(self.coordinates, other.coordinates):
                new_vector.append(first_coordinate - second_coordinate)
            return Vector(*new_vector)
        else:
            raise VectorException("The dimension of the vectors is not equal")

    def __isub__(self, other):
        if self.dimension == other.dimension:
            for index, second_vector in enumerate(other.coordinates):
                self.coordinates[index] -= second_vector
            return self
        else:
            raise VectorException("The dimension of the vectors is not equal")

    def __abs__(self):
        return math.sqrt(sum(coordinate ** 2 for coordinate in self.coordinates))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_coordinates = []
            for coordinate in self.coordinates:
                new_coordinates.append(coordinate * other)
            return Vector(*new_coordinates)
        elif isinstance(other, Vector):
            return sum(first * second for first, second in zip(self.coordinates, other.coordinates))

    def __imul__(self, const):
        for index, coordinate in enumerate(self.coordinates):
            self.coordinates[index] *= const
        return self

    def __iter__(self):
        return self.coordinates.__iter__()

    def __len__(self):
        return self.dimension

    def __getitem__(self, index):
        if index < self.dimension:
            return self.coordinates[index]
        else:
            raise VectorException()

    def __eq__(self, other):
        if self.dimension == other.dimension:
            equal = False
            for first_coordinate, second_coordinate in zip(self.coordinates, other.coordinates):
                if first_coordinate != second_coordinate:
                    break
            else:
                equal = True
            return equal
        else:
            raise VectorException()
