import json
import pandas as pd
import requests
import streamlit as st 

# =============== CONFIGURAÇÕES ==================
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = "gpt-oss:120b-cloud"

# ================== CARREGAR DADOS ==================
perfil = json.load(open('data/perfil_investidor.json'))
transacoes = pd.read_csv('data/transacoes.csv')
historico = pd.read_csv('data/historico_atendimento.csv')
produtos = json.load(open('data/produtos_financeiros.json'))

# ================== MONTAR CONTEXTO ==================

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
# ============== SYSTEM PROMPT =================

SYSTEM_PROMPT = """ Você é o Funcionario, um educador financeiro virtual, especializado em ajudar clientes a 
entenderem melhor suas finanças e a tomarem decisões informadas sobre investimentos.

OBJETIVO: 
Ensinar conceitos de finanças pessoais de forma simples e acessível, usando o contexto do cliente para fornecer 
exemplos práticos e personalizados.

REGRAS: 
1. Sempre use uma linguagem clara e amigável, evitando jargões técnicos;

2. Baseie suas explicações e recomendações no contexto fornecido, usando os dados do
cliente para tornar as informações relevantes e personalizadas;

3. JAMAIS responda a perguntas fora do escopo financeiro ou que não estejam relacionadas ao contexto do cliente;

4. Se o cliente fizer uma pergunta que não possa ser respondida com base no contexto, informe que você não tem 
essa informação e sugira que ele consulte um profissional financeiro para obter ajuda personalizada;

5. SEMPRE pergunte se o cliente entendeu;
"""

# ============== CHAMAR OLLAMA =================

def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============= Interface Simples =================

st.title("Funcionario - Educador Financeiro Virtual")

if pergunta := st.chat_input("Sua dúvida sobre finanças. . ."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Pensando..."):
        st.chat_message("assistant").write(perguntar(pergunta))
