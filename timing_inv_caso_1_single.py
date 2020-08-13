import numpy as np 
from numpy import zeros,float32,half,single,double,longdouble
from time import perf_counter
import matplotlib.pyplot as plt
from scipy import linalg

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
    
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800, 1000,2000, 5000, 10000]
numpy_values =[]
scipy_values = []
name = ("matmul1.txt")
file=open(name,'w')    
memory = []
for N in list1:
    A = matriz_laplaciana(N,single)
    t1 = perf_counter()
    B = np.linalg.inv(A)
    t2 = perf_counter()
    dt = t2 - t1
    print(f"Para N = {N}, el tiempo transcurrido numpy = {dt} s\n")
    size = 1*(N*N)*8
    memory.append(size)
    file.write(f"{N} {dt}\n")
file.close()
   
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] #esta linea define visualmente el 
#escalado en el eje y en mili segundos, segundos y minutos
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]

plt.figure()
#creo el gráfico 1

plt.subplot(2,1,1)
  
times_list = []
name = ("matmul1.txt")
file = open(name,'r')
results_matrix = [[(num) for num in line.split(' ')] for line in file]
for i in range(len(list1)):
    times_yi_values = results_matrix[i][1]
    times_list.append(float(times_yi_values))

file.close()
plt.loglog(list1,times_list,"-o")
    
plt.xticks(x,[],rotation='45')
plt.yticks(y,ylab)
plt.grid() 
plt.ylabel("Tiempo Transcurrido (s) ")
plt.title("Rendimiento A@B")

#creo el grafico 2
plt.subplot(2,1,2)
plt.loglog(list1,memory,"-o")  
plt.xticks(x,xlab,rotation='45')
plt.yticks(y2,ylab2)
plt.grid() 
plt.ylabel("Uso Memoria (bytes)")
plt.xlabel("Tamaño de la matriz")
plt.show()