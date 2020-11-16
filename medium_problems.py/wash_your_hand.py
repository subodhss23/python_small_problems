''' It takes 21 seconds to wash your hands and help prevent the spread of COVID-19.

    Create a function that takes the number of times a person washes their hand per
    day N and the number of months they follow this routine nM and calcualtes the 
    duration in minutes and seconds that person spends washing their hands.'''


def wash_hand(N, nM):
    day = N * 21
    month = day * 30
    return str(month*nM//60) + ' minutes and '+ str(month*nM%60) + ' seconds'


print(wash_hand(8, 7))
print(wash_hand(0, 0))
print(wash_hand(7, 9))