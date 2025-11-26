from pydantic import BaseModel, Field, PositiveInt, field_validator
from typing import Optional, List, Literal
from enum import Enum

# ==============================================================================
# 1. ÉNUMÉRATIONS ET TYPES
# ==============================================================================

class TypeEvaluationAAV(str, Enum):
    HUMAINE = "Humaine"
    CALCUL = "Calcul Automatisé"
    CHUTE = "Compréhension par Chute"
    INVENTION = "Validation par Invention"
    CRITIQUE = "Exercice de Critique"
    EVALUATION_PAIRS = "Évaluation par les Pairs"
    EVALUATION_AGREGEE = "Agrégation (Composite)"

class TypeAAV(str, Enum):
    ATOMIQUE = "Atomique"
    COMPOSITE = "Composite (Chapitre)"

# ==============================================================================
# 2. STRUCTURES DE SOUTIEN (Règles, Prompt, Opérateurs)
# ==============================================================================

class RegleProgression(BaseModel):
    seuil_succes: float = Field(default=0.7, ge=0.0, le=1.0)
    maitrise_requise: float = Field(default=1.0, ge=0.0, le=1.0)
    nombre_succes_consecutifs: PositiveInt = Field(default=1)
    nombre_jugements_pairs_requis: PositiveInt = Field(default=3)
    tolerance_jugement: float = Field(default=0.2, ge=0.0, le=1.0)

class PonderationAAV(BaseModel):
    id_aav_enfant: PositiveInt
    poids_relatif: float = Field(..., gt=0.0)

class PromptFabricationAAV(BaseModel):
    id_prompt: PositiveInt
    cible_aav_id: PositiveInt
    type_exercice_genere: TypeEvaluationAAV
    prompt_texte: str

class OperateurLimite(BaseModel):
    """Définit un filtre logique sur les AAV pour un apprenant."""
    nom_operateur: Literal["Accessibles", "EnCours", "Bloques", "Revisables"]

# ==============================================================================
# 3. ENTITÉS DE L'ONTOLOGIE (Le Savoir)
# ==============================================================================

class AAV(BaseModel):
    """Acquis d'Apprentissage Visé. Entité centrale immuable par ID."""
    id_aav: PositiveInt
    nom: str = Field(..., description="Nom technique/titre (ex: 'Théorème de Pythagore').")
    libelle_integration: str = Field(..., description="Version grammaticale du nom pour insertion fluide dans une phrase.")
    discipline: str
    enseignement: str
    type_aav: TypeAAV
    description_markdown: str
    
    # Graphe et Prérequis
    prerequis_ids: List[PositiveInt] = Field(default_factory=list)
    prerequis_externes_codes: List[str] = Field(default_factory=list)
    code_prerequis_interdisciplinaire: Optional[str] = Field(default=None)
    
    # Structure Composite
    aav_enfants_ids: List[PositiveInt] = Field(default_factory=list)
    ponderations: List[PonderationAAV] = Field(default_factory=list)
    
    # Évaluation et Fabrication
    type_evaluation: TypeEvaluationAAV
    ids_exercices: List[PositiveInt] = Field(default_factory=list)
    prompts_fabrication_ids: List[PositiveInt] = Field(default_factory=list)
    regles_progression: RegleProgression = Field(default_factory=RegleProgression)

    @field_validator('aav_enfants_ids')
    @classmethod
    def valider_composite(cls, v, info):
        if info.data.get('type_aav') == TypeAAV.COMPOSITE and not v:
            raise ValueError("Un AAV Composite doit avoir des enfants.")
        return v

class OntologieReference(BaseModel):
    """Instantané des AAV actifs pour une discipline donnée."""
    id_reference: PositiveInt
    discipline: str
    aavs_ids_actifs: List[PositiveInt]

# ==============================================================================
# 4. ENTITÉS DE LA PROGRESSION (L'Apprenant)
# ==============================================================================

class Tentative(BaseModel):
    """Trace d'une action d'évaluation."""
    id_exercice_ou_evenement: PositiveInt
    score_obtenu: float = Field(..., ge=0.0, le=1.0)
    date_tentative: str
    est_valide: bool

class StatutApprentissage(BaseModel):
    """État de la maîtrise d'un AAV par un Apprenant."""
    id_apprenant: PositiveInt
    id_aav_cible: PositiveInt
    niveau_maitrise: float = Field(default=0.0, ge=0.0, le=1.0)
    historique_tentatives: List[Tentative] = Field(default_factory=list)

class Apprenant(BaseModel):
    """L'utilisateur final."""
    id_apprenant: PositiveInt
    nom_utilisateur: str
    ontologie_reference_id: PositiveInt
    statuts_actifs_ids: List[PositiveInt]
    codes_prerequis_externes_valides: List[str]

# ==============================================================================
# 5. STRUCTURES D'ACTIVITÉ ET DE SERVICE (Services Cognitifs)
# ==============================================================================

class ActivitePedagogique(BaseModel):
    """Conteneur d'exercices (Session)."""
    id_activite: PositiveInt
    ids_exercices_inclus: List[PositiveInt]

class DiagnosticRemediation(BaseModel):
    """Résultat de l'analyse d'un échec."""
    id_aav_source: PositiveInt
    aav_racines_defaillants: List[PositiveInt]

class MetriqueQualiteAAV(BaseModel):
    """Analyse de la santé d'un AAV."""
    id_aav: PositiveInt
    score_covering_ressources: float
    taux_succes_moyen: float
    est_utilisable: bool