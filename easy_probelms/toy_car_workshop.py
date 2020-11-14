'''You work in a toy car workshop, and your job is to build toy cars from a collection of parts.
    Each toy car needs 4 wheens, 1 car body, and 2 figures of people to be placed inside. Given
    the total number of wheels, car bodies and figures available, how many complete toy cars
    can you make?'''


def cars(wheels, bodies, figures):
    one_wheel = wheels // 4
    one_bodies = bodies
    figures = figures // 2
    return min([one_wheel, one_bodies, figures])

print(cars(8, 2, 4))
print(cars(2, 48, 76))
print(cars(43, 15, 87))
print(cars(88, 37, 17))