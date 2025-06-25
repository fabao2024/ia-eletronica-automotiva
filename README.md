# IA na Eletrônica Automotiva 🚗🤖

Este projeto é um MVP de uma plataforma baseada em Inteligência Artificial aplicada à eletrônica automotiva. O objetivo é auxiliar mecânicos e técnicos no diagnóstico de falhas complexas utilizando visão computacional, processamento de linguagem natural e aprendizado contínuo com dados reais.

## 🔍 Visão Geral

- 🎯 Diagnóstico inteligente e guiado por IA
- 🧠 Interpretação de esquemas elétricos com GPT + RAG
- 👁️ Reconhecimento visual de componentes com OpenCV e YOLOv8
- 🧾 Aprendizado contínuo com mensagens reais de mecânicos via WhatsApp API

## 📦 Funcionalidades do MVP

- Upload de imagem de módulo eletrônico
- Sugestão automatizada de falhas prováveis
- Simulação do fluxo de perguntas/respostas com IA
- Interface simples e interativa via Streamlit

## 🛠️ Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Pip
- Visual Studio Code (Opcional)

### Passos

```bash
# Clone o repositório (ou baixe)
git clone https://github.com/fabao2024/ia-eletronica-automotiva.git
cd ia-eletronica-automotiva

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

### Executando com o Visual Studio Code

1. Abra a pasta do projeto no Visual Studio Code.
2. Instale a extensão recomendada para Python.
3. Abra o painel "Run and Debug" (Ctrl+Shift+D).
4. Selecione a configuração "Python: Streamlit" e pressione F5 para iniciar.

## 🧪 Tecnologias Usadas

- Python
- Streamlit
- OpenCV / YOLOv8
- Tesseract OCR
- GPT (OpenAI API)
- MongoDB / PostgreSQL

## 🚀 Próximos Passos

- Finalizar backend com integração real com APIs
- Lançar versão beta para oficinas parceiras
- Incluir base de dados com falhas reais
- Construção do modelo neural proprietário

## 🤝 Contribua

Contribuições são bem-vindas! Sinta-se livre para abrir uma issue ou pull request.

## 📄 Licença

Este projeto está sob a licença MIT.