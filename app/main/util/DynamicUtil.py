import os
import configparser


class DynamicUtil():

    def __init__(self, configfile):
        self.config = self.get_parser_sections(configfile=configfile)

    def get_file_path(self, configfile):
        try:
            cwd = os.getcwd()
            config_file = "app/main/config/"+configfile
            config_file_path = os.path.join(cwd, config_file)
            return config_file_path
        except Exception as e:
            print("Error in DynamicUtil.get_file_path(): ", e)

    def get_parser_sections(self, configfile):
        try:
            config = configparser.ConfigParser()
            config.read(self.get_file_path(configfile=configfile))
            return config
        except Exception as e:
            print("Error in DynamicUtil.get_parser_sections() : ", e)