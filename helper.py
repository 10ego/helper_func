#Input any nested json object to return it as a single dict to add as a new row in your dataframe

def flatify(json):

    def engine(data, header=''):
        
        if type(data) is list:
            c=0
            for obj in data:
                engine(obj, '{}[{}]'.format(header,str(c)))
                c+=1
                
        elif type(data) is dict:
            for k,v in data.items():
                engine(v, header+k+',')
        
        else:
            row[header]=data
            
    row={}
    engine(json)
    return row


#Recursively replaces double spacing with single spacing

def recursive_spaces(text):
    if '  ' in text:
        text = recursive_spaces(text.replace('  ', ' '))
    return text


# Build a Structured JSON object from HTML <table> elements using BeautifulSoup
def tableDataText(table):
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        #rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return headerow, rows, table.caption.stripped_strings

def tableDataDict(html):
    soup = BeautifulSoup(html)
    l = []
    for s in soup.find_all('table'):
        d = {}
        header, table, caption = tableDataText(BeautifulSoup(str(s)))
        d['caption'] = [text for text in caption][0]
        d['header'] = header
        d['data'] = table
        l.append(d)
    return l
