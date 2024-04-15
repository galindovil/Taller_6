import numpy as np
#matplotlib tiene muchos modulos. Importar uno solo 
import matplotlib.pyplot as plt

#crear un ndarray de 1 dimension, 100 elementos equiespaciados, de 0 a 2*PI

x=np.linspace(0,2*np.pi)
y=np.sin(x)


#usar matplotlib

plt.figure(figsize=(8,4))
plt.title("Mi primer Grafico cientifico en programacion")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
