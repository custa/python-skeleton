"""
https://stackoverflow.com/questions/12158048/changing-loggings-basicconfig-which-is-already-set
"""
import logging

logging.warning("before logging.basicConfig")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    format="%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s",
    level=logging.INFO)

if __name__ == "__main__":
    logging.warning('Watch out!: %d', 1)  # will print a message to the console
    logging.info('I told you so')
