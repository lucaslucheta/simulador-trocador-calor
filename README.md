# 🔥 Simulador Interativo de Trocador de Calor ($\varepsilon$-NTU)

Aplicativo web interativo desenvolvido em Python para o cálculo e dimensionamento térmico de trocadores de calor tubulares utilizando o **Método da Efetividade-NTU ($\varepsilon$-NTU)**. O projeto faz parte do meu portfólio de Engenharia Química, unindo fundamentos de Operações Unitárias e desenvolvimento de software.

## 🚀 Funcionalidades

* **Interface Web Interativa:** Construída com Streamlit, permitindo alterar vazões, temperaturas e parâmetros de projeto em tempo real via barra lateral.
* **Cálculo Rigoroso:** Determinação automática da capacidade térmica ($C_{min}$, $C_{max}$, $C_r$), número de unidades de transferência ($NTU$), efetividade ($\varepsilon$), carga térmica total ($Q$) e temperaturas de saída dos fluidos.
* **Múltiplos Arranjos:** Suporte para escoamento em **contra-corrente** e **paralelo**.
* **Validação Visual:** Alertas dinâmicos e indicadores visuais de variação de temperatura.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **Streamlit** (Interface gráfica web)
* **NumPy** (Processamento numérico e funções matemáticas)

---

## 📦 Como Rodar o Projeto

1. **Link pelo Streamlit:**
   ```bash
   [git clone [https://github.com/SEU-USUARIO/simulador-trocador-calor.git](https://github.com/SEU-USUARIO/simulador-trocador-calor.git)
   cd simulador-trocador-calor](https://simulador-trocador-calor.streamlit.app/)

---

## 📐 Fundamentos de Engenharia Aplicados

O método $\varepsilon$-NTU é amplamente utilizado quando a temperatura de saída dos fluidos é desconhecida. As principais equações implementadas no código seguem a formulação clássica de transferência de calor:

* **Razão de Capacidades Térmicas:** 
  $$C_r = \frac{C_{min}}{C_{max}}$$

* **Número de Unidades de Transferência:** 
  $$NTU = \frac{U \cdot A}{C_{min}}$$

* **Efetividade para Contracorrente:** 
  $$\varepsilon = \frac{1 - \exp[-NTU(1 - C_r)]}{1 - C_r \exp[-NTU(1 - C_r)]}$$

---

## 🤖 Notas de Desenvolvimento e Apoio Tecnológico

Este projeto foi concebido, estruturado e validado por **Lucas Reis Lucheta**. Durante o processo de desenvolvimento e programação da interface em Streamlit, foram utilizadas ferramentas de Inteligência Artificial (como o **Gemini**) como suporte técnico de mentoria, estruturação de código e boas práticas de desenvolvimento.

---

## 👨‍💻 Autor

Desenvolvido por **Lucas Reis Lucheta**  
Estudante de Engenharia Química | EEL-USP  
[LinkedIn](https://www.linkedin.com/in/lucas-reis-lucheta) | [GitHub](https://github.com/lucaslucheta)
