import time
from concurrent.futures.thread import ThreadPoolExecutor

from timecounter import TimeCounter


def test_timecount():
    counter = TimeCounter(10, 0.1)
    counter.add(1)
    time.sleep(0.1)
    counter.add(2)
    counter.add(3)
    assert counter.last(1) == 6


def add_one(counter: TimeCounter):
    counter.add(1)
    time.sleep(0.01)


def test_multithreaded():
    counter = TimeCounter(20, 0.4)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(10000):
            executor.submit(add_one, (counter))

    assert counter.last(20) == 10000
