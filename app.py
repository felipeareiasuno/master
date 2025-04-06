import streamlit as st

# App config - DEVE vir primeiro
st.set_page_config(page_title="Simulador Indicação Suno", layout="centered")


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

st.title("☀️ Indicação Premiada Suno")

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

    with st.expander("Como gero meu cupom de desconto?"):
        st.markdown("Acesse a aba '🎟️ Cupom', insira seu e-mail e receba um código exclusivo para usar em sua próxima assinatura.")

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

    recompensa_assinatura = None
    recompensas_extra = []
    pontos_usados = 0
    saldo_a_pagar = 0.0

    recompensas_selecionadas = []
    pontos_usados = 0
    saldo_a_pagar = 0.0

        recompensas_totais = []
    pontos_usados = 0
    saldo_a_pagar = 0.0

    if escolha != "Nenhuma" and escolha in mapa_assinatura:
        recompensa_assinatura, pontos_assinatura, valor_final = mapa_assinatura[escolha]
        if pontos_assinatura <= pontos:
            recompensas_totais.append(recompensa_assinatura)
            pontos_usados += pontos_assinatura
            saldo_a_pagar += valor_final

    for c in cursos:
        if pontos - pontos_usados >= c["points"] and st.session_state.get(c['name']):
            recompensas_totais.append(c['name'])
            pontos_usados += c['points']

    for b in brindes:
        if pontos - pontos_usados >= b["points"] and st.session_state.get(b['name']):
            recompensas_totais.append(b['name'])
            pontos_usados += b['points']

    if recompensas_totais:
        st.markdown(f"**Você escolheu:** {', '.join(recompensas_totais)}")
        st.markdown(f"**Pontos usados:** {pontos_usados}")
        st.markdown(f"**Pontos restantes:** {pontos - pontos_usados}")
        if saldo_a_pagar > 0:
            st.markdown(f"**Saldo a pagar:** R$ {saldo_a_pagar:,.2f}".replace('.', ','))
    else:
        st.markdown("_Nenhuma recompensa selecionada ainda._")
    st.markdown("---")
    st.subheader("🔄 Escolha o que deseja trocar")

    st.markdown("### Cursos")
    for c in cursos:
        if pontos - pontos_usados >= c["points"]:
            if st.checkbox(f"{c['name']} ({c['points']} pts)", key=c['name']):
                recompensas_extra.append(c['name'])
                pontos_usados += c['points']
        else:
            faltam = c["points"] - (pontos - pontos_usados)
            st.markdown(f"{c['name']} (precisa de {c['points']} pts) → falta {faltam} {'ponto' if faltam == 1 else 'pontos'}")

    st.markdown("### Brindes")
    for b in brindes:
        if pontos - pontos_usados >= b["points"]:
            if st.checkbox(f"{b['name']} ({b['points']} pts)", key=b['name']):
                recompensas_extra.append(b['name'])
                pontos_usados += b['points']
        else:
            faltam = b["points"] - (pontos - pontos_usados)
            st.markdown(f"{b['name']} (precisa de {b['points']} pts) → falta {faltam} {'ponto' if faltam == 1 else 'pontos'}")

    st.markdown("### Assinaturas")
    opcoes_assinatura = []
    mapa_assinatura = {}
    if pontos > 0:
        opcoes_assinatura.append("Nenhuma")
        for item in assinaturas:
            if planos_ordenados.index(item["name"]) >= nivel_atual:
                max_desconto = min(100, int((pontos / item["points"]) * 100))
                desconto_aplicado = (max_desconto // 10) * 10
                if desconto_aplicado >= 10:
                    valor_total = valores_reais[item["name"]]
                    valor_final = valor_total * (1 - desconto_aplicado / 100)
                    pontos_necessarios = int(item["points"] * (desconto_aplicado / 100))
                    label = f"{item['name']} - {desconto_aplicado}% de desconto → R$ {valor_final:,.2f}".replace('.', ',')
                    opcoes_assinatura.append(label)
                    mapa_assinatura[label] = (item["name"], pontos_necessarios, valor_final)

    escolha = st.radio("Escolha uma assinatura:", opcoes_assinatura, index=0) if opcoes_assinatura else "Nenhuma"

with abas[3]:
    st.header("🎯 Quero conquistar uma recompensa")

    tipo_recompensa = st.selectbox("Qual tipo de recompensa você quer?", ["Assinatura", "Curso", "Brinde"])

    if tipo_recompensa == "Assinatura":
        plano_atual_obj = st.selectbox("Qual assinatura você possui?", planos_ordenados, key="plano_obj")
        opcoes = [a for a in assinaturas if planos_ordenados.index(a["name"]) >= planos_ordenados.index(plano_atual_obj)]
        desejada = st.selectbox("Qual assinatura você quer conquistar?", [a["name"] for a in opcoes])
        pontos_necessarios = next(a["points"] for a in opcoes if a["name"] == desejada)

    elif tipo_recompensa == "Curso":
        desejado = st.selectbox("Qual curso você quer conquistar?", [c["name"] for c in cursos])
        pontos_necessarios = next(c["points"] for c in cursos if c["name"] == desejado)

    elif tipo_recompensa == "Brinde":
        desejado = st.selectbox("Qual brinde você quer conquistar?", [b["name"] for b in brindes])
        pontos_necessarios = next(b["points"] for b in brindes if b["name"] == desejado)

    st.markdown(f"### 🧩 Pontos necessários: **{pontos_necessarios} {'ponto' if pontos_necessarios == 1 else 'pontos'}**")

    st.markdown("---")
    st.markdown("### 💡 Exemplos de combinações para conquistar sua recompensa:")
    for a in assinaturas:
        pontos_gerados = round((valores_reais[a["name"]] * 0.10) / 5.94)
        if pontos_gerados > 0:
            qtd = (pontos_necessarios + pontos_gerados - 1) // pontos_gerados
            st.markdown(f"- {qtd} {'indicação' if qtd == 1 else 'indicações'} do plano **{a['name']}** ({pontos_gerados} {'ponto' if pontos_gerados == 1 else 'pontos'} cada)")

with abas[4]:
    st.header("🎟️ Gere seu cupom exclusivo")
    email = st.text_input("Digite seu e-mail para gerar o cupom:")
    if email:
        import hashlib
        hash_value = hashlib.new('whirlpool')
        hash_value.update(email.encode())
        coupon_code = hash_value.hexdigest()[:8].upper()
        st.success(f"Seu cupom exclusivo: **{coupon_code}**")
