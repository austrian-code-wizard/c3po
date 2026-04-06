import logging

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s [ %(name)s - %(levelname)s]: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
