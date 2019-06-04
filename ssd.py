from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np

def cargarImagen():
    filename2 = askopenfilename()

    image = cv2.imread(filename2) #Leemos la ruta y convertimos a imagen

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Convertimos imagene a escala de grises

    rows_y,cols_x = gray_image.shape #Obtenemos la cantidad de columnas y filas
    
    gray = np.zeros(gray_image.shape, gray_image.dtype) #Hacemos una matriz temporal del mismo tamaño de la imagen a escala de grises

    print(gray_image)
    print("Nueva matriz")
    print(gray)

    cv2.imshow("Imagen 1", gray_image) #Mostramos imagen a escala de grises
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ventana = Tk()

#Variables
xPosicion1 = StringVar()
yPosicion1 = StringVar()
xPosicion2 = StringVar()
yPosicion2 = StringVar()


ventana.geometry("500x260+0+0")
ventana.title('SSD')
#Posicion 1
etiquetaPosicion1 = Label(ventana, text="POSICION 1").place(x= 50, y=50)
etiquetaXPosicion1 = Label(ventana, text="X").place(x=50, y=75)
entryXPosicion1 = Entry(ventana, textvariable=xPosicion1).place(x=100, y=75)
etiquetaYPosicion2 = Label(ventana, text="Y").place(x=50, y=100)
entryYPosicion1 = Entry(ventana, textvariable=yPosicion1).place(x=100, y=100)

#Posicion 2
etiquetaPosicion2 = Label(ventana, text="POSICION 2").place(x= 250, y=50)
etiquetaXPosicion2 = Label(ventana, text="X").place(x=250, y=75)
entryXPosicion2 = Entry(ventana, textvariable=xPosicion2).place(x=300, y= 75)
etiquetaYPosicion2 = Label(ventana, text="Y").place(x=250, y=100)
entryYPosicion2 = Entry(ventana, textvariable=yPosicion2).place(x=300, y= 100)

#Botones de carga de imagenes
btn1 = Button(ventana, width=20, text="Imagen escala de grises", command=cargarImagen).place(x=180, y=150)
print("hola mundo")
ventana.mainloop()