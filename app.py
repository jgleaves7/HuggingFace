import torch
# Carga del modelo
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

#Carga de modelo optimizada

modelq = AutoModelForCausalLM.from_pretrained("openai-community/gpt2",torch_dtype=torch.float16, device_map="auto", attn_implementation="sdpa")

# Comparativo de uso de memoria
gbsO = model.get_memory_footprint() / 1e9
gbs = modelq.get_memory_footprint() / 1e9

print(f"Numero de parametros modelo Original: {model.num_parameters()}")
print(f"Numero de parametros modelo Optimizado: {modelq.num_parameters()}")
print(f"Memory footprint FP32: {gbsO:.2f} GB")
print(f"Memory footprint FB16: {gbs:.2f} GB")

# Crear función de salida

def Generate(text):
  # eneración de tokens del texto de entrada
  input_ids = tokenizer(text, return_tensors="pt").input_ids
  # Modelos de generación de texto
  output_idsq = modelq.generate(input_ids, do_sample=True,temperature=0.4, repetition_penalty=1.2, max_new_tokens=40)
  output_ids = model.generate(input_ids, do_sample=True,temperature=0.4, repetition_penalty=1.2, max_new_tokens=40)
  # Decodificación de los tokens generados

  decoded_textq = tokenizer.decode(output_idsq[0])
  decoded_text = tokenizer.decode(output_ids[0])
  return f"Generated text sin cuantificación: {decoded_text}/n Generated text con cuantificación: {decoded_textq}"

# Importación de Biblioteca para interface
import gradio as gr

iface = gr.Interface(
    fn=Generate,
    inputs=gr.Textbox(lines=2, placeholder="Escriba una oración aquí... Debe ser en el idioma inglés"),
    outputs=gr.Textbox(placeholder="Ejemplo de texto generado"),
    title="Creador de historias",
    description="Introduce una oración para crear más contexto sobre el texto inicial. El modelo puede generar texto."
    )

iface.launch()
