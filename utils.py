import numpy as np


# Custom DTW function with real penalty
def dtw_real_penalty(s1, s2):
    n, m = len(s1), len(s2)
    dtw_matrix = np.zeros((n + 1, m + 1))
    dtw_matrix[0, :] = np.inf
    dtw_matrix[:, 0] = np.inf
    dtw_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(s1[i - 1] - s2[j - 1])
            dtw_matrix[i, j] = cost + min(dtw_matrix[i - 1, j],  # insertion
                                          dtw_matrix[i, j - 1],  # deletion
                                          dtw_matrix[i - 1, j - 1])  # match

    return dtw_matrix


# Extract warping path
def extract_path(dtw_matrix, s1, s2):
    i, j = len(s1), len(s2)
    path = []
    while i > 0 and j > 0:
        path.append((i - 1, j - 1))
        if i == 1:
            j -= 1
        elif j == 1:
            i -= 1
        else:
            min_index = np.argmin([dtw_matrix[i - 1, j], dtw_matrix[i, j - 1], dtw_matrix[i - 1, j - 1]])
            if min_index == 0:
                i -= 1
            elif min_index == 1:
                j -= 1
            else:
                i -= 1
                j -= 1
    path.reverse()
    return path


def extract_erp_path(s1, s2):
    dtw_matrix = dtw_real_penalty(s1, s2)
    return extract_path(dtw_matrix, s1, s2)

def extacted_twed_path(s1, t1, s2, t2, nu, lamb):
    twed_matrix = twed(s1, t1, s2, t2, nu, lamb)
    return extract_path(twed_matrix, s1, s2)


# TWED function
def twed(s1, t1, s2, t2, nu, lamb):
    n, m = len(s1), len(s2)
    dp_matrix = np.full((n + 1, m + 1), np.inf)
    dp_matrix[0, 0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(s1[i - 1] - s2[j - 1])
            temporal_cost = abs(t1[i - 1] - t2[j - 1])

            dp_matrix[i, j] = min(
                dp_matrix[i - 1, j] + lamb + nu * (t1[i - 1] - t1[i - 2]),
                dp_matrix[i, j - 1] + lamb + nu * (t2[j - 1] - t2[j - 2]),
                dp_matrix[i - 1, j - 1] + cost + temporal_cost
            )

    return dp_matrix

