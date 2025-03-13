def generer_fichier_correction(self, sujets, nom_fichier="correction.txt"):
    """
    Génère le fichier de correction pour l'enseignant.
    
    Args:
        sujets (list): Liste des sujets générés.
        nom_fichier (str): Nom du fichier de correction à générer.
        
    Returns:
        tuple: (succès (bool), message (str))
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            for sujet in sujets:
                f.write(f"Sujet {sujet['numero']}\n")
                
                # Écriture des réponses en groupes de 5
                # Conversion 1->a, 2->b, etc.
                reponses = [chr(96 + q['solution']) for q in sujet['questions']]
                
                for i in range(0, len(reponses), 5):
                    f.write(''.join(reponses[i:i+5]) + ' ')
                
                f.write('\n\n')
            
            # Approfondissement: traçabilité des questions
            f.write("\n--- Traçabilité des questions ---\n\n")
            
            # Pour chaque sujet, quelles questions initiales ont été intégrées
            for sujet in sujets:
                indices_questions = [q['question_originale_index'] for q in sujet['questions']]
                f.write(f"Sujet {sujet['numero']} : questions {','.join(map(str, indices_questions))}\n")
            
            # Pour chaque question initiale, dans quels sujets elle apparaît
            for i, _ in enumerate(self.questions):
                sujets_avec_question = [
                    s['numero'] for s in sujets 
                    if any(q['question_originale_index'] == i for q in s['questions'])
                ]
                f.write(f"Question {i} : sujets {','.join(map(str, sujets_avec_question))}\n")
            
        return True, f"Fichier de correction généré avec succès: {nom_fichier}"
    except Exception as e:
        return False, f"Erreur lors de la génération du fichier de correction: {str(e)}"