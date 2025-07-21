"""
Funciones auxiliares y helpers para la UI
"""

import streamlit as st
from typing import List

def render_protected_command(command_text: str, language: str = "bash") -> str:
    """
    Renderiza un comando con protección anti-traducción máxima
    """
    protected_html = f"""
    <div class="protected-command" 
         translate="no" 
         data-translate="no" 
         data-google="notranslate"
         lang="en"
         dir="ltr">
        <code translate="no" 
              data-translate="no" 
              data-google="notranslate"
              class="language-{language}">
            {command_text}
        </code>
    </div>
    """
    return protected_html

def render_command_option(option_text: str, option_letter: str) -> None:
    protected_html = f"""
    <div style="margin: 8px 0; padding: 12px; background-color: #f8f9fa; 
                border: 1px solid #dee2e6; border-radius: 6px;">
        <div style="font-weight: bold; margin-bottom: 4px; color: #495057;">
            Opción {option_letter}:
        </div>
        <div class="protected-command" 
             translate="no" 
             data-translate="no" 
             data-google="notranslate"
             lang="en">
            <code translate="no" 
                  data-translate="no" 
                  data-google="notranslate"
                  style="font-family: 'Consolas', 'Courier New', monospace; 
                         font-size: 14px; color: #212529; background: transparent;">
                {option_text}
            </code>
        </div>
    </div>
    """
    st.markdown(protected_html, unsafe_allow_html=True)

def create_info_box(title: str, content: str, box_type: str = "info"):
    if box_type == "info":
        st.info(f"**{title}**\n\n{content}")
    elif box_type == "warning":
        st.warning(f"**{title}**\n\n{content}")
    elif box_type == "success":
        st.success(f"**{title}**\n\n{content}")
    elif box_type == "error":
        st.error(f"**{title}**\n\n{content}")

def create_code_example(title: str, code: str, language: str = "bash", explanation: str = ""):
    st.subheader(title)
    st.code(code, language=language)
    if explanation:
        st.markdown(f"**Explicación:** {explanation}")

def create_comparison_table(cmd_data: List[str], ps_data: List[str], headers: List[str]):
    import pandas as pd
    df = pd.DataFrame({
        headers[0]: cmd_data,
        headers[1]: ps_data
    })
    st.dataframe(df, use_container_width=True)

def create_learning_objective_card(objectives: List[str]):
    with st.container():
        st.markdown("### 🎯 Objetivos de Aprendizaje")
        for i, objective in enumerate(objectives, 1):
            st.markdown(f"{i}. {objective}")

def create_tip_card(title: str, content: str, tip_type: str = "info"):
    if tip_type == "info":
        st.info(f"**{title}**\n\n{content}")
    elif tip_type == "success":
        st.success(f"**{title}**\n\n{content}")
    elif tip_type == "warning":
        st.warning(f"**{title}**\n\n{content}")
    elif tip_type == "error":
        st.error(f"**{title}**\n\n{content}")

def create_dual_console_demo(cmd_example: str, ps_example: str, description: str = ""):
    from .console_components import ConsoleSimulator
    if description:
        st.markdown(description)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🖤 CMD**")
        cmd_simulator = ConsoleSimulator("cmd")
        cmd_simulator.render(key_suffix="demo_cmd")
    with col2:
        st.markdown("**🔷 PowerShell**")
        ps_simulator = ConsoleSimulator("powershell")
        ps_simulator.render(key_suffix="demo_ps")

def create_command_reference_table(title: str, commands_data: dict):
    st.markdown(f"### {title}")
    st.markdown("""
    <style>
    .command-ref-container {
        background-color: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        margin: 16px 0;
    }
    .command-row {
        display: flex;
        align-items: center;
        padding: 8px 0;
        border-bottom: 1px solid #dee2e6;
    }
    .command-col {
        flex: 1;
        padding: 0 8px;
    }
    .command-code {
        translate: no !important;
        -webkit-translate: no !important;
        font-family: 'Consolas', 'Courier New', monospace !important;
        background-color: #e9ecef !important;
        padding: 4px 8px !important;
        border-radius: 4px !important;
        font-size: 13px !important;
        color: #495057 !important;
        display: inline-block !important;
    }
    </style>
    """, unsafe_allow_html=True)
    available_keys = list(commands_data.keys())
    main_key = None
    for key in ["Comando", "Parámetro", "Verbo", "Cmdlet", "Símbolo"]:
        if key in available_keys:
            main_key = key
            break
    if not main_key:
        main_key = available_keys[0]
    desc_key = None
    for key in ["Función", "Descripción", "Propósito", "Significado"]:
        if key in available_keys:
            desc_key = key
            break
    extra_key = None
    for key in ["Ejemplo", "Alias Comunes"]:
        if key in available_keys:
            extra_key = key
            break
    html_content = '<div class="command-ref-container" translate="no" data-translate="no">'
    html_content += f'''
    <div class="command-row" style="font-weight: bold; background-color: #e9ecef; border-bottom: 2px solid #dee2e6;">
        <div class="command-col">{main_key}</div>
    '''
    if desc_key:
        html_content += f'<div class="command-col">{desc_key}</div>'
    if extra_key:
        html_content += f'<div class="command-col">{extra_key}</div>'
    html_content += '</div>'
    num_entries = len(commands_data[main_key])
    for i in range(num_entries):
        html_content += '<div class="command-row">'
        main_value = commands_data[main_key][i]
        comandos_es_en = {
            "Sustantivo-Verbo": "Verb-Noun",
            "Verbo-Sustantivo": "Verb-Noun",
            "Comando-Argumento": "Command-Argument",
            "Función-Parámetro": "Function-Parameter",
            "Mostrar": "Show",
            "Listar": "List",
            "Ayuda": "Help",
            "Ejecutar": "Run",
            "Eliminar": "Delete",
            "Crear": "Create",
            "Archivo": "File",
            "Directorio": "Directory",
            "Parámetro": "Parameter",
            "Función": "Function",
            "Comando": "Command",
            "Símbolo": "Symbol",
            "Alias": "Alias"
        }
        if main_value in comandos_es_en:
            main_value = comandos_es_en[main_value]
        html_content += f'''
        <div class="command-col">
            <code class="command-code" translate="no" data-translate="no">{main_value}</code>
        </div>
        '''
        if desc_key:
            desc_value = commands_data[desc_key][i]
            html_content += f'<div class="command-col">{desc_value}</div>'
        if extra_key:
            extra_value = commands_data[extra_key][i]
            html_content += f'''
            <div class="command-col">
                <code class="command-code" translate="no" data-translate="no">{extra_value}</code>
            </div>
            '''
        html_content += '</div>'
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)