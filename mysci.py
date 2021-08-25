# Initialize data variable
data = []

filename = "data/wxobs20170821.txt"


with open(filename, 'r') as datafile:
     # read the first three lines 
    for _ in range(3):
        print(_)
        datafile.readline()         

    # Read amd parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

# Debug
print(data[5:8][0]) 
print(data[5])  
