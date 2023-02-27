
def add(*args):
    addition = 0
    for n in args:
        addition += n

    return addition

print(add(1,2,3,4,5,6))