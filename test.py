import numpy as np
def unique(L):
    i = 0
    while i < len(L):
        j = i + 1
        while j < len(L):
            if L[j] == L[i]:
                del L[j]
            else:
                j += 1
        i += 1

    return L


if __name__ == '__main__':

    arr = np.random.randint(1, 11, size=20)
    print(arr)

    print(unique(arr))
