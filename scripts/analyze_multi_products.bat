@echo off
title 🔍 Análise Multi-Produtos - Bazar da Thaís
cls

echo.
echo  ╔═══════════════════════════════════════════════════════╗
echo  ║            🔍 ANÁLISE MULTI-PRODUTOS                 ║  
echo  ║         Buscar produtos adicionais em fotos          ║
echo  ╚═══════════════════════════════════════════════════════╝
echo.

echo 💡 Este script irá analisar todas as fotos já processadas
echo    em busca de produtos adicionais que podem ter sido perdidos.
echo.
echo 🎯 BENEFÍCIOS:
echo    ✅ Encontra produtos que foram perdidos no processamento inicial
echo    ✅ Detecta múltiplos produtos em fotos de coleção/flat lay  
echo    ✅ Adiciona automaticamente novos produtos ao dashboard
echo    ✅ Mantém histórico completo de origem das fotos
echo.
echo ⚠️  IMPORTANTE:
echo    • O processo pode levar alguns minutos  
echo    • Fotos serão re-analisadas mas não reprocessadas
echo    • Apenas produtos novos serão adicionados
echo.

set /p confirm=🚀 Iniciar análise multi-produtos? (s/n): 

if /i "%confirm%"=="s" (
    echo.
    echo 🔄 Iniciando análise...
    echo ═══════════════════════════════════════════════════
    
    python scripts/auto_process.py --analyze-existing
    
    echo.
    echo ═══════════════════════════════════════════════════
    echo ✅ Análise concluída!
    echo.
    echo 📊 Próximos passos:
    echo    1. Confira o dashboard: http://localhost:8501
    echo    2. Novos produtos aparecerão automaticamente
    echo    3. Verifique os logs para detalhes da análise
    echo.
    
) else (
    echo.
    echo ❌ Análise cancelada pelo usuário.
    echo.
)

echo Pressione qualquer tecla para continuar...
pause >nul