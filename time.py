import numpy as np
import time
import pandas as pd

a = [time.ctime()]

a.append(time.ctime())
df = pd.DataFrame(a)
df.to_csv('FechaHora.csv')

print(a)
