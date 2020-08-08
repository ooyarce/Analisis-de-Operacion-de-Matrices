- Marca/modelo: DELL PRECISION M2800

- Tipo: Notebook

- Año adquisición: 2017

- Procesador:
  - Marca/Modelo: Intel® Core™ i7-4810MQ 
  - Velocidad Base: 2.80 GHz
  - Velocidad Máxima: 3.80 GHz
  - Numero de núcleos: 4
  - Numero de hilos: 8
  - Arquitectura: x86_64
  - Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
  
- Tamaño de las cachés del procesador
  - L1: 256 KB 
  - L2: 1.0 MB
  - L3: 6.9 MB

- Memoria
  - Total: 12B
  - Tipo memoria: DDR3
  - Velocidad: 1600 MHz
  - Numero de (SO)DIMM: 2
 
- Tarjeta Gráfica
  - Marca / Modelo: AMD FirePro W4170M (FireGL V)
  - Memoria dedicada: 2000 MB
  - Resolución: 1920 x 1080

- Disco 1:
  - Marca: Samsung
  - Tipo: SSD
  - Tamaño: 239GB
  - Particiones: 1

- Sistema de archivos: NTFS

- Dirección IP (Interna, del router): 192.168.0.1

- Dirección IP (Externa, del ISP): 201.214.100.251

- Proveedor internet: VTR Banda Ancha S.A.

**- Desempeño MATMUL**
https://github.com/ooyarce/MCOC2020-P0/issues/1#issue-675418312
- ¿Como difiere del gráfico del profesor/ayudante?
  - La diferencia entre ambos gráficos está en que la curva de mi gráfica presenta variaciones mucho menos pronunciadas en relación a la     del profesor. La mayoria de los valores     iniciales (0-50) en mi caso hay un tiempo de demora mayor al del profesor. Por otro lado,     entre los valores 50 y 2000 mi computador presenta tiempos de ejecución menores a los   del profesor. Finalmente entre los 2000 y         10000 valores los resultados son idénticos.
  
- ¿A qué se pueden deber las diferencias?
  - Las diferencias se deben a los diferentes procesadores que hay entre ambos computadores, por ende los tiempos de ejecución varían         levemente. 
  
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  - Porque la cantidad de memoria usada es una función lineal "y = 2*(N*N)*8 con N fijo", mientras que la función del tiempo toma en         cuento el proceso de multiplicar matrices. Por   otro lado, son muchos los factores que inlfuyen en cuánto se demora el procesar una     operación matemática, como los programas que están abiertos entre otros.
  
- ¿Qué versión de python está usando? 
  - Estoy usando la versión 3.8
 
- ¿Qué versión de numpy está usando?
  - Estoy usando la versión 1.18.5
  
- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida     para confirmar. 
  - Se utilizan los 4 núcleos y en total son 8 los hilos usado. 






































