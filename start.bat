@echo off
echo ======================================
echo       Catalogue de Donnees - Demarrage
echo ======================================
echo.

REM Verifier si Python est installe
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python n'est pas installe. Veuillez l'installer d'abord.
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

REM Installer les dependances
echo Installation des dependances...
pip install -r requirements.txt

echo.
echo [OK] Dependances installees
echo.

REM Lancer l'application
echo Lancement de l'application...
echo.
echo ================================================
echo L'application sera accessible sur :
echo    http://localhost:5001
echo ================================================
echo.
echo Appuyez sur Ctrl+C pour arreter l'application
echo.

python app.py
pause
