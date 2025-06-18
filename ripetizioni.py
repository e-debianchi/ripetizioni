import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import json
import os

# create executable with pyinstaller ripetizioni.py --onefile --windowed

FILE = r'C:\Users\edebi\Documents\programs\lavoro\ripetizioni.json'

# Creiamo una finestra con customtkinter
class TableApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ripetizioni")

        # Creiamo una cornice per la tabella
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=10)

        # Intestazioni di colonna
        self.headers = ["", "Paga", "Settembre", "Ottobre", "Novembre", "Dicembre", 
                        "Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno"]

        # Creiamo l'intestazione della tabella
        for c, header in enumerate(self.headers):
            header_label = ctk.CTkLabel(self.frame, text=header, width=50, height=30, font=("Arial", 12, "bold"))
            header_label.grid(row=0, column=c+1, padx=2, pady=5)

        # Nomi per la prima colonna
        self.names = ["Alice", "Viola", "Mariangela", "Pietro", "Nicolò", "Paulo", "Carolina", "Totale"]

        # Numero di righe e colonne
        self.rows = len(self.names)  # Ultima riga è per il totale
        self.cols = len(self.headers) - 1

        # Memorizzare i valori delle celle della tabella
        self.table_values = [[0 for _ in range(self.cols)] for _ in range(self.rows-1)]  # Solo 4 righe da modificare
        self.cell_labels = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # Ottieni il mese corrente (gennaio = 1, dicembre = 12)
        self.current_month = datetime.now().month

        # Load saved data if available
        self.load_data()

        # Creiamo la tabella con 4 righe e 12 colonne
        for r in range(self.rows):
            # Prima colonna con i nomi
            name_label = ctk.CTkLabel(self.frame, text=self.names[r], width=70, height=30, font=("Arial", 12))
            name_label.grid(row=r+1, column=0, padx=5, pady=5)

            if r < self.rows-1:
                # Aggiungiamo due bottoni per le prime tre righe (quadrati)
                btn_frame = ctk.CTkFrame(self.frame)
                btn_frame.grid(row=r+1, column=1, padx=5, pady=5)

                btn1 = ctk.CTkButton(btn_frame, text="+1", width=30, height=30, 
                                     command=lambda r=r: self.button_action(r, 1))
                btn1.pack(side=tk.LEFT, padx=2)

                btn2 = ctk.CTkButton(btn_frame, text="+2", width=30, height=30, 
                                     command=lambda r=r: self.button_action(r, 2))
                btn2.pack(side=tk.LEFT, padx=2)

            # Colonna "Paga" con valori fissi per le prime tre righe
            if r < self.rows-1:                
                self.table_values[r][0] = [20, 15, 15, 15, 25, 25, 20][r]  # I valori per "Paga"
                paga_label = ctk.CTkLabel(self.frame, text=str(self.table_values[r][0]), width=50, height=30)
                paga_label.grid(row=r+1, column=2, padx=2, pady=5)
            elif r == self.rows-1:
                # Lascia la cella "Paga" per l'ultima riga (Totale) vuota
                paga_label = ctk.CTkLabel(self.frame, text="", width=50, height=30)
                paga_label.grid(row=r+1, column=2, padx=2, pady=5)

            # Creiamo le celle della tabella per le prime tre righe
            for c in range(1, self.cols):
                if r < self.rows-1:
                    self.cell_labels[r][c] = ctk.CTkLabel(self.frame, text=str(self.table_values[r][c]), 
                                                          width=50, height=30)
                    self.cell_labels[r][c].grid(row=r+1, column=c+2, padx=2, pady=5)
                elif r == self.rows-1:
                    # Le celle della riga "Totale" mostreranno la somma
                    self.cell_labels[r][c] = ctk.CTkLabel(self.frame, text="0", width=50, height=30)
                    self.cell_labels[r][c].grid(row=r+1, column=c+2, padx=2, pady=5)

        self.update_totals()

        # Handle window close event to save data
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def button_action(self, row, increment):
        # Individuare la colonna corrispondente al mese corrente (Paga = colonna 1, Settembre = colonna 2, ecc.)
        # month_column = self.current_month - 8
        month_column = self.current_month + 4

        # Aggiungi l'incremento (1 o 2) al valore corrente della cella
        self.table_values[row][month_column] += increment

        # Aggiorna il testo nella cella
        self.cell_labels[row][month_column].configure(text=str(self.table_values[row][month_column]))

        # Aggiorna la riga del totale
        self.update_totals()

        # Stampa l'azione
        print(f"Aggiunto {increment} alla riga {row+1}, mese {self.headers[month_column+1]}")

    def update_totals(self):
        # Calcola la somma delle colonne moltiplicata per il valore nella colonna "Paga"
        for c in range(1, self.cols):
            total = 0
            for r in range(self.rows-1):
                paga = self.table_values[r][0]  # Il valore nella colonna "Paga" della riga
                total += self.table_values[r][c] * paga
            # Aggiorna il testo nella cella della riga "Totale"
            self.cell_labels[self.rows-1][c].configure(text=str(total))

    def save_data(self):
        # Save the table values to a file
        with open(FILE, "w") as file:
            json.dump(self.table_values, file)
        print("Dati salvati con successo!")

    def load_data(self):
        # Load the table values from the file if it exists
        if os.path.exists(FILE):
            with open(FILE, "r") as file:
                self.table_values = json.load(file)
            print("Dati caricati con successo!")
        else:
            print("Nessun dato salvato trovato.")

    def on_closing(self):
        # Save data and close the window
        self.save_data()
        self.destroy()

if __name__ == "__main__":
    app = TableApp()
    app.mainloop()
