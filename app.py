
import streamlit as st

# Dados dos produtos
assinaturas = [
    {"name": "Start", "points": 2},
    {"name": "FIIs", "points": 8},
    {"name": "Ações", "points": 8},
    {"name": "Renda Variável", "points": 14},
    {"name": "Premium", "points": 16},
    {"name": "Inter", "points": 42},
    {"name": "Small Caps", "points": 42},
    {"name": "Suno Black", "points": 93},
]

cursos = [
    {"name": "Valuation e Precificação", "points": 47},
    {"name": "Viva de Dividendos", "points": 14},
    {"name": "FIIs", "points": 18},
    {"name": "Contabilidade", "points": 16},
    {"name": "Matemática Financeira", "points": 16},
    {"name": "Economia", "points": 23},
    {"name": "Renda Fixa", "points": 16},
]

brindes = [
    {"name": "Livros", "points": 8},
    {"name": "Caneca", "points": 8},
    {"name": "Camiseta", "points": 16},
    {"name": "Agasalho", "points": 39},
]

planos_ordenados = [p["name"] for p in assinaturas]

st.title("📊 Simulador de Indicação Premiada - Suno")

aba = st.sidebar.radio("Escolha o simulador:", ["1. Quantos pontos vou ganhar", "2. O que posso trocar com meus pontos"])

if aba == "1. Quantos pontos vou ganhar":
    st.header("🎯 Simulador de pontos por indicação")
    total_pontos = 0
    for plano in assinaturas:
        qtd = st.number_input(f"Quantas indicações do plano {plano['name']}?", min_value=0, step=1, key=plano['name'])
        pontos = (plano['points'] * 5.94) * 0.1  # Convertendo para reais e pegando 10%
        total_pontos += (pontos / 5.94) * qtd
    st.success(f"✨ Total estimado de pontos: {round(total_pontos)} pts")
    st.caption("*Os pontos podem ser trocados por produtos de acordo com o catálogo e regras do programa.")

else:
    st.header("🎁 Simulador de trocas por pontos")
    pontos = st.number_input("Quantos pontos você tem?", min_value=0.0, step=0.5)
    plano_atual = st.selectbox("Qual plano você possui atualmente?", planos_ordenados)
    nivel_atual = planos_ordenados.index(plano_atual)

    st.subheader("🔄 Trocas disponíveis")

    st.markdown("**Assinaturas** (com desconto proporcional):")
    for item in assinaturas:
        if planos_ordenados.index(item["name"]) >= nivel_atual:
            desconto = min(100, int((pontos / item["points"])*100))
            if desconto > 0:
                st.markdown(f"- {item['name']} ({item['points']} pts) → **{desconto}% de desconto**")

    st.markdown("**Cursos**:")
    cursos_disp = [c for c in cursos if pontos >= c["points"]]
    if cursos_disp:
        for c in cursos_disp:
            st.markdown(f"- {c['name']} ({c['points']} pts)")
    else:
        st.markdown("_Nenhum curso disponível._")

    st.markdown("**Brindes**:")
    brindes_disp = [b for b in brindes if pontos >= b["points"]]
    if brindes_disp:
        for b in brindes_disp:
            st.markdown(f"- {b['name']} ({b['points']} pts)")
    else:
        st.markdown("_Nenhum brinde disponível._")
