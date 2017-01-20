from scipy import stats
import numpy as np
x = [62,63,64,65,66,67,68,69,70,71,72,73]
y = [128,131,135,139,142,146,150,154,158,162,167,172]
new_x = [1,2,3,4,5,6,7,8,9,10,11,12]
#slope,intercept,r_value,p_value,stderr = stats.linregress(new_x,y)
slope,intercept = np.polyfit(new_x,y,1)
print(slope)
print(intercept)
#print(r_value)
