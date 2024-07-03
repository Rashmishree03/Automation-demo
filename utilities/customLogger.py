import logging
import os


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename=os.path.dirname(os.getcwd()) + "/OrangeHRM/Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
