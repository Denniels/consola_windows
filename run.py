"""
🖥️ Curso Interactivo de Consolas Windows: PowerShell y CMD
Script principal para lanzar la aplicación Streamlit

Autor: Daniel Mardones
"""

import streamlit as st
import sys
import os

# Agregar el directorio de la aplicación al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'streamlit_app'))

def main():
    """Función principal que configura y ejecuta la aplicación"""
    
    # Configuración de la página
    st.set_page_config(
        page_title="🖥️ Curso Consolas Windows",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Importar y ejecutar la aplicación principal
    from streamlit_app.app import run_app
    run_app()

if __name__ == "__main__":
    main()
