import streamlit as st

# App config - DEVE vir primeiro
st.set_page_config(page_title="Simulador Indicação Suno", layout="centered")

# CSS para travar o menu
st.markdown("""
    <style>
    .block-container {
        padding-top: 0rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        position: sticky;
        top: 0;
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
])

with abas[0]:
    st.header("📘 Sobre o Programa de Indicação")
    st.success("Indique amigos e acumule pontos para trocar por recompensas exclusivas!")
    st.markdown("---")

    st.markdown("### Como funciona")
    st.markdown("""
    - Ao indicar amigos para a Suno, você acumula pontos a cada assinatura confirmada.
    - Esses pontos podem ser trocados por cursos, assinaturas e brindes.
    - Quanto mais indicações, mais recompensas disponíveis para você.
    """)

    st.markdown("---")
    st.markdown("### 💬 Depoimentos de Clientes")
    st.markdown("""
    > "Já troquei meus pontos por dois cursos e economizei uma boa grana! Recomendo demais."  
    — Fernanda R.

    > "Indiquei três amigos e consegui desconto na minha renovação. Programa simples e vantajoso."  
    — Lucas M.

    > "O catálogo de recompensas é excelente. Muito bom poder escolher como usar os pontos!"  
    — Carla T.
    """)

    st.image("https://cdn.pixabay.com/photo/2015/01/08/18/27/startup-593341_960_720.jpg", caption="Ganhe recompensas indicando amigos.", use_column_width=True)

    st.markdown("---")
    st.markdown("### ❓ Regras Gerais (FAQ)")
    with st.expander("Quem pode participar do programa?"):
        st.markdown("Qualquer cliente Suno com uma assinatura ativa pode participar indicando novos assinantes.")

    with st.expander("Como os pontos são gerados?"):
        st.markdown("Sempre que um amigo indicado assinar um plano Suno, você ganha pontos automaticamente.")

    with st.expander("Como posso usar os pontos acumulados?"):
        st.markdown("Você pode trocar seus pontos por assinaturas, cursos ou brindes no nosso catálogo.")

    with st.expander("Posso trocar pontos parcialmente?"):
        st.markdown("Sim! Você pode usar os pontos como desconto proporcional nas recompensas.")

    with st.expander("Os pontos expiram?"):
        st.markdown("Sim, os pontos possuem validade de 12 meses após a data da indicação confirmada.")

    with st.expander("Onde acompanho meus pontos?"):
        st.markdown("Dentro da sua conta Suno, na área do programa de indicações.")

    with st.expander("Existe limite de indicações?"):
        st.markdown("Não! Você pode indicar quantas pessoas quiser — quanto mais indicações, mais pontos e recompensas. 😊")
