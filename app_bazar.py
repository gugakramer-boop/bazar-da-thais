import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os

# ══════════════════════════════════════════════════════
#  🌸 BAZAR DA THAÍS — Dashboard Live
# ══════════════════════════════════════════════════════

st.set_page_config(
    page_title="🌸 Bazar da Thaís",
    page_icon="💄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-title {
    font-size: 3rem;
    color: #1B2A4A;
    font-weight: bold;
    text-align: center;
    margin-bottom: 0.5rem;
}
.subtitle {
    text-align: center;
    color: #E8A5C8;
    font-style: italic;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}
.metric-card {
    background: linear-gradient(135deg, #E8F5E9 0%, #F3E5F5 100%);
    padding: 1rem;
    border-radius: 10px;
    border-left: 4px solid #1B2A4A;
    margin-bottom: 1rem;
}
.price-tag {
    font-size: 1.1rem;
    font-weight: bold;
    padding: 0.3rem 0.6rem;
    border-radius: 5px;
    display: inline-block;
    margin: 0.2rem;
}
.price-nunca { background: #E8F5E9; color: #2E7D32; }
.price-25 { background: #FFF9C4; color: #F57C00; }
.price-50 { background: #FFE0B2; color: #E65100; }
.price-75 { background: #FFCDD2; color: #C62828; }
</style>
""", unsafe_allow_html=True)

# ── Função para carregar dados ──
@st.cache_data(ttl=5)  # Cache por 5 segundos, atualiza automaticamente
def carregar_dados():
    json_path = os.path.join(os.path.dirname(__file__), "produtos_bazar.json")
    try:
        with open(json_path, 'r', encoding='utf-8-sig') as f:
            produtos = json.load(f)
        return pd.DataFrame(produtos) if produtos else pd.DataFrame()
    except (FileNotFoundError, json.JSONDecodeError):
        # Se não encontrar o arquivo, criar com dados de exemplo
        exemplo_dados = [
            {
                "id": 1,
                "marca": "Tarte Cosmetics",
                "produto": "Shape Tape Contour Concealer",
                "cor_tom": "22S Light Medium Sand",
                "tipo": "Corretivo",
                "volume": "10ml",
                "categoria_risco": "Normal",
                "preco_min": 165.00,
                "preco_max": 189.00,
                "preco_medio": 178.00,
                "mediana": 179.00,
                "fontes": 5,
                "data_pesquisa": "2026-03-27",
                "ajuste_categoria": -0.08,
                "nunca_usado": 113.85,
                "usado_25": 107.40,
                "usado_50": 80.55,
                "usado_75": 53.70,
                "observacoes": "Produto de demonstração - Tarte premium"
            }
        ]
        return pd.DataFrame(exemplo_dados)

# ── Header ──
st.markdown('<h1 class="main-title">🌸 Bazar da Thaís</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Dashboard Live • Atualiza automaticamente a cada 5 segundos</p>', unsafe_allow_html=True)

# ── Carregar dados ──
df = carregar_dados()
if df.empty:
    st.warning("📭 Nenhum produto no catálogo ainda!")
    st.info("""
    💡 **Como adicionar produtos:**
    1. Use o agente @bazar-maquiagem no VS Code
    2. Envie foto da maquiagem 
    3. Agente pesquisa preços automaticamente
    4. Dashboard atualiza em tempo real
    
    ✨ **Versão demo:** Alguns produtos de exemplo foram carregados para demonstração.
    """)
    st.stop()

# ── Auto-refresh ──
st_autorefresh = st.empty()
with st_autorefresh.container():
    st.markdown(f"🔄 Última atualização: {datetime.now().strftime('%H:%M:%S')} • {len(df)} produtos cadastrados")

# ══════════════════════════════════════════════════════
#  📊 KPIs EXECUTIVOS
# ══════════════════════════════════════════════════════

st.markdown("## 📊 Indicadores Executivos")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    total_produtos = len(df)
    st.metric("Total Produtos", total_produtos, help="Produtos cadastrados no bazar")

with col2:
    valor_mercado = df['mediana'].sum()
    st.metric("Valor de Mercado", f"R$ {valor_mercado:,.0f}", help="Soma das medianas dos preços de mercado")

with col3:
    valor_nunca = df['nunca_usado'].sum()
    st.metric("Valor Bazar (Nunca)", f"R$ {valor_nunca:,.0f}", help="Se todos fossem vendidos como nunca usados")

with col4:
    economia_media = ((valor_mercado - valor_nunca) / valor_mercado * 100) if valor_mercado > 0 else 0
    st.metric("Economia Média", f"{economia_media:.0f}%", help="Desconto médio vs. mercado")

with col5:
    ticket_medio = valor_nunca / total_produtos if total_produtos > 0 else 0
    st.metric("Ticket Médio", f"R$ {ticket_medio:.0f}", help="Preço médio por produto (nunca usado)")

# ══════════════════════════════════════════════════════
#  📋 CATÁLOGO COMPLETO
# ══════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📋 Catálogo de Produtos")

# Sidebar para filtros
with st.sidebar:
    st.markdown("### 🔍 Filtros")
    
    # Filtro por marca
    marcas_unicas = ['Todas'] + sorted(df['marca'].unique().tolist())
    marca_selecionada = st.selectbox("Marca", marcas_unicas)
    
    # Filtro por tipo
    tipos_unicos = ['Todos'] + sorted(df['tipo'].unique().tolist())
    tipo_selecionado = st.selectbox("Tipo", tipos_unicos)
    
    # Filtro por faixa de preço
    if not df.empty:
        min_preco = float(df['nunca_usado'].min())
        max_preco = float(df['nunca_usado'].max())
        faixa_preco = st.slider(
            "Faixa de Preço (Nunca Usado)",
            min_preco, max_preco,
            (min_preco, max_preco),
            help="Filtre produtos por preço"
        )

# Aplicar filtros
df_filtrado = df.copy()
if marca_selecionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['marca'] == marca_selecionada]
if tipo_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['tipo'] == tipo_selecionado]
if not df.empty:
    df_filtrado = df_filtrado[
        (df_filtrado['nunca_usado'] >= faixa_preco[0]) & 
        (df_filtrado['nunca_usado'] <= faixa_preco[1])
    ]

# Exibir produtos filtrados
if df_filtrado.empty:
    st.warning("🔍 Nenhum produto encontrado com os filtros selecionados.")
else:
    st.markdown(f"**{len(df_filtrado)} produtos encontrados**")
    
    for _, produto in df_filtrado.iterrows():
        with st.container():
            col_info, col_precos = st.columns([3, 2])
            
            with col_info:
                st.markdown(f"### {produto['marca']} — {produto['produto']}")
                st.markdown(f"**Tipo:** {produto['tipo']} | **Volume:** {produto['volume']} | **Cor:** {produto['cor_tom']}")
                
                # Preços de mercado
                col_merc1, col_merc2, col_merc3 = st.columns(3)
                with col_merc1:
                    st.metric("Menor Mercado", f"R$ {produto['preco_min']:.0f}")
                with col_merc2:
                    st.metric("Mediana", f"R$ {produto['mediana']:.0f}")
                with col_merc3:
                    ajuste_pct = produto['ajuste_categoria'] * 100
                    st.metric("Ajuste", f"{ajuste_pct:+.1f}%")
                
                if produto['observacoes']:
                    with st.expander("📝 Observações"):
                        st.text(produto['observacoes'])
            
            with col_precos:
                st.markdown("#### 💰 Preços Sugeridos")
                
                # Cards de preços
                st.markdown(f"""
                <div class="price-tag price-nunca">🟢 Nunca Usado: R$ {produto['nunca_usado']:.0f}</div>
                <div class="price-tag price-25">🟡 25% Usado: R$ {produto['usado_25']:.0f}</div>
                <div class="price-tag price-50">🟠 50% Usado: R$ {produto['usado_50']:.0f}</div>
                <div class="price-tag price-75">🔴 75% Usado: R$ {produto['usado_75']:.0f}</div>
                """, unsafe_allow_html=True)
                
                # Gráfico de barras com os preços
                precos_data = pd.DataFrame({
                    'Condição': ['🟢 Nunca', '🟡 25%', '🟠 50%', '🔴 75%'],
                    'Preço': [produto['nunca_usado'], produto['usado_25'], produto['usado_50'], produto['usado_75']],
                    'Cor': ['#4CAF50', '#FFC107', '#FF9800', '#F44336']
                })
                
                fig = px.bar(
                    precos_data, x='Condição', y='Preço',
                    color='Cor', color_discrete_map="identity",
                    title=f"Preços {produto['marca']}",
                    height=300
                )
                fig.update_layout(showlegend=False, margin=dict(l=0,r=0,t=30,b=0))
                fig.update_traces(texttemplate='R$ %{y:.0f}', textposition='outside')
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")

# ══════════════════════════════════════════════════════
#  📊 ANALYTICS
# ══════════════════════════════════════════════════════

if len(df) >= 2:
    st.markdown("## 📊 Análise por Tipo de Produto")
    
    # Agrupamento por tipo
    tipo_stats = df.groupby('tipo').agg({
        'id': 'count',
        'mediana': 'sum',
        'nunca_usado': 'sum'
    }).rename(columns={'id': 'quantidade'}).reset_index()
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        # Pizza: distribuição por tipo
        fig_pizza = px.pie(
            tipo_stats, values='quantidade', names='tipo',
            title="Distribuição por Tipo de Produto",
            height=400
        )
        st.plotly_chart(fig_pizza, use_container_width=True)
    
    with col_chart2:
        # Barras: valor por tipo
        fig_barras = px.bar(
            tipo_stats, x='tipo', y='nunca_usado',
            title="Valor Total por Tipo (Nunca Usado)",
            height=400,
            labels={'nunca_usado': 'Valor (R$)', 'tipo': 'Tipo'}
        )
        fig_barras.update_traces(texttemplate='R$ %{y:.0f}', textposition='outside')
        st.plotly_chart(fig_barras, use_container_width=True)

# ══════════════════════════════════════════════════════
#  🎯 ESTRATÉGIAS DE VENDA
# ══════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 🎯 Estratégias de Venda")

col_estrategia1, col_estrategia2 = st.columns(2)

with col_estrategia1:
    st.markdown("""
    ### 💡 Dicas de Preço Psicológico
    - **R$ 119 → R$ 119,90** (mais atrativo)
    - **R$ 64 → R$ 63,90** (melhor percepção)
    - **Kits**: "3 produtos por R$ X" vende mais rápido
    - **Urgência**: "Últimas unidades" ou "Edição limitada"
    """)

with col_estrategia2:
    st.markdown("""
    ### 🚀 Velocidade de Venda
    - **Princípio**: Velocidade > Margem
    - **Meta**: Liquidez rápida, não maximização
    - **Premium**: Marcas famosas vendem mais fácil
    - **Drugstore**: Precisa de desconto maior
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #808080; font-size: 0.9rem;">
🌸 Bazar da Thaís • Dashboard automatizado • Dados atualizados em tempo real
<br>Para adicionar produtos, use o agente @bazar-maquiagem no VS Code
</div>
""", unsafe_allow_html=True)