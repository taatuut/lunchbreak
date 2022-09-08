import random

while True:
    nodes = ""
    links = ""
    n = 8 # initial number of nodes
    i = int(n * random.random())+4 # always add minimum of two because random function can give back zero, but add four for bit longer funnel by default
    sep = ","
    for x in range(i):
        node = {
            "node": x,
            "name": "node"+str(x)
        }
        nodes = nodes + str(node)
        if x < i-1:
            nodes = nodes + sep
            m = 2 # initial number of links per node
            j = int(m * random.random())+2 # always add minimum of two because random function can give back zero
            for l in range(j): # create links per node 
                t = x+int(3 * random.random())+1
                t = t if t < i-1 else i-1 # limit target to 'highest' node
                v = int(4 * random.random())+1 # weight of the link connecting two nodes 
                link = {
                    "source": x,
                    "target": t,
                    "value": v
                }
                links = links + str(link) + sep
    links = links if links[-1] != "," else links[:-1]
    doc = {
    "nodes": [
        nodes
    ],
    "links": [
        links
    ]
    }
    # yes, I like to mess around with dictionaries, str, and replace, could be done more neat with json dump stuff.
    doc = str(doc).replace("'",'"').replace('["',"[").replace('"]',"]")
    print(doc)
