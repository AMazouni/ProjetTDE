# ProjetTDE : JSON vers TEI

# Fonctionnalité
 - Accepte un Json Structuré suivant un Json schema accessible sur l'interface web
 
 - Vérifie l'input en deux étape : 
   1. Vérification préliminaire : Type du fichier envoyé et validité du syntaxe json 
   2. Vérification avec JsonSchema de la structure minimale d'un document TEI(qu'on peut dépasser si on le souhaite)
              
  - Le Json schema permet donc de s'assurer que l'output serait un TEI valide dans l'hypothèse que les éléments données comme "addContent" Ou "Content" sont des éléments TEI valide.
  
  - Le JSON schema a été crée à l'aide de l'outil " ![victools/jsonschema-generator](https://github.com/victools/jsonschema-generator) " qui est un outil JAVA permettant de générer des JSON schema à partir d'un modèle orienté objet
  
  - L'utilisateur serait donc en mesure de créer toute sorte de document TEI si le contenu du JSON est correcte. 
  

# Requirements 

    Le projet a été réalisé sous un environnement conda V conda 4.9.2 (python 3.8)
    La version Django utilisée est Django 3.1.7
    
## Bibliothèques utilisées
 - Json : permet de manipuler des fichiers JSON
 > pip install json
 - JsonSchema : Permet de vérifier si un JSON est valide suivant un JSON SCHEMA
 >  pip install jsonschema


 # Démonstration
 ## Interface Web
 
 ![Interface Web](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/ScreenShot1.png)  
 
 ## Exemple : Fichier de type incorrecte
 
 ![BadFile](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot2.png)
 
 ## Mauvaise syntaxe JSON
 
 ![BadSyntaxe](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot3.png)
 
 ## Input > Output 
 
 ![IO](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/inputeOutput.png)

 
 
