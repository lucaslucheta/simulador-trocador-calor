import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Simulador de Trocador de Calor - NUT", layout="centered"
)

st.title("Simulador de Trocador de Calor (Método ε-NUT)")
st.markdown(
    "Este aplicativo calcula a **efetividade**, a **carga térmica** e as"
    " **temperaturas de saída** de um trocador de calor tubular com base nas"
    " propriedades dos fluidos."
)

st.sidebar.header("⚙️ Parâmetros de Entrada")

st.sidebar.subheader("Fluido Quente")
m_h = st.sidebar.number_input(
    "Vazão mássica (kg/s)",
    value=2.0,
    min_value=0.01,
    step=0.1,
    key="m_h",
)
cp_h = st.sidebar.number_input(
    "Calor específico (J/kg·K)",
    value=4184.0,
    min_value=100.0,
    step=50.0,
    key="cp_h",
)
t_h_in = st.sidebar.number_input(
    "Temperatura de entrada (°C)", value=80.0, step=1.0, key="t_h_in"
)

st.sidebar.subheader("Fluido Frio")
m_c = st.sidebar.number_input(
    "Vazão mássica (kg/s)",
    value=1.5,
    min_value=0.01,
    step=0.1,
    key="m_c",
)
cp_c = st.sidebar.number_input(
    "Calor específico (J/kg·K)",
    value=4184.0,
    min_value=100.0,
    step=50.0,
    key="cp_c",
)
t_c_in = st.sidebar.number_input(
    "Temperatura de entrada (°C)", value=20.0, step=1.0, key="t_c_in"
)

st.sidebar.subheader("Projeto do Trocador")
U = st.sidebar.number_input(
    "Coef. Global de Transf. Térmica - U (W/m²·K)",
    value=500.0,
    min_value=10.0,
    step=10.0,
    key="U",
)
A = st.sidebar.number_input(
    "Área de troca térmica - A (m²)",
    value=10.0,
    min_value=0.1,
    step=0.5,
    key="A",
)
flow_type = st.sidebar.selectbox(
    "Arranjo do Fluxo", ["Contra-corrente", "Paralelo"], key="flow_type"
)

C_h = m_h * cp_h
C_c = m_c * cp_c
C_min = min(C_h, C_c)
C_max = max(C_h, C_c)
C_r = C_min / C_max

NTU = (U * A) / C_min

if flow_type == "Contra-corrente":
  if abs(C_r - 1.0) < 1e-5:
    eps = NTU / (1.0 + NTU)
  else:
    eps = (1.0 - np.exp(-NTU * (1.0 - C_r))) / (
        1.0 - C_r * np.exp(-NTU * (1.0 - C_r))
    )
else:
  eps = (1.0 - np.exp(-NTU * (1.0 + C_r))) / (1.0 + C_r)

Q_max = C_min * (t_h_in - t_c_in)
Q = eps * Q_max

t_h_out = t_h_in - (Q / C_h)
t_c_out = t_c_in + (Q / C_c)

st.markdown("---")
st.subheader("📊 Resultados da Simulação")

col1, col2, col3 = st.columns(3)
col1.metric("Carga Térmica (Q)", f"{Q / 1000:.2f} kW")
col2.metric("Efetividade (ε)", f"{eps * 100:.1f} %")
col3.metric("NTU", f"{NTU:.2f}")

st.markdown("### 🌡️ Temperaturas de Saída")
col_a, col_b = st.columns(2)
col_a.metric(
    "Saída Fluido Quente",
    f"{t_h_out:.2f} °C",
    delta=f"-{t_h_in - t_h_out:.2f} °C",
    delta_color="inverse",
)
col_b.metric(
    "Saída Fluido Frio",
    f"{t_c_out:.2f} °C",
    delta=f"+{t_c_out - t_c_in:.2f} °C",
    delta_color="normal",
)
