import timeit
a = [i for i in range(1000)]

print(timeit.timeit('a = [i for i in range(10)]', number=100))
print(timeit.timeit('a = [i for i in range(100)]', number=100))
print(timeit.timeit('a = [i for i in range(1000)]', number=100))
print(timeit.timeit('a = [i for i in range(10000)]', number=100))
print(timeit.timeit('a = [i for i in range(100000)]', number=100))