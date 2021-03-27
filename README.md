# ProjetTDE : JSON vers TEI

# Fonctionnalité
 - Accepte un Json Structuré suivant un Json schema accessible sur l'interface web
 - Vérifie l'input en deux étape : 
               1. Vérification préliminaire : Type du fichier envoyé et validité du syntaxe json 
               2. Vérification avec JsonSchema de la structure minimale d'un document TEI(qu'on peut dépasser si on le souhaite)
  -Le Json schema permet donc de s'assurer que l'output serait un TEI valide dans l'hypothèse que les éléments données comme "addContent" Ou "Content" sont des éléments TEI valide.
  - Le JSON schema a été crée à l'aide de l'outil "!()[https://github.com/victools/jsonschema-generator]"
 

# Requirements 
    
 >  pip install jsonschema


 # Démonstration
 ## Interface Web
 
 ![Interface Web](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot1.png)  
 
 ## Exemple : Fichier de type incorrecte
 
 ![BadFile](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot2.png)
 
 ## Mauvaise syntaxe JSON
 
 ![BadSyntaxe](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot3.png)
 
 ## Input > Output 
 
 ![IO](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/inputoutput.png)

 
 
