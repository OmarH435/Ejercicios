import tkinter as tk

# voy a crear mi ventama donde "Ventanaroot" es una variable
ventanaroot =tk.Tk()

ventanaroot.title("Mi ventana de ejemplo") #titulo de la ventana
ventanaroot.geometry("500x500")   # instrucción para indicar el tamaño debe especificarse conuna "x" minuscula


label=tk.Label(ventanaroot, text="Hola, Bienvenidos a mi primera Ventana con una etiqueta",font=("Arial", 11) )
label.pack(pady=10)

# Sí, desamos un apantalla emergente secundaria, utilizamos esta función
# def on_button_click ():
    #  ventanaroot1 =tk.Tk()
    # ventanaroot1.title("Mi ventana de ejemplo2") #titulo de la ventana
    #ventanaroot1.geometry("500x500")   # instrucción para indicar el tamaño debe especificarse conuna "x" minuscula
    #label=tk.Label(ventanaroot1, text="Hola, Bienvenidos a mi primera Ventana con una etiqueta2",font=("Arial", 11) )
    # label.pack(pady=10)

def on_button_click ():
    label.config(text="Gracias por dar click en mi botón")
    
    
button=tk.Button(ventanaroot, text="Puedes dar click acá?", command=on_button_click )
button.pack(pady=10)






ventanaroot.mainloop() # bucle para mantener la ventana