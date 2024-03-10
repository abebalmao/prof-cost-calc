from util.config import Config

config = Config()


def log(string):
    if config.log_to_file == 1:
        print("log: " + string)