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
* 
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









