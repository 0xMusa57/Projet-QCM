# Conteneur principal avec padding
    main_frame = ttk.Frame(root, padding="20 20 20 20", style="TFrame")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Titre de l'application
    title_label = ttk.Label(main_frame, text="Générateur de QCM", style="Title.TLabel")
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="w")
    
    # Séparateur
    separator = ttk.Separator(main_frame, orient="horizontal")
    separator.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 20))
    
    # Section Fichier
    fichier_label = ttk.Label(main_frame, text="1. Sélection du fichier QCM", style="Header.TLabel")
    fichier_label.grid(row=2, column=0, columnspan=3, sticky="w", pady=(0, 10))
    
    help_text = ttk.Label(
        main_frame, 
        text="Sélectionnez un fichier texte (.txt) contenant les questions au format spécifié."
    )
    help_text.grid(row=3, column=0, columnspan=3, sticky="w", pady=(0, 10))
    
    fichier_frame = ttk.Frame(main_frame, style="TFrame")
    fichier_frame.grid(row=4, column=0, columnspan=3, sticky="ew", pady=(0, 20))
    
    fichier_entry = ttk.Entry(fichier_frame, textvariable=fichier_var, width=50)
    fichier_entry.pack(side=tk.LEFT, padx=(0, 10), fill=tk.X, expand=True)

# Ajout des fonctions de sélection de fichier et de génération de QCM


# Variables globales pour stocker le fichier sélectionné et le statut
fichier_var = tk.StringVar()
status_var = tk.StringVar()

def lire_fichier_qcm(fichier):
    """Fonction pour lire un fichier QCM et retourner un message de statut."""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        
        if contenu.strip():  # Vérifie que le fichier n'est pas vide
            return True, "Fichier QCM chargé avec succès."
        else:
            return False, "Le fichier est vide."
    
    except Exception as e:
        return False, f"Erreur lors de la lecture : {str(e)}"

def selectionner_fichier():
    """Permet à l'utilisateur de sélectionner un fichier QCM."""
    fichier = filedialog.askopenfilename(
        title="Sélectionner un fichier QCM",
        filetypes=[("Fichiers texte", "*.txt")]
    )
    
    if fichier:
        fichier_var.set(fichier)  # Met à jour la variable de fichier sélectionné
        
        # Lire le fichier pour afficher les infos
        success, message = lire_fichier_qcm(fichier)
        status_var.set(message)

        if success:
            messagebox.showinfo("Information", message)
        else:
            messagebox.showerror("Erreur", message)

    
    fichier_button = ttk.Button(fichier_frame, text="Parcourir...", command=selectionner_fichier)
    fichier_button.pack(side=tk.LEFT)
    
    # Fonction pour générer les QCM