class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
