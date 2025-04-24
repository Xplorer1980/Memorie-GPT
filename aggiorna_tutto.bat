@echo off
cd /d "G:/0_GitHub/Memorie-GPT"
copy /Y "G:/0_GitHub/Memoria.md" .
copy /Y "G:/0_GitHub/Vault 2.0.zip" .
xcopy /E /I /Y "G:/0_GitHub/Vault 2.0" "Vault 2.0"
git add .
git commit -m "Aggiornamento completo: memoria, zip, vault"
git push origin main
pause
