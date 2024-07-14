# Instalar as bibliotecas necessárias
!pip install -qr https://huggingface.co/briaai/RMBG-1.4/resolve/main/requirements.txt
!pip install gradio
!pip install transformers

# Importar as bibliotecas e carregar o modelo de segmentação de imagem
import gradio as gr
from transformers import pipeline
from PIL import Image

# Carregar o pipeline do modelo
pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)

# Criar a função para remover o fundo da imagem
def remove_background(image):
    pillow_image = pipe(image)  # Aplica a máscara na imagem de entrada e retorna uma imagem Pillow
    return pillow_image

# Configurar a interface Gradio
iface = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Remove Background",
    description="Upload an image to remove the background using the RMBG-1.4 model from Hugging Face."
)

# Executar a interface
iface.launch()
