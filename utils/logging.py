import logging

from pythonjsonlogger import jsonlogger


def get_logger(level, name):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    json_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    json_handler.setFormatter(formatter)
    logger.addHandler(json_handler)
    return logger
