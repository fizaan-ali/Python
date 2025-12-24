def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
        return x

    return inner()

f = outer
print(f())