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