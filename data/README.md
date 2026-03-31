# 📊 Data - Base de Dados do Bazar

## 📁 **Arquivos Principais**

### `produtos_bazar.json`
**🎯 Base de dados principal**
- Todos os produtos do bazar
- Preços calculados para 4 condições  
- Dados de pesquisa de mercado
- Atualizado automaticamente

### `processing_logs.json`
**📝 Logs de processamento**
- Histórico de fotos processadas
- Status: success, failed, low_confidence
- Timestamps e dados de debug
- Últimas 1000 operações

### `processing_logs.log`
**🔍 Logs detalhados**
- Log textual detalhado do sistema
- Erros e informações técnicas
- Usado para troubleshooting

---

## 🔧 **Formato do Produto**

```json
{
  "id": 1,
  "marca": "Fenty Beauty",
  "produto": "Pro Filt'r Foundation", 
  "cor_tom": "350",
  "tipo": "Base",
  "volume": "32ml",
  "categoria_risco": "medium_risk",
  "preco_min": 165.00,
  "preco_max": 189.00, 
  "preco_medio": 178.00,
  "mediana": 175.00,
  "fontes": 8,
  "data_pesquisa": "2026-03-31",
  "ajuste_categoria": "premium",
  "nunca_usado": 123.75,
  "usado_25": 105.00,
  "usado_50": 78.75,
  "usado_75": 52.50,
  "observacoes": "Processado automaticamente",
  "auto_processed": true,
  "processed_timestamp": "2026-03-31T10:30:00"
}
```

## 🎯 **Campos Importantes**

- **`id`**: Identificador único
- **`nunca_usado` → `usado_75`**: 4 faixas de preço
- **`categoria_risco`**: high_risk, medium_risk, low_risk  
- **`ajuste_categoria`**: ultra_premium, premium, mid, nacional, drugstore
- **`auto_processed`**: true/false para identificar origem

## 🔒 **Backup Automático**

O sistema mantém backups automáticos:
- A cada 10 produtos adicionados
- Antes de alterações importantes  
- Localização: `data/backups/`

## ⚠️ **IMPORTANTE**

- **NÃO edite** `produtos_bazar.json` manualmente
- Use sempre os agentes do VS Code
- Para correções, use agente manual
- Backups ficam em `data/backups/`

---

**🔧 Para manutenção, use sempre os scripts em `scripts/`**