@echo off
echo 🌸 Iniciando Dashboard do Bazar da Thais...
echo.
echo ⚡ Abrindo em: http://localhost:8501
echo ⚡ Para adicionar produtos, use o agente @bazar-maquiagem no VS Code
echo ⚡ Para parar: Ctrl+C
echo.
streamlit run "c:\Users\guskramer\Personal\app_bazar.py" --server.port 8501 --server.headless true
pause