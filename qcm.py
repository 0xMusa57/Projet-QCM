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