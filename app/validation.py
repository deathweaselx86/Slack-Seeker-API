def isValid(resp):
    command, payload = resp["command"], resp["payload"]
    if not command:
        return True, None
    if command == "tags":
        if payload:
            pass    # TODO: Drop payload when user adds text after "tags" 
        return True, None
    if command == "show":
        return True, None
    if command == "search":
        firstElem = payload[0]
        if firstElem[0] != '\"':
            return False, "missing_starting_quote"
        for elem in payload:
            if elem[-1] == '\"':
                return True, None
        return False, "missing_ending_quote"
    if command == "save":
        if payload:
            pass    # TODO: Implement save with multiple parameters
        return True, None
        
        
        




    
    

