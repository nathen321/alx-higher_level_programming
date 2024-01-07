#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = validate(tuple_a)
    tuple_b = validate(tuple_b)
    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

def validate(v_tuple=()):
    if len(v_tuple) < 2:
        if len(v_tuple) == 1:
            v_tuple = (v_tuple[0], 0)
        elif len(v_tuple) == 0:
            v_tuple = (0, 0)
    elif len(v_tuple) > 2:
        v_tuple = (v_tuple[0], v_tuple[1])
    return v_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
