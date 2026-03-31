#!/usr/bin/env python3
"""
Ajuste de preços para marcas importadas não vendidas no Brasil.

Lógica:
- Produtos vendidos oficialmente no BR têm markup médio de ~70-90% sobre preço US
  (Fenty US$42 → BR R$279 = ~33% sobre câmbio; ABH US$29→R$279 = ~92%;
   Dior US$52→R$435 = ~67%). Considerando câmbio ~R$5, markup real ~60-90%.
- Produtos SÓ via importação são MAIS CAROS:
  - Imposto importação 60% + ICMS 17-25%
  - Frete internacional
  - Margem do importador
  - Escassez / dificuldade de acesso
- Estimativa conservadora: preço de importação = preço US × 5 (câmbio) × 1.8-2.2 (markup total)
  Ou seja, ~80-120% sobre o preço convertido

Ajuste: multiplicar preços atuais dos importados por 1.15 (15% extra pela escassez/dificuldade)
"""
import json
from datetime import datetime

DATA_FILE = "data/produtos_bazar.json"

with open(DATA_FILE, 'r', encoding='utf-8-sig') as f:
    produtos = json.load(f)

def calc_prices(min_price, median, brand_adj, risk_adj):
    total = brand_adj + risk_adj
    return {
        "nunca_usado": round(max(min_price * 0.75 * (1 + total), 5.0), 2),
        "usado_25": round(max(median * 0.60 * (1 + total), 5.0), 2),
        "usado_50": round(max(median * 0.45 * (1 + total), 5.0), 2),
        "usado_75": round(max(median * 0.30 * (1 + total), 5.0), 2),
    }

today = datetime.now().strftime("%Y-%m-%d")

# IDs de produtos que NÃO são vendidos oficialmente no Brasil
# (marcados com ⚠️ nas observações)
import_only_ids = {
    4,   # Pat McGrath (ultra premium)
    6,   # Danessa Myricks Waterproof Cream
    7,   # Danessa Myricks Lip Cream
    8,   # ColourPop Stone Cold Fox
    9,   # Tarte Maracuja Juicy
    10,  # Tarte Tartelette Starlight
    12,  # Tarte Juicy Clay
    13,  # Jason Wu Flora 9
    14,  # Danessa Myricks ColorFix Neons
    16,  # ILIA Color Haze
    17,  # Outdoor Girl Beach
    18,  # Outdoor Girl Pro Pigment
    19,  # MUFE HD Skin #1
    20,  # MUFE HD Skin #2
    22,  # By Mario SurrealSkin
    25,  # Danessa Myricks Yummy Skin
    26,  # MUFE Step 1 Primer
}

# Premium de escassez: 15% extra porque não tem acesso fácil no Brasil
SCARCITY_PREMIUM = 1.15

# Brand-specific adjustments & risk from original data
brand_risk = {
    4:  (-0.05, 0.0),    # Pat McGrath ultra premium
    6:  (-0.03, 0.0),    # Danessa Myricks
    7:  (-0.03, -0.18),  # Danessa Myricks lip
    8:  (0.0, 0.0),      # ColourPop
    9:  (-0.03, 0.0),    # Tarte
    10: (-0.03, 0.0),    # Tarte
    12: (-0.03, 0.0),    # Tarte
    13: (0.0, 0.0),      # Jason Wu
    14: (-0.03, -0.05),  # Danessa Myricks
    16: (-0.03, -0.05),  # ILIA
    17: (0.05, 0.0),     # Outdoor Girl drugstore
    18: (0.05, 0.0),     # Outdoor Girl drugstore
    19: (-0.03, -0.05),  # MUFE
    20: (-0.03, -0.05),  # MUFE
    22: (-0.03, -0.05),  # By Mario
    25: (-0.03, -0.05),  # Danessa Myricks
    26: (-0.03, -0.05),  # MUFE
}

for p in produtos:
    pid = p['id']
    if pid not in import_only_ids:
        continue
    
    old_min = p['preco_min']
    old_med = p['mediana']
    
    # Apply scarcity premium
    p['preco_min'] = round(p['preco_min'] * SCARCITY_PREMIUM, 2)
    p['preco_max'] = round(p['preco_max'] * SCARCITY_PREMIUM, 2)
    p['preco_medio'] = round(p['preco_medio'] * SCARCITY_PREMIUM, 2)
    p['mediana'] = round(p['mediana'] * SCARCITY_PREMIUM, 2)
    p['data_pesquisa'] = today
    
    # Add scarcity note
    p['observacoes'] = p['observacoes'].replace(
        "Data: 31/03/2026",
        "+15% prêmio escassez (sem acesso fácil BR) | Data: 31/03/2026"
    )
    
    ba, ra = brand_risk[pid]
    prices = calc_prices(p['preco_min'], p['mediana'], ba, ra)
    p['nunca_usado'] = prices['nunca_usado']
    p['usado_25'] = prices['usado_25']
    p['usado_50'] = prices['usado_50']
    p['usado_75'] = prices['usado_75']
    
    print(f"📈 ID {pid:2d} | {p['marca']:30s} | Med R${old_med:6.0f} → R${p['mediana']:6.0f} (+15%) | Bazar: R${prices['nunca_usado']:6.0f} ~ R${prices['usado_75']:6.0f}")

# Save
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(produtos, f, indent=2, ensure_ascii=False)

with open("produtos_bazar.json", 'w', encoding='utf-8') as f:
    json.dump(produtos, f, indent=2, ensure_ascii=False)

print(f"\n✅ {len(import_only_ids)} produtos importados ajustados com +15% prêmio de escassez")
print("💡 Justificativa: marcas sem distribuição oficial no Brasil custam mais pela dificuldade de acesso")
