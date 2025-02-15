def initial_state():
    return (8, 0, 0)

def is_goal(s):
    a, b, _ = s
    if a == 4 and b == 4:
        return True
    else:
        return False

def successors(s):
    a, b, c = s

    t = 5 - b
    if a > 0 and t > 0:
        if a > t:
            yield(( a-t, 5, c), t)
        else:
            yield(( 0, a+b, c), a)
    if c > 0 and t > 0:
        if c > t:
            yield(( a, 5, c-t), t)
        else:
            yield(( a, b+c, 0), c)

    t = 8 - a
    if b > 0 and t > 0:
        if b > t:
            yield(( 8, b-t, c), t)
        else:
            yield(( a+b, 0, c), b)
    if c > 0 and t > 0:
        if c > t:
            yield(( 8, b, c-t), t)
        else:
            yield(( a+c, b, 0), c)

    t = 3 - c
    if b > 0 and t > 0:
        if b > t:
            yield(( a, b-t, 3), t)
        else:
            yield(( a, 0, c+b), b)
    if a > 0 and t > 0:
        if a > t:
            yield(( a-t, b, 3), t)
        else:
            yield(( 0, b, a+c), a)
