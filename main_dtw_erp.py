from src import ERP_Code as erp_C
from src import DTW_Code as dtw_c
import pandas as pd

#__________________Properties__________________#
def show_non_metric_DTW():
    """
        This function aims to show a case of Non triangularity-inequality.
        This shows proove that DTW isn't a metric.
    """
    A =[0,1,1,2]
    B=[0,1,2]
    C=[0,2,2]


    dtw_c.lib_DTW_inequality_ex(A,B,C)
    dtw_c.manual_DTW_inequality_ex(A,B,C)

#__________________ERP/DTW Calls__________________#
def DTW_lib_algo(data_path_A,data_path_B,sep=";",aimed_column_A = "value1",aimed_column_B = "value1"):
    serie_A = pd.read_csv(data_path_A,sep=sep)
    serie_A = serie_A[aimed_column_A]

    serie_B = pd.read_csv(data_path_B,sep=sep)
    serie_B = serie_B[aimed_column_B]


    distance = dtw_c.dtw.distance(serie_A, serie_B)
    return distance
def DTW_manual_algo(data_path_A,data_path_B,sep=";",aimed_column_A = "value1",aimed_column_B = "value1"):
    serie_A = pd.read_csv(data_path_A,sep=sep)
    serie_A = serie_A[aimed_column_A]

    serie_B = pd.read_csv(data_path_B,sep=sep)
    serie_B = serie_B[aimed_column_B]

    distance = dtw_c.dtw_distance(serie_A, serie_B)
    return distance
def ERP_manual_algo(gap_value,data_path_A,data_path_B,sep=";",aimed_column_A = "value1",aimed_column_B = "value1"):
    serie_A = pd.read_csv(data_path_A,sep=sep)
    serie_A = serie_A[aimed_column_A]

    serie_B = pd.read_csv(data_path_B,sep=sep)
    serie_B = serie_B[aimed_column_B]

    distance = erp_C.edit_distance_with_real_penalty_timeSeries(serie_A, serie_B, gap_value)
    return distance


#__________________Main__________________#
aimed_column_A = "value1"
aimed_column_B = "value1"

serie_A = "data/serie_A.csv"
serie_B = "data/serie_B.csv"

distance = ERP_manual_algo(0,serie_A,serie_B,sep=";",aimed_column_A=aimed_column_A,aimed_column_B=aimed_column_B)
print(f"distance : {distance}")