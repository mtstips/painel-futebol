import streamlit as st
import pandas as pd
import time
import random

def gerar_dados_jogos():
    jogos = []
    times = [
        ("Flamengo", "Grêmio"),
        ("Palmeiras", "Corinthians"),
        ("Arsenal", "Chelsea"),
        ("Barcelona", "Real Madrid"),
        ("PSG", "Marseille"),
        ("River Plate", "Boca Juniors")
    ]
    for casa, fora in times:
        minuto = random.randint(1, 30)
        ataques_perigosos = random.randint(5, 30)
        escanteios = random.randint(0, 5)
        chutes = random.randint(0, 15)
        cartoes = random.randint(0, 3)
        placar_casa = random.randint(0, 2)
        placar_fora = random.randint(0, 2)

        if minuto < 20 and ataques_perigosos >= 10 and escanteios >= 1:
            jogos.append({
                "Jogo": f"{casa} x {fora}",
                "Minuto": f"{minuto}'",
                "Placar": f"{placar_casa} x {placar_fora}",
                "Ataques Perigosos": ataques_perigosos,
                "Escanteios": escanteios,
                "Chutes Totais": chutes,
                "Cartões": cartoes
            })
    return jogos

st.set_page_config(page_title="Painel de Jogos - Volume Ofensivo", layout="wide")
st.title("⚽ Painel de Jogos com Alto Volume Ofensivo")
st.caption("Atualizado automaticamente a cada 30 segundos. Exibe somente jogos com:")
st.markdown("- Menos de 20 minutos")
st.markdown("- 10 ou mais ataques perigosos")
st.markdown("- Pelo menos 1 escanteio")

placeholder = st.empty()

while True:
    with placeholder.container():
        jogos = gerar_dados_jogos()
        if jogos:
            df = pd.DataFrame(jogos)
            st.dataframe(df, use_container_width=True)
            st.success("⚠️ Novo(s) jogo(s) detectado(s) com alto volume ofensivo!")
        else:
            st.info("Nenhum jogo com os critérios agora.")
    time.sleep(30)
