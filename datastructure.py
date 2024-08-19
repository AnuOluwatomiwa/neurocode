import scipy.io

# Load the .mat files
data_s1 = scipy.io.loadmat('dataset/S1.mat')
data_s2 = scipy.io.loadmat('dataset/S2.mat')

# Print keys to understand the structure
print("Keys in S1.mat:", data_s1.keys())
print("Keys in S2.mat:", data_s2.keys())