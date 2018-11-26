import configparser
config = configparser.ConfigParser()
config.read("Config.ini")
print(config.sections())
print(config["FFmpeg"]["ExecutablePath"])