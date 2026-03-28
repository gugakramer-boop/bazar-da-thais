# 💄 Bazar da Thaís — Dashboard de Precificação

Sistema de precificação inteligente para revenda de maquiagens, criado para a maquiadora Thaís.

## 🌟 Funcionalidades

- **📸 Identificação de Produtos**: Análise automática de fotos de maquiagem
- **🔍 Pesquisa de Mercado**: Consulta em 14+ lojas brasileiras especializadas  
- **💰 Precificação Inteligente**: Algoritmo com ajustes por marca, tipo e condição do produto
- **📊 Dashboard em Tempo Real**: Interface web com atualizações automáticas
- **📱 Mobile-Friendly**: Acesso otimizado para celular e tablet

## 🚀 Acesso

### 🌐 **Dashboard Público**
👉 **[Acesse o Dashboard Online](https://share.streamlit.io)** (após deploy)

### 💻 **Uso Local**
```bash
# Opção 1: Duplo clique
iniciar_dashboard.bat

# Opção 2: Terminal  
streamlit run app_bazar.py --server.port 8501
```
🌐 **Dashboard local:** http://localhost:8501

## 📈 Como Usar

### 1. **Adicionar Produtos**

Use o agente no VS Code:
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