''' A pie chart is a circular graphical representation of a dataset, where each category frequency is represented
    by a slice(or circular sector) with an amplitude in degrees given by the single frequency percentage over the 
    total of frequencies. You can obtain the degree of sectors follwing these steps:
        - Calculate frequencies total.
        - Calculate percentage of every category frequency dividing it by the frequencies total.
        - Transform every percentage in degree multiplying it for 360.'''


def pie_chart(data):
    # new_obj = {}
    # sum = 0
    # single = 0
    # for i, j in data.items():
    #     sum += j
    # single = 360/sum
    # new_key = list(data.keys())
    # new_values = list(data.values())
    # for i in range(len(new_key)):
    #     new_obj.update({new_key[i] : round(float(new_values[i]) * single,1)})
    # return new_obj

    sum = 0
    single = 0
    for i, j in data.items():
        sum+=j
    single = 360/sum
    for i, j in data.items():
        data[i] = round(j * single,1)
    return data


print(pie_chart({ "a": 1, "b": 2 }))
print(pie_chart({ "a": 30, "b": 15, "c": 55 }))
print(pie_chart({ "a": 8, "b": 21, "c": 12, "d": 5, "e": 4 }))