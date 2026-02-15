# IA na Eletronica Automotiva

Este projeto e um MVP de uma plataforma de IA aplicada a eletronica automotiva. O foco atual e demonstrar fluxos de diagnostico e interpretacao visual por meio de mockups interativos em Streamlit.

## Visao Geral

- Diagnostico inteligente e guiado por IA
- Interpretacao de esquemas eletricos
- Reconhecimento visual de componentes
- Estrutura para evolucao com integracoes reais

## Funcionalidades do MVP

- Upload de imagem de modulo eletronico
- Sugestao automatizada de falhas provaveis
- Simulacao do fluxo de perguntas e respostas com IA
- Interface simples e interativa via Streamlit

## Status atual do repositorio

- Este repositorio e um MVP visual (mockups interativos).
- O codigo atual usa: `Python`, `Streamlit` e `Pillow`.
- As imagens em `mockups/` sao geradas automaticamente apenas quando estiverem ausentes.

## Como Executar

### Pre-requisitos

- Python 3.8+
- Pip
- Visual Studio Code (opcional)

### Passos

```bash
git clone https://github.com/fabao2024/ia-eletronica-automotiva.git
cd ia-eletronica-automotiva

python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

### Nota de execucao

- O app nao recria os arquivos de `mockups/` em toda interacao.
- Se algum PNG for removido, ele e gerado novamente na proxima execucao.

### Executando com Visual Studio Code

1. Abra a pasta do projeto no VS Code.
2. Instale a extensao Python.
3. Abra "Run and Debug" (`Ctrl+Shift+D`).
4. Selecione `Python: Streamlit` e pressione `F5`.

## Tecnologias Usadas

### Atualmente no codigo

- Python
- Streamlit
- Pillow

### Planejadas para proximas fases

- OpenCV / YOLOv8
- Tesseract OCR
- GPT (OpenAI API)
- MongoDB / PostgreSQL

## Proximos Passos

- Finalizar backend com integracao real com APIs
- Lancar versao beta para oficinas parceiras
- Incluir base de dados com falhas reais
- Evoluir para modelo neural proprietario

## Contribua

Contribuicoes sao bem-vindas. Abra uma issue ou pull request.

## Licenca

Este projeto esta sob a licenca MIT.
