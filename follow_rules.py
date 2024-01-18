import os
import time
from typing import NoReturn

import schedule


def run_rule() -> None:
    os.system(
        "/home/encryptedbee/programfiles/anaconda3/bin/python /home/encryptedbee/tesla/projects/20_20_20/rule.py"
    )


def main() -> NoReturn:
    print("20-20-20 rule starting.")
    schedule.every(20).minutes.do(run_rule)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
