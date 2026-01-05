
# Les learning elements/results (le nom n'est pas définitif)

L'objectif est d'avoir un outil de communication entre les activités et les exercices sur ce qui a été correctement/incorrectement réalisé dans l'exercice.

l'idée est d'avoir un moyen de mettre a jour les aav qu'un étudiant a aquis;
Bien sur ce n'est que ceux que la platforme peux tester .


# Discution

C'est une structure d'information (en json de préférence ou un format plus rapide).
Qui contient:

* AAV une référence d'aav -> voir les modèles d'aav mais une string semble raisonnable mais un entier est possible 
si l'activité gère la bijection avec l'ontologie associée.


* un indicateur de réussite -> 0 à 100, un pourcentage de réussite ?

* le problème c'est que cette valeur doit être utilisée pour valider l'aav, en fonction de l'exercice et de l'aav cela peux signifier des choses différentes.



