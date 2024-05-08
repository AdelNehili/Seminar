from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np

# Character mapping
char_map = {char: idx for idx, char in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")}

# Function to convert a string into a sequence of integers
def encode_string(s, char_map):
    return np.array([char_map[char] for char in s])

# Encode the two strings
s1 = encode_string("Hello World", char_map)
s2 = encode_string("Hello Dear", char_map)

# Compute DTW warping path
path = dtw.warping_path(s1, s2)

# Visualize the DTW alignment
dtwvis.plot_warping(s1, s2, path, filename="warp_hello.png")
