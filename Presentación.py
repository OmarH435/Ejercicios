import tkinter as tk

def show_presentation():
    # Crear una ventana flotante
    root = tk.Tk()
    root.title("Presentación Personal")  #titulo de la ventana

    # todo lo que vaya escrito dentro de "Message", va a ser el mensaje de la ventanita flotante
    message = "¡Hola! mi nombre es: Omar Aristides Donald David Casiá Herrera\n" \
        "\n" \
              "Actualmente estudio la  licenciatura en administración de sistemas informáticos y una maestría en consultoría tributaria.\n" \
              "Soy perito contador, con cierre de pensum en contaduría pública y auditoria;\n" \
                  "laboro como auxiliar de análisis financiero, en relación de dependencia y Freelancer como consultor empresarial y análista de datos\n" \
               "Tengo 23 años de edad\n" \
               "Mis pasatiempos son aprender, leer, Ejecutar la guitarra, jugar videojuegos y ver series. \n" \
                 "Algo que me gusta mucho, es poder enseñarle a las demas personas, lo que he aprendido y de esta manera, poder aportar un granito de arena a la sociedad"  
    
    # Crear la etiqueta para mostrar el mensaje
    label = tk.Label(root, text=message, font=("Helvetica", 12), justify="left") # en este punto, se declara como queremos que aparezca el mensaje dentro de la ventana
    label.pack(pady=20, padx=20)  # Empaquetar la etiqueta en la ventana, no comprendo muy bien, pero en el video lo utilizaban

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()

# Llamar a la función para mostrar la presentación
show_presentation()
