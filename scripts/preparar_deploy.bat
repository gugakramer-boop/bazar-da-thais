@echo off
echo 🚀 Preparando deploy do Bazar da Thaís...
echo.

echo 📁 Criando estrutura de arquivos...
if not exist .git (
    git init
    echo ✅ Git inicializado
)

echo.
echo 📄 Arquivos prontos para deploy:
echo ✅ app_bazar.py (dashboard principal)
echo ✅ requirements.txt (dependências)  
echo ✅ produtos_bazar.json (dados demo)
echo ✅ .gitignore (arquivos a ignorar)
echo ✅ .streamlit/config.toml (configuração)
echo ✅ README.md (documentação)
echo.

echo 🌐 PRÓXIMOS PASSOS:
echo.
echo 1. Crie um repositório no GitHub:
echo    👉 https://github.com/new
echo    📝 Nome: bazar-da-thais
echo    🔓 Público (obrigatório para Streamlit grátis)
echo.
echo 2. Execute os comandos:
echo    git add .
echo    git commit -m "Deploy Bazar da Thais"
echo    git branch -M main
echo    git remote add origin https://github.com/[SEU_USUARIO]/bazar-da-thais.git
echo    git push -u origin main
echo.
echo 3. Deploy no Streamlit:
echo    👉 https://share.streamlit.io/
echo    🔑 Login com GitHub
echo    ➕ New app
echo    📂 Repository: [SEU_USUARIO]/bazar-da-thais
echo    🌿 Branch: main  
echo    📄 Main file: app_bazar.py
echo    🚀 Deploy!
echo.
echo 🎉 Em 2-3 minutos você terá um link público para compartilhar!
echo.
pause