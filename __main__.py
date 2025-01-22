import json
file = open("./config.json")
config = json.loads(file.read())
file.close()
print(config["data_port"])