def parse(text):
    if not text:
        return {
            "command": None,
            "payload": None
        }
    tokens = text.split()
    command = tokens[0]
    payload = tokens[1:]
    return {
        "command": command,
        "payload": payload
    }
