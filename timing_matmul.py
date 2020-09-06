import numpy as np 
from time import perf_counter
import matplotlib.pyplot as plt
from mimatmul import mimatmul

Ncorridas = 10
list1 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800, 1000,2000, 5000, 10000]

for i in range(Ncorridas):
    
    time_values =[]
    memory = []
    name = (f"matmul{i}.txt")
    file=open(name,'w')    
    
    for N in list1:
        A = np.array(np.random.rand(N,N))
        B = np.array(np.random.rand(N,N))
        t1 = perf_counter()
        C = mimatmul(A,B)
        t2 = perf_counter()
        dt = t2 - t1
        print(f"Tiempo transcurrido = {dt} s")
        memory_used = 3*(N*N)*8
        time_values.append(dt)
        memory.append(memory_used)
        file.write(f"{N} {dt} {memory_used}\n")
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
for i in range(Ncorridas):
    
    times_list = []
    name = (f"matmul{i}.txt")
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
plt.axhline(y=12000000000, xmin=0.001, xmax=0.9999,color="black",ls="--")
plt.xticks(x,xlab,rotation='45')
plt.yticks(y2,ylab2)
plt.grid() 
plt.ylabel("Uso Memoria (bytes)")
plt.xlabel("Tamaño de la matriz")
plt.show()