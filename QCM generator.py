import random
import os
from docx import Document
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.font import Font


class GenerateurQCM:
    """Classe pour générer des QCM personnalisés à partir d'un fichier de questions."""
    
    def __init__(self):
        """Initialise le générateur de QCM."""
        self.questions = []
        self.fichier_entree = ""
        self.nombre_eleves = 0
        self.nombre_questions = 0
        self.graine = 0
        
    def lire_fichier_qcm(self, nom_fichier):
        """
        Lit le fichier contenant les questions et réponses.
        
        Args:
            nom_fichier (str): Chemin vers le fichier de questions.
            
        Returns:
            tuple: (succès (bool), message (str))
        """
        self.fichier_entree = nom_fichier
        questions = []
        
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read().strip().split('\n\n')
                
                for bloc in contenu:
                    lignes = bloc.strip().split('\n')
                    if len(lignes) >= 6:  # Au moins une question, 4 réponses et 1 solution
                        question = lignes[0]
                        reponses = lignes[1:5]
                        solution = int(lignes[5])
                        
                        questions.append({
                            'question': question,
                            'reponses': reponses,
                            'solution': solution
                        })
                
            self.questions = questions
            return True, f"{len(questions)} questions lues avec succès"
        except Exception as e:
            return False, f"Erreur lors de la lecture du fichier: {str(e)}"


def generer_sujets(self, nombre_eleves, nombre_questions, graine):
        """
        Génère les sujets pour chaque élève.
        
        Args:
            nombre_eleves (int): Nombre de sujets à générer.
            nombre_questions (int): Nombre de questions par sujet.
            graine (int): Graine pour le générateur aléatoire.
            
        Returns:
            tuple: (succès (bool), sujets ou message d'erreur)
        """
        self.nombre_eleves = nombre_eleves
        self.nombre_questions = nombre_questions
        self.graine = graine
        
        random.seed(graine)  # Initialisation du générateur aléatoire
        
        if nombre_questions > len(self.questions):
            return False, (
                f"Pas assez de questions dans le fichier ({len(self.questions)}) "
                f"pour générer {nombre_questions} questions par sujet"
            )
        
        # Liste qui contiendra tous les sujets
        sujets = []
        
        # Pour chaque élève, on génère un sujet
        for num_sujet in range(nombre_eleves):
            # Sélection aléatoire des questions pour ce sujet
            questions_selectionnees = random.sample(self.questions, nombre_questions)
            
            # On prépare le sujet avec questions et réponses mélangées
            sujet = {
                'numero': num_sujet,
                'questions': []
            }
            
            for q in questions_selectionnees:
                # Copie des réponses pour les mélanger
                reponses = q['reponses'].copy()
                solution_originale = q['solution']
                
                # Mélange des réponses
                indices_melanges = list(range(4))
                random.shuffle(indices_melanges)
                
                reponses_melangees = [reponses[i] for i in indices_melanges]
                
                # Calculer la nouvelle position de la bonne réponse
                nouvelle_solution = indices_melanges.index(solution_originale - 1) + 1
                
                sujet['questions'].append({
                    'question': q['question'],
                    'reponses': reponses_melangees,
                    'solution': nouvelle_solution,
                    'question_originale_index': self.questions.index(q)
                })
            
            sujets.append(sujet)
        
        return True, sujets