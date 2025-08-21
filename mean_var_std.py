import numpy as np

def calculate(list):

    #Verificar se tem 9 numeros dentro da lista
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')

    #Transformar a lista em uma matriz
    e = np.array(list).reshape(3 ,3)

    mean_cols = e.mean(axis=0).tolist()
    mena_cows = e.mean(axis=1).tolist()
    mean_all =float(e.mean())

    var_cols = e.var(axis=0).tolist()
    var_cows = e.var(axis=1).tolist()
    var_all =float(e.var())

    std_cols = e.std(axis = 0).tolist()
    std_cows = e.std(axis=1).tolist()
    std_all = float(e.std())

    max_cols = e.max(axis=0).tolist()
    max_cows = e.max(axis=1).tolist()
    max_all = float(e.max())

    min_cols = e.min(axis=0).tolist()
    min_cows = e.min(axis=1).tolist()
    min_all = float(e.min())

    sum_cols = e.sum(axis=0).tolist()
    sum_cows = e.sum(axis=1).tolist()
    sum_all = float(e.sum())

    calculations = {
        'mean': [mean_cols, mena_cows, mean_all],
        'variance': [var_cols, var_cows, var_all],
        'standard deviation': [std_cols, std_cows, std_all],
        'max': [max_cols, max_cows, max_all],
        'min': [min_cols, min_cows, min_all],
        'sum': [sum_cols, sum_cows, sum_all],
    }

    return calculations

