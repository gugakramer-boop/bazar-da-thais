import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from pathlib import Path

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
.sold-badge {
    background: linear-gradient(135deg, #4CAF50 0%, #388E3C 100%);
    color: white;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-weight: bold;
    font-size: 1rem;
    display: inline-block;
    margin: 0.3rem 0;
}
.sold-overlay {
    opacity: 0.6;
}
</style>
""", unsafe_allow_html=True)

# ── Funções de dados ──
def get_data_path():
    """Retorna o caminho do arquivo de dados"""
    # Try data/ subfolder first (organized structure)
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "produtos_bazar.json")
    if os.path.exists(data_path):
        return data_path
    # Fallback to root (Streamlit Cloud / legacy)
    old_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "produtos_bazar.json")
    if os.path.exists(old_path):
        return old_path
    return old_path  # Default to root for cloud

def salvar_dados(produtos_list):
    """Salva dados atualizados no JSON"""
    data_path = get_data_path()
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(produtos_list, f, indent=2, ensure_ascii=False)

def marcar_vendido(produto_id, preco_venda):
    """Marca um produto como vendido e registra o preço de venda"""
    data_path = get_data_path()
    try:
        with open(data_path, 'r', encoding='utf-8-sig') as f:
            produtos = json.load(f)
        for p in produtos:
            if p.get('id') == produto_id:
                p['vendido'] = True
                p['preco_venda'] = preco_venda
                p['data_venda'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                break
        salvar_dados(produtos)
        return True
    except Exception as e:
        st.error(f"Erro ao salvar venda: {e}")
        return False

def desfazer_venda(produto_id):
    """Remove marcação de vendido de um produto"""
    data_path = get_data_path()
    try:
        with open(data_path, 'r', encoding='utf-8-sig') as f:
            produtos = json.load(f)
        for p in produtos:
            if p.get('id') == produto_id:
                p.pop('vendido', None)
                p.pop('preco_venda', None)
                p.pop('data_venda', None)
                break
        salvar_dados(produtos)
        return True
    except Exception as e:
        st.error(f"Erro ao desfazer venda: {e}")
        return False

def remover_produto(produto_id):
    """Remove um produto permanentemente do catálogo"""
    data_path = get_data_path()
    try:
        with open(data_path, 'r', encoding='utf-8-sig') as f:
            produtos = json.load(f)
        produtos = [p for p in produtos if p.get('id') != produto_id]
        salvar_dados(produtos)
        return True
    except Exception as e:
        st.error(f"Erro ao remover produto: {e}")
        return False

@st.cache_data(ttl=5)  # Cache por 5 segundos, atualiza automaticamente
def carregar_dados():
    """Carrega dados com fallback para múltiplos caminhos"""
    # Try data/ subfolder first (organized structure)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    paths_to_try = [
        os.path.join(base_dir, "data", "produtos_bazar.json"),
        os.path.join(base_dir, "produtos_bazar.json"),
    ]
    
    for path in paths_to_try:
        try:
            with open(path, 'r', encoding='utf-8-sig') as f:
                produtos = json.load(f)
            if produtos:
                return pd.DataFrame(produtos)
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    
    # Se não encontrar, dados de exemplo
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

# Contadores de vendas
total_produtos = len(df)
vendidos = df[df.get('vendido', pd.Series([False]*len(df))) == True] if 'vendido' in df.columns else pd.DataFrame()
disponiveis = len(df) - len(vendidos)

with st_autorefresh.container():
    st.markdown(f"🔄 Última atualização: {datetime.now().strftime('%H:%M:%S')} • {total_produtos} produtos • {disponiveis} disponíveis • {len(vendidos)} vendidos")

# ══════════════════════════════════════════════════════
#  📊 KPIs EXECUTIVOS
# ══════════════════════════════════════════════════════

st.markdown("## 📊 Indicadores Executivos")

# Separar vendidos e disponíveis
has_vendido_col = 'vendido' in df.columns
if has_vendido_col:
    df_vendidos = df[df['vendido'] == True]
    df_disponiveis = df[df['vendido'] != True]
else:
    df_vendidos = pd.DataFrame()
    df_disponiveis = df.copy()

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Total Produtos", len(df), help="Produtos cadastrados no bazar")

with col2:
    st.metric("🟢 Disponíveis", len(df_disponiveis), help="Produtos ainda à venda")

with col3:
    st.metric("✅ Vendidos", len(df_vendidos), help="Produtos já vendidos")

with col4:
    receita_total = df_vendidos['preco_venda'].sum() if not df_vendidos.empty and 'preco_venda' in df_vendidos.columns else 0
    st.metric("💰 Receita", f"R$ {receita_total:,.0f}", help="Total arrecadado com vendas")

with col5:
    valor_estoque = df_disponiveis['nunca_usado'].sum() if not df_disponiveis.empty else 0
    st.metric("📦 Estoque", f"R$ {valor_estoque:,.0f}", help="Valor disponível no bazar")

with col6:
    taxa_venda = (len(df_vendidos) / len(df) * 100) if len(df) > 0 else 0
    st.metric("📈 Taxa Venda", f"{taxa_venda:.0f}%", help="Percentual de produtos vendidos")

# ══════════════════════════════════════════════════════
#  📋 CATÁLOGO COMPLETO
# ══════════════════════════════════════════════════════

st.markdown("---")
st.markdown("## 📋 Catálogo de Produtos")

# Sidebar para filtros
with st.sidebar:
    st.markdown("### 🔍 Filtros")
    
    # Filtro por status
    status_opcoes = ['Todos', '🟢 Disponíveis', '✅ Vendidos']
    status_selecionado = st.selectbox("Status", status_opcoes)
    
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
if status_selecionado == '🟢 Disponíveis':
    if has_vendido_col:
        df_filtrado = df_filtrado[df_filtrado['vendido'] != True]
    # If no vendido column, all are available
elif status_selecionado == '✅ Vendidos':
    if has_vendido_col:
        df_filtrado = df_filtrado[df_filtrado['vendido'] == True]
    else:
        df_filtrado = pd.DataFrame()  # None sold yet
if marca_selecionada != 'Todas':
    df_filtrado = df_filtrado[df_filtrado['marca'] == marca_selecionada]
if tipo_selecionado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['tipo'] == tipo_selecionado]
if not df.empty and not df_filtrado.empty:
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
        produto_id = int(produto['id'])
        is_sold = produto.get('vendido', False) == True
        
        with st.container():
            # Header com badge de vendido
            if is_sold:
                preco_venda = produto.get('preco_venda', 0)
                data_venda = produto.get('data_venda', '')
                st.markdown(f'<div class="sold-badge">✅ VENDIDO por R$ {preco_venda:.0f} em {data_venda}</div>', unsafe_allow_html=True)
            
            # Layout com imagem
            img_url = str(produto.get('imagem_url', '')).strip()
            src_img = str(produto.get('source_image', '')).strip()
            has_image = False
            image_path = None
            
            if img_url:
                has_image = True
                image_path = img_url
            elif src_img:
                # Tentar encontrar foto local em photos/processed/
                base_dir = os.path.dirname(os.path.abspath(__file__))
                for folder in ['photos/processed', 'photos/to_process', 'photos']:
                    candidate = os.path.join(base_dir, folder, src_img)
                    if os.path.exists(candidate):
                        has_image = True
                        image_path = candidate
                        break
            
            if has_image:
                col_img, col_info, col_precos, col_acao = st.columns([1, 2.5, 2, 1.2])
                with col_img:
                    try:
                        st.image(image_path, width=140)
                    except Exception:
                        st.markdown("📷 *Imagem indisponível*")
            else:
                col_img = None
                col_info, col_precos, col_acao = st.columns([3, 2, 1.2])
            
            with col_info:
                titulo = f"### {produto['marca']} — {produto['produto']}"
                if is_sold:
                    titulo = f"### ~~{produto['marca']} — {produto['produto']}~~"
                st.markdown(titulo)
                st.markdown(f"**Tipo:** {produto['tipo']} | **Volume:** {produto['volume']} | **Cor:** {produto['cor_tom']}")
                
                # Preços de mercado
                col_merc1, col_merc2, col_merc3 = st.columns(3)
                with col_merc1:
                    st.metric("Menor Mercado", f"R$ {produto['preco_min']:.0f}")
                with col_merc2:
                    st.metric("Mediana", f"R$ {produto['mediana']:.0f}")
                with col_merc3:
                    try:
                        ajuste_pct = float(produto['ajuste_categoria']) * 100
                        st.metric("Ajuste", f"{ajuste_pct:+.1f}%")
                    except (ValueError, TypeError):
                        st.metric("Ajuste", str(produto['ajuste_categoria']))
                
                if produto.get('observacoes'):
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
            
            with col_acao:
                st.markdown("#### 🛒 Ação")
                
                if is_sold:
                    # Botão para desfazer venda
                    if st.button("↩️ Desfazer Venda", key=f"undo_{produto_id}", type="secondary"):
                        if desfazer_venda(produto_id):
                            st.success("Venda desfeita!")
                            st.cache_data.clear()
                            st.rerun()
                    
                    st.markdown(f"**Vendido por:** R$ {produto.get('preco_venda', 0):.0f}")
                    st.markdown(f"**Data:** {produto.get('data_venda', 'N/A')}")
                
                # Botão remover (disponível para vendidos e não vendidos)
                with st.expander("🗑️ Remover produto"):
                    st.warning("⚠️ Esta ação é permanente!")
                    if st.button("Confirmar remoção", key=f"del_{produto_id}", type="primary"):
                        if remover_produto(produto_id):
                            st.success("Produto removido!")
                            st.cache_data.clear()
                            st.rerun()
                
                if not is_sold:
                    # Formulário para registrar venda
                    with st.form(key=f"venda_{produto_id}", clear_on_submit=True):
                        st.markdown("**Registrar Venda:**")
                        
                        # Preço sugerido como referência
                        preco_sugerido = float(produto['nunca_usado'])
                        preco_input = st.number_input(
                            "Preço de venda (R$)",
                            min_value=0.0,
                            value=preco_sugerido,
                            step=5.0,
                            format="%.2f",
                            key=f"preco_{produto_id}"
                        )
                        
                        submitted = st.form_submit_button("✅ Vendido!", type="primary")
                        if submitted:
                            if marcar_vendido(produto_id, preco_input):
                                st.success(f"🎉 Vendido por R$ {preco_input:.0f}!")
                                st.cache_data.clear()
                                st.rerun()
        
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

# ══════════════════════════════════════════════════════
#  💰 RELATÓRIO DE VENDAS
# ══════════════════════════════════════════════════════

if not df_vendidos.empty:
    st.markdown("---")
    st.markdown("## 💰 Relatório de Vendas")
    
    col_v1, col_v2, col_v3, col_v4 = st.columns(4)
    
    with col_v1:
        receita = df_vendidos['preco_venda'].sum() if 'preco_venda' in df_vendidos.columns else 0
        st.metric("💰 Receita Total", f"R$ {receita:,.0f}")
    
    with col_v2:
        ticket_medio_venda = receita / len(df_vendidos) if len(df_vendidos) > 0 else 0
        st.metric("🎫 Ticket Médio", f"R$ {ticket_medio_venda:,.0f}")
    
    with col_v3:
        # Calcular margem vs preço sugerido
        if 'preco_venda' in df_vendidos.columns:
            sugerido_total = df_vendidos['nunca_usado'].sum()
            diff = receita - sugerido_total
            st.metric("📊 vs. Sugerido", f"R$ {diff:+,.0f}", help="Diferença entre preço de venda e preço sugerido (nunca usado)")
    
    with col_v4:
        valor_mercado_vendidos = df_vendidos['mediana'].sum() if 'mediana' in df_vendidos.columns else 0
        economia_comprador = ((valor_mercado_vendidos - receita) / valor_mercado_vendidos * 100) if valor_mercado_vendidos > 0 else 0
        st.metric("🎁 Economia Comprador", f"{economia_comprador:.0f}%", help="Quanto o comprador economizou vs. mercado")
    
    # Tabela de vendas recentes
    st.markdown("### 📋 Vendas Recentes")
    vendas_display = df_vendidos[['marca', 'produto', 'tipo', 'preco_venda', 'nunca_usado', 'mediana', 'data_venda']].copy()
    vendas_display.columns = ['Marca', 'Produto', 'Tipo', 'Vendido Por (R$)', 'Sugerido (R$)', 'Mercado (R$)', 'Data Venda']
    st.dataframe(vendas_display, use_container_width=True, hide_index=True)
    
    # Gráfico de vendas
    if len(df_vendidos) >= 2 and 'preco_venda' in df_vendidos.columns:
        col_g1, col_g2 = st.columns(2)
        
        with col_g1:
            fig_comp = go.Figure()
            fig_comp.add_trace(go.Bar(
                name='Preço Venda', 
                x=df_vendidos['marca'] + ' - ' + df_vendidos['produto'].str[:20],
                y=df_vendidos['preco_venda'],
                marker_color='#4CAF50'
            ))
            fig_comp.add_trace(go.Bar(
                name='Mediana Mercado',
                x=df_vendidos['marca'] + ' - ' + df_vendidos['produto'].str[:20], 
                y=df_vendidos['mediana'],
                marker_color='#E8A5C8'
            ))
            fig_comp.update_layout(
                title="Preço de Venda vs. Mercado",
                barmode='group', height=400,
                margin=dict(l=0,r=0,t=30,b=0)
            )
            st.plotly_chart(fig_comp, use_container_width=True)
        
        with col_g2:
            fig_pie_vendas = px.pie(
                df_vendidos, values='preco_venda', names='marca',
                title="Receita por Marca",
                height=400
            )
            st.plotly_chart(fig_pie_vendas, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #808080; font-size: 0.9rem;">
🌸 Bazar da Thaís • Dashboard automatizado • Dados atualizados em tempo real
<br>Para adicionar produtos, use o agente @bazar-maquiagem no VS Code
</div>
""", unsafe_allow_html=True)
