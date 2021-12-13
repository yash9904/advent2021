
def modefn(list_here, i):
    '''
    Arguments: 
        list_here = a candidate list of strings for which we are going to find the 'mode' of the values at index i
        i = the index for which we will find the mode

    Returns:
        mode = the most occuring values at index i of all the strings, the values being 0 and 1. If both the values are having same frequency we choose 1
    
    '''
    count_0 = 0
    count_1 = 0

    size = len(list_here)

    for j in range(size):
        if list_here[j][i: i + 1] == '0':
            count_0 += 1
        else:
            count_1 += 1
    
    if count_0 > count_1:
        return 0
    else:
        return 1

def sublist(k, indices):
    filtered_list = list()
    for i in range(len(k)):
        if i in indices:
            filtered_list.append(k[i])
    return filtered_list

with open('day3\input.txt') as f:
    k = f.read().split('\n')

size = len(k[0])

indices_o2 = list(range(len(k)))
indices_co2 = list(range(len(k)))

temp_arr_o2 = list()
temp_arr_co2 = list()

for i in range(size):
    temp_indices_o2 = list()
    temp_indices_co2 = list()

    sub_k_o2 = sublist(k, indices_o2)
    sub_k_co2 = sublist(k, indices_co2)
    
    temp_mode_o2 = modefn(sub_k_o2, i)
    temp_mode_co2 = modefn(sub_k_co2, i)


    for j in range(len(k)):
        if k[j][i: i + 1] == str(temp_mode_o2) and j in indices_o2:
            temp_arr_o2.append(k[j])
            temp_indices_o2.append(j)
        if k[j][i: i + 1] == str(1 - temp_mode_co2) and j in indices_co2:
            temp_arr_co2.append(k[j])
            temp_indices_co2.append(j)

    indices_o2 = temp_indices_o2
    indices_co2 = temp_indices_co2

ox_rate = temp_arr_o2[-1]
co2_rate = temp_arr_co2[-1]

ox_dec = 0
co2_dec = 0

for i in range(size):
    if ox_rate[i: i + 1] == '0':
        pass
    elif ox_rate[i: i + 1] == '1':
        ox_dec += pow(2, size - i - 1)
    if co2_rate[i: i + 1] == '0':
        pass
    elif co2_rate[i: i + 1] == '1':
        co2_dec += pow(2, size - i - 1)

print(ox_dec * co2_dec)