import pandas as pd
import math
#obtaining the values of sin, cos, tan through "for" loop
sin = []
for s_value in range(0,10):
    sin.append(math.sin(s_value))
    s_value = s_value + 0.2
cos = []
for c_value in range(0,10):
    cos.append(math.cos(c_value))
    c_value = c_value + 0.2
tan = []
for t_value in range(0,10):
    tan.append(math.tan(t_value))
    t_value = t_value + 0.2

# Define a dictionary 
data = {'sin(x)': sin,
        'cos(x)': cos,
        'tan(x)': tan}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Observe the result
df
