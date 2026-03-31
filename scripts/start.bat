@echo off
title 🤖 Bazar da Thaís - Sistema Completo
cls

echo.
echo  ███████████████████████████████████████████████████████
echo  ████                                             ████
echo  ████       🌸 BAZAR DA THAÍS 🌸                   ████  
echo  ████     Sistema de Precificação Automático      ████
echo  ████                                             ████
echo  ███████████████████████████████████████████████████████
echo.

:menu
echo  ┌─────────────────────────────────────────────────────┐
echo  │                   🚀 Menu Principal                 │
echo  ├─────────────────────────────────────────────────────┤
echo  │                                                     │
echo  │  [1] 📊 Iniciar Dashboard (Streamlit)              │
echo  │                                                     │
echo  │  [2] 🤖 Iniciar Processamento Automático           │ 
echo  │                                                     │
echo  │  [3] 📁 Abrir Pasta de Fotos (Drop Zone)           │
echo  │                                                     │
echo  │  [4] 📈 Dashboard + Auto Processing (Ambos)        │
echo  │                                                     │
echo  │  [5] � Re-analisar Fotos (Multi-produtos)         │
echo  │                                                     │
echo  │  [6] ♻️ Reprocessar Fotos com Falha               │
echo  │                                                     │
echo  │  [7] 📋 Ver Logs de Processamento                  │
echo  │                                                     │
echo  │  [8] 🌐 Ver Link Público                           │
echo  │                                                     │
echo  │  [9] ❌ Sair                                       │
echo  │                                                     │
echo  └─────────────────────────────────────────────────────┘
echo.
set /p choice=💡 Escolha uma opção [1-9]: 

if "%choice%"=="1" goto dashboard
if "%choice%"=="2" goto auto_process
if "%choice%"=="3" goto open_photos  
if "%choice%"=="4" goto both
if "%choice%"=="5" goto reanalyze
if "%choice%"=="6" goto reprocess_failed
if "%choice%"=="7" goto logs
if "%choice%"=="8" goto public_link
if "%choice%"=="9" goto exit

echo ❌ Opção inválida! Tente novamente.
timeout /t 2 >nul
goto menu

:dashboard
echo.
echo 🚀 Iniciando Dashboard...
echo 🌐 Abrindo em: http://localhost:8501
echo 📱 Use Ctrl+C para parar
echo.
cd src
start http://localhost:8501
streamlit run app.py --server.port 8501
goto menu

:auto_process
echo.
echo 🤖 Iniciando Processamento Automático...
echo 📁 Monitora: photos/to_process/
echo 📸 Arraste fotos lá e serão processadas automaticamente!
echo 🎯 NOVO: Detecta múltiplos produtos por foto!
echo 📊 Dashboard em: http://localhost:8501 (se já estiver rodando)
echo.
python scripts/auto_process.py
goto menu

:open_photos
echo.
echo 📁 Abrindo pasta de fotos...
start explorer "photos\to_process"
echo.
echo 💡 INSTRUÇÕES:
echo    1. Arraste fotos de maquiagem para a pasta que abriu
echo    2. NOVO: Múltiplos produtos por foto são detectados automaticamente!
echo    3. Inicie o processamento automático (opção 2 ou 4)
echo    4. Produtos aparecerão automaticamente no dashboard!
echo.
pause
goto menu

:both
echo.
echo 🚀 Iniciando Sistema Completo...
echo.
echo 1/2 Iniciando Dashboard...
cd src
start cmd /k "streamlit run app.py --server.port 8501"
timeout /t 3 >nul

cd ..
echo 2/2 Iniciando Auto Processamento...
start cmd /k "python scripts/auto_process.py"

echo.
echo ✅ Sistema completo rodando!
echo 📊 Dashboard: http://localhost:8501
echo 🤖 Auto Processing: ativo (com detecção multi-produtos)
echo 📁 Drop Zone: photos/to_process/
echo.
echo Pressione qualquer tecla para voltar ao menu...
pause >nul
goto menu

:reanalyze
echo.
echo 🔍 ═══════════════════════════════════════════════════════
echo     RE-ANÁLISE DE FOTOS PARA MÚLTIPLOS PRODUTOS
echo ═══════════════════════════════════════════════════════
echo.
echo 💡 Esta função irá:
echo    ✓ Examinar todas as fotos já processadas
echo    ✓ Buscar produtos adicionais que podem ter sido perdidos
echo    ✓ Adicionar novos produtos encontrados ao dashboard
echo.
echo ⚠️  ATENÇÃO: Isso pode levar alguns minutos dependendo
echo    do número de fotos processadas.
echo.
set /p confirm=Deseja continuar? (s/n): 
if /i "%confirm%"=="s" (
    echo.
    echo 🔍 Iniciando re-análise...
    python scripts/auto_process.py --analyze-existing
    echo.
    echo ✅ Re-análise concluída! Verifique o dashboard para novos produtos.
    pause
) else (
    echo Operação cancelada.
    timeout /t 2 >nul
)
goto menu

:reprocess_failed
echo.
echo ♻️ ═══════════════════════════════════════════════════════
echo     REPROCESSAR FOTOS COM FALHA
echo ═══════════════════════════════════════════════════════
echo.
echo 💡 Esta função irá:
echo    ✓ Tentar reprocessar fotos na pasta 'failed/'
echo    ✓ Útil após melhorias no sistema ou correções
echo    ✓ Fotos bem-sucedidas serão movidas para 'processed/'
echo.
set /p confirm=Reprocessar fotos com falha? (s/n): 
if /i "%confirm%"=="s" (
    echo.
    echo ♻️ Reprocessando fotos com falha...
    python scripts/auto_process.py --reprocess failed
    echo.
    echo ✅ Reprocessamento concluído!
    pause
) else (
    echo Operação cancelada.
    timeout /t 2 >nul
)
goto menu

:logs
echo.
echo 📋 Visualizando logs de processamento...
if exist "data\processing_logs.log" (
    type "data\processing_logs.log" | more
) else (
    echo ❌ Nenhum log encontrado ainda.
    echo 💡 Execute o processamento automático primeiro!
)
echo.
pause
goto menu

:public_link
echo.
echo 🌐 ═══════════════════════════════════════════════════════
echo     🌍 LINK PÚBLICO DO BAZAR DA THAÍS
echo ═══════════════════════════════════════════════════════
echo.
echo 📱 Dashboard Online 24/7:
echo 👉 https://bazar-da-thais.streamlit.app/
echo.
echo 🔗 Repositório GitHub:  
echo 👉 https://github.com/gugakramer-boop/bazar-da-thais
echo.
echo 💡 Compartilhe esses links com quem quiser ver o bazar!
echo    O dashboard atualiza automaticamente quando você
echo    adiciona novos produtos.
echo.
pause
goto menu

:exit
echo.
echo 👋 Obrigado por usar o Bazar da Thaís!
echo 💄 Vendas incríveis para a Thaís! 🎉
timeout /t 2 >nul
exit