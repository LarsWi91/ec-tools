
from transonic import boost

@boost
def func(n: int):
    return 2 * n

if __name__ == "__main__":
    print("result func(1):", func(1))
