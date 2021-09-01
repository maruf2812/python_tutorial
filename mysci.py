# Initialize data variable
columns = {'data':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12}
 
types ={'tempout':float, 'windspeed':float, 'windchill':float}

data = {}
for column in columns:
    data[column] = []

filename = 'data/wxobs20170821.txt'

filename = "data/wxobs20170821.txt"


with open(filename, 'r') as datafile:
     # read the first three lines 
    for _ in range(3):
        headerline =  datafile.readline()         
        print(headerline) 
    # Read amd parse the rest of the file
    for line in datafile:
        split_line = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)
        

def compute_windchill(t, v):
    a = 35.74
    b = 0.6215
    c= 35.75
    d = 0.4275

    v16 = v ** 0.16
   
    wci = a = (b*t) - (c * v16) + (d * t * v16)
    return wci

#Running the fucntion to compute wci
windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp, windspeed))

#Output comparison ofr data
print('                original  computed')
print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
print('------- ------ --------- --------- ----------')
zip_data = zip(data['data'], data['time'], data['windchill'], windchill)
for date, time, wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')
