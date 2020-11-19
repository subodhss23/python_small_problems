''' From point A, an object is moving towards point B at constant velocity va(in km/hr). From point
    B, anohter object is moving towards point A at contant velocity vb(in km/hr). Knowing this and
    the distance between point A and B(in km), write a function that returns how much time passes
    until both objects meets.'''

def lets_meet(distance, va, vb):
    t = distance / (va + vb)
    h = int(t)
    m = 60*(t-h)
    ans = str(h) + "h " + str(int(m)) + "min " + str(int(60 * (m - int(m)))) + "s"
    return ans
    
print(lets_meet(100, 10, 30))
print(lets_meet(280, 70, 80))
print(lets_meet(90, 75, 65))