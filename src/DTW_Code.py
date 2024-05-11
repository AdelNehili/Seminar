from dtaidistance import dtw

#DTW MANUAL implementation
def dtw_distance(sequence_a, sequence_b, dist=lambda x, y: abs(x - y)):
    n, m = len(sequence_a), len(sequence_b)
    # Create the cost matrix
    dtw_matrix = [[float('inf') for _ in range(m)] for _ in range(n)]

    # Initialize the first cell of the matrix
    dtw_matrix[0][0] = dist(sequence_a[0], sequence_b[0])

    # Initialize the first row and column of the matrix
    for i in range(1, n):
        dtw_matrix[i][0] = dtw_matrix[i-1][0] + dist(sequence_a[i], sequence_b[0])
    for j in range(1, m):
        dtw_matrix[0][j] = dtw_matrix[0][j-1] + dist(sequence_a[0], sequence_b[j])

    # Populate the rest of the matrix
    for i in range(1, n):
        for j in range(1, m):
            cost = dist(sequence_a[i], sequence_b[j])
            dtw_matrix[i][j] = cost + min(dtw_matrix[i-1][j],
                                          dtw_matrix[i][j-1],
                                          dtw_matrix[i-1][j-1])

    return dtw_matrix[-1][-1]


#Properties testing
def manual_DTW_inequality_ex(A,B,C):

    print("Testing DTW manual implementation : Does it respect the 'Triangle Inequality'?")
    # Calculate DTW distances
    distance_AB = dtw_distance(A, B)
    distance_BC = dtw_distance(B, C)
    distance_AC = dtw_distance(A, C)

    # Print distances
    print("\tDTW Distance |AB|:", distance_AB)
    print("\tDTW Distance |BC|:", distance_BC)
    print("\tDTW Distance |AC|:", distance_AC)

    result = distance_AC<=distance_AB+distance_BC
    print(f"\tDoes |AC| <= |AB|+|BC| : {result}\n")
def lib_DTW_inequality_ex(A,B,C):

    print("Testing DTW library implementation : Does it respect the 'Triangle Inequality'?")
    # Calculate DTW distances
    distance_AB = dtw.distance(A, B)
    distance_BC = dtw.distance(B, C)
    distance_AC = dtw.distance(A, C)

    # Print distances
    print("\tDTW Distance |AB|:", distance_AB)
    print("\tDTW Distance |BC|:", distance_BC)
    print("\tDTW Distance |AC|:", distance_AC)

    result = distance_AC<=distance_AB+distance_BC
    print(f"\tDoes |AC| <= |AB+BC| : {result}\n")

