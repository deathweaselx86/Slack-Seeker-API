def isValid(resp):
    command, payload = resp["command"], resp["payload"]
    if not command:
        return True, None
    if command == "tags":
        if payload:
            pass    # TODO: Drop payload when user adds text after "tags" 
        return True, None
    if command == "tag":
        return True, None
    if command == "search":
        firstElem = payload[0]
        if firstElem[0] != '\"':
            return False, "missing_starting_quote"
        if firstElem[-1] == '\"':
            return True, None




    
    

