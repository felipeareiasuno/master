import streamlit as st

# Preço real das assinaturas
valores_reais = {
    "Start": 59.40,
    "FIIs": 251.16,
    "Ações": 251.16,
    "Renda Variável": 419.16,
    "Premium": 461.16,
    "Inter": 1236.20,
    "Small Caps": 1236.20,
    "Suno Black": 2774.40,
}

assinaturas = [{"name": nome, "points": pts} for nome, pts in {
    "Start": 2,
    "FIIs": 8,
    "Ações": 8,
    "Renda Variável": 14,
    "Premium": 16,
    "Inter": 42,
    "Small Caps": 42,
    "Suno Black": 93,
}.items()]

cursos = [
    {"name": "Valuation e Precificação", "points": 47, "valor": 837.90},
    {"name": "Viva de Dividendos", "points": 14, "valor": 242.90},
    {"name": "Investindo em Fundos Imobiliários", "points": 18, "valor": 312.90},
    {"name": "Contabilidade para Investidores", "points": 16, "valor": 277.90},
    {"name": "Matemática Financeira", "points": 16, "valor": 277.90},
    {"name": "Economia para Investidores", "points": 23, "valor": 417.90},
    {"name": "Investindo em Renda Fixa", "points": 16, "valor": 277.90},
]

brindes = [
    {"name": "Livros", "points": 8},
    {"name": "Caneca", "points": 8},
    {"name": "Camiseta", "points": 16},
    {"name": "Agasalho", "points": 39},
]

planos_ordenados = list(valores_reais.keys())

# App
st.set_page_config(page_title="Simulador Indicação Suno", layout="centered")
st.title("📊 Simulador de Indicação Premiada - Suno")

aba = st.sidebar.radio("Escolha o simulador:", ["1. Quantos pontos vou ganhar", "2. O que posso trocar com meus pontos"])

if aba == "1. Quantos pontos vou ganhar":
    st.header("🎯 Simulador de pontos por indicação")

    total_pontos = 0
    inputs = {}

    for plano in valores_reais:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**{plano}**")
        with col2:
            qtd = st.number_input("", min_value=0, step=1, key=plano, label_visibility="collapsed")
        valor_pago = valores_reais[plano]
        pontos = (valor_pago * 0.10) / 5.94 * qtd
        total_pontos += pontos

    st.markdown(f"### ✨ Total estimado de pontos: **{round(total_pontos)} pts**")
    st.caption("Cada ponto pode ser trocado por recompensas no catálogo.")

else:
    st.header("🎁 Simulador de trocas por pontos")
    col1, col2 = st.columns([1, 1])
    with col1:
        pontos = st.number_input("Quantos pontos você tem?", min_value=0, step=1)
    with col2:
        plano_atual = st.selectbox("Qual plano você possui atualmente?", planos_ordenados)

    nivel_atual = planos_ordenados.index(plano_atual)

    st.subheader("🔄 Trocas disponíveis")

    st.markdown("**Assinaturas** (com desconto proporcional):", help=None)
    for item in assinaturas:
        if planos_ordenados.index(item["name"]) >= nivel_atual:
            desconto = min(100, int((pontos / item["points"]) * 100))
            if desconto > 0:
                valor_final = valores_reais[item['name']] * (1 - desconto / 100)
                st.markdown(f"- {item['name']} ({item['points']} pts) → {desconto}% de desconto → R$ {valor_final:,.2f}".replace('.', ','), unsafe_allow_html=True)

    st.markdown("**Cursos**:")
    for c in cursos:
        desconto = min(100, int((pontos / c["points"]) * 100))
        saldo = c["valor"] * (1 - (desconto / 100))
        st.markdown(f"- {c['name']} ({c['points']} pts) → {desconto}% de desconto → Saldo a pagar: R$ {saldo:,.2f}".replace('.', ','), unsafe_allow_html=True)

    st.markdown("**Brindes**:")
    brindes_disp = [b for b in brindes if pontos >= b["points"]]
    if brindes_disp:
        for b in brindes_disp:
            st.markdown(f"- {b['name']} ({b['points']} pts)", unsafe_allow_html=True)
    else:
        st.markdown("_Nenhum brinde disponível._")
