  # config.readfp(open('/include/clusteTester.conf'))
    #try:
    #    aa=open(CONFIG_FILE, "r")
    #except Exception as exceptObj:
    #    print("Errore: ", str(exceptObj))



"""   config.read(CONFIG_FILE)  
        username = config.get('N4J_CONNECT', 'username')
        password = config.get('N4J_CONNECT', 'password')
        hostname = config.get('N4J_CONNECT', 'url')
        database = config.get('N4J_CONNECT', 'database') 

oppure:
 
    for section in config.sections():
        for key in config[section]:
            print((key, config[section][key]))
"""