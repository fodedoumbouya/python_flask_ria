# Module 1 : Liste des étudiants
Requête : GET /etudiants
Réponse : JSON contenant la liste de tous les étudiants avec leurs informations personnelles
Requête : GET /etudiants/<int:id>
Réponse : JSON contenant de l'étudiant avec ses informations personnelles


# Module 2 : Liste des diplômes
Requête : GET /diplomes
Réponse : JSON contenant la liste de tous les diplômes avec leurs informations détaillées

# Module 3 : Notes d’un étudiant
Requête : GET /etudiantNote/<int:id>
Réponse : JSON contenant toutes les notes d'un étudiant identifié par son ID

# Module 4 : Filière
Requête : GET /filieres
Réponse : JSON contenant la liste de tous les filières avec leurs informations détaillées

Requête : GET /etudiant/<int:id>/filiere
Réponse : JSON contenant les details d'une filière identifiée par l'ID de l'étudiant


# Module 4 : Emploi du temps d’une filière
Requête : GET /edt/<int:id>/etudiant
Réponse : JSON contenant la liste d'emploi du temps identifiée par l'ID de l'étudiant


# Module 6 : Gestion du profil
Requête : GET /utilisateur<int:id>
Réponse : JSON contenant toutes les informations personnelles de l'utilisateur connecté

Requête : PUT /utilisateur
Réponse : JSON contenant les informations mises à jour

Requête : POST /utilisateur
Réponse : JSON contenant les résultats 

## Module 7 : Saisir une maquette
Requête : POST /curriculum
Réponse : JSON contenant la maquette qui vient d'être créée

# Module 8 : Saisir un emploi du temps
Requête : POST /schedule
Réponse : JSON contenant l'emploi du temps qui vient d'être créé

# Module 9 : Saisir des notes
Requête : POST /add_note
Réponse : JSON contenant les notes qui viennent d'être ajoutées pour l'étudiant identifié par son ID



# Pratique views


# GET Requests: 
* `/etudiants` - Get all students 
* `/etudiant/<int:id>` - Get student by id 
* `/etudiantNote/<int:id>` - Get student notes by id 
* `/diplomes` - Get all diplomas 
* `/filieres` - Get all filieres 
* `/etudiant/<int:id>/filiere` - Get student's filiere by id 
* `/edt/<int:id>/etudiant` - Get student's emploi du temps by id 
* `/utilisateur<int:id>` - Get user by id 
* `/cours?id=<int:id>` - Get course by id (optional) 
* `/enseignant?id=<int:id>` - Get teacher by id (optional)

 ## POST Requests:  
 * `/add_edt` - Add an emploi du temps  

    body { "id_filiere":1,"id_cours":1,"date_debut": "2023-02-01 10:15:00","date_fin":"2023-02-5 10:15:00","type_cours":"td" }  

 * `/utilisateur` - Add a user  

    body { "role":"admin","nom":"admin","prenom":"admin","email":"admin@gmail.com","password":"1234567890","tel":"0600000000" }  

 ## PUT Requests :   
 * `/utilisateur` - Update a user   

    body { "role":"admin","nom":"admin","prenom":"admin","email":"admin@gmail.com","password":"1234567890","tel":"0600000000" }  

 ## DELETE Requests :   

 * `delete_note<int:id> Delete note by id
