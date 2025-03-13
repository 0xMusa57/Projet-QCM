import random
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class GenerateurQCM:
    """Classe pour générer des QCM personnalisés à partir d'un fichier de questions."""
    
    def __init__(self):
        """Initialise le générateur de QCM."""
        self.questions = []
        self.fichier_entree = ""
        self.nombre_eleves = 0
        self.nombre_questions = 0
        self.graine = 0

if __name__ == "__main__":
    generateur = GenerateurQCM()


