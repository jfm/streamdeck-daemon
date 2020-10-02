import logging


class Logger(object):
    def __init__(self, config):
        self.logger = logging.getLogger('StreamDeck')

        if(config.config['streamdeck']['logger'] == "logfile"):
            hdlr = logging.FileHandler("streamdeck.log")
        else:
            hdlr = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s " + " %(levelname)s %(message)s"
        )
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        if config.config['streamdeck']['loglevel'] == "debug":
            self.logger.setLevel(logging.DEBUG)
        elif config.config['streamdeck']['loglevel'] == "error":
            self.logger.setLevel(logging.ERROR)
        else:
            self.logger.setLevel(logging.INFO)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
