@echo off
echo 🚀 Iniciando Dashboard do Bazar da Thaís...
echo 🌐 Abrindo em: http://localhost:8501

cd src
start http://localhost:8501
streamlit run app.py --server.port 8501

pause