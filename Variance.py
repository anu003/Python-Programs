def variance(data):
    mean = sum(data)/len(data)
    print mean
    var = sum((x-mean)**2 for x in data)/len(data)
    ci = 1.96*((var/len(data))**0.5)
    print mean - ci
    print mean + ci
    return var

print variance([0.79,0.7,0.73,0.66,0.65,0.7,0.74,0.81,0.71,0.7])
