import numpy as np 
from numpy import zeros,float32
from time import perf_counter
import matplotlib.pyplot as plt

def matriz_laplaciana(N,dtype = float32):
    A =zeros((N,N),dtype =dtype)
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i+1 ==j:
                A[i,j] = -1
            if i-1 == j:
                A[i,j] = -1
    return A
    
Ncorridas = 10
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800, 1000,2000, 5000, 10000]
names = ["A_invB_inv.txt", "A_invB_npSolve.txt"]
files = [open(name,"w") for name in names]

for N in list1:
    print (f"Para N = {N}")
    dts = np.zeros((Ncorridas, len(files)))
    
    for i in range(Ncorridas):
        print (f"Corrida numero {i}")    
        #metodo1    
        A = matriz_laplaciana(N) #matriz A
        b = np.ones(N) #vector b
        t1 = perf_counter()
        A_invertida = np.linalg.inv(A)
        X = A_invertida@b #aqui se resuelve el sitema X = A^-1 * b
        t2 = perf_counter()
        dt = t2-t1
        dts[i][0] = dt
        
        #metodo2
        A2 = matriz_laplaciana(N)
        b2 = np.ones(N)
        t3 = perf_counter()
        X2 = np.linalg.solve(A2,b2)
        t4 = perf_counter()
        dt2 = t4-t3
        dts[i][1] = dt2
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    print (f"dts_mean = {dts_mean}")
    
    #relleno con la info de la media de los tiempos los archivos de texto
    for i in range(len(files)):
        files[i].write(f"{N} {dts_mean[i]}\n")
        files[i].flush()
[file.close() for file in files]        

#ahora grafico
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] #esta linea define visualmente el 
#escalado en el eje y en mili segundos, segundos y minutos
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]


plt.figure()
#creo el gráfico 
plt.subplot(2,1,1)
#valores que tomara y en la lista times_list
for i in range(len(list1)):
    times_list = []
    times_list2 = []
    name = ("A_invB_inv.txt")
    name2 =("A_invB_npSolve.txt")
    file = open(name,'r')
    results_matrix = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values = results_matrix[i][1]
        times_list.append(float(times_yi_values))
    file.close()
    
    file = open(name2,'r')
    results_matrix2 = [[(num) for num in line.split(' ')] for line in file]
    for i in range(len(list1)):
        times_yi_values2 = results_matrix2[i][1]
        times_list2.append(float(times_yi_values2))
    file.close()
plt.loglog(list1,times_list,"-o")
plt.loglog(list1,times_list2,"-o")
#defino mi grafico

plt.xticks(x,xlab,rotation='45')
plt.yticks(y,ylab)
plt.grid() 
plt.xlabel("Tamaño de la matriz")
plt.ylabel("Tiempo Transcurrido (s)")
plt.legend(["A_invB_inv.txt","A_invB_npSolve.txt"],loc = 'upper left')
plt.title("Rendimiento A@B")

#creo el grafico 2

plt.show()