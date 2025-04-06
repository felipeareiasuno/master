import streamlit as st

# App config - DEVE vir primeiro
st.set_page_config(page_title="Simulador Indicação Suno", layout="centered")

# CSS para travar o menu e adicionar espaçamento no topo
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
    }
    header[data-testid="stHeader"] {
        position: sticky;
        top: 0;
        background-color: white;
        z-index: 100;
    }
    .stTabs [data-baseweb="tab-list"] {
        position: sticky;
        top: 3.5rem;
        background-color: white;
        z-index: 99;
        padding-top: 1rem;
        border-bottom: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

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

st.title("📊 Simulador de Indicação Premiada - Suno")

abas = st.tabs([
    "📘 Sobre o Programa",
    "🎯 Quantos pontos vou ganhar",
    "🎁 O que posso trocar com meus pontos"
, "🎟️ Gerar meu cupom"])

with abas[0]:
    st.header("📘 Sobre o Programa")
    st.markdown("""
    Participe do Programa de Indicação Suno e ganhe pontos a cada amigo que se tornar assinante.

    ### Como funciona:
    - Compartilhe seu link de indicação
    - Seus amigos assinam um plano da Suno
    - Você acumula pontos que podem ser trocados por recompensas

    ### O que você pode trocar:
    - Assinaturas Suno com desconto
    - Cursos exclusivos
    - Brindes como camisetas, livros e canecas

    Quanto mais amigos você indicar, mais pontos você acumula!
    """)

with abas[1]:
    st.header("🎯 Simulador de pontos por indicação")
    total_pontos = 0
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

with abas[2]:
    st.header("🎁 Simulador de trocas por pontos")
    col1, col2 = st.columns([1, 1])
    with col1:
        pontos = st.number_input("Quantos pontos você tem?", min_value=0, step=1)
    with col2:
        plano_atual = st.selectbox("Qual plano você possui atualmente?", planos_ordenados)

    nivel_atual = planos_ordenados.index(plano_atual)

    st.subheader("🔄 Trocas disponíveis")

    st.markdown("**Assinaturas** (com desconto proporcional):")
    for item in assinaturas:
        if planos_ordenados.index(item["name"]) >= nivel_atual:
            desconto = min(100, int((pontos / item["points"]) * 100))
            if desconto > 0:
                valor_final = valores_reais[item['name']] * (1 - desconto / 100)
                st.markdown(f"- {item['name']} ({item['points']} pts) → {desconto}% de desconto → R$ {valor_final:,.2f}".replace('.', ','))

    st.markdown("**Cursos**:")
    for c in cursos:
        if pontos >= c["points"]:
            st.markdown(f"- {c['name']} ({c['points']} pts)")
        else:
            faltam = c["points"] - pontos
            st.markdown(f"- {c['name']} (precisa de {c['points']} pts) → faltam {faltam} pts")

    st.markdown("**Brindes**:")
    for b in brindes:
        if pontos >= b["points"]:
            st.markdown(f"- {b['name']} ({b['points']} pts)")
        else:
            faltam = b["points"] - pontos
            st.markdown(f"- {b['name']} (precisa de {b['points']} pts) → faltam {faltam} pts")

with abas[3]:
    st.header("🎟️ Gere seu cupom exclusivo")
    email = st.text_input("Digite seu e-mail para gerar o cupom:")
    if email:
        import hashlib
        hash_value = hashlib.new('whirlpool')
        hash_value.update(email.encode())
        coupon_code = hash_value.hexdigest()[:8].upper()
        st.success(f"Seu cupom exclusivo: **{coupon_code}**")
