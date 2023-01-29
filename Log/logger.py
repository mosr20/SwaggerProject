import logging


def Creatinglog(level , logname):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s      %(levelname)s     %(message)s')
    handler = logging.FileHandler(logname+'.log')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if level =='info':
        return logger.info("Rest Api info")
    if level =='error':
        return logger.error("Rest Api info")



