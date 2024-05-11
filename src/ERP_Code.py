import numpy as np

def print_matrix(matrix, source, target):
    from tabulate import tabulate
    headers = [" "] + list(target)
    rows = [[source[i - 1] if i > 0 else " "] + row for i, row in enumerate(matrix)]
    print(tabulate(rows, headers, tablefmt="grid"))

#STRING COMPARAISON VERSION
def edit_distance_with_real_penalty_string(source, target, gap_value=0):
    n = len(source)
    m = len(target)
    
    # Create a distance matrix
    dist = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    # Initialize the first row and column of the matrix
    for i in range(1, n + 1):
        dist[i][0] = dist[i - 1][0] + abs(gap_value - ord(source[i-1]))
    for j in range(1, m + 1):
        dist[0][j] = dist[0][j - 1] + abs(gap_value - ord(target[j-1]))
    

    # Print initial matrix setup
    print_matrix(dist, source, target)
    
    # Populate the distance matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost_sub = abs(ord(source[i - 1]) - ord(target[j - 1]))
            cost_del = abs(ord(source[i - 1]) - gap_value)
            cost_ins = abs(ord(target[j - 1]) - gap_value)


            dist[i][j] = min(dist[i - 1][j] + cost_del,    # Deletion, We use the horizontal path
                             dist[i][j - 1] + cost_ins,    # Insertion, We use the vertical path
                             dist[i - 1][j - 1] + cost_sub) # Substitution, We use the diaganole path
    print_matrix(dist, source, target)
    
    return dist[n][m]
def minimum_edit_cost(source, target):
    n = len(source)
    m = len(target)
    
    # Create a distance matrix
    dist = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Initialize the first row and column of the matrix
    for i in range(1, n + 1):
        dist[i][0] = i  # Cost of deleting all characters from source up to i
    for j in range(1, m + 1):
        dist[0][j] = j  # Cost of inserting all characters from target up to j

    # Print initial matrix setup
    #print_matrix(dist, source, target)
    
    # Populate the distance matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                cost_sub = 0  # No cost if the characters are the same
            else:
                cost_sub = 1  # Cost of 1 for substituting different characters
            
            cost_del = 1  # Cost of 1 for deletion
            cost_ins = 1  # Cost of 1 for insertion

            dist[i][j] = min(dist[i - 1][j] + cost_del,    # Deletion
                             dist[i][j - 1] + cost_ins,    # Insertion
                             dist[i - 1][j - 1] + cost_sub) # Substitution

    # Print final populated matrix
    print_matrix(dist, source, target)
    
    return dist[n][m]

#TIME SERIES COMPARAISON Versions
def edit_distance_with_real_penalty_timeSeries(source, target, gap_value=0):
    n = len(source)
    m = len(target)
    
    # Create a distance matrix
    dist = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Initialize the first row and column of the matrix
    for i in range(1, n + 1):
        dist[i][0] = dist[i - 1][0] + abs(gap_value - source[i - 1])
    for j in range(1, m + 1):
        dist[0][j] = dist[0][j - 1] + abs(gap_value - target[j - 1])
    


    # Populate the distance matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost_sub = abs(source[i - 1] - target[j - 1])
            cost_del = abs(source[i - 1] - gap_value)
            cost_ins = abs(target[j - 1] - gap_value)


            dist[i][j] = min(dist[i - 1][j] + cost_del,    # Deletion, We use the horizontal path
                             dist[i][j - 1] + cost_ins,    # Insertion, We use the vertical path
                             dist[i - 1][j - 1] + cost_sub) # Substitution, We use the diaganole path
    return dist[n][m]

#________________________________Testing part

#STRING
def test_erp_string_comparaison():
    # Example usage
    source = "azced"
    target = "abcdef"
    gap_value = 100  # Assuming gap_value is zero for simplicity in this example



    print("Minimum edit cost:",minimum_edit_cost(source, target))
    #print("________________________________________________________________________________________________________________\n\n")
    print("Minimum edit distance:",edit_distance_with_real_penalty_string(source, target, gap_value))

#TIME SERIES
def test_erp_series():
    A =[1,2,3]
    B=[1,2,3]

    gap_value = 0
    erp_V1 = edit_distance_with_real_penalty_timeSeries(A,B,gap_value)

    print(f"edit_distance_with_real_penalty_timeSeries : {erp_V1}")
