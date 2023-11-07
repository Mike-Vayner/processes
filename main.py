"""This program creates 10 subprocesses,
which then contain a varying number of threads."""

import time
from concurrent import futures


def wait_and_print(x: int, y: int) -> None:
    """Wait `x * y` seconds, then prints the product."""

    product = x * y
    time.sleep(product)
    print(product)


def create_threads(i: int) -> None:
    """Create `i` threads in this process."""

    if i <= 0:
        return
    with futures.ThreadPoolExecutor() as executor:
        for j in range(10):
            executor.submit(wait_and_print, i, j)


def main() -> None:
    with futures.ProcessPoolExecutor() as executor:
        for i in range(10):
            executor.submit(create_threads, i)


if __name__ == "__main__":
    main()
