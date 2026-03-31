# 💄 Bazar da Thaís — Sistema Completo de Precificação

Sistema inteligente de precificação para revenda de maquiagens, com processamento automático de fotos.

## 🌟 Funcionalidades

- **📸 Drag & Drop Processing**: Arraste fotos e processamento automático  
- **🎯 Multi-Product Detection**: Detecta TODOS os produtos em cada foto
- **🤖 AI Vision Enhanced**: Identifica marca, produto, cor e condição
- **🔍 Market Research**: Consulta automática em 14+ lojas brasileiras
- **💰 Smart Pricing**: 4 faixas de preço com ajustes por marca/risco
- **📊 Real-time Dashboard**: Interface web com atualizações automáticas
- **📱 Mobile-Ready**: Acesso otimizado para todos os dispositivos

## 🚀 Quick Start

### 🌐 **Dashboard Público**
👉 **[Acesse Online](https://bazar-da-thais.streamlit.app)** (24/7 disponível)

### 💻 **Modo Local**
```bash
# Iniciar dashboard local
./scripts/start.bat

# Ou manual:
streamlit run src/app.py --server.port 8501
```
🌐 **URL local:** http://localhost:8501

## 📁 Estrutura do Projeto

```
bazar-da-thais/
├── 📸 photos/              # Drop fotos aqui!
│   ├── to_process/         # Fotos para analisar
│   ├── processed/          # Fotos já analisadas
│   └── failed/             # Fotos com erro
├── 🤖 agents/              # VS Code AI agents
├── 📊 src/                 # Dashboard e scripts
├── 💾 data/                # Base de dados
├── 📄 docs/                # Documentação
└── 🛠️ scripts/             # Utilitários
```

## 🎯 Como Usar

### 1. **📸 Método Automático (Recomendado)**

**Arraste fotos para:** `photos/to_process/`
- ✅ Processamento automático a cada 30 segundos
- ✅ Identificação de marca, produto e cor
- ✅ Pesquisa de preços em tempo real
- ✅ Adição automática ao dashboard

### 2. **🤖 Método Manual (VS Code Agent)**

Use o agente do VS Code para análise individual:
- `@auto-processing` - Automatic photo processing 
- `@manual-processing` - Individual photo analysis

## 🏷️ Metodologia de Preços

Sistema aplica descontos baseados na condição:
- **Nunca usado**: 25% abaixo do menor preço de mercado
- **25% usado**: 40% abaixo da mediana
- **50% usado**: 55% abaixo da mediana  
- **75% usado**: 70% abaixo da mediana

### Ajustes Automáticos
- **Marca Premium**: -3% a -8% (mantém mais valor)
- **Alto Risco Sanitário**: -15% a -20% (batom, máscara)
- **Produto Lacrado**: +5% (garantia de integridade)
- **Edição Limitada**: +5% a +10% (escassez)

## 🛠️ Tecnologia

- **Backend**: Python + Streamlit  
- **AI Agents**: VS Code Copilot (2 agents especializados)
- **Data**: JSON com encoding UTF-8-sig
- **Vision AI**: Identificação automática por foto
- **Market Research**: 14+ lojas brasileiras
- **Deploy**: Streamlit Community Cloud

## 📊 Dashboard KPIs

- Total de produtos catalogados
- Valor total do estoque  
- Ticket médio por condição
- Distribuição por marca
- Performance de vendas em tempo real

## 📁 Estrutura Organizada

```
📁 bazar-da-thais/
├── 📸 photos/to_process/     # Drop photos here!
├── 🤖 agents/               # VS Code AI agents  
├── 📊 src/app.py           # Dashboard
├── 💾 data/                # Database & logs
├── 📚 docs/                # Documentation  
└── 🛠️ scripts/start.bat    # Main launcher
```

## 🚀 Início Rápido

### 🎮 **Método Completo**
```bash
1. Execute: scripts/start.bat  
2. Opção: 4 (Sistema Completo)
3. Arraste fotos: photos/to_process/  
4. Acesse: http://localhost:8501
```
- Digite `@bazar-maquiagem` no chat
- Envie foto da maquiagem
- Agente pesquisa preços automaticamente
- Agente pergunta se deve adicionar no dashboard

### 3. **Visualizar Resultados**

O dashboard atualiza **automaticamente** a cada 5 segundos mostrando:
- 📊 KPIs executivos (total valor, economia, ticket médio)
- 📋 Catálogo completo com preços para cada condição de uso
- 🎯 Estratégias de venda otimizadas
- 📈 Analytics por tipo de produto

## 📁 Estrutura de Arquivos

```
Personal/
├── 📊 app_bazar.py              # Dashboard Streamlit principal
├── 💾 produtos_bazar.json       # Base de dados dos produtos
├── 🤖 .github/agents/           # Agente de precificação
│   └── bazar-maquiagem.agent.md
├── ⚡ iniciar_dashboard.bat     # Script para iniciar
├── 🧪 testar_adicionar_produto.py  # Teste manual
└── 📖 README.md                 # Este arquivo
```

## 🔧 Metodologia de Preços

### Base de Cálculo
- **🟢 Nunca Usado** = Menor Preço × 0,75 × (1 + Ajuste)
- **🟡 25% Usado** = Mediana × 0,60 (~40% desconto)
- **🟠 50% Usado** = Mediana × 0,45 (~55% desconto)  
- **🔴 75% Usado** = Mediana × 0,30 (~70% desconto)

### Ajustes Automáticos
| Categoria | Ajuste | Motivo |
|-----------|---------|---------|
| **Ultra Premium** (Dior, Charlotte) | -5% | Segura mais valor |
| **Premium** (MAC, NARS, Tarte) | -3% | Marca reconhecida |
| **Alto Risco Sanitário** (batom, máscara) | -15% | Higiene crítica |
| **Drugstore** (< R$50) | +13% | Margem mínima |

## 💡 Vantagens vs. Excel

| Aspecto | Excel | Dashboard Live |
|---------|-------|---------------|
| **Atualização** | Manual, fecha/abre | ✅ Automática (5s) |
| **Visualização** | Básica | ✅ Gráficos e KPIs |
| **Acessibilidade** | Só com Office | ✅ Qualquer browser |
| **Performance** | Lenta com muitos dados | ✅ Rápida |
| **Analytics** | Limitado | ✅ Completo |

## 🎯 Próximos Passos

1. **✅ Implementado**: Sistema base funcionando
2. **📱 Mobile**: Versão responsiva para celular
3. **🔗 Compartilhamento**: Link público para clientes
4. **📷 Upload**: Drag&drop de fotos direto no dashboard
5. **💾 Backup**: Exportar/importar dados
6. **🏷️ QR Codes**: Geração automática de etiquetas

## 🆘 Troubleshooting

**Dashboard não carrega?**
```bash
pip install streamlit plotly
streamlit run app_bazar.py
```

**Agente não encontra produtos?**
- Verifique se `produtos_bazar.json` existe
- Confirme permissões de escrita na pasta

**Preços não calculam?**
- Verifique se todos campos obrigatórios estão preenchidos
- Confirme que `preco_min` e `mediana` são números válidos

---

*🌸 Sistema desenvolvido para otimizar vendas do Bazar da Thaís*