import logging

logging.basicConfig(
    filename="app.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


def get_logger(name: str):
    logger = logging.getLogger(name)
    return logger
