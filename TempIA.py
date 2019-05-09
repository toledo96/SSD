from tkinter import *
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt
import numpy as np
import cv2


def histograma_imagen_e_imagen(imagen):
    cv2.imshow("venta",imagen)
    plt.hist(imagen.ravel(),256,[0,256]); plt.show()

# A L G O R I T M O   S S D
def ssd_escala_grises(imagen_original, imagen_temporal, dimension):
    matriz_ssd = np.zeros((posicion_y.get() - inicio_x.get(), fin_x.get() - inicio_x.get()))
    recorte_matriz_original = np.zeros((posicion_y.get() - inicio_x.get(), fin_x.get() - inicio_x.get())) #recorte de la imagen original que sera utilizada para comparar 
    recorte_matriz_temporal = np.zeros((posicion_y.get() - inicio_x.get(), fin_x.get() - inicio_x.get())) #recorte de la imagen temporal que sera utilizada para comparar
    histograma_imagen_e_imagen(imagen_original)
    # selecciona el punto medio de la imagen que sera utilizada para comparar
    seccion_centro = np.zeros((dimension,dimension))
    #SE CREA LA MATRIZ QUE SERA UTILIZADA PARA EXAMINAR LA MATRIZ
    for y in range(inicio_x.get(),posicion_y.get()):
        for x in range(inicio_x.get(), fin_x.get()):
            recorte_matriz_original[y - inicio_x.get()][x - inicio_x.get()] = imagen_original[y][x]
            recorte_matriz_temporal[y - inicio_x.get()][x - inicio_x.get()] = imagen_temporal[y][x]
    
    for y in range(int(posicion_y.get() / 2), int((posicion_y.get() / 2) + dimension)):
        for x in range(int(fin_x.get() / 2), int((fin_x.get() / 2) + dimension)):
            seccion_centro[y - int(posicion_y.get() / 2)][x - int(fin_x.get() / 2)] = imagen_original[y][x]


    #recorrido_matriz(matriz_ssd, recorte_matriz_original,recorte_matriz_temporal, seccion_centro, dimension)

def recorrido_matriz(matriz_ssd, recorte_matriz_original,recorte_matriz_temporal, seccion_centro, dimension):
    posicion_y,posicion_x = recorte_matriz_original.shape
    punto_medio_x = int(dimension/2) + 1
    punto_medio_y = punto_medio_x
    sumatoria = 0
    x_dimension= 0
    y_dimension = 0
    #se resta la matriz con el punto centro de la muestra que se obtuvo
    for y in range(1, posicion_y):
        for x in range(1,posicion_x):
            y_dimension = 0   
            if((y+dimension)-1 < posicion_y and (x + dimension)-1 < posicion_x and x_dimension < dimension and y_dimension < dimension):
                for y2 in range(y,(y+dimension)):
                    for x2 in range(x,(x+dimension)):
                        resta = pow(recorte_matriz_temporal[y2][x2] - seccion_centro[y_dimension][x_dimension],2)
                        sumatoria += resta                      
                        x_dimension += 1
                    y_dimension += 1
                    x_dimension = 0
            matriz_ssd[int((y+dimension)/2) + 1][int((x + dimension)/2) + 1] = int(sumatoria)   
            sumatoria = 0

# L O G I C A D E  B O T O N E S 

def accion_boton_escala_grises():
    # I M A G E N  O R I G I N A L
    filename = askopenfilename() # obtenemos la ruta de la imagen
    image = cv2.imread(filename) # se hace lectura de la imagen
    escala_grises_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convierte una imagen a escala de grises

    # I M A G E N  T E M P O R A L
    filename2 = askopenfilename()  # obtenemos la ruta de la imagen
    image2 = cv2.imread(filename2)  # se hace lectura de la imagen
    escala_grises_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) #convierte una imagen a escala de grises

    rows_y, cols_x = escala_grises_image.shape # obtiene las filas y columnas de la matriz de la imagen original

    print("IMPRIMIENDO IMAGEN")
    ssd_escala_grises(escala_grises_image, escala_grises_image2, 3)


def accion_boton_rgb():
    # I M A G E N  O R I G I N A L
    filename = askopenfilename()  # obtenemos la ruta de la imagen
    image = cv2.imread(filename)  # se hace lectura de la imagen

    # I M A G E N  T E M P O R A L
    filename2 = askopenfilename()  # obtenemos la ruta de la imagen
    image2 = cv2.imread(filename2)  # se hace lectura de la imagen

# MAIN PRINCIPAL
ventana = Tk()

ventana.title("Inteligencia Artificial") #nombre de la ventana
ventana.geometry("500x300") #tamaño de la ventana

Label(ventana, text="Seleccione el tipo de imagen", font=(18)).place(x=145, y=30)

    # C R E A C I O N  D E  B O T O N E S
Button(ventana, text="Escala de grises", command=accion_boton_escala_grises).place(x=150, y=70)
Button(ventana, text="Imagen a color", command=accion_boton_rgb).place(x=250, y=70)

    #Creacion textbox con su respectivo label que sera utilizado para verifica el áre donde se realizaran la busqueda

inicio_x = IntVar()
fin_x = IntVar()
posicion_y = IntVar()
gama_valor = DoubleVar()

x_entry = Entry(ventana, textvariable=inicio_x).place(x=50 , y=125)
Label(ventana,text="Inicio X").place(x=90,y=100)

x_fin_entry = Entry(ventana, text=fin_x).place(x=190 , y=125)
Label(ventana,text="fin X").place(x=230,y=100)

y_entry = Entry(ventana, textvariable =posicion_y).place(x=330 , y=125)
Label(ventana,text="Inicio y").place(x=360,y=100)

gama_entry = Entry(ventana,textvariable = gama_valor).place(x=200, y=150)
Label(ventana,text="Valor gamma").place(x=120, y=150)

ventana.mainloop()