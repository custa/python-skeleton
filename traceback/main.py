def a():
    return 0 / 0


def b():
    a()


if __name__ == "__main__":
    b()
