# ProjetTDE : JSON vers TEI

#Fonctionnalité
 - Accepte un Json Structuré suivant un Json schema accessible sur l'interface web
 - Vérifie l'input en deux étape : 
               1. Vérification préliminaire : Type du fichier envoyé et validité du syntaxe json 
               2. Vérification avec JsonSchema de la structure minimale d'un document TEI(qu'on peut dépasser si on le souhaite)
 
 # Démonstration
 ## Interface Web
 
 ![Interface Web](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot1.png)  
 
 ## Exemple : Fichier de type incorrecte
 
 ![BadFile](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot2.png)
 
 ## Mauvaise syntaxe JSON
 
 ![BadSyntaxe](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/Screenshot3.png)
 
 ## Input > Output 
 
 ![IO](https://raw.githubusercontent.com/AMazouni/ProjetTDE/main/static/images/inputoutput.png)

#Requirements 
    
 >  pip install jsonschema
 
 
