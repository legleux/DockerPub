import logging
import datetime
import os

file_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
class CustomFormatter(logging.Formatter):

    grey      = "\x1b[38;20m"
    bold_grey = "\x1b[38;1m"
    yellow    = "\x1b[33;20m"
    red       = "\x1b[31;20m"
    bold_red  = "\x1b[31;1m"
    inverted  = "\x1b[7;1m"
    cyu       = "\x1b[32;1m"
    reset     = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: cyu + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: inverted + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, "%b %d-%H:%M:%S")
        return formatter.format(record)

logger = logging.getLogger("dockerpub")
logger.setLevel(logging.DEBUG)

if not os.path.isdir("log"):
    os.mkdir("log")
ct = datetime.datetime.now()
stamp = "_".join(str(ct).split(" "))
fh = logging.FileHandler(f"log/{stamp}.log")
file_format = logging.Formatter(file_format)
fh.setLevel(level=logging.DEBUG)
# create console handler with a same? log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())
fh.setFormatter(file_format)

logger.addHandler(ch)
logger.addHandler(fh)
# logger.debug("Initialized logging")
