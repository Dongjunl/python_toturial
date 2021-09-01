
# Read the data file
columns ={'data':0, 'time':1, 'tempout':2, 'windspeed':7}

types = {'tempout': float, 'windspeed':float}

data = {}

for column in columns:
    data[column] = []




filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    
    # read the first three lines (header)
    for _ in range(3):
        datafile.readline()
        print(headerline)

    
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)


#print (data)
