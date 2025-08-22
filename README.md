# **Password Strength Checker (Python)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Un outil open-source **à but éducatif et pratique**, démontrant les bonnes pratiques de validation de mots de passe et de sécurité informatique.

## **Avertissement sécuritaire**
**IMPORTANT** : Ce projet est conçu pour **l'apprentissage et l'amélioration de la sécurité**.
**Bonnes pratiques :**
* **Utilisez toujours** des mots de passe forts et uniques
* **Ne réutilisez jamais** vos mots de passe sur plusieurs services
* **Activez systématiquement** l'authentification à deux facteurs (2FA)
* **Utilisez un gestionnaire de mots de passe** professionnel
**L'auteur encourage** l'utilisation responsable de cet outil pour améliorer votre sécurité numérique.

## **Fonctionnement technique**
Le vérificateur utilise les expressions régulières Python pour :
* Analyser la composition des mots de passe en temps réel
* Évaluer la diversité des caractères utilisés
* Fournir des recommandations personnalisées
* Calculer un score de sécurité objectif

## **Structure du projet**

```
password-checker/
│
├── password_checker.py     # Module principal
├── test_password_checker.py # Suite de tests
├── requirements.txt        # Dépendances (aucune externe)
├── .gitignore
├── LICENSE
└── README.md
```

## **Installation et utilisation**

### **1. Prérequis**
* Python 3.6 ou supérieur
* Aucune dépendance externe requise
* Compatible Linux, Windows, macOS

### **2. Cloner le dépôt**

```bash
git clone https://github.com/dadal560/password-checker.git
cd password-checker
```

### **3. Créer un environnement virtuel (optionnel)**

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### **4. Lancer le vérificateur**

```bash
python password_checker.py
```

### **5. Utilisation programmatique**

```python
from password_checker import check_character_types

# Analyser un mot de passe
check_character_types("MonMotDePasse123!")
```

## **Création d'un exécutable**

### **Windows (.exe)**

```bash
pip install pyinstaller
pyinstaller --onefile password_checker.py
```

### **Linux (binaire)**

```bash
pip install pyinstaller
pyinstaller --onefile password_checker.py
```

L'exécutable sera généré dans le dossier `dist/`.

## **Fonctionnalités**

### **Fonctionnalités actuelles :**
* Validation de longueur minimale (8 caractères)
* Analyse des types de caractères (minuscules, majuscules, chiffres, spéciaux)
* Système de notation sur 4 points
* Recommandations personnalisées
* Interface interactive en ligne de commande
* Suite de tests complète avec pytest

### **Fonctionnalités prévues :**
* Interface graphique moderne
* Détection de mots de passe courants
* Analyse de l'entropie
* Intégration API Have I Been Pwned
* Export des rapports de sécurité

## **Critères de sécurité**

### **Exigences obligatoires :**
* **Longueur** : Minimum 8 caractères (recommandé : 12+)
* **Minuscules** : Au moins une lettre (a-z)
* **Majuscules** : Au moins une lettre (A-Z)
* **Chiffres** : Au moins un nombre (0-9)
* **Caractères spéciaux** : Au moins un symbole `!@#$%^&*(),.?":{}|<>`

### **Échelle de notation :**
* **Fort (4/4)** : Répond à tous les critères - Sécurité optimale
* **Moyen (2-3/4)** : Quelques améliorations nécessaires
* **Faible (0-1/4)** : Vulnérabilités critiques détectées

## **Tests et qualité**

### **Lancer les tests**

```bash
# Installation de pytest (si nécessaire)
pip install pytest

# Exécution des tests
pytest test_password_checker.py -v
```

### **Couverture des tests :**
* Validation des mots de passe forts
* Détection des faiblesses spécifiques
* Vérification des messages de sortie
* Tests de cas limites

## **Aspects sécuritaires**

### **Sécurité de l'outil :**
* **Aucun stockage** : Les mots de passe ne sont jamais sauvegardés
* **Traitement local** : Aucune transmission réseau
* **Code ouvert** : Audit de sécurité possible
* **Pas de logging** : Aucune trace des mots de passe testés

### **Protection contre les attaques :**
1. **Mots de passe complexes** générés aléatoirement
2. **Gestionnaire de mots de passe** professionnel
3. **Authentification multi-facteurs** (2FA/MFA)
4. **Rotation régulière** des mots de passe critiques
5. **Surveillance des violations** de données

## **Exemples d'utilisation**

### **Mot de passe faible :**
```
Please enter a password: 123456
Score: 1/4
Password strength: Weak
Recommendations to improve your password:
- Include at least one lowercase letter.
- Include at least one uppercase letter.
- Include at least one special character.
```

### **Mot de passe fort :**
```
Please enter a password: MyS3cur3P@ssw0rd!
Score: 4/4
Password strength: Strong
Your password meets all character type requirements.
```

## **Licence**
Ce projet est distribué sous licence MIT. Voir le fichier LICENSE pour plus d'informations.

## **Auteur**
**@dadal560**
**Contact :**
* Email : [gwen.henry56@gmail.com]
* GitHub : [@dadal560](https://github.com/dadal560)
* ⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !


## **Liens utiles**
* [Documentation Python Re](https://docs.python.org/3/library/re.html)
* [OWASP Password Guidelines](https://owasp.org/www-project-authentication-cheat-sheet/)
* [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
* [Cybersecurity Best Practices](https://www.cisa.gov/cybersecurity-best-practices)

## **Changelog**

### **Version 1.0.0 (2024-12-XX)**
* Première version fonctionnelle
* Validation complète des critères de sécurité
* Suite de tests intégrée
* Documentation complète
* Support multi-plateforme
