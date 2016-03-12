def dirReduc(arr):
    # your code
    reducible_dir = {"NORTH":"SOUTH", "SOUTH":"NORTH","EAST":"WEST", "WEST":"EAST"}
    i = 0
    while i < len(arr)-1:
        if reducible_dir[arr[i]] == arr[i+1]:
            del arr[i]
            del arr[i]
            i = 0
        else:
            i = i + 1
    return arr

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
b = ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']
u =["NORTH", "WEST", "SOUTH", "EAST"]
print dirReduc(u)
