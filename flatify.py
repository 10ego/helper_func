#Input any nested json object to return it as a single dict to add as a new row in your dataframe

def flatify(json):
    row={}
    def engine(data, header=''):
        if type(data) is list:
            c=0
            for obj in data:
                engine(obj, '{}[{}]'.format(header,str(c)))
                c+=1
        elif type(data) is dict:
            for k,v in data.items():
                engine(v, header+'.'+k)
        
        else:
            row[header]=data
    engine(json)
    return row
