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
    z-index: 999;
    border-bottom: 1px solid #eee;
}
section[data-testid="stSidebar"] {
    z-index: 1000;
}
section.main > div:first-child {
    position: sticky;
    top: 3.5rem;
    background-color: white;
    z-index: 998;
    padding-top: 0.5rem;
    border-bottom: 1px solid #eee;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    transition: box-shadow 0.3s ease-in-out;
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
    "Internacional": 1236.20,
    "Small Caps": 1236.20,
    "Suno Black": 2774.40,
}

assinaturas = [{"name": nome, "points": pts} for nome, pts in {
    "Start": 2,
    "FIIs": 8,
    "Ações": 8,
    "Renda Variável": 14,
    "Premium": 16,
    "Internacional": 42,
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

valores_reais = dict(("Internacional" if k == "Inter" else k, v) for k, v in valores_reais.items())
planos_ordenados = list(valores_reais.keys())

st.title("📊 Indicação Premiada Suno")

abas = st.tabs([
    "📘 Sobre",
    "📈 Acumule",
    "🎁 Ganhe",
    "🎯 Objetivo",
    "🎟️ Cupom"
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
        pontos = round((valor_pago * 0.10) / 5.94) * qtd
        total_pontos += pontos
    st.markdown(f"### ✨ Total estimado de pontos: **{round(total_pontos)} {'ponto' if round(total_pontos) == 1 else 'pontos'}**")

with abas[2]:
    st.header("🎁 Simulador de trocas por pontos")
    col1, col2 = st.columns([1, 1])
    with col1:
        pontos = st.number_input("Quantos pontos você tem?", min_value=0, step=1)
    with col2:
        plano_atual = st.selectbox("Qual plano você possui atualmente?", planos_ordenados)

    nivel_atual = planos_ordenados.index(plano_atual)

    st.subheader("🔄 Trocas disponíveis")

    st.markdown("**Assinaturas** (descontos em múltiplos de 10%):")
    for item in assinaturas:
        if planos_ordenados.index(item["name"]) >= nivel_atual:
            max_desconto = min(100, int((pontos / item["points"]) * 100))
            desconto_aplicado = (max_desconto // 10) * 10
            if desconto_aplicado >= 10:
                valor_final = valores_reais[item['name']] * (1 - desconto_aplicado / 100)
                st.markdown(f"- {item['name']} ({item['points']} pts) → {desconto_aplicado}% de desconto → R$ {valor_final:,.2f}".replace('.', ','))

    st.markdown("**Cursos**:")
    for c in cursos:
        if pontos >= c["points"]:
            st.markdown(f"- {c['name']} ({c['points']} pts)")
        else:
            faltam = c["points"] - pontos
            st.markdown(f"- {c['name']} (precisa de {c['points']} pts) → falta {faltam} {'ponto' if faltam == 1 else 'pontos'}")

    st.markdown("**Brindes**:")
    for b in brindes:
        if pontos >= b["points"]:
            st.markdown(f"- {b['name']} ({b['points']} pts)")
        else:
            faltam = b["points"] - pontos
            st.markdown(f"- {b['name']} (precisa de {b['points']} pts) → falta {faltam} {'ponto' if faltam == 1 else 'pontos'}")

with abas[3]:
    st.header("🎟️ Gere seu cupom exclusivo")
    email = st.text_input("Digite seu e-mail para gerar o cupom:")
    if email:
        import hashlib
        hash_value = hashlib.new('whirlpool')
        hash_value.update(email.encode())
        coupon_code = hash_value.hexdigest()[:8].upper()
        st.success(f"Seu cupom exclusivo: **{coupon_code}**")

with abas[4]:
    st.header("🧮 Quero conquistar uma recompensa")

    tipo_recompensa = st.selectbox("Qual tipo de recompensa você quer?", ["Assinatura", "Curso", "Brinde"])

    if tipo_recompensa == "Assinatura":
        plano_atual = st.selectbox("Qual assinatura você possui?", planos_ordenados)
        opcoes = [a for a in assinaturas if planos_ordenados.index(a["name"]) >= planos_ordenados.index(plano_atual)]
        desejada = st.selectbox("Qual assinatura você quer conquistar?", [a["name"] for a in opcoes])
        pontos_necessarios = next(a["points"] for a in opcoes if a["name"] == desejada)

    elif tipo_recompensa == "Curso":
        desejado = st.selectbox("Qual curso você quer conquistar?", [c["name"] for c in cursos])
        pontos_necessarios = next(c["points"] for c in cursos if c["name"] == desejado)

    elif tipo_recompensa == "Brinde":
        desejado = st.selectbox("Qual brinde você quer conquistar?", [b["name"] for b in brindes])
        pontos_necessarios = next(b["points"] for b in brindes if b["name"] == desejado)

    st.markdown(f"### 🧩 Pontos necessários: **{pontos_necessarios} pts**")

    st.markdown("---")
    st.markdown("### 💡 Exemplos de combinações para conquistar sua recompensa:")
    for a in assinaturas:
        pontos_gerados = round((valores_reais[a["name"]] * 0.10) / 5.94)
        if pontos_gerados > 0:
            qtd = (pontos_necessarios + pontos_gerados - 1) // pontos_gerados
            st.markdown(f"- {qtd} {'indicação' if qtd == 1 else 'indicações'} do plano **{a['name']}** ({pontos_gerados} pts cada)")
