import scipy.io
mat=scipy.io.loadmat('GDN0001_1_Resting.mat')

#your_data = mat['GDN0001_1_Resting']

import pandas as pd
df = pd.DataFrame(mat)
df.to_csv('your_data.csv') #your_data.csv final data in csv file
