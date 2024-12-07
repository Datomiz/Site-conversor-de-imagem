# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:02:38 2024

@author: user
"""


import streamlit as st
from PIL import Image
import pillow_avif
import os

st.set_page_config(layout = "centered")

st.title("Conversor de imagens para png")

st.write("Converta aquelas imagens chatas .webp para pngs")

arquivo = st.file_uploader(label = "Upload Imagem",
                 type = ["png","jpg","jpeg","webp","AVIF"],
                 help = "Clique para dar upload sua imagem")


if arquivo != "" and arquivo != None:
        
    arquivos = os.listdir()
    for i in arquivos:
        if ".png" in i:
            #print(i)
            os.remove(i)
    
    nome = arquivo.name
    
    Imagem = Image.open(arquivo)
    
    path_dps_ponto = nome[:nome.find(".")]
    
    png = Imagem.convert("RGBA")
    
    png.save(path_dps_ponto + ".png")   
    
    with open(path_dps_ponto + ".png", "rb") as file:
    
        st.download_button(label = f"Baixe {path_dps_ponto}.png",
                               data = file,
                               file_name = path_dps_ponto + ".png",
                               help = "Clique para baixar sua imagem convertida",
                               icon = "💾",
                               mime = "image/png")

