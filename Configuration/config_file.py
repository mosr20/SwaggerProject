import logging
from configparser import ConfigParser


class set_config:
    def __init__(self):
        self.file = 'D:\SwaggerProject\Configuration\config.ini'
        self.config = ConfigParser()
        self.read = self.config.read(self.file)

    def send_get(self):
        try:
            return self.config['PATH']['GET_PATH']
        except ConfigParser.NoOptionError as error:
            logging.error(error)


    def send_post(self):
        try:
            return self.config['PATH']['POST_PATH']
        except ConfigParser.NoOptionError as error:
            logging.error(error)


    def send_put(self):
        try:
            return self.config['PATH']['PUT_PATH']
        except ConfigParser.NoOptionError as error:
            logging.error(error)
