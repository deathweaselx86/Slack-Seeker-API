import queue as Q
from models.message import Message

def scoreMessage():
    q = Q.PriorityQueue()
    terms = ["monolith", "frontend", "backend", "python", "javascript", "config", "pipeline", "flaky"]
    messages = [
        Message("No config secrets file", 0, ["monolith"]),
        Message("Monolith backend in python", 0, ["backend"]),
        Message("Javascript error in client-js", 0, ["javascript", "client-js"]),
        Message("Ruby not working", 0, ["fullstack"]),
        Message("Config file missing in app backend", 0, ["backend"]),
        Message("Python requirement outdated", 0, ["python"]),
        Message("RUM Metrics is flaky", 0, ["testing", "rum"]),
        Message("Jenkins pipeline generating weird errors", 0, ["jenkins"]),
        Message("Services not found", 0, ["data services"]),
        Message("JS-SDK having problem in build pipeline", 0, ["sdk", "fullstack", "javascript"])
    ]
    
    for msg in messages:
        text = msg.text.lower()
        tags = msg.tags
        for term in terms:
            if term in text:
                msg.score += 1
            for tag in tags:
                if term in tag or tag in term:
                    msg.score += 5
        q.put(msg)
    
    while not q.empty():
        cur = q.get()
        print('Message: {}, score: {}, tags: {}'.format(cur.text, cur.score, cur.tags))
        
scoreMessage()
    

