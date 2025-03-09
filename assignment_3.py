# Question 1


def euler(func, a, y0, b, N):
    h = (b-a)/N
    t = a
    y = y0

    for i in range(N):
        y = y + h *func(t,y)
        t += h

    return y 
    

def func(t, y):
    return t-y**2

a = 0
b = 2
N = 10
y0 = 1

results = euler(func, a, y0, b, N)
print(results)


# Question 2
def func(t, y):
    return t-y**2

def runge(func, a, y0, b , N):
    h = (b-a)/N
    t = a
    y = y0

    for i in range(N):
        k1 = h*func(t, y)
        k2 = h*func(t + (h / 2), y + (.5 * k1))
        k3 = h*func(t + (h / 2), y + (.5 * k2))
        k4 = h*func(t + h, y + k3)
        
        y = y + ((k1 + (2 * k2) + (2 * k3) + k4) / 6)
        
        t += h
    return y 

a = 0
y0 = 1
b = 2
N = 10
answer = runge(func, a, y0, b, N)
print(answer)

