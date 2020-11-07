# Your code here


def expensive_seq(x, y, z):
    hashtable = {}
    return calc_seq(x, y, z, hashtable)


def calc_seq(x, y, z, hashtable):
    if (x, y, z) in hashtable:
        return hashtable[(x, y, z)]

    if x <= 0:
        hashtable[(x, y, z)] = y+z
        return hashtable[(x, y, z)]

    hashtable[(x, y, z)] = calc_seq(x-1, y+1, z, hashtable) + \
        calc_seq(x-2, y+2, z*2, hashtable) + calc_seq(x-3, y+3, z*3, hashtable)
    return hashtable[(x, y, z)]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
