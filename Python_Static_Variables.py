def f():
    f.x = getattr(f, 'x', 5)
    print(f.x)
    f.x += 1
    return

def main():
    f()
    f()
    f()
    return

main()