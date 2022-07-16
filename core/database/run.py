from mongo import database

insertDisciplines = [
    { "name": "Matemática", "tag": "matematica" },
    { "name": "Física", "tag": "fisica" },
    { "name": "Química", "tag": "quimica" },
    { "name": "Biologia", "tag": "biologia" },
]

insertBranches = [

    # Matemática

    { "name": "Razão e proporção", "tag": "razao_e_proporcao", "discipline_tag": "matematica" },
    { "name": "Porcentagem", "tag": "porcentagem", "discipline_tag": "matematica" },
    { "name": "Estatística", "tag": "estatistica", "discipline_tag": "matematica" },
    { "name": "Geometria analítica", "tag": "geometria_analitica", "discipline_tag": "matematica" },
    { "name": "Geometria plana", "tag": "geometria_plana", "discipline_tag": "matematica" },
    { "name": "Geometria espacial", "tag": "geometria_espacial", "discipline_tag": "matematica" },
    { "name": "Trigonometria", "tag": "trigonometria", "discipline_tag": "matematica" },
    { "name": "Conjuntos", "tag": "conjuntos", "discipline_tag": "matematica" },
    { "name": "Função afim", "tag": "funcao_afim", "discipline_tag": "matematica" },
    { "name": "Função quadrática", "tag": "funcao_quadratia", "discipline_tag": "matematica" },
    { "name": "Função exponencial", "tag": "funcao_exponencial", "discipline_tag": "matematica" },
    { "name": "Função logarítmica", "tag": "funcao_logaritmica", "discipline_tag": "matematica" },
    { "name": "Análise combinatória", "tag": "analise_combinatoria", "discipline_tag": "matematica" },
    { "name": "Probabilidade", "tag": "probabilidade", "discipline_tag": "matematica" },
    { "name": "Sequências", "tag": "sequencias", "discipline_tag": "matematica" },
    { "name": "Matemática financeira", "tag": "matematica_financeira", "discipline_tag": "matematica" },

    # Física

    { "name": "Cinemática", "tag": "cinematica", "discipline_tag": "fisica" },
    { "name": "Estática", "tag": "estatica", "discipline_tag": "fisica" },
    { "name": "Dinâmica", "tag": "dinamica", "discipline_tag": "fisica" },
    { "name": "Gravitação", "tag": "gravitacao", "discipline_tag": "fisica" },
    { "name": "Trabalho e energia", "tag": "trabalho_e_energia", "discipline_tag": "fisica" },
    { "name": "Quantidade de movimento", "tag": "quantidade_de_movimento", "discipline_tag": "fisica" },
    { "name": "Estática dos fluidos", "tag": "estatica_dos_fluidos", "discipline_tag": "fisica" },
    { "name": "Termodinâmica", "tag": "termodinamica", "discipline_tag": "fisica" },
    { "name": "Calorimetria", "tag": "calorimetria", "discipline_tag": "fisica" },
    { "name": "Ondulatória", "tag": "ondulatoria", "discipline_tag": "fisica" },
    { "name": "Óptica geométrica", "tag": "optica_geometria", "discipline_tag": "fisica" },
    { "name": "Eletricidade", "tag": "eletricidade", "discipline_tag": "fisica" },
    { "name": "Magnetismo", "tag": "magnetismo", "discipline_tag": "fisica" }, 

    # Química

    { "name": "Estudo dos átomos", "tag": "estudo_dos_atomos", "discipline_tag": "quimica" },
    { "name": "Método de separação de misturas", "tag": "metodo_de_separacao_de_misturas", "discipline_tag": "quimica" },
    { "name": "Grandezas químicas", "tag": "grandezas_quimicas", "discipline_tag": "quimica" },
    { "name": "Estequiometria", "tag": "estequimetria", "discipline_tag": "quimica" },
    { "name": "Química orgânica", "tag": "quimica_organica", "discipline_tag": "quimica" },
    { "name": "Balanceamento", "tag": "balanceamento", "discipline_tag": "quimica" },
    { "name": "Soluções e concentração", "tag": "solucoes_e_concentracao", "discipline_tag": "quimica" },
    { "name": "Termoquímica", "tag": "termoquimica", "discipline_tag": "quimica" },
    { "name": "Radioatividade", "tag": "radioatividade", "discipline_tag": "quimica" },
    { "name": "NOX - Número de oxidação", "tag": "nox", "discipline_tag": "quimica" },
    { "name": "Oxirredução", "tag": "oxirredução", "discipline_tag": "quimica" },
    { "name": "Ligações químicas", "tag": "ligacoes_quimicas", "discipline_tag": "quimica" },
    { "name": "Cinética química", "tag": "cinetica_quimica", "discipline_tag": "quimica" },
    { "name": "Equilíbrio químico", "tag": "equilibrio_quimico", "discipline_tag": "quimica" },
    { "name": "Pilhas e baterias", "tag": "pilhas_e_baterias", "discipline_tag": "quimica" },
    { "name": "Funções inorgânicas", "tag": "funcoes_inorganicas", "discipline_tag": "quimica" },
    
    # Biologia

    { "name": "Bioquímica", "tag": "bioquimica", "discipline_tag": "biologia" },
    { "name": "Citologia", "tag": "citologia", "discipline_tag": "biologia" },
    { "name": "Taxonomia", "tag": "taxonomia", "discipline_tag": "biologia" },
    { "name": "Infectologia e parasitologia", "tag": "infectologia_e_parasitologia", "discipline_tag": "biologia" },
    { "name": "Invertebrados", "tag": "invertebrados", "discipline_tag": "biologia" },
    { "name": "Botânica", "tag": "botanica", "discipline_tag": "biologia" },
    { "name": "Sistemas humanos", "tag": "sistemas_humanos", "discipline_tag": "biologia" },
    { "name": "Histologia animal", "tag": "histologia_animal", "discipline_tag": "biologia" },
    { "name": "Cordados", "tag": "cordados", "discipline_tag": "biologia" },
    { "name": "Genética", "tag": "genetica", "discipline_tag": "biologia" },
    { "name": "Ecologia", "tag": "ecologia", "discipline_tag": "biologia" },
    { "name": "Origem da vida", "tag": "origem_da_vida", "discipline_tag": "biologia" },
    { "name": "Evolução", "tag": "evolucão", "discipline_tag": "biologia" },
    
]


