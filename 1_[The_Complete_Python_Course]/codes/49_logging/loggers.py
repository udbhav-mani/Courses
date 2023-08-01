import logging

logging.basicConfig(
    format="%(name)s :: %(levelname)-8s :: %(message)s",
    level=logging.INFO,
    filename="logs.txt",
)
logger = logging.getLogger(__name__)

logger.info("This is a info message")
logger.debug("This is a info message")
logger.critical("This is a info message")

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL"""
