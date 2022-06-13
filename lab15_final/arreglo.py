from multiprocessing import Process, Array, Lock
import time

def sumale_100(numeros, candado):
    for i in range(100):
        time.sleep(0.01)
        
        for i in range(len(numeros)):
            with candado:
                numeros[i] += 1

if __name__ == "__main__":
    candado = Lock()
    numeros_compartidos = Array('d', [0.0, 100.0, 200.0])

    print("Al principio vale = ", numeros_compartidos[:])

    p1 = Process(target = sumale_100, args = (numeros_compartidos, candado))
    p2 = Process(target = sumale_100, args = (numeros_compartidos, candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numeros_compartidos[:])
