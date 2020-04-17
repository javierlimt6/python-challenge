#!/usr/bin/python3.8

functions = {}
strmtds = {}
listmtds = {}
with open('Consolidating-Basic-Python-Notes.csv', 'r') as f:
    f.readline()
    for row in f:
        row = row.strip().split(',')
        #print(f'original row: {row}')
        start, end = [], []
        for index, each in enumerate(row):
            if each.startswith('"'):
                start.append(index)
            elif each.endswith('"'):
                end.append(index + 1)
        for start, end in zip(reversed(start), reversed(end)):
            new_cell = ''.join(row[start:end])
            #print(f'create new cell idx {start} to {end - 1}: {new_cell}')
            del row[start:end]
            row.insert(start, new_cell.strip('"'))
        #print(f'new row: {row}')
                
        for col, datadict in zip(range(2, 5), (functions, strmtds, listmtds)):
            keys = row[col].split('; ')
            for key in keys:
                datadict[key] = datadict.get(key, 0) + 1
                #print(f'{key}: {datadict[key]}')

with open('histo.csv', 'w') as f:
    for name,data in zip(('functions', 'strings', 'lists'), (functions, strmtds, listmtds)):
        print(name, file=f)
        for key, value in data.items():
            print(f'{key}: {value}', file=f)
        print('', file=f)
        
