import logging


def log_details():
    logging.basicConfig(
        filename="debug.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %p"
    )

    return logging.getLogger()


logger = log_details()
logger.info("Program execution started")