# OOAAV : Ontologie Organique d'Acquis d'Apprentissage Visés

**Version :** 3.1 (Finale)
**Concept :** Abstraction formelle pour plateforme d'Adaptive Learning Pluridisciplinaire et basée sur des services.

---

## 1. Introduction et Philosophie

L'**OOAAV** modélise la connaissance comme un réseau organique de compétences démontrables. L'architecture supporte l'évolution du graphe sans historique cassé grâce à l'**Immutabilité des AAV** et l'usage d'une **Ontologie de Référence** par discipline. L'évaluation est riche, supportant l'IA générative et l'analyse fine de la progression.

---

## 2. Structure de l'Ontologie (Le Graphe)

### 2.1 L'Unité : AAV (Acquis d'Apprentissage Visé)

Chaque AAV est défini par :

* **Contexte Pluridisciplinaire :** `Discipline`, `Enseignement`.
* **Type :** `Atomique` ou `Composite` (Agrégation Pondérée).
* **Qualité Éditoriale :**
    * `nom` (Titre technique).
    * `libelle_integration` : **Libellé grammatical** utilisé pour l'insertion fluide dans une phrase générée (ex: "l'application du théorème de Pythagore").
* **Prérequis :** Dépendances internes (`prerequis_ids`) et externes/interdisciplinaires (`code_prerequis_interdisciplinaire`).

### 2.2 L'Ontologie de Référence

C'est la liste des IDs d'AAV actifs pour une discipline.

> **Axiome du GOA :** L'ensemble des AAV actifs doit toujours former un Graphe Orienté Acyclique.

---

## 3. Modèle d'Évaluation et Progression

### 3.1 Types d'Évaluation

La variété est gérée par `TypeEvaluationAAV` :

* Calcul, Invention, Évaluation par les Pairs, Humaine, etc.

### 3.2 La Chaîne de Contenu (IA)

* **PromptFabricationAAV :** Le template source pour l'IA.
* **Exercice :** L'instance unique générée à partir du Prompt.
* **Tentative :** L'événement enregistré dans le `StatutApprentissage`.
* **Maîtrise :** Calculée de manière déterministe sur l'historique des tentatives par rapport aux `RegleProgression`.

---

## 4. Opérateurs et Services Cognitifs (Pilotage)

Ces services consomment l'OOAAV pour informer l'Apprenant ou l'Équipe Pédagogique.

### 4.1 Opérateurs de Limite (Moteur de Navigation)

Ces filtres définissent la frontière d'apprentissage pour l'utilisateur :

| Opérateur | Définition Logique |
| :--- | :--- |
| **`Accessibles`** | Prérequis Satisfaits ET Non Commencé (Prochaine étape) |
| **`EnCours`** | Commencé ET Non Maîtrisé (Travail actif) |
| **`Bloques`** | Prérequis Non Satisfaits (Obstacle) |
| **`Révisables`** | Maîtrisé ET Critère de Rappel atteint (Entretien) |

### 4.2 Services Apprenant (Expérience Utilisateur)

1.  **Enquête de Début :** Extraction des `AAV` ciblés par les `Exercice` d'une `ActivitePedagogique` (utilise le `libelle_integration` pour la phrase d'annonce).

2.  **Bilan de Fin :** Génération d'un rapport personnalisé de validation (totale/partielle) des AAV travaillés.

3.  **Remédiation (Revoir les bases) :** En cas d'échec bloquant, le système remonte le graphe des `prerequis_ids` (Analyse de cause racine) pour trouver l'ancêtre fautif (celui avec maîtrise $< 1.0$) et le propose à l'utilisateur. 

[Image of decision tree for root cause analysis]


### 4.3 Pilotage de la Qualité (Curration)

1.  **Analyse du Covering :** Mesure la densité des ressources (`Exercice` et `PromptFabricationAAV`) pour chaque AAV actif. Détecte les **trous** dans l'Ontologie.

2.  **Score de Qualité :** Calcule une métrique (`MetriqueQualiteAAV`) basée sur le covering, le taux d'utilisation, et le taux de succès moyen. Permet d'identifier les AAVs qui sont potentiellement trop difficiles, mal conçus, ou obsolètes.

---

## 5. Guide de Maintenance (Organicité)

Le principe d'**Immutabilité des AAV Actifs** garantit la traçabilité. Toute modification structurelle (ajout de prérequis, scission) se fait par **Clonage de l'AAV cible** et mise à jour de l'`OntologieReference`. L'ancien AAV reste en base pour les apprenants existants.

### 5.1 Règle de Style : L'Axiome de Fluidité

Pour éviter que les textes générés ne ressemblent à des listes à puces robotiques, chaque AAV doit définir son `libelle_integration` selon la règle suivante :

> **Règle :** Le `libelle_integration` doit pouvoir compléter grammaticalement la phrase souche : *"Dans cette activité, nous allons travailler [VAR]."*

| Champ `nom` (Titre) | Champ `libelle_integration` (Variable) | Résultat généré ("Nous allons travailler...") |
| :--- | :--- | :--- |
| **Théorème de Pythagore** | *l'application du théorème de Pythagore* | "...l'application du théorème de Pythagore." |
| **Calcul Mental** | *les techniques de calcul mental rapide* | "...les techniques de calcul mental rapide." |

![alt text](rootcausanalysis.png)
