import time
t = time.time()
t = int(t+(5.5*60*60))
s = t%60
t = t//60
m = t%60
t = t//60
h = t%60
print(f"The time is {h}:{m}:{s} in IST")
