#!/usr/bin/env python3

from datetime import datetime
from random import randint


if __name__ == '__main__':
    timestamp = datetime.utcnow()
    rint = randint(1, 1000000)

    output_string = "Timestamp: %s, Random int: %d" % (timestamp, rint)

    with open("output.txt", "w") as f:
        f.write(output_string)
