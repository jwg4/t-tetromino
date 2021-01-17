import os

from datetime import datetime
from random import randint

FOLDER = "/aci/output"


if __name__ == '__main__':
    timestamp = datetime.utcnow()
    rint = randint(1, 1000000)

    output_string = "Timestamp: %s, Random int: %d" % (timestamp, rint)
    destination = os.path.join(FOLDER, "output.txt")

    with open(destination, "w") as f:
        f.write(output_string)
    print(output_string)
