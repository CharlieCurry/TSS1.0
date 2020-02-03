import numpy as np
src = 'dsyr2k'
features = [1,0,0,0,1,3,0,2,1,0,0,2,1,2,0,1,0,0,4,1,0,0,1]
features = np.tile(features,(32000,1))
print(features)
print(features.shape)
np.savetxt('features/'+src+'_train&valiation_features.txt',features,fmt="%1.1f")
data = np.loadtxt('features/'+src+'_train&valiation_features.txt')
print(data)
print(data.shape)
e=np.append(features,data,axis=1)
print(e.shape)

