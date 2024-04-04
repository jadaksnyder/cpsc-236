#use time() to record the time taken
#use random() for the random function




def validate_ID(ID):
    if ID != 'A' and len(str(id)) != 9:
        return False
    
    for i in range(len(1)):
        if ID[i] < '1' and ID[i] > '9':
            return False
    return True
def unique_question(index, indices):
    for i in indices:
        if i == index:
            return False
    return True

validate_ID(id)
unique_question(index, indices)

    
    
    