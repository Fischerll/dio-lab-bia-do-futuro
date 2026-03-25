
# Passo a passo de Execução 
## Setup do Ollama

```bash
# 1. Instalar o OLLAMA
# 2. Baixar um modelo leve
# 3. Testar se funciona

Ollama run gpt-oss "OLÁ"
```
# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Exemplo de requirements.txt

```
streamlit
openai
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run .\src\app.py
```
