import numpy as np
from dtaidistance import dtw # type: ignore
from ERP_Code import edit_distance_with_real_penalty_timeSeries



def DTW_inequality_test():
    # Calculate the DTW distances manually using the defined function
    distance_AB = dtw.distance(A, B)
    distance_BC = dtw.distance(B, C)
    distance_AC = dtw.distance(A, C)

    print(f"distance_AB : {distance_AB}")
    print(f"distance_BC : {distance_BC}")
    print(f"distance_AC : {distance_AC}")

    print(f"Does AC <= AB+BC : {distance_AC<=distance_AB+distance_BC}")
def ERP_inequality_test():
    # Calculate the DTW distances manually using the defined function
    distance_AB = edit_distance_with_real_penalty_timeSeries(A, B)
    distance_BC = edit_distance_with_real_penalty_timeSeries(B, C)
    distance_AC = edit_distance_with_real_penalty_timeSeries(A, C)

    print(f"distance_AB : {distance_AB}")
    print(f"distance_BC : {distance_BC}")
    print(f"distance_AC : {distance_AC}")

    print(f"Does AC <= AB+BC : {distance_AC<=distance_AB+distance_BC}")

A =[0,1,1,2]
B=[0,1,2]
C=[0,2,2]

DTW_inequality_test()
ERP_inequality_test()