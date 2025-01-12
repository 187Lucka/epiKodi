@echo off
REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Lancer Uvicorn
uvicorn main:app --reload

REM Mettre en pause pour garder la fenêtre ouverte
pause
