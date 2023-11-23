import tkinter as tk

def eb(nombre): # verification si le nombre est binaire ou pas pour les fonctions qui ont besoin d'avoir une entré en binaire
    for carac in nombre:
        if carac not in '01':
            return False
    return True

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
    if not eb(binaire):
        return "Veuillez entrer une valeur binaire valide"
    decimal = 0
    binaire = binaire[::-1] # retourne la chaine de caractère
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
        caractere = hex_value[i].upper()
        x = 0
        for j in range(len(hex_carac)):
            if hex_carac[j] == caractere:
                x = j
        decimal = decimal + x * (16 ** i)
    return decimal

def bth(binaire): # convertisseur du binaire au hexadecimal
    if not eb(binaire):
        return "Veuillez entrer une valeur binaire valide"
    decimal_value = btd(binaire)
    return dth(decimal_value)

def htb(hex_value): # convertisseur du hexadecimal au binaire
    decimal_value = htd(hex_value)
    return dtb(decimal_value)

def dtb_complement_deux(decimal, bits=8):
    if decimal < 0:
        binaire = bin(2**bits + decimal)[2:]
    else:
        binaire = bin(decimal)[2:]
    
    if len(binaire) > bits: # Supprimer les bits excédentaires à gauche
        binaire = binaire[-bits:]
    else: # Ajouter des zéros à gauche si la longueur est inférieure au nombre de bits spécifié (donc 8)
        binaire = '0' * (bits - len(binaire)) + binaire
    
    return binaire

def convert(): # Fonction appelée lorsqu'un bouton est cliqué
    input_text = entry.get()
    conversion_type = conversion_var.get()
    
    result = ""  # Valeur par défaut de result

    if not input_text: # Texte pour quand l'utilisateur n'entre pas de valeur
        result_label.config(text="Veuillez entrer une valeur")
        return

    if conversion_type != "Complément à deux en 8 Bits" and input_text[0] == '-':  # Ajout de la vérification pour les nombres négatifs
        result_label.config(text="Veuillez entrer une valeur positive")
        return

    if conversion_type == "Decimal au Binaire":
        result = dtb(int(input_text))
    elif conversion_type == "Binaire au Decimal":
        result = btd(input_text)
    elif conversion_type == "Decimal au Hexadecimal":
        result = dth(int(input_text))
    elif conversion_type == "Hexadecimal au Decimal":
        result = htd(input_text)
    elif conversion_type == "Binaire au Hexadecimal":
        result = bth(input_text)
    elif conversion_type == "Hexadecimal au Binaire":
        result = htb(input_text)
    elif conversion_type == "Complément à deux en 8 Bits":
        result = dtb_complement_deux(int(input_text))
    
    result_label.config(text=f"Resultat: {result}") # formatage de la valeur

# Création de la fenêtre Tkinter
window = tk.Tk()
window.geometry("300x200")
window.title("Convertisseur")

# Empêcher la redimension de la fenêtre
window.resizable(False, False)

entry = tk.Entry(window)
entry.pack()

conversion_var = tk.StringVar()
conversion_var.set("Decimal au Binaire")

# Menu déroulant
conversion_menu = tk.OptionMenu(window, conversion_var, "Decimal au Binaire", "Binaire au Decimal", "Decimal au Hexadecimal", "Hexadecimal au Decimal", "Binaire au Hexadecimal", "Hexadecimal au Binaire", "Complément à deux en 8 Bits")

conversion_menu.pack()

# Bouton de conversion
convert_button = tk.Button(window, text="Convertion", command=convert)
convert_button.pack()

# Affiche le résultat
result_label = tk.Label(window, text="Resultat:")
result_label.pack()

window.mainloop()
