import configparser
config = configparser.ConfigParser()
config.read('config.ini')

for i in config.sections():
    for j in config[i]:
        print(f'{config[i]}\t: {j}\t: {config.get(i, j)}')
