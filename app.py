import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import base64
from io import BytesIO

MOCKUP_DIR = "mockups"
MOCKUP_FILES = [
    "login.png",
    "vehicle_selection.png",
    "diagnostic.png",
    "results.png",
    "upload.png",
    "recognition.png",
    "schematic.png",
    "dashboard.png",
    "knowledge.png",
]

# Configuração da página
st.set_page_config(
    page_title="Mockups - IA para Eletrônica Automotiva",
    page_icon="🚗",
    layout="wide"
)

# Função para criar imagens de mockup
def create_mockup(width, height, title, elements=None, bg_color="#f0f2f6", theme="light"):
    # Criar imagem base
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Definir cores com base no tema
    if theme == "dark":
        text_color = "#FFFFFF"
        accent_color = "#4287f5"
        secondary_bg = "#2c3e50"
    else:
        text_color = "#333333"
        accent_color = "#2c7be5"
        secondary_bg = "#e9ecef"
    
    # Desenhar cabeçalho
    draw.rectangle([(0, 0), (width, 60)], fill=accent_color)
    
    # Tentar carregar fonte, se falhar usar fonte padrão
    try:
        font_title = ImageFont.truetype("arial.ttf", 24)
        font_normal = ImageFont.truetype("arial.ttf", 16)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        font_title = ImageFont.load_default()
        font_normal = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Adicionar título
    draw.text((20, 15), title, fill="#FFFFFF", font=font_title)
    
    # Adicionar elementos personalizados se fornecidos
    if elements:
        for elem in elements:
            elem_type = elem.get("type")
            x, y = elem.get("position", (0, 0))
            
            if elem_type == "text":
                draw.text((x, y), elem.get("content", ""), fill=elem.get("color", text_color), font=font_normal)
            
            elif elem_type == "rectangle":
                width_rect = elem.get("width", 100)
                height_rect = elem.get("height", 40)
                draw.rectangle([(x, y), (x + width_rect, y + height_rect)], 
                              fill=elem.get("fill", secondary_bg),
                              outline=elem.get("outline", accent_color))
            
            elif elem_type == "button":
                width_btn = elem.get("width", 120)
                height_btn = elem.get("height", 40)
                draw.rectangle([(x, y), (x + width_btn, y + height_btn)], 
                              fill=elem.get("fill", accent_color),
                              outline=elem.get("outline", "#1a5cb0"))
                
                # Texto do botão
                btn_text = elem.get("text", "Botão")
                # Calcular tamanho do texto usando textbbox
                bbox = draw.textbbox((0, 0), btn_text, font=font_normal)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                text_x = x + (width_btn - text_w) // 2
                text_y = y + (height_btn - text_h) // 2
                draw.text((text_x, text_y), btn_text, fill="#FFFFFF", font=font_normal)
            
            elif elem_type == "input":
                width_input = elem.get("width", 200)
                height_input = elem.get("height", 40)
                draw.rectangle([(x, y), (x + width_input, y + height_input)], 
                              fill="#FFFFFF",
                              outline="#cccccc")
                
                # Placeholder
                placeholder = elem.get("placeholder", "")
                draw.text((x + 10, y + 10), placeholder, fill="#999999", font=font_normal)
            
            elif elem_type == "image_placeholder":
                width_img = elem.get("width", 150)
                height_img = elem.get("height", 150)
                draw.rectangle([(x, y), (x + width_img, y + height_img)], 
                              fill="#e0e0e0",
                              outline="#cccccc")
                
                # Ícone de imagem
                icon_text = "📷"
                draw.text((x + width_img//2 - 10, y + height_img//2 - 10), icon_text, fill="#999999", font=font_title)
            
            elif elem_type == "card":
                width_card = elem.get("width", 300)
                height_card = elem.get("height", 200)
                draw.rectangle([(x, y), (x + width_card, y + height_card)], 
                              fill="#FFFFFF",
                              outline="#dddddd")
                
                # Título do card
                card_title = elem.get("title", "")
                draw.text((x + 15, y + 15), card_title, fill=text_color, font=font_normal)
                
                # Conteúdo do card
                card_content = elem.get("content", "")
                draw.text((x + 15, y + 50), card_content, fill=text_color, font=font_small)
            
            elif elem_type == "menu":
                menu_items = elem.get("items", [])
                item_height = 40
                menu_width = elem.get("width", 200)
                
                for i, item in enumerate(menu_items):
                    item_y = y + (i * item_height)
                    # Fundo do item
                    draw.rectangle([(x, item_y), (x + menu_width, item_y + item_height)], 
                                  fill=secondary_bg if i % 2 == 0 else "#FFFFFF")
                    # Texto do item
                    draw.text((x + 15, item_y + 10), item, fill=text_color, font=font_normal)
    
    return img

# Função para converter imagem para base64 (para exibição no Streamlit)
def get_image_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Função para salvar mockup
def save_mockup(img, filename):
    os.makedirs(MOCKUP_DIR, exist_ok=True)
    filepath = os.path.join(MOCKUP_DIR, filename)
    img.save(filepath)
    return filepath

# Função para criar e salvar todos os mockups
def create_all_mockups():
    mockups = {}
    
    # 1. Tela de Login
    login_elements = [
        {"type": "text", "position": (width//2-150, 100), "content": "Diagnóstico Inteligente Automotivo", "color": "#333333"},
        {"type": "text", "position": (width//2-100, 150), "content": "Acesso ao Sistema", "color": "#666666"},
        {"type": "text", "position": (width//2-150, 200), "content": "Usuário:", "color": "#333333"},
        {"type": "input", "position": (width//2-150, 230), "width": 300, "placeholder": "Digite seu nome de usuário"},
        {"type": "text", "position": (width//2-150, 290), "content": "Senha:", "color": "#333333"},
        {"type": "input", "position": (width//2-150, 320), "width": 300, "placeholder": "Digite sua senha"},
        {"type": "button", "position": (width//2-150, 390), "width": 300, "text": "Entrar"},
        {"type": "text", "position": (width//2-100, 450), "content": "Esqueceu sua senha?", "color": "#2c7be5"},
    ]
    login_img = create_mockup(width, height, "Login - IA para Eletrônica Automotiva", login_elements)
    mockups["login"] = save_mockup(login_img, "login.png")
    
    # 2. Tela de Seleção de Veículo
    vehicle_elements = [
        {"type": "text", "position": (20, 80), "content": "Selecione o Veículo", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Marca:", "color": "#666666"},
        {"type": "input", "position": (20, 150), "width": 300, "placeholder": "Selecione a marca"},
        {"type": "text", "position": (350, 120), "content": "Modelo:", "color": "#666666"},
        {"type": "input", "position": (350, 150), "width": 300, "placeholder": "Selecione o modelo"},
        {"type": "text", "position": (20, 210), "content": "Ano:", "color": "#666666"},
        {"type": "input", "position": (20, 240), "width": 300, "placeholder": "Selecione o ano"},
        {"type": "text", "position": (350, 210), "content": "Motor:", "color": "#666666"},
        {"type": "input", "position": (350, 240), "width": 300, "placeholder": "Selecione o motor"},
        {"type": "text", "position": (20, 300), "content": "Ou insira o código do chassi:", "color": "#666666"},
        {"type": "input", "position": (20, 330), "width": 630, "placeholder": "Digite o código do chassi"},
        {"type": "button", "position": (530, 390), "width": 120, "text": "Continuar"},
        {"type": "text", "position": (20, 390), "content": "Veículos recentes:", "color": "#333333"},
        {"type": "card", "position": (20, 430), "width": 200, "height": 100, "title": "Fiat Uno 2019", "content": "Motor 1.0 Fire\nÚltimo acesso: 25/05/2025"},
        {"type": "card", "position": (240, 430), "width": 200, "height": 100, "title": "VW Gol 2018", "content": "Motor 1.6 MSI\nÚltimo acesso: 20/05/2025"},
        {"type": "card", "position": (460, 430), "width": 200, "height": 100, "title": "Toyota Corolla 2020", "content": "Motor 2.0 Flex\nÚltimo acesso: 15/05/2025"},
    ]
    vehicle_img = create_mockup(width, height, "Seleção de Veículo", vehicle_elements)
    mockups["vehicle_selection"] = save_mockup(vehicle_img, "vehicle_selection.png")
    
    # 3. Interface de Diagnóstico
    diagnostic_elements = [
        {"type": "text", "position": (20, 80), "content": "Diagnóstico Guiado - VW Gol 2018 (Motor 1.6 MSI)", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Problema relatado: Falha na partida", "color": "#666666"},
        {"type": "text", "position": (20, 160), "content": "Passo 1 de 5: Verificação da bateria", "color": "#333333"},
        {"type": "text", "position": (20, 200), "content": "Realize a medição da tensão da bateria com o veículo desligado:", "color": "#666666"},
        {"type": "input", "position": (20, 230), "width": 200, "placeholder": "Digite a tensão (V)"},
        {"type": "button", "position": (240, 230), "width": 120, "text": "Confirmar"},
        {"type": "text", "position": (20, 280), "content": "Histórico de verificações:", "color": "#333333"},
        {"type": "rectangle", "position": (20, 310), "width": 630, "height": 150},
        {"type": "text", "position": (30, 320), "content": "• Tensão da bateria: 12.3V (Dentro do esperado: 12.0V - 12.8V)", "color": "#333333"},
        {"type": "text", "position": (30, 350), "content": "• Teste de carga da bateria: Aprovado", "color": "#333333"},
        {"type": "text", "position": (30, 380), "content": "• Verificação visual dos cabos: Sem oxidação", "color": "#333333"},
        {"type": "text", "position": (30, 410), "content": "• Teste do motor de arranque: Pendente", "color": "#999999"},
        {"type": "text", "position": (20, 480), "content": "Próxima verificação recomendada:", "color": "#333333"},
        {"type": "card", "position": (20, 510), "width": 630, "height": 80, "title": "Verificar tensão nos terminais do motor de arranque durante a tentativa de partida", 
         "content": "Conecte o multímetro aos terminais e peça para um auxiliar tentar dar a partida. Registre a tensão."},
        {"type": "button", "position": (530, 610), "width": 120, "text": "Próximo Passo"},
        {"type": "button", "position": (390, 610), "width": 120, "text": "Sugerir Solução"},
    ]
    diagnostic_img = create_mockup(width, height, "Diagnóstico Guiado", diagnostic_elements)
    mockups["diagnostic"] = save_mockup(diagnostic_img, "diagnostic.png")
    
    # 4. Visualização de Resultados
    results_elements = [
        {"type": "text", "position": (20, 80), "content": "Resultados do Diagnóstico - VW Gol 2018 (Motor 1.6 MSI)", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Problema identificado: Falha no relé de partida", "color": "#2c7be5"},
        {"type": "text", "position": (20, 160), "content": "Resumo das verificações:", "color": "#333333"},
        {"type": "rectangle", "position": (20, 190), "width": 630, "height": 180},
        {"type": "text", "position": (30, 200), "content": "• Tensão da bateria: 12.3V (Normal)", "color": "#333333"},
        {"type": "text", "position": (30, 230), "content": "• Teste de carga da bateria: Aprovado", "color": "#333333"},
        {"type": "text", "position": (30, 260), "content": "• Verificação visual dos cabos: Sem oxidação", "color": "#333333"},
        {"type": "text", "position": (30, 290), "content": "• Tensão nos terminais do motor de arranque: 0.3V (Abaixo do esperado: >10V)", "color": "#ff0000"},
        {"type": "text", "position": (30, 320), "content": "• Teste do relé de partida: Falha detectada", "color": "#ff0000"},
        {"type": "text", "position": (30, 350), "content": "• Verificação do chicote elétrico: Sem danos visíveis", "color": "#333333"},
        {"type": "text", "position": (20, 390), "content": "Solução recomendada:", "color": "#333333"},
        {"type": "card", "position": (20, 420), "width": 630, "height": 100, "title": "Substituição do relé de partida", 
         "content": "O relé de partida apresenta falha e não está enviando corrente suficiente ao motor de arranque.\nLocalização: Caixa de fusíveis principal, posição R7. Código da peça: 5U0 951 253 A"},
        {"type": "text", "position": (20, 540), "content": "Esquema elétrico relacionado:", "color": "#333333"},
        {"type": "image_placeholder", "position": (20, 570), "width": 630, "height": 200},
        {"type": "button", "position": (530, 790), "width": 120, "text": "Finalizar"},
        {"type": "button", "position": (390, 790), "width": 120, "text": "Imprimir"},
    ]
    results_img = create_mockup(width, height, "Resultados do Diagnóstico", results_elements)
    mockups["results"] = save_mockup(results_img, "results.png")
    
    # 5. Interface de Upload/Captura de Imagem
    upload_elements = [
        {"type": "text", "position": (20, 80), "content": "Interpretação Visual - VW Gol 2018", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Selecione o tipo de imagem:", "color": "#666666"},
        {"type": "button", "position": (20, 150), "width": 150, "text": "Módulo ECU"},
        {"type": "button", "position": (190, 150), "width": 150, "text": "Etiqueta"},
        {"type": "button", "position": (360, 150), "width": 150, "text": "Componente"},
        {"type": "button", "position": (530, 150), "width": 150, "text": "Esquema"},
        {"type": "text", "position": (20, 210), "content": "Envie ou capture a imagem:", "color": "#333333"},
        {"type": "rectangle", "position": (20, 240), "width": 630, "height": 300},
        {"type": "image_placeholder", "position": (235, 290), "width": 200, "height": 200},
        {"type": "button", "position": (20, 560), "width": 200, "text": "Carregar Imagem"},
        {"type": "button", "position": (240, 560), "width": 200, "text": "Usar Câmera"},
        {"type": "button", "position": (460, 560), "width": 190, "text": "Analisar Imagem"},
        {"type": "text", "position": (20, 610), "content": "Dicas:", "color": "#333333"},
        {"type": "text", "position": (20, 640), "content": "• Certifique-se de que a imagem está bem iluminada e focada", "color": "#666666"},
        {"type": "text", "position": (20, 670), "content": "• Evite reflexos e sombras sobre o componente", "color": "#666666"},
        {"type": "text", "position": (20, 700), "content": "• Para etiquetas, aproxime o máximo possível mantendo a legibilidade", "color": "#666666"},
    ]
    upload_img = create_mockup(width, height, "Upload/Captura de Imagem", upload_elements)
    mockups["upload"] = save_mockup(upload_img, "upload.png")
    
    # 6. Reconhecimento de Componentes
    recognition_elements = [
        {"type": "text", "position": (20, 80), "content": "Reconhecimento de Componentes - Módulo ECU", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Componentes identificados:", "color": "#666666"},
        {"type": "image_placeholder", "position": (20, 150), "width": 300, "height": 300},
        {"type": "rectangle", "position": (340, 150), "width": 310, "height": 300},
        {"type": "text", "position": (350, 160), "content": "Informações do Componente", "color": "#333333"},
        {"type": "text", "position": (350, 190), "content": "Tipo: Módulo de Controle do Motor (ECU)", "color": "#666666"},
        {"type": "text", "position": (350, 220), "content": "Fabricante: Bosch", "color": "#666666"},
        {"type": "text", "position": (350, 250), "content": "Número de Série: 032 906 032 BF", "color": "#666666"},
        {"type": "text", "position": (350, 280), "content": "Aplicação: VW Gol 1.6 MSI (2017-2019)", "color": "#666666"},
        {"type": "text", "position": (350, 310), "content": "Compatibilidade: Original", "color": "#666666"},
        {"type": "text", "position": (350, 340), "content": "Status: Componente identificado com sucesso", "color": "#2c7be5"},
        {"type": "button", "position": (350, 380), "width": 300, "text": "Ver Esquema Elétrico"},
        {"type": "text", "position": (20, 470), "content": "Histórico de diagnósticos deste componente:", "color": "#333333"},
        {"type": "card", "position": (20, 500), "width": 300, "height": 80, "title": "Falha P0120", 
         "content": "Sensor de posição do acelerador - Circuito aberto\nFrequência: Alta (23 casos registrados)"},
        {"type": "card", "position": (340, 500), "width": 300, "height": 80, "title": "Falha P0322", 
         "content": "Sensor de rotação - Sem sinal\nFrequência: Média (12 casos registrados)"},
        {"type": "card", "position": (20, 600), "width": 300, "height": 80, "title": "Falha P0505", 
         "content": "Sistema de controle de marcha lenta\nFrequência: Baixa (5 casos registrados)"},
        {"type": "card", "position": (340, 600), "width": 300, "height": 80, "title": "Falha P0130", 
         "content": "Sensor de oxigênio - Circuito defeituoso\nFrequência: Baixa (3 casos registrados)"},
        {"type": "button", "position": (530, 700), "width": 120, "text": "Exportar Dados"},
    ]
    recognition_img = create_mockup(width, height, "Reconhecimento de Componentes", recognition_elements)
    mockups["recognition"] = save_mockup(recognition_img, "recognition.png")
    
    # 7. Visualização de Esquemas Elétricos
    schematic_elements = [
        {"type": "text", "position": (20, 80), "content": "Esquema Elétrico - Módulo ECU VW Gol 1.6 MSI", "color": "#333333"},
        {"type": "image_placeholder", "position": (20, 120), "width": 630, "height": 400},
        {"type": "text", "position": (20, 540), "content": "Legenda de Componentes:", "color": "#333333"},
        {"type": "text", "position": (20, 570), "content": "1. Módulo ECU (032 906 032 BF)", "color": "#666666"},
        {"type": "text", "position": (20, 600), "content": "2. Sensor de posição do acelerador (G79)", "color": "#666666"},
        {"type": "text", "position": (20, 630), "content": "3. Sensor de rotação do motor (G28)", "color": "#666666"},
        {"type": "text", "position": (20, 660), "content": "4. Sensor de oxigênio pré-catalisador (G39)", "color": "#666666"},
        {"type": "text", "position": (350, 570), "content": "5. Válvula EGR (N18)", "color": "#666666"},
        {"type": "text", "position": (350, 600), "content": "6. Bobina de ignição (N70)", "color": "#666666"},
        {"type": "text", "position": (350, 630), "content": "7. Injetores de combustível (N30-N33)", "color": "#666666"},
        {"type": "text", "position": (350, 660), "content": "8. Relé da bomba de combustível (J17)", "color": "#666666"},
        {"type": "button", "position": (20, 700), "width": 150, "text": "Ampliar"},
        {"type": "button", "position": (190, 700), "width": 150, "text": "Imprimir"},
        {"type": "button", "position": (360, 700), "width": 150, "text": "Salvar PDF"},
        {"type": "button", "position": (530, 700), "width": 120, "text": "Voltar"},
    ]
    schematic_img = create_mockup(width, height, "Esquema Elétrico", schematic_elements)
    mockups["schematic"] = save_mockup(schematic_img, "schematic.png")
    
    # 8. Dashboard Principal
    dashboard_elements = [
        {"type": "text", "position": (20, 80), "content": "Dashboard - Visão Geral", "color": "#333333"},
        {"type": "card", "position": (20, 120), "width": 200, "height": 100, "title": "Diagnósticos Realizados", "content": "Total: 157\nEste mês: 23\nHoje: 3"},
        {"type": "card", "position": (240, 120), "width": 200, "height": 100, "title": "Taxa de Sucesso", "content": "Geral: 92%\nEste mês: 95%\nComponentes: 89%"},
        {"type": "card", "position": (460, 120), "width": 200, "height": 100, "title": "Tempo Médio", "content": "Diagnóstico: 12 min\nInterpretação: 3 min\nTotal: 15 min"},
        {"type": "text", "position": (20, 240), "content": "Diagnósticos Recentes:", "color": "#333333"},
        {"type": "rectangle", "position": (20, 270), "width": 630, "height": 150},
        {"type": "text", "position": (30, 280), "content": "Data       | Veículo           | Problema                  | Solução                  | Mecânico", "color": "#333333"},
        {"type": "text", "position": (30, 310), "content": "28/05/2025 | VW Gol 2018      | Falha na partida          | Substituição de relé     | Carlos Silva", "color": "#333333"},
        {"type": "text", "position": (30, 340), "content": "27/05/2025 | Fiat Uno 2019    | Luz de injeção acesa      | Sensor MAP substituído   | Maria Oliveira", "color": "#333333"},
        {"type": "text", "position": (30, 370), "content": "27/05/2025 | Toyota Corolla 20| Consumo elevado           | Limpeza de bicos         | João Pereira", "color": "#333333"},
        {"type": "text", "position": (30, 400), "content": "26/05/2025 | Honda Civic 2021 | Ar condicionado sem frio  | Recarga de gás           | Carlos Silva", "color": "#333333"},
        {"type": "text", "position": (20, 440), "content": "Problemas Mais Frequentes:", "color": "#333333"},
        {"type": "image_placeholder", "position": (20, 470), "width": 300, "height": 200},
        {"type": "text", "position": (340, 440), "content": "Componentes Mais Substituídos:", "color": "#333333"},
        {"type": "image_placeholder", "position": (340, 470), "width": 300, "height": 200},
        {"type": "text", "position": (20, 690), "content": "Base de Conhecimento:", "color": "#333333"},
        {"type": "button", "position": (200, 690), "width": 150, "text": "Acessar"},
        {"type": "text", "position": (370, 690), "content": "Relatórios:", "color": "#333333"},
        {"type": "button", "position": (470, 690), "width": 180, "text": "Gerar Relatório"},
    ]
    dashboard_img = create_mockup(width, height, "Dashboard Principal", dashboard_elements)
    mockups["dashboard"] = save_mockup(dashboard_img, "dashboard.png")
    
    # 9. Base de Conhecimento
    knowledge_elements = [
        {"type": "text", "position": (20, 80), "content": "Base de Conhecimento", "color": "#333333"},
        {"type": "text", "position": (20, 120), "content": "Pesquisar:", "color": "#666666"},
        {"type": "input", "position": (100, 120), "width": 450, "placeholder": "Digite o problema, componente ou modelo de veículo"},
        {"type": "button", "position": (570, 120), "width": 80, "text": "Buscar"},
        {"type": "text", "position": (20, 170), "content": "Filtrar por:", "color": "#666666"},
        {"type": "button", "position": (100, 170), "width": 100, "text": "Todos"},
        {"type": "button", "position": (210, 170), "width": 100, "text": "Elétricos"},
        {"type": "button", "position": (320, 170), "width": 100, "text": "Mecânicos"},
        {"type": "button", "position": (430, 170), "width": 100, "text": "Sensores"},
        {"type": "button", "position": (540, 170), "width": 110, "text": "Injeção"},
        {"type": "text", "position": (20, 220), "content": "Soluções Populares:", "color": "#333333"},
        {"type": "card", "position": (20, 250), "width": 630, "height": 100, "title": "Falha P0120 - Sensor de posição do acelerador", 
         "content": "Sintomas: Marcha lenta irregular, aceleração instável, luz de injeção acesa.\nSolução: Verificar conexões do sensor TPS, medir resistência (deve estar entre 0.5-4.5 kΩ), substituir se necessário."},
        {"type": "card", "position": (20, 370), "width": 630, "height": 100, "title": "Falha na Partida - Relé de Partida", 
         "content": "Sintomas: Motor de arranque não gira, sem ruído de partida, luzes do painel funcionam normalmente.\nSolução: Testar tensão nos terminais do motor de arranque, verificar relé na caixa de fusíveis, substituir relé."},
        {"type": "card", "position": (20, 490), "width": 630, "height": 100, "title": "Ar Condicionado sem Refrigeração", 
         "content": "Sintomas: Ventilador funciona mas ar não resfria, compressor não liga.\nSolução: Verificar pressão do gás, testar sensor de pressão, verificar relé do compressor e embreagem."},
        {"type": "text", "position": (20, 610), "content": "Contribuir com Conhecimento:", "color": "#333333"},
        {"type": "button", "position": (250, 610), "width": 200, "text": "Adicionar Nova Solução"},
        {"type": "text", "position": (20, 660), "content": "Estatísticas da Base:", "color": "#666666"},
        {"type": "text", "position": (20, 690), "content": "Total de soluções: 1.247 | Contribuições este mês: 37 | Soluções verificadas: 89%", "color": "#666666"},
    ]
    knowledge_img = create_mockup(width, height, "Base de Conhecimento", knowledge_elements)
    mockups["knowledge"] = save_mockup(knowledge_img, "knowledge.png")
    
    return mockups

# Definir dimensões padrão para os mockups
width, height = 670, 850

# Gerar mockups apenas quando necessÃ¡rio
@st.cache_resource
def ensure_mockups_generated():
    missing_files = [
        filename
        for filename in MOCKUP_FILES
        if not os.path.exists(os.path.join(MOCKUP_DIR, filename))
    ]
    if missing_files:
        create_all_mockups()

ensure_mockups_generated()

language = st.selectbox("Language / Idioma", ["Portuguese", "English"], index=0)

# English rendering branch; the original Portuguese flow stays below.
if language == "English":
    st.title("Mockups - AI for Automotive Electronics")
    st.markdown(
        """
## Project Overview
This project demonstrates an AI-assisted automotive electronics prototype focused on:
- guided diagnostics,
- visual interpretation of components and schematics,
- dashboard and knowledge-base workflows.
"""
    )

    tab1, tab2, tab3 = st.tabs(["Guided Diagnosis", "Visual Interpretation", "Dashboard"])

    def en_mockup(title, subtitle):
        elements = [
            {"type": "text", "position": (20, 90), "content": subtitle, "color": "#333333"},
            {"type": "rectangle", "position": (20, 130), "width": 630, "height": 620},
            {"type": "text", "position": (40, 160), "content": "English preview mockup", "color": "#666666"},
        ]
        return create_mockup(width, height, title, elements)

    with tab1:
        st.header("Guided Diagnosis Flow")
        st.markdown("### 1. Login Screen")
        st.image(en_mockup("Login", "User authentication and access flow"))
        st.markdown("**Description:** Entry point with user identification and access control.")

        st.markdown("### 2. Vehicle Selection")
        st.image(en_mockup("Vehicle Selection", "Select make, model, year, and engine"))
        st.markdown("**Description:** Vehicle lookup by make/model/year/engine or chassis code.")

        st.markdown("### 3. Diagnostic Interface")
        st.image(en_mockup("Diagnostic Interface", "Guided checklist and test results"))
        st.markdown("**Description:** Step-by-step diagnosis with test results and next actions.")

        st.markdown("### 4. Results View")
        st.image(en_mockup("Results View", "Diagnosis summary and recommended repair"))
        st.markdown("**Description:** Final diagnosis summary and recommended repair path.")

    with tab2:
        st.header("Visual Interpretation System")
        st.markdown("### 1. Image Upload/Capture")
        st.image(en_mockup("Image Upload/Capture", "Upload or capture component images"))
        st.markdown("**Description:** Upload or capture images of modules, labels, components, or schematics.")

        st.markdown("### 2. Component Recognition")
        st.image(en_mockup("Component Recognition", "Detected component details"))
        st.markdown("**Description:** Component details and related history context.")

        st.markdown("### 3. Electrical Schematics View")
        st.image(en_mockup("Electrical Schematics", "Related diagram and legend"))
        st.markdown("**Description:** Related schematic with component legend and export options.")

        st.markdown("---")
        st.subheader("Interactive Upload/Capture Test")
        st.caption("Functional section to validate image upload in the prototype.")

        image_type = st.selectbox(
            "Image type",
            ["ECU Module", "Label", "Component", "Schematic"],
            index=2,
            key="image_type_en",
        )

        col_upload, col_camera = st.columns(2)
        uploaded_file = None
        camera_file = None

        with col_upload:
            uploaded_file = st.file_uploader(
                "Upload image",
                type=["png", "jpg", "jpeg", "webp"],
                help="Upload an image of the component or label.",
                key="upload_en",
            )

        with col_camera:
            enable_camera = st.checkbox(
                "Enable camera capture",
                value=False,
                help="Camera permission is requested only after enabling this option.",
                key="enable_camera_en",
            )
            if enable_camera:
                camera_file = st.camera_input("Capture with camera", key="camera_en")
            else:
                st.caption("Camera is disabled by default. Enable above to capture.")

        selected_image_file = uploaded_file or camera_file

        if selected_image_file is not None:
            image = Image.open(selected_image_file)
            st.image(image, caption=f"Received image ({image_type})", use_container_width=True)

            if st.button("Analyze image", type="primary", key="analyze_en"):
                with st.spinner("Running sample analysis..."):
                    width_img, height_img = image.size
                    st.success("Image processed successfully.")
                    st.write(f"Detected resolution: {width_img}x{height_img}")
                    st.write(f"Color mode: {image.mode}")
                    st.info(
                        "This result is a placeholder. "
                        "Connect your computer vision model here for real diagnostics."
                    )
        else:
            st.info("Upload an image or enable the camera to run analysis.")

    with tab3:
        st.header("Dashboard and Knowledge Base")
        st.markdown("### 1. Main Dashboard")
        st.image(en_mockup("Main Dashboard", "Usage metrics and diagnosis indicators"))
        st.markdown("**Description:** Operational overview with diagnostics and usage indicators.")

        st.markdown("### 2. Knowledge Base")
        st.image(en_mockup("Knowledge Base", "Solutions and technical references"))
        st.markdown("**Description:** Technical repository organized by issue type and component.")

    st.markdown(
        """
## Implemented Technical Resources
- **Guided Diagnosis:** intelligent checklist and decision flow
- **Visual Interpretation:** component/label/schematic recognition path
- **Knowledge Base:** structure for issue and solution cataloging
- **Data Integration:** foundation for technical data ingestion
- **Responsive Interface:** usable across workshop device types
"""
    )
    st.stop()

# Exibir os mockups no Streamlit
st.title("Mockups - IA para Eletrônica Automotiva")

st.markdown("""
## Visão Geral do Projeto
Este projeto desenvolve uma solução de Inteligência Artificial aplicada à eletrônica automotiva, 
focada em auxiliar mecânicos no diagnóstico de falhas e interpretação de esquemas elétricos.
""")

# Exibir os mockups em abas
tab1, tab2, tab3 = st.tabs(["Diagnóstico Guiado", "Interpretação Visual", "Dashboard"])

with tab1:
    st.header("Fluxo de Diagnóstico Guiado")
    st.markdown("### 1. Tela de Login")
    st.image("mockups/login.png")
    st.markdown("""
    **Descrição:** Interface inicial onde o mecânico se identifica no sistema. Permite controle de acesso
    e personalização da experiência com base no histórico do usuário.
    """)
    
    st.markdown("### 2. Seleção de Veículo")
    st.image("mockups/vehicle_selection.png")
    st.markdown("""
    **Descrição:** Permite ao mecânico selecionar o veículo a ser diagnosticado através de marca, modelo, 
    ano e motor, ou diretamente pelo código do chassi. Exibe também veículos recentemente diagnosticados.
    """)
    
    st.markdown("### 3. Interface de Diagnóstico")
    st.image("mockups/diagnostic.png")
    st.markdown("""
    **Descrição:** Guia o mecânico através de um processo de diagnóstico passo a passo, solicitando testes 
    específicos e coletando resultados. A IA analisa as respostas e determina os próximos passos mais relevantes.
    """)
    
    st.markdown("### 4. Visualização de Resultados")
    st.image("mockups/results.png")
    st.markdown("""
    **Descrição:** Apresenta o diagnóstico final com o problema identificado, resumo das verificações realizadas
    e solução recomendada. Inclui informações detalhadas sobre a peça a ser substituída e esquema elétrico relacionado.
    """)

with tab2:
    st.header("Sistema de Interpretação Visual")
    st.markdown("### 1. Upload/Captura de Imagem")
    st.image("mockups/upload.png")
    st.markdown("""
    **Descrição:** Interface para envio ou captura de imagens de componentes, módulos, etiquetas ou esquemas elétricos.
    Inclui dicas para obter imagens de qualidade que facilitem o reconhecimento pela IA.
    """)
    
    st.markdown("### 2. Reconhecimento de Componentes")
    st.image("mockups/recognition.png")
    st.markdown("""
    **Descrição:** Exibe o componente identificado com informações detalhadas como tipo, fabricante, número de série
    e aplicação. Mostra também histórico de diagnósticos relacionados a este componente específico.
    """)
    
    st.markdown("### 3. Visualização de Esquemas Elétricos")
    st.image("mockups/schematic.png")
    st.markdown("""
    **Descrição:** Apresenta o esquema elétrico relacionado ao componente identificado, com legenda detalhada
    dos componentes e suas conexões. Permite ampliar, imprimir ou salvar o esquema em PDF.
    """)

with tab3:
    st.header("Dashboard e Base de Conhecimento")
    st.markdown("### 1. Dashboard Principal")
    st.image("mockups/dashboard.png")
    st.markdown("""
    **Descrição:** Visão geral das atividades de diagnóstico, incluindo estatísticas de uso, taxa de sucesso,
    tempo médio de diagnóstico, histórico recente e gráficos de problemas mais frequentes.
    """)
    
    st.markdown("### 2. Base de Conhecimento")
    st.image("mockups/knowledge.png")
    st.markdown("""
    **Descrição:** Repositório de soluções e informações técnicas organizadas por tipo de problema, componente
    ou modelo de veículo. Permite busca, filtragem e contribuição de novas soluções pelos mecânicos.
    """)

st.markdown("""
## Recursos Técnicos Implementados

- **Diagnóstico Guiado:** Sistema de checklist inteligente baseado em redes neurais e lógica de decisão
- **Interpretação Visual:** Reconhecimento de componentes, etiquetas e esquemas usando visão computacional
- **Base de Conhecimento:** Estruturação de dados de problemas e soluções em categorias
- **Integração de Dados:** Processamento de mensagens de grupos técnicos e manuais de serviço
- **Interface Responsiva:** Design adaptável para uso em diferentes dispositivos na oficina
""")

st.markdown("---")
st.subheader("Teste Interativo de Upload/Captura")
st.caption("Sessao funcional para validar envio de imagem no prototipo.")

image_type_pt = st.selectbox(
    "Tipo de imagem",
    ["Modulo ECU", "Etiqueta", "Componente", "Esquema"],
    index=2,
    key="image_type_pt",
)

col_upload_pt, col_camera_pt = st.columns(2)
uploaded_file_pt = None
camera_file_pt = None

with col_upload_pt:
    uploaded_file_pt = st.file_uploader(
        "Carregar imagem",
        type=["png", "jpg", "jpeg", "webp"],
        help="Envie uma imagem do componente ou etiqueta.",
        key="upload_pt",
    )

with col_camera_pt:
    enable_camera_pt = st.checkbox(
        "Ativar captura por camera",
        value=False,
        help="A camera so sera solicitada apos ativar esta opcao.",
        key="enable_camera_pt",
    )
    if enable_camera_pt:
        camera_file_pt = st.camera_input("Capturar com camera", key="camera_pt")
    else:
        st.caption("Camera desativada por padrao. Ative acima para capturar.")

selected_image_file_pt = uploaded_file_pt or camera_file_pt

if selected_image_file_pt is not None:
    image_pt = Image.open(selected_image_file_pt)
    st.image(image_pt, caption=f"Imagem recebida ({image_type_pt})", use_container_width=True)

    if st.button("Analisar imagem", type="primary", key="analyze_pt"):
        with st.spinner("Executando analise de exemplo..."):
            width_img_pt, height_img_pt = image_pt.size
            st.success("Imagem processada com sucesso.")
            st.write(f"Resolucao detectada: {width_img_pt}x{height_img_pt}")
            st.write(f"Modo de cor: {image_pt.mode}")
            st.info(
                "Este resultado e um placeholder. "
                "Conecte aqui seu modelo de visao computacional para diagnostico real."
            )
else:
    st.info("Envie uma imagem ou ative a camera para habilitar a analise.")
