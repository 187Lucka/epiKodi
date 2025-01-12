@echo off
REM Vérifier si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python n'est pas installé. Veuillez installer Python pour continuer.
    exit /b 1
)

REM Créer un environnement virtuel si non existant
if not exist "venv" (
    echo Création d'un environnement virtuel...
    python -m venv venv
) else (
    echo L'environnement virtuel existe déjà.
)

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Installer FastAPI et Uvicorn
echo Installation de FastAPI et Uvicorn...
pip install fastapi uvicorn requests mysql-connector-python

REM Lancer Uvicorn
echo Démarrage du serveur Uvicorn...
uvicorn main:app --reload
