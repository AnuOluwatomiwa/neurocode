import scipy.io

# Load the .mat files
data_s1 = scipy.io.loadmat('dataset/S1.mat')
data_s2 = scipy.io.loadmat('dataset/S2.mat')

# Print keys to understand the structure
print("Keys in S1.mat:", data_s1.keys())
print("Keys in S2.mat:", data_s2.keys())

#Inspect the 'Info' key
info_s1 = data_s1['Info']
info_s2 = data_s2['Info']

print("Info for S1.mat:\n", info_s1)
print("\nInfo for S2.mat:\n",info_s2)