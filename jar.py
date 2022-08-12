class Jar:
    def __init__(self, capacity=12):
        # capacity is max number, raise valueerror if not positive int
        if capacity < 0:
            raise ValueError("capacity too low")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        # return n 🍪's for what is in the jar
        return self.size * '🍪'
    def deposit(self, n):
        # add n cookies to the jar, but if exceeds capacity raises ValueError
        if n + self.size > self.capacity:
            raise ValueError("exceeds capacity")
        self._size += n
    def withdraw(self, n):
        # remove n cookies from jar, but if exceeds then raise valueerror
        if self.size - n < 0:
            raise ValueError('withdrawing too many')
        self._size = self._size - n

    @property
    def capacity(self):
        # return the jar's capacity
        return self._capacity

    @property
    def size(self):
        # return the number of cookies in the jar
        return self._size