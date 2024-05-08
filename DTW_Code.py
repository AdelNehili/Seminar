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


def DTW_inequality_ex(A,B,C):


    # Calculate DTW distances
    distance_AB = dtw_distance(A, B)
    distance_BC = dtw_distance(B, C)
    distance_AC = dtw_distance(A, C)

    # Print distances
    print("DTW Distance A to B:", distance_AB)
    print("DTW Distance B to C:", distance_BC)
    print("DTW Distance A to C:", distance_AC)

# Example usage with integer sequences
sequence_a = [1, 2, 3, 4, 5]
sequence_b = [2, 3, 4, 5, 6]


A =[0,1,1,2]
B=[0,1,2]
C=[0,2,2]


# Calculate the DTW distances manually using the defined function
distance_AB = dtw.distance(A, B)
distance_BC = dtw.distance(B, C)
distance_AC = dtw.distance(A, C)

print(f"distance_AB : {distance_AB}")
print(f"distance_BC : {distance_BC}")
print(f"distance_AC : {distance_AC}")

print(f"Does AC <= AB+BC : {distance_AC<=distance_AB+distance_BC}")