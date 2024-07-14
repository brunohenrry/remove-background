Claro! Aqui está o README atualizado sem a seção de contribuição:

---

# Remove Background with Gradio and Hugging Face

Este projeto utiliza Gradio para criar uma interface de usuário que remove o fundo de imagens utilizando o modelo de segmentação de imagem RMBG-1.4 da Hugging Face.

## Instalação

### Google Colab

1. Crie um novo notebook no [Google Colab](https://colab.research.google.com/).
2. Copie e cole as células de código abaixo no seu notebook e execute-as na ordem.

### Código no Colab:

```python
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
```

## Uso

1. Execute todas as células no seu notebook do Google Colab.
2. Quando a última célula (que contém `iface.launch()`) for executada, uma interface Gradio será exibida.
3. Faça upload de uma imagem e veja o resultado com o fundo removido.

## Funcionalidades

- **Upload de Imagens:** Carregue uma imagem de qualquer formato compatível.
- **Remoção de Fundo:** O modelo de segmentação de imagem RMBG-1.4 da Hugging Face será utilizado para remover o fundo da imagem.
- **Download da Imagem Processada:** Baixe a imagem com o fundo removido diretamente da interface.

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
