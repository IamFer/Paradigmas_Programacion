from multiprocessing import Process, Value, Lock
import time

def sumale_100(numero, candado):
    for i in range(100):
        time.sleep(0.01)
        
        with candado:
            numero.value += 1

if __name__ == "__main__":
    candado = Lock()
    numero_compartido = Value('i', 0)

    print("Al principio vale = ", numero_compartido.value)

    p1 = Process(target = sumale_100, args = (numero_compartido, candado))
    p2 = Process(target = sumale_100, args = (numero_compartido, candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numero_compartido.value)
