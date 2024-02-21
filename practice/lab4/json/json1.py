import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("/Users/IeilaUmarova/lab4/json/sample.json", "r") as file:
    data = json.load(file)
    for item in data['imdata']:
        print(f"{item['l1PhysIf']['attributes']['dn']}                              {item['l1PhysIf']['attributes']['speed']}   {item['l1PhysIf']['attributes']['mtu']}")