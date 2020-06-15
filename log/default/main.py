import logging


if __name__ == "__main__":
    logging.warning('Watch out!')  # will print a message to the console
    logging.info('I told you so')  # will not print anything
    logging.warning('%s, %s', 1, 2)  # will print a message to the console
