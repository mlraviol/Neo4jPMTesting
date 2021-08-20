CT_PROMPT = "    N4jTester --> "
CT_MENU = " 1: CONNECT\n 2: DISCONNECT\n 3: START RO TX\n 4: START RW TX\n 5: COMMIT TX\n 6: ROLLBACK TX\n 7: EXECUTE QUERY\n 0: QUIT\n\n"
CONNECT_PROMPTS = { 'URI :' : "", 'DB Name :':  "", 'Username : ': "", 'Password : ':  "" }
CONFIG_FILE = "./Include/clusterTester.conf"


import configparser, os
from typing import IO

def ctInit():

    configDict = {}
    config = configparser.RawConfigParser()
    config.read(CONFIG_FILE)

    configDict = dict(config.items('N4J_CONNECT'))
    return configDict