# 📚 Documentação - Bazar da Thaís

## 🚀 **Quick Start Guide**

### ⚡ **Setup Rápido (2 minutos)**
1. Execute `scripts/start.bat`
2. Escolha opção **4** (Sistema Completo)
3. Arraste fotos para `photos/to_process/`  
4. Acesse http://localhost:8501

### 🌐 **Dashboard Público**
👉 **[bazar-da-thais.streamlit.app](https://bazar-da-thais.streamlit.app)**

---

## 📁 **Estrutura de Pastas**

```
bazar-da-thais/
├── 📸 photos/               # Drop zone para fotos
│   ├── to_process/         # Arraste fotos aqui!  
│   ├── processed/          # Fotos processadas
│   └── failed/             # Fotos com erro
├── 🤖 agents/              # VS Code AI agents
│   ├── auto-processing.md  # Processamento automático
│   └── manual-processing.md # Processamento manual
├── 📊 src/                 # Dashboard e aplicação
│   └── app.py             # Dashboard principal
├── 💾 data/                # Base de dados
│   ├── produtos_bazar.json # Catálogo de produtos
│   └── processing_logs.json # Logs do sistema
├── 📄 docs/                # Documentação
├── 🛠️ scripts/             # Scripts utilitários
│   ├── start.bat          # Menu principal
│   ├── auto_process.py    # Processamento automático
│   └── start_dashboard.bat # Só dashboard
└── 📋 diversos arquivos de configuração
```

---

## 🎯 **Workflows Principais**

### 🤖 **Automático (Recomendado)**
```
Foto → to_process/ → AI Detection → Market Research → 
Price Calculation → Database → Dashboard (30s)
```

### 📱 **Manual (VS Code)**
```  
Foto → VS Code Agent → Validação Humana → 
Aprovação → Database → Dashboard (imediato)
```

### 🔄 **Híbrido**
```
Auto para volume + Manual para casos especiais
```

---

## 🎨 **User Interfaces**

### 📊 **Dashboard Web** (`src/app.py`)
- Catálogo completo em tempo real
- KPIs automáticos
- Filtros por marca/tipo
- Mobile-friendly
- Auto-refresh 5s

### 🤖 **VS Code Agents**
- **Auto**: monitora pasta automaticamente
- **Manual**: processamento individual
- Integração com GitHub Copilot

### 💻 **Menu Windows** (`scripts/start.bat`) 
- Interface amigável
- Inicia todos os componentes  
- Logs e troubleshooting

---

## 🔧 **Configurações Avançadas**

### ⚙️ **Auto Processing**
```python
# scripts/auto_process.py
interval = 30          # segundos entre verificações
confidence_threshold = 70  # % mínimo para processar
max_logs = 1000       # máximo de logs mantidos
```

### 🌐 **Dashboard**
```python
# src/app.py  
cache_ttl = 5         # segundos cache streamlit
port = 8501          # porta local
auto_refresh = 5     # segundos entre updates
```

### 🤖 **AI Detection**
```python
# Formatos suportados
extensions = ['.jpg', '.jpeg', '.png', '.webp', '.heic', '.bmp', '.tiff']

# Confidence levels
high_confidence = 90+    # Produtos premium
medium_confidence = 70+  # Auto-processo
low_confidence = <70     # Vai para failed/
```

---

## 🎯 **Algoritmo de Preços**

### 📐 **Fórmulas Base**
```
Nunca usado  = Menor Preço × 0,75     (~25% desc.)
25% usado    = Mediana × 0,60         (~40% desc.)  
50% usado    = Mediana × 0,45         (~55% desc.)
75% usado    = Mediana × 0,30         (~70% desc.)
```

### 🏷️ **Ajustes por Marca**
- **Ultra Premium**: -5% (mantém mais valor)
- **Premium**: -3%  
- **Mid-market**: 0%
- **Nacional**: 0%
- **Drugstore**: +5% (desconto maior)

### 🧴 **Ajustes por Risco Sanitário**
- **Alto Risco**: -18% (batom, máscara, gloss)
- **Médio Risco**: -5% (base, pó, blush)  
- **Baixo Risco**: 0% (sombra, iluminador)

---

## 🛠️ **Troubleshooting**

### ❌ **Dashboard não abre**
```bash
# Verificar se Streamlit está instalado
pip install streamlit plotly pandas

# Testar manualmente  
cd src && streamlit run app.py
```

### 🤖 **Auto processing não funciona**
```bash
# Verificar Python
python --version

# Executar manualmente
python scripts/auto_process.py
```

### 📸 **Fotos não processam**
- Verificar formato (JPG, PNG, etc.)
- Renomear arquivo (sem caracteres especiais)
- Usar agente manual para debug

### 💾 **Dados não salvam**
- Verificar permissões da pasta `data/`
- Checar espaço em disco
- Verificar encoding UTF-8

---

## 🚀 **Performance Tips**

### ⚡ **Para Processamento Rápido**
- Use fotos de até 5MB
- Resolução máxima: 1920x1080
- Lote de até 20 fotos por vez

### 📊 **Para Dashboard Rápido**  
- Mantenha até 500 produtos ativos
- Archive produtos vendidos
- Use filtros para listas grandes

### 🔄 **Para Sync em Tempo Real**
- Dashboard atualiza a cada 5s automaticamente
- Auto processor verifica a cada 30s  
- Sem necessidade de refresh manual

---

## 📞 **Suporte**

### 🤖 **Agentes VS Code**
- **@auto-processing**: para automação
- **@manual-processing**: para casos específicos

### 📋 **Logs**
- `data/processing_logs.log`: erros detalhados  
- `data/processing_logs.json`: histórico estruturado

### 🔧 **Scripts Úteis**
- `scripts/start.bat`: menu principal
- `scripts/view_logs.py`: visualizar logs  
- `scripts/backup_data.py`: backup manual

---

**✨ Sistema completo para acelerar vendas do bazar! 🎉**