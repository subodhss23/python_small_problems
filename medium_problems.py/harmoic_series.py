''' In mathematics, the harmonic series is the divergent infinite series:

    Its name derives from the concept of overtons, or harmonic in music.

    Create a function that, given a precision parameter, returns the value of the harmonic series. '''


def harmonic(n):
    result = 0
    for i in range(1,n+1):
        result += 1/i
    return round(result,3)

print(harmonic(3))
print(harmonic(1))
print(harmonic(5))