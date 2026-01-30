import json
import pandas as pd
import requests
import streamlit as st

# ==================== CONFIGURAÇÕES ====================
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# ==================== CARREGAAR DADOS ====================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ==================== MONTAR CONTEXTO ====================
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']}, anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R${perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ==================== SYSTEM PROMPT ====================
SYSTEM_PROMPT = """Você é o Din, um agente educacional financeiro especializado em educação financeira básica e intermediária.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS GERAIS:
1. Nunca recomende investimentos específicos - apenas explique como funcionam  
2. Use os dados fornecidos para dar exemplos personalizados  
3. Linguagem simples, como se explicasse para um amigo  
4. Se não souber algo, admita: "Não tenho esta informação, mas posso explicar..."  
5. Sempre pergunte se o cliente entendeu  
6. Sempre baseie suas respostas nos dados fornecidos  
7. Nunca invente informações financeiras  
"""

# ==================== CHAMAR OLLAMA ====================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    pergunta: {msg}
    """
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ==================== iNTERFACE ====================
st.title("Din, o educador financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
