def checkOrder(order):
    for item in order:
        for item2 in order:
            if(item == item2):
                continue
            if(item[0] == item2[1] and item[1] == item2[0]):
                return True
    return False