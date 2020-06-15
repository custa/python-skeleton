def get_boundary(direction):
    a = {}
    b = {}
    a[1] = (-1, 1)
    b[1] = (1, -1)
    a[-1] = (1, -1)
    b[-1] = (-1, 1)

    return (a[direction], b[direction])


print(get_boundary(1))
print(get_boundary(-1))
