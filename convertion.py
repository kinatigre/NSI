import tkinter as tk

def dtb(decimal): # convertisseur du décimal au binaire
    binaire = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        reste = decimal % 2
        binaire = str(reste) + binaire
        decimal = decimal // 2 # Division de décimal par 2 pour passer au chiffre binaire inverse donc si decimal = 0 il sera égal à 1
    return binaire

def btd(binaire): # convertisseur du binaire au décimal
    decimal = 0
    binaire = binaire[::-1] # retourne la chaine de character
    for i in range(len(binaire)):
        if binaire[i] == '1':
            decimal += 2**i
    return decimal

def dth(decimal): # convertisseur du décimal au hexadecimal
    hex_carac = "0123456789ABCDEF"
    hex_value = ""
    if decimal == 0:
        return "0"
    while decimal > 0:
        reste = decimal%16
        hex_value = hex_carac[reste] + hex_value
        decimal = decimal//16 # Division de décimal par 16 pour passer au chiffre hexadécimal suivant
    return hex_value

def htd(hex_value): # convertisseur du hexadecimal au décimal
    hex_carac = "0123456789ABCDEF"
    decimal = 0
    hex_value = hex_value[::-1] # retourne la chaine de caractere
    for i in range(len(hex_value)):
        caractere = hex_value[i]
        x = 0
        for j in range(len(hex_carac)):
            if hex_carac[j] == caractere:
                x = j
        decimal = decimal + x * (16 ** i)
    return decimal

def bth(binaire): # convertisseur du binaire au hexadecimal
    decimal_value = btd(binaire)
    return dth(decimal_value)

def htb(hex_value): # convertisseur du hexadecimal au binaire
    decimal_value = htd(hex_value)
    return dtb(decimal_value)


def convert(): # Fonction appelée lorsqu'un bouton est cliqué
    input_text = entry.get()
    conversion_type = conversion_var.get()
    
    if conversion_type == "Decimal au Binaire":
        result = dtb(int(input_text))
    elif conversion_type == "Binaire au Decimal":
        result = btd(input_text)
    elif conversion_type == "Decimal au Hexadecimal":
        result = dth(int(input_text))
    elif conversion_type == "Hexdecimal au Decimal":
        result = htd(input_text)
    elif conversion_type == "Binaire au Hexadecimal":
        result = bth(input_text)
    elif conversion_type == "Hexadecimal au Binaire":
        result = htb(input_text)
    
    result_label.config(text=f"Resultat: {result}")

# Création de la fenêtre Tkinter
window = tk.Tk()
window.geometry("500x400")
window.title("Convertisseur")

entry = tk.Entry(window)
entry.pack()

conversion_var = tk.StringVar()
conversion_var.set("Decimal au Binaire")

# Menu déroulant
conversion_menu = tk.OptionMenu(window, conversion_var, "Decimal au Binaire", "Binaire au Decimal", "Decimal au Hexadecimal", "Hexadecimal au Decimal", "Binaire au Hexadecimal", "Hexadecimal au Binaire")
conversion_menu.pack()

# Bouton de conversion
convert_button = tk.Button(window, text="Convertion", command=convert)
convert_button.pack()

# Affiche le résultat
result_label = tk.Label(window, text="Resultat:")
result_label.pack()

window.mainloop()