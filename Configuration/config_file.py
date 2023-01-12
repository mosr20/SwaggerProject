from configparser import ConfigParser


class set_config:
    def __init__(self):
        self.file = 'config.ini'
        self.config = ConfigParser()
        self.read = self.config.read(self.file)

    def send_get(self):
        return self.config['PATH']['GET_PATH']

    def send_post(self):
        return self.config['PATH']['POST_PATH']

    def send_put(self):
        return self.config['PATH']['PUT_PATH']


aaa = set_config()
ddd = aaa.send_get()
print(ddd)



