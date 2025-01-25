import logging

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

debug_logger = logging.getLogger("debug")
debug_logger.setLevel(logging.DEBUG)
