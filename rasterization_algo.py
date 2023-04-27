def get_coefficients_of_general_equation_of_line(start: tuple[float, float], 
                                                 end: tuple[float, float]) \
                                                 -> tuple[float, float]:
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        raise RuntimeError('Vertical line')

    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return k, b    



def step_algo(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    if start == end:
        return [start]
    try:
        k, b = get_coefficients_of_general_equation_of_line(start, end)
    except RuntimeError:
        return [(start[0], y) for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1)]
    if start[0] > end[0]:
        start, end = end, start
    x1 = start[0]
    x2 = end[0]
    result = []
    for x in range(x1, x2 + 1):
        y = k * x + b
        result.append((x, round(y)))
    return result


def digital_differential_analyzer_algo(start: tuple[int, int], 
                                       end: tuple[int, int]) \
                                        -> list[tuple[int, int]]:
    if start == end:
        return [start]
    if start[0] > end[0]:
        start, end = end, start
    try:
        k, _ = get_coefficients_of_general_equation_of_line(start, end)
    except RuntimeError:
        return [(start[0], y) for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1)]
    step = 1
    result = [start]
    x1 = start[0]
    x2 = end[0]
    for x in range(x1 + 1, x2 + 1):
        result.append((x, result[-1][1] + k * step))
    return result


def bresenham_for_line_algo(start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    if start == end:
        return [start]
    try:
        k, _ = get_coefficients_of_general_equation_of_line(start, end)
    except RuntimeError:
        return [(start[0], y) for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1)]
    
    if not (0 <= k <= 1):
        raise RuntimeError("Line not from 1 octant")
    if start[0] > end[0]:
        start, end = end, start
    
    result = [start]
    x, y = start
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    error = 2 * dy - dx

    while x <= end[0]:
        x += 1
        if error >= 0:
            y += 1
            error += 2 * (dy - dx)
        else:
            error += 2 * dy

        result.append((x, y))
    
    return result

def bresenham_for_circle_in_center_of_coordinates(radius: int) -> list[tuple[int, int]]:
    x = 0
    y = radius
    error = 3 - 2 * radius
    result = [(x, y), (x, -y), (y, x), (-y, x)]
    while x < y:
        x += 1
        if error >= 0:
            error += 4 * (x - y) + 10
            y -= 1
        else:
            error += 4 * x + 6
        
        result.append((x, y))
        result.append((x, -y))
        result.append((-x, y))
        result.append((-x, -y))

        result.append((y, x))
        result.append((y, -x))
        result.append((-y, x))
        result.append((-y, -x))

    return result


def bresenham_for_circle_algo(center: tuple[int, int], radius: int) -> list[tuple[int, int]]:
    if radius == 0:
        return center

    result = bresenham_for_circle_in_center_of_coordinates(radius)

    for i, (x_center, y_center) in enumerate(result):
        x = x_center + center[0]
        y = y_center + center[1]
        result[i] = (x, y)
    
    return result
