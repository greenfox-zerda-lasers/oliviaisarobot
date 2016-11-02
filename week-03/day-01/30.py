ac = 8

time = 120

out = ''

if ac%4 is 0 and time < 200:
    out = "Check"
    print(out)
elif time > 200:
    out = "Time out"
    print(out)
else:
    out = "Run Forest Run!"
    print(out)
