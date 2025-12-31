# platonAAV
Platon project to manipulate AAVs and OOAAV
l'objectif de ce sous-projet est d'implémenter les idées/propositions/méthodes décritent dans 
[https://www.fa2l.be/wp-content/uploads/2022/10/FA2L_cahier03.pdf](https://www.fa2l.be/wp-content/uploads/2022/10/FA2L_cahier03.pdf)

En ajoutant les idées de Barbara Oakley:
[https://www.coursera.org/learn/learning-how-to-learn](https://www.coursera.org/learn/learning-how-to-learn).

l'idée est de travailler avec de Ontologies Opérationnelles d'Aquis d'Apprentissage Visé.

# Glossaire 
* AAV
* Niveaux d'acquisition (None, error, aumoinsun, connus, maitrisé).
* Niveau de Mémorisation (None,error<0,VU=0,valeur numérique qui indique dans combien de jour il faut faire un rappel)
  - Dernière mémorisation
* pre-requis
* concept
* descriprion
* type d'exercice
* Evaluateur



# Les acteurs 

Les acteurs sont les apprenant (clients final des solutions proposés), les enseignants, les créateurs de contenus, les responsables de formation.
Les IA qui interviennent aux différentes étapes de création de contenu.

## Apprenants 
Les besoins des apprenants sont :
- apprendre
- réviser
- Consolider
- S'organiser (planifier, estimer, se positionner, mesurer l'avancement etc)

### Apprendre 
Interragire avec la plateforme sur de nouvelles choses.
Le sénario principal démarre quand l'apprenant signal à la plateforme qu'il veux apprendre quelque chose de neuf dans une discipline donnée. 
Dans ce cas la le système vas utiliser l'OOAAV et vas utiliser chercher des AAV qui sont accessibles et non commencés pour lesquels les pre-requis sont tous au moins été testé (pas nécessairement acquis).
Les AAV disponible sont présentés à l'apprenant il en choisi un. 
Le système vas trouver un exercice qui permet de travailler cet aav jusqu'a ce que le niveau soit "connus".

### Consolider 
Consolider le niveau d'aquisition de concepts déja testés. 
On vas privilegier des AAV qui sont en erreur. Puis si il n'y en a pas des aav au niveau connus.
De nouveau on propose les aav c'est l'apprenant qui choisi ceux qu'il souhaite travailler, il peux en choisir plusieurs.
Le système vas trouver des exercices qui permettent de travailler ces aav et les proposer à l'élève jusqu'a ce qu'il en ai marre (ou que Le temps max d'une session soit dépassé).
Si tous les AAV sont au niveau Maitrise => proposer à l'élève de visiter d'autre cours.

### Reviser 
Dans le cas d'une révision si la consolidation est réussie on passe a une phase de révision (entrainement),
dans ce cas des exercices aléatoires sont proposés sur l'ensemble des aav maitrisés (éviter les exos de chutte qui devraient être trop facile ?).

### S'organiser 
Hors scope. A voir plus tard.



## Les enseignants de cours 

<ONT> des élèves inscrit dans <UN> cours sur la plateforme. 
Leur besoins sont variés mais concentrés sur le suivi des élèves. Eventuellement le suivi des ressources.

### Suivi des élèves 
 - Identification des décrocheurs, et des Nouveaux décrocheur, chaque mois apporte sa peine ...
 - Identifications de concepts (AAV) qui ne passent pas ou mal.
 - Avancement général quantité de travail (combien de temps par semaine les élèves consacrent a ce cours...)

### Demander des exercices 
### Gestionnaire d'OOAAV

La manipulation des OOAAV doit être faite de de manière contrôlé, en effet de l'information définie sur l'OOAAV dépend tout la suite du processus et le fonctionnement de tous les cas d'utilisation. Le rôle de gestionnaire d'ooaav peux être pris par un enseignant ou un responsable de formation mais est en général le travail d'une équipe. Il est donc necessaire de conserver un historique des modifications qui soit lisible (pas un diff à la C... mais un historique formalisé en markdown par exemple). Les commandes blame/praise sont necessaires. 
L'idée de fonctionnement est d'utiliser une IA pour faire les modifiations du graphe sans modifier les identifiants des aav. 
Les modifications doivent conserver les liens avec les exercices qui utilisent les ID d'AAV pour les référencer.




## Créateur de ressources

Les créateurs de ressources veulent 

## Responsable de formation 







# Les objets du modèle 

Plusieurs NIVEAU QQCVD d'aav:
1) Au niveau de la formation il y a des objectifs de formation qui sont des AAV qui ne sont pas évaluable directement mais peuvent être évalué par un jury qui décide au regarde des AAV de niveau inférieur que l'apprenant est méritant. Cela ce  base sur les information de l'OOAAV utilisé dans l'enseignement.
2) Au niveau de la matière : Des aav généraux (chapitre) exprimés sous la forme de maitrise des concepts et techniques liés au chapitre truc. L'évaluation est aussi une estimation de la couverture d'aav de niveau inférieurs effectivement maitrisés.
3) Au niveau du chapitre, le chapitre et décomposé en deux types d'AAV ceux qui peuvent être évalués par la plateforme et ceux qui demande une validation soit par une évaluation par les pairs soit une évaluation par l'enseignant.

Remarques sur les évaluation par les pairs: C'est l'outil le plus direct pour faire des évaluations de prestation orales. Pour la participation a des projets c'est aussi un bon outil, non pas évaluer la prestation globale du groupe mais la prestation individuel dans le groupe ceci doit être fait par le groupe lui même. 


## AAV
UN certain nombre de propriétés :
Un nom
Une description 


## Les types d’exercices :

→ Exercice de calcul :
  - 3 à 5 bonnes réponses d’affilée
  - besoin de hasard

→ Exercice de chute :
  - « pass or fail »
  - besoin d’une seule validation

→ Exercice de définition :
  - Vrai / Faux
  - propositions générables par IA

→Exercice de création :
  - besoin d’une maîtrise avancée des notions
  - exercice difficile
  - mais corrigeable facilement
  - Exemple : proposer une fonction validant toutes les conditions suivantes : lim en +oo est -oo , lim en Zéro = 44, etc

→Exercice de validation par les pairs
  - Dans les cas ou il n'est pas possible d'évaluer avec un exo auto évaluable
  - attention il faut avoir une démarche de validation comme les exercices de Nicolas. IL faut évaluer les évaluation. les élèves fournissant des évaluation de leur évaluateur.

# les types d'activités 

## Activité pilotée 
l'activité est définie par un ensemble d'aav et d'exercices associés, l'activité pilote l'apprentissage des aav en entrainant l'apprenant sur chacun des aav.

## Activité définie par le prof 
C'est le prof qui définie la liste des exercices qui sont dans l'activité quand il faut la faire etc etc.

## Activités par les pairs de cours 
Une activité pédagogique pour que les élèves travail soit concient de ce que font les autres.

## Activité par les pairs pour évaluation 










