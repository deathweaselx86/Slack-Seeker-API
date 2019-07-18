def parse(text):
    if not text:
        return {
            "command": None,
            "payload": None
        }
    tokens = text.split()
    command = tokens[0]
    payload = tokens[1:]

    if command == "save":
        new_payload = retokenize(payload)
        return {
            "command": command,
            "payload": new_payload
        }
    elif command == "search":
        new_payload = 

    return {
        "command": command,
        "payload": payload
    }

def retokenize(payload):
    message_URL = payload[0]
    tags = []
    description = []
    description_index = -1
    for i in range(1, len(payload)):
        if "|" in payload[i]:
            vertical_split = payload[i].split("|")
            # if "|" split by itself
            if vertical_split[0] == "" and vertical_split[1] == "":
                description.extend(payload[i+1:])
            # if "|" attached to description
            elif vertical_split[0] == "":
                description.append(vertical_split[1])
                # if the description is more than one word
                if payload[i+1:]:
                    description.extend(payload[i+1:])
            # if "|" attached to a tag
            elif vertical_split[1] == "":
                tags.append("`" + vertical_split[0] + "`")
                description.extend(payload[i+1:])
            # if "|" attached to both tag and description
            else:
                tags.append("`" + vertical_split[0] + "`")
                description.append(vertical_split[1])
                # if the description is more than one word
                if payload[i+1:]:
                    description.extend(payload[i+1:])
            break
        else:
            tags.append("`" + payload[i] + "`")
    description = " ".join(description)
    return {
        "message_URL": message_URL,
        "tags": tags,
        "description": description
    }
