''' Wrtei a function to returnthe city from each of these vacation spots. '''

def grab_city(txt):
    find_city = ""
    for i in reversed(txt):
        find_city+=i
        if i == '[':
            return (find_city[::-1].strip(']')).strip('[')

print(grab_city("[Last Day!] Beer Festival [Munich]"))
print(grab_city("Cheese Factory Tour [Portland]"))
print(grab_city("[50% Off!][Group Tours Included] 5-Day Trip to Onsen [Kyoto]"))