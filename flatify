#Input any nested json object to return it as a single value to add as a new row in your dataframe

def flatify(json):
    row={}
    
    def engine(data, header=''):
        if type(data) is dict:
            for obj in data:
                engine(obj, header+obj+'.')
        elif type(data) is list:
            c=0
            for elem in data:
                engine(elem, header+str(c)+'..')
                c+=1
        else:
            row[header]=data
            
    engine(json)
    return row
