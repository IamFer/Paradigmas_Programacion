import multiprocessing as mp
import numpy as np
import time

def my_function(i, param1, param2, param3):
    result = param1 ** 2 + param2 + param3 # - Calcula un Polinomio
    time.sleep(2) # Se hace tonta 2 segundos :v

    return (i, result)

def get_result(result):
    global results
    results.append(result)

# ------------------------------ #
# ----- Programa Principal ----- #
# ------------------------------ #
if __name__ == "__main__":
    params =  np.random.random((10, 3)) * 100.0
    results = []
    ts = time.time()

    pool = mp.Pool(mp.cpu_count())

    for i in range(0, params.shape[0]):
        pool.apply_async(my_function, args = (i, params[i, 0], params[i, 1], params[i, 2]), callback = get_result)

    pool.close()
    pool.join()

    print("Tiempo en Paralelo = ", time.time() - ts)
    print(results)
