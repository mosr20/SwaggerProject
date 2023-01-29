import logging


def Creatinglog(logname):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s      %(levelname)s     %(message)s')
    handler = logging.FileHandler(logname+'.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.error("Rest Api error")


