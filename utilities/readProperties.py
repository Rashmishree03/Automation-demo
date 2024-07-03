import configparser
import os

project_folder = os.path.dirname(os.getcwd())
config_file = project_folder + '/OrangeHRM/Configurations/config.ini'
config = configparser.RawConfigParser()
print("config file path")
print(config_file)
config.read(config_file)


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        return config.get('common', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('common', 'username')

    @staticmethod
    def getPassword():
        return config.get('common', 'password')
