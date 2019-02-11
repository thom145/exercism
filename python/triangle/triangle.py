def is_equilateral(sides):
    if check_if_triangle(sides):
        for side in sides:
            if side == 0:
                return False
            else:
                return len({side for side in sides}) == 1
    else:
        return False

def is_isosceles(sides):
    if check_if_triangle(sides):
        for side in sides:
            if side == 0:
                return False
            else:
                return len({side for side in sides}) <= 2
    else:
        return False

def is_scalene(sides):
    if check_if_triangle(sides):
        for side in sides:
            if side == 0:
                return False
            else:
                return len({side for side in sides}) == 3
    else:
        return False

def check_if_triangle(sides):
    if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
        return True
    else:
        return False
