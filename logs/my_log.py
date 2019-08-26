import logging
from anphat_pc.settings import BASE_DIR


class AnphatLogger(object):
    __instance = None

    @staticmethod
    def initialize():
        return AnphatLogger.get_instance()

    @staticmethod
    def get_instance():
        if AnphatLogger.__instance is None:
            AnphatLogger()

        return AnphatLogger.__instance

    def __init__(self, name):
        super(AnphatLogger, self).__init__()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # File handler which logs even debug messages
        fh = logging.FileHandler(BASE_DIR+'/logs/anphatpc.log')
        fh.setLevel(logging.DEBUG)

        # Console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
