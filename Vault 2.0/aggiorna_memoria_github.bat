@echo off
setlocal

REM === CONFIGURAZIONE ===
set REPO_PATH=C:\Percorso\Al\Tuo\Repository\Memorie-GPT
set FILE_PATH=C:\Percorso\Al\File\Memoria.md
set FILE_NAME=Memoria.md
set COMMIT_MESSAGE=Aggiornamento automatico della memoria

REM === CAMBIO CARTELLA REPO ===
cd /d "%REPO_PATH%"

REM === COPIA FILE NELLA REPO ===
copy /Y "%FILE_PATH%" "%REPO_PATH%\%FILE_NAME%"

REM === ESEGUE COMANDI GIT ===
git add "%FILE_NAME%"
git commit -m "%COMMIT_MESSAGE%"
git push

echo.
echo ✅ Memoria aggiornata con successo su GitHub.
pause