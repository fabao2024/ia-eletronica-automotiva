# Instruções para Executar os Mockups Localmente

Este pacote contém os mockups visuais para o projeto de IA aplicada à eletrônica automotiva, criados como uma aplicação Streamlit.

Siga os passos abaixo para visualizar os mockups no seu próprio computador:

## Pré-requisitos

*   **Python 3:** Certifique-se de que você tem o Python 3 instalado. Você pode baixá-lo em [https://www.python.org/downloads/](https://www.python.org/downloads/).
*   **Pip:** O gerenciador de pacotes do Python, geralmente instalado junto com o Python.

## Passos

1.  **Descompacte o arquivo:** Extraia o conteúdo do arquivo `mockups_automotivos_ia.zip` para uma pasta de sua preferência no seu computador.

2.  **Abra o Terminal ou Prompt de Comando:**
    *   **Windows:** Procure por "cmd" ou "PowerShell".
    *   **macOS:** Procure por "Terminal".
    *   **Linux:** Use o terminal padrão da sua distribuição.

3.  **Navegue até a pasta:** Use o comando `cd` para navegar até a pasta onde você descompactou os arquivos. Por exemplo:
    ```bash
    cd caminho/para/a/pasta/mockups
    ```
    Substitua `caminho/para/a/pasta/mockups` pelo caminho real no seu sistema.

4.  **Crie um ambiente virtual (Recomendado):** É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv venv
    ```
    Ative o ambiente virtual:
    *   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

5.  **Instale as dependências:** Use o pip para instalar as bibliotecas necessárias listadas no arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

6.  **Execute a aplicação Streamlit:** Agora você pode iniciar a aplicação.
    ```bash
    streamlit run app.py
    ```

7.  **Visualize no navegador:** O Streamlit geralmente abre automaticamente uma aba no seu navegador padrão com os mockups. Se não abrir, o terminal mostrará os endereços (Local URL e Network URL) que você pode copiar e colar no seu navegador para acessar a aplicação.

## Solução de Problemas

*   **Erro de fonte:** Se encontrar erros relacionados a fontes (como `IOError: cannot open resource`), pode ser necessário instalar fontes TrueType padrão no seu sistema (como a Arial) ou ajustar o código em `app.py` para usar uma fonte disponível.
*   **Comando `streamlit` não encontrado:** Certifique-se de que o ambiente virtual está ativado e que as dependências foram instaladas corretamente.

Aproveite a visualização dos mockups!
