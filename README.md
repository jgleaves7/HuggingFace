# Modelo Generador de Texto
---
title: Prueba AI Engineer Gradio
emoji: 😻
colorFrom: green
colorTo: indigo
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
license: creativeml-openrail-m
short_description: Prueba Técnica AI Engineer Asdeporte
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

El siguiente programa usa el modelo GPT2 en su función de generador de text. Es decir a partir de una entrada de texto el modelo completará la frase o historia previa.

La información especifica del modelo se encuentra: 
[GPT-2 Especificaciones](https://huggingface.co/docs/transformers/model_doc/gpt2?usage=AutoModel#gpt-2)

**Instrucciones**
Este modelo acepta texto en el idioma inglés
1. En el recuadro de texto que con la etiqueta texto escriba una oración
2. Una vez que la oración se termino de escribir presione el botón naranja submit

El modelo arrojara oraciones que intentarán dar coherencia y continuidad a la oración inicial. 
La primera línea es una oración con el modelo original
La segunda línea es una oración con el modelo optimizado

Los resultados de la cuantificación son los siguientes:
Numero de parametros modelo: 124,439,808
Memory footprint FP32: 0.51 GB
Memory footprint FB16: 0.26 GB

Abra la aplicación con el siguiente link:
https://huggingface.co/spaces/jgleaves7/prueba_AI_engineer_Gradio
