import time


class TimeCounter:
    retention: int
    bucket: float
    increments: list[tuple[float, int]] = []

    def __init__(self, retention: int, bucket: float):
        """
        TimeCounter is a class to count the number of events in a given time period.

        :param retention: Number of seconds to keep the data
        :param bucket:
        """
        self.retention = retention
        self.bucket = bucket

    def add(self, n: int):
        curtime = time.time()
        cur = curtime // self.bucket
        if self.increments and self.increments[-1][0] == cur:
            self.increments[-1] = (cur, self.increments[-1][1] + n)
        else:
            self.increments.append((cur, n))

        for i in range(len(self.increments)):
            if self.increments[i][0] < (curtime - self.retention) // self.bucket:
                self.increments.pop(0)

    def last(self, seconds: int) -> int:
        """
        Returns the number of events in the last n seconds.
        :param seconds: Number of seconds to look back
        :return: Number of events
        """
        if seconds > self.retention:
            raise ValueError("Cannot measure time more than retention")
        if seconds < self.bucket:
            raise ValueError("Cannot measure time less than bucket")
        return sum(
            [i[1] for i in self.increments if i[0] >= (time.time() - seconds) // self.bucket]
        )
