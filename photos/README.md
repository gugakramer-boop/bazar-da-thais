# 📸 Pasta de Fotos - Processamento Automático

## 🎯 **Como Funciona**

Esta pasta é o **coração do sistema automático!** 

### 📁 **to_process/**
**👆 ARRASTE SUAS FOTOS AQUI!**
- ✅ Suporta: JPG, JPEG, PNG, WEBP, HEIC, BMP, TIFF
- 🤖 Processamento automático a cada 30 segundos
- 📊 Produtos aparecem automaticamente no dashboard

### 📁 **processed/**
- ✅ Fotos processadas com sucesso
- 🎉 Produtos já adicionados ao dashboard
- 📂 Arquivo histórico para referência

### 📁 **failed/**  
- ❌ Fotos que não puderam ser processadas
- 🔍 Baixa confiança na identificação
- 🛠️ Reprocesse manualmente no VS Code se necessário

---

## 🚀 **Quick Start**

1. **Arraste fotos** para `to_process/` 
2. **Execute** `scripts/start.bat` (opção 4 - Sistema Completo)
3. **Aguarde** até 30 segundos  
4. **Veja produtos** em http://localhost:8501

## 📱 **Formatos Suportados**

✅ `.jpg` `.jpeg` `.png` `.webp` `.heic` `.bmp` `.tiff`  
❌ Evite: vídeos, GIFs, arquivos corrompidos

## 🎯 **Dicas para Melhores Resultados**

- 📷 **Fotos nítidas** com boa iluminação
- 🔍 **Rótulos visíveis** (marca, produto, cor) 
- 📏 **Enquadramento** focado no produto
- 🌟 **Múltiplos ângulos** podem ajudar no reconhecimento

## 🔧 **Troubleshooting**

**Foto não processou?**
- Verifique se está nos formatos suportados
- Tente renomear o arquivo (sem caracteres especiais)
- Processe manualmente no VS Code Agent

**Sistema não está monitorando?**
- Verifique se `scripts/auto_process.py` está rodando
- Use `scripts/start.bat` opção 2 ou 4

---

**📞 Precisa de ajuda? Use o agente manual no VS Code!**