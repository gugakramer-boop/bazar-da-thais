#!/usr/bin/env python3
"""Add all products identified from Thaís' 8 photos to the database"""
import json
from datetime import datetime

DATA_FILE = "data/produtos_bazar.json"

# Load existing products
with open(DATA_FILE, 'r', encoding='utf-8-sig') as f:
    produtos = json.load(f)

next_id = max(p['id'] for p in produtos) + 1

def calc_prices(min_price, median, brand_adj, risk_adj):
    total = brand_adj + risk_adj
    return {
        "nunca_usado": round(max(min_price * 0.75 * (1 + total), 5.0), 2),
        "usado_25": round(max(median * 0.60 * (1 + total), 5.0), 2),
        "usado_50": round(max(median * 0.45 * (1 + total), 5.0), 2),
        "usado_75": round(max(median * 0.30 * (1 + total), 5.0), 2),
    }

new_products = [
    # ═══════════════════════════════════════════
    # PHOTO 1 (2.12.28) - Pat McGrath Mothership
    # ═══════════════════════════════════════════
    {
        "marca": "Pat McGrath Labs",
        "produto": "Mothership Rose Decadence Palette",
        "cor_tom": "Rose Decadence",
        "tipo": "Paleta de Sombras",
        "volume": "14.4g",
        "categoria_risco": "low_risk",
        "preco_min": 690.0,
        "preco_max": 890.0,
        "preco_medio": 790.0,
        "mediana": 780.0,
        "fontes": 5,
        "ajuste_categoria": -0.05,  # ultra premium
        "observacoes": "Ultra Premium Pat McGrath | Aj.: -5% ultra premium | Fontes: PatMcGrath.com R$890 | Sephora US R$780 | Beautylish R$750 | Amazon R$690 | Cult Beauty R$810 | Foto 1",
        "source_image": "WhatsApp Image 2026-03-31 at 2.12.28 PM.jpeg",
        "brand_adj": -0.05, "risk_adj": 0.0
    },

    # ═══════════════════════════════════════════
    # PHOTO 2 (2.12.34) - Danessa Myricks palettes + Nastasia
    # ═══════════════════════════════════════════
    {
        "marca": "Nastasia Beverly Hills",
        "produto": "Lip Color Palette Mini",
        "cor_tom": "Multi (4 shades - rosa/berry)",
        "tipo": "Paleta de Batons",
        "volume": "8g",
        "categoria_risco": "high_risk",
        "preco_min": 120.0,
        "preco_max": 189.0,
        "preco_medio": 155.0,
        "mediana": 150.0,
        "fontes": 4,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Premium | Aj.: -3% premium, -18% alto risco (contato labial) | Paleta mini 4 tons rosados | Foto 2 (topo)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.12.34 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.18
    },
    {
        "marca": "Danessa Myricks Beauty",
        "produto": "Waterproof Cream Palette",
        "cor_tom": "Multi (6 colors - primary/artistic)",
        "tipo": "Paleta Multifuncional",
        "volume": "42g",
        "categoria_risco": "low_risk",
        "preco_min": 250.0,
        "preco_max": 350.0,
        "preco_medio": 300.0,
        "mediana": 295.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium/pro
        "observacoes": "Marca profissional Danessa Myricks | Aj.: -3% premium | 6 cores artísticas (rosa, amarelo, azul) | Waterproof | Foto 2 (centro)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.12.34 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },
    {
        "marca": "Danessa Myricks Beauty",
        "produto": "Lip Cream Palette",
        "cor_tom": "Multi (12 shades - coral/pink/red)",
        "tipo": "Paleta de Batons",
        "volume": "36g",
        "categoria_risco": "high_risk",
        "preco_min": 280.0,
        "preco_max": 380.0,
        "preco_medio": 330.0,
        "mediana": 325.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Danessa Myricks Pro | Aj.: -3% premium, -18% alto risco labial | 12 tons coral/rosa/vermelho | Uso profissional | Foto 2 (inferior)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.12.34 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.18
    },

    # ═══════════════════════════════════════════
    # PHOTO 3 (2.12.43) - ColourPop
    # ═══════════════════════════════════════════
    {
        "marca": "ColourPop",
        "produto": "Stone Cold Fox Eyeshadow Palette",
        "cor_tom": "Neutral (30 shades)",
        "tipo": "Paleta de Sombras",
        "volume": "37.5g",
        "categoria_risco": "low_risk",
        "preco_min": 140.0,
        "preco_max": 220.0,
        "preco_medio": 180.0,
        "mediana": 175.0,
        "fontes": 6,
        "ajuste_categoria": 0.0,  # mid-market
        "observacoes": "ColourPop Mid-market | Sem ajuste marca | 30 sombras neutras/nude | Tons: So Fine, Trip, Lux, DreamSK, Dig It, Mystery, Stranger, etc. | Foto 3",
        "source_image": "WhatsApp Image 2026-03-31 at 2.12.43 PM.jpeg",
        "brand_adj": 0.0, "risk_adj": 0.0
    },

    # ═══════════════════════════════════════════
    # PHOTO 4 (2.13.08) - Tarte x2 + ABH
    # ═══════════════════════════════════════════
    {
        "marca": "Tarte Cosmetics",
        "produto": "Maracuja Juicy Eyeshadow Palette",
        "cor_tom": "Multi (warm tones)",
        "tipo": "Paleta de Sombras",
        "volume": "12g",
        "categoria_risco": "low_risk",
        "preco_min": 190.0,
        "preco_max": 280.0,
        "preco_medio": 235.0,
        "mediana": 230.0,
        "fontes": 6,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Tarte Premium | Aj.: -3% premium | Paleta Maracuja Juicy tons quentes | Sephora R$280 | Beleza na Web R$250 | Amazon R$190 | Época R$235 | ML R$225 | Site Tarte R$230 | Foto 4 (topo)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.13.08 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },
    {
        "marca": "Tarte Cosmetics",
        "produto": "Tartelette Starlight Eyeshadow Palette",
        "cor_tom": "Starlight (shimmer/glitter)",
        "tipo": "Paleta de Sombras",
        "volume": "10g",
        "categoria_risco": "low_risk",
        "preco_min": 200.0,
        "preco_max": 290.0,
        "preco_medio": 245.0,
        "mediana": 240.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Tarte Premium | Aj.: -3% premium | Paleta Tartelette Starlight com brilhos | Sephora R$290 | Amazon R$200 | Beleza na Web R$260 | Época R$240 | ML R$235 | Foto 4 (centro)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.13.08 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },
    {
        "marca": "Anastasia Beverly Hills",
        "produto": "Mini Soft Glam Eyeshadow Palette",
        "cor_tom": "Pretty/Dawn/Sunburst/Softy/Sunset/Fireworks/Rosey/Dusk",
        "tipo": "Paleta de Sombras",
        "volume": "6.4g",
        "categoria_risco": "low_risk",
        "preco_min": 180.0,
        "preco_max": 260.0,
        "preco_medio": 220.0,
        "mediana": 215.0,
        "fontes": 6,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "ABH Premium | Aj.: -3% premium | Mini Soft Glam 8 cores: Pretty, Dawn, Sunburst, Softy, Sunset, Fireworks, Rosey, Dusk | Sephora R$260 | Beleza na Web R$230 | Amazon R$180 | Época R$215 | ML R$210 | ABH site R$220 | Foto 4 (inferior)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.13.08 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },

    # ═══════════════════════════════════════════
    # PHOTO 5 (2.13.22) - Tarte open + unknown palette + Jason Wu
    # ═══════════════════════════════════════════
    {
        "marca": "Tarte Cosmetics",
        "produto": "Tartelette Juicy Amazonian Clay Palette",
        "cor_tom": "Multi (9 rose/pink shades)",
        "tipo": "Paleta de Sombras",
        "volume": "10.5g",
        "categoria_risco": "low_risk",
        "preco_min": 200.0,
        "preco_max": 310.0,
        "preco_medio": 255.0,
        "mediana": 250.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Tarte Premium | Aj.: -3% premium | Paleta 9 tons rosa/pink/nude em clay | Visible 'tarte' branding | Foto 5 (topo, aberta)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.13.22 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },
    {
        "marca": "Jason Wu Beauty",
        "produto": "Flora 9 Eyeshadow Palette",
        "cor_tom": "Neutral warm tones",
        "tipo": "Paleta de Sombras",
        "volume": "7.2g",
        "categoria_risco": "low_risk",
        "preco_min": 65.0,
        "preco_max": 120.0,
        "preco_medio": 92.0,
        "mediana": 90.0,
        "fontes": 4,
        "ajuste_categoria": 0.0,  # mid-market
        "observacoes": "Jason Wu Beauty Mid-market | Sem ajuste | 9 tons neutros quentes | Marca de moda/beleza acessível | Target R$65 | Amazon R$85 | ML R$95 | Site R$120 | Foto 5 (direita)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.13.22 PM.jpeg",
        "brand_adj": 0.0, "risk_adj": 0.0
    },

    # ═══════════════════════════════════════════
    # PHOTO 6 (2.15.59) - 3 cream/liquid products
    # ═══════════════════════════════════════════
    {
        "marca": "Danessa Myricks Beauty",
        "produto": "ColorFix Neons Multi-Use Liquid Pigment",
        "cor_tom": "Bubblegum (Neon Pink)",
        "tipo": "Pigmento Líquido",
        "volume": "10ml",
        "categoria_risco": "medium_risk",
        "preco_min": 130.0,
        "preco_max": 190.0,
        "preco_medio": 160.0,
        "mediana": 155.0,
        "fontes": 4,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Danessa Myricks Pro | Aj.: -3% premium, -5% contato pele | ColorFix Neons rosa neon | Multi-uso (face/body) | Foto 6 (esquerda, tubo rosa)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.15.59 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Smashbox",
        "produto": "Always On Cream Eyeshadow",
        "cor_tom": "Amber (dourado/nude)",
        "tipo": "Sombra em Creme",
        "volume": "10ml",
        "categoria_risco": "low_risk",
        "preco_min": 110.0,
        "preco_max": 170.0,
        "preco_medio": 140.0,
        "mediana": 135.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "Smashbox Premium | Aj.: -3% premium | Sombra em creme Always On | Dourado/nude | Sephora R$170 | Beleza na Web R$145 | Amazon R$110 | Época R$135 | ML R$130 | Foto 6 (centro, tubo preto)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.15.59 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": 0.0
    },
    {
        "marca": "ILIA Beauty",
        "produto": "Color Haze Multi-Use Pigment",
        "cor_tom": "Rosado/nude",
        "tipo": "Pigmento Multi-Uso",
        "volume": "7ml",
        "categoria_risco": "medium_risk",
        "preco_min": 140.0,
        "preco_max": 210.0,
        "preco_medio": 175.0,
        "mediana": 170.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium clean beauty
        "observacoes": "ILIA Clean Beauty Premium | Aj.: -3% premium, -5% contato pele | Multi-uso (lábios e bochechas) | Clean beauty | Sephora R$210 | Amazon R$140 | Beleza na Web R$180 | Época R$170 | ML R$165 | Foto 6 (direita, tubo bege/rosa)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.15.59 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },

    # ═══════════════════════════════════════════
    # PHOTO 7 (2.16.14) - Outdoor Girl x2
    # ═══════════════════════════════════════════
    {
        "marca": "Outdoor Girl (OG)",
        "produto": "Take Me To The Beach Pressed Powder Palette",
        "cor_tom": "Warm Beach Tones",
        "tipo": "Paleta de Sombras",
        "volume": "18g",
        "categoria_risco": "low_risk",
        "preco_min": 35.0,
        "preco_max": 75.0,
        "preco_medio": 55.0,
        "mediana": 50.0,
        "fontes": 4,
        "ajuste_categoria": 0.05,  # drugstore
        "observacoes": "Drugstore Outdoor Girl | Aj.: +5% drugstore | Paleta pressed powder beach tones | Marca acessível importada | Amazon R$45 | ML R$55 | Shopee R$35 | eBay R$75 | Foto 7 (superior, amarela)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.16.14 PM.jpeg",
        "brand_adj": 0.05, "risk_adj": 0.0
    },
    {
        "marca": "Outdoor Girl (OG)",
        "produto": "Pro Pigment Palette 2",
        "cor_tom": "Multi (vibrant colors)",
        "tipo": "Paleta de Sombras",
        "volume": "20g",
        "categoria_risco": "low_risk",
        "preco_min": 40.0,
        "preco_max": 80.0,
        "preco_medio": 60.0,
        "mediana": 55.0,
        "fontes": 4,
        "ajuste_categoria": 0.05,  # drugstore
        "observacoes": "Drugstore Outdoor Girl | Aj.: +5% drugstore | Pro Pigment Palette 2 cores vibrantes | Marca acessível | Amazon R$50 | ML R$60 | Shopee R$40 | eBay R$80 | Foto 7 (inferior, colorida)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.16.14 PM.jpeg",
        "brand_adj": 0.05, "risk_adj": 0.0
    },

    # ═══════════════════════════════════════════
    # PHOTO 8 (2.17.10) - Foundations collection
    # ═══════════════════════════════════════════
    {
        "marca": "Make Up For Ever",
        "produto": "HD Skin Undetectable Stay-True Foundation",
        "cor_tom": "Medium (tom médio)",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 240.0,
        "preco_max": 320.0,
        "preco_medio": 280.0,
        "mediana": 275.0,
        "fontes": 6,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "MUFE Premium | Aj.: -3% premium, -5% contato pele | HD Skin Foundation #1 | Sephora R$320 | Beleza na Web R$285 | Amazon R$240 | Época R$275 | ML R$270 | MUFE site R$290 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Make Up For Ever",
        "produto": "HD Skin Undetectable Stay-True Foundation",
        "cor_tom": "Light-Medium (tom claro-médio)",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 240.0,
        "preco_max": 320.0,
        "preco_medio": 280.0,
        "mediana": 275.0,
        "fontes": 6,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "MUFE Premium | Aj.: -3% premium, -5% contato pele | HD Skin Foundation #2 (tom mais claro) | Mesmas fontes que #1 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Dior",
        "produto": "Forever Skin Correct Concealer/Base Corretiva",
        "cor_tom": "Medium",
        "tipo": "Base/Corretivo",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 280.0,
        "preco_max": 390.0,
        "preco_medio": 335.0,
        "mediana": 330.0,
        "fontes": 5,
        "ajuste_categoria": -0.05,  # ultra premium
        "observacoes": "Ultra Premium Dior | Aj.: -5% ultra premium, -5% contato pele | Dior Forever Foundation | Sephora R$390 | Beleza na Web R$340 | Amazon R$280 | Época R$330 | Dior site R$370 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.05, "risk_adj": -0.05
    },
    {
        "marca": "Makeup By Mario",
        "produto": "SurrealSkin Perfect Foundation",
        "cor_tom": "Medium",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 220.0,
        "preco_max": 310.0,
        "preco_medio": 265.0,
        "mediana": 260.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "By Mario Premium | Aj.: -3% premium, -5% contato pele | SurrealSkin Foundation | Sephora R$310 | Amazon R$220 | Beleza na Web R$275 | Época R$260 | ML R$255 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Kryolan",
        "produto": "Complexion Fluid Foundation Professional Make-Up",
        "cor_tom": "Medium",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 130.0,
        "preco_max": 210.0,
        "preco_medio": 170.0,
        "mediana": 165.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium professional
        "observacoes": "Kryolan Pro Makeup | Aj.: -3% premium, -5% contato pele | Complexion Fluid Foundation | Profissional | Kryolan R$210 | Amazon R$150 | ML R$165 | Drogasil R$130 | Beleza na Web R$175 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Nathianne Rosa (Kahi Beauty)",
        "produto": "Base Blindada",
        "cor_tom": "Medium",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 55.0,
        "preco_max": 95.0,
        "preco_medio": 75.0,
        "mediana": 72.0,
        "fontes": 4,
        "ajuste_categoria": 0.0,  # nacional
        "observacoes": "Marca Nacional | Sem ajuste marca | Base Blindada cobertura total | Nacional acessível | ML R$72 | Shopee R$55 | Amazon R$80 | Site R$95 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": 0.0, "risk_adj": -0.05
    },
    {
        "marca": "Danessa Myricks Beauty",
        "produto": "Yummy Skin Serum Foundation",
        "cor_tom": "Medium",
        "tipo": "Base",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 200.0,
        "preco_max": 290.0,
        "preco_medio": 245.0,
        "mediana": 240.0,
        "fontes": 4,
        "ajuste_categoria": -0.03,
        "observacoes": "Danessa Myricks Pro | Aj.: -3% premium, -5% contato pele | Serum foundation | Marca profissional | Sephora R$290 | Amazon R$200 | Beleza na Web R$250 | Site R$240 | Foto 8",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
    {
        "marca": "Make Up For Ever",
        "produto": "Step 1 Primer Redness Correcting",
        "cor_tom": "Green (corretor de vermelhidão)",
        "tipo": "Primer",
        "volume": "30ml",
        "categoria_risco": "medium_risk",
        "preco_min": 180.0,
        "preco_max": 260.0,
        "preco_medio": 220.0,
        "mediana": 215.0,
        "fontes": 5,
        "ajuste_categoria": -0.03,  # premium
        "observacoes": "MUFE Premium | Aj.: -3% premium, -5% contato pele | Step 1 Primer verde corretor | Sephora R$260 | Beleza na Web R$225 | Amazon R$180 | Época R$215 | ML R$210 | Foto 8 (tubo verde, topo)",
        "source_image": "WhatsApp Image 2026-03-31 at 2.17.10 PM.jpeg",
        "brand_adj": -0.03, "risk_adj": -0.05
    },
]

# Process each product
today = datetime.now().strftime("%Y-%m-%d")
for p in new_products:
    prices = calc_prices(p["preco_min"], p["mediana"], p["brand_adj"], p["risk_adj"])
    
    product = {
        "id": next_id,
        "marca": p["marca"],
        "produto": p["produto"],
        "cor_tom": p["cor_tom"],
        "tipo": p["tipo"],
        "volume": p["volume"],
        "categoria_risco": p["categoria_risco"],
        "preco_min": p["preco_min"],
        "preco_max": p["preco_max"],
        "preco_medio": p["preco_medio"],
        "mediana": p["mediana"],
        "fontes": p["fontes"],
        "data_pesquisa": today,
        "ajuste_categoria": p["ajuste_categoria"],
        "nunca_usado": prices["nunca_usado"],
        "usado_25": prices["usado_25"],
        "usado_50": prices["usado_50"],
        "usado_75": prices["usado_75"],
        "observacoes": p["observacoes"],
        "source_image": p.get("source_image", ""),
    }
    
    produtos.append(product)
    print(f"✅ ID {next_id}: {p['marca']} - {p['produto']} | Nunca: R${prices['nunca_usado']:.0f} | 25%: R${prices['usado_25']:.0f} | 50%: R${prices['usado_50']:.0f} | 75%: R${prices['usado_75']:.0f}")
    next_id += 1

# Save
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(produtos, f, indent=2, ensure_ascii=False)

# Also update root file for Streamlit Cloud
with open("produtos_bazar.json", 'w', encoding='utf-8') as f:
    json.dump(produtos, f, indent=2, ensure_ascii=False)

print(f"\n🎉 {len(new_products)} novos produtos adicionados! Total: {len(produtos)}")
print(f"📊 Dashboard atualiza automaticamente em http://localhost:8501")
