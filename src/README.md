# Guia de Execução do Projeto

## Preparando o Ollama

Antes de tudo, é necessário ter o Ollama instalado e funcionando corretamente na sua máquina. Após a instalação, faça o download de um modelo leve e confirme se ele está respondendo como esperado.

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Estrutura do Projeto

Toda a lógica da aplicação está concentrada no arquivo `app.py`, que contém o código-fonte completo do projeto.

## Executando a Aplicação

Com o ambiente preparado, basta instalar as dependências necessárias, garantir que o Ollama esteja em execução e iniciar o Streamlit para rodar o app localmente.

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run .\src\app.py
```
