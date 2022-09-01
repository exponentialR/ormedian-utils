import logging
import itertools
import time
import sys
from colorama import Fore

class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)



# done = False

def animate(done=True):
    for c in itertools.cycle(['||||||', '/', '-----', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


def animated_exit(someText):
    print(Fore.RED + someText, end='');
    for i in range(10):
        print(Fore.RED + '|||||', end='')
        time.sleep(0.1)
# t.start()
#
# #long process here
# time.sleep(100)
# done = True

# import logging
# import datetime
#
# # Create custom logger logging all five levels
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# # Define format for logs
# fmt = '%(asctime)s | %(levelname)8s | %(message)s'
#
# # Create stdout handler for logging to the console (logs all five levels)
# stdout_handler = logging.StreamHandler()
# stdout_handler.setLevel(logging.DEBUG)
# stdout_handler.setFormatter(CustomFormatter(fmt))
#
# # Create file handler for logging to a file (logs all five levels)
# today = datetime.date.today()
# file_handler = logging.FileHandler('my_app_{}.log'.format(today.strftime('%Y_%m_%d')))
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(logging.Formatter(fmt))
#
# # Add both handlers to the logger
# logger.addHandler(stdout_handler)
# logger.addHandler(file_handler)
#
#
# logger.debug('This is a debug-level message')
# logger.info('This is an info-level message')
# logger.warning('This is a warning-level message')
# logger.error('This is an error-level message')
# logger.critical('This is a critical-level message')
#
# mu = [i for i in range(1, 202)]
# mx = 204
# for i in range (5):
#     if mx not in mu:
#         logger.exception(f'{mx} not in {mu}', exc_info=False)
#         # break
#     else:
#         print('That is not correct')