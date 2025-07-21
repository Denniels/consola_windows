"""
Componentes para simulador de consola interactiva
"""

import streamlit as st
import sys
import os

# Agregar utils al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

from command_parser import CommandParser

class ConsoleSimulator:
    """Simulador de consola interactivo con formateo consistente"""
    def __init__(self, console_type: str = "cmd"):
        self.console_type = console_type
        self.parser = CommandParser()
        self._initialize_history()

    def _initialize_history(self):
        if f'{self.console_type}_history' not in st.session_state:
            st.session_state[f'{self.console_type}_history'] = []
        self.history = st.session_state[f'{self.console_type}_history']

    def _build_console_text(self, console_type: str):
        """Construye el texto de consola con formato auténtico"""
        if console_type == "cmd":
            if not self.history:
                # Banner inicial auténtico de CMD
                return """Microsoft Windows [Versión 10.0.19045.3570]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\\Users\\Usuario>"""
            
            lines = [
                "Microsoft Windows [Versión 10.0.19045.3570]",
                "(c) Microsoft Corporation. Todos los derechos reservados.",
                ""
            ]
            
            # Agregar historial de comandos con formato auténtico
            for entry in self.history:
                lines.append(f"C:\\Users\\Usuario>{entry['command']}")
                if entry['output']:
                    # Dividir output en líneas y mantener formato
                    output_lines = entry['output'].split('\n')
                    for line in output_lines:
                        if line.strip():  # Solo agregar líneas no vacías
                            lines.append(line)
                lines.append("")  # Línea vacía entre comandos
            
            lines.append("C:\\Users\\Usuario>")
            return '\n'.join(lines)
            
        else:  # PowerShell
            if not self.history:
                # Banner inicial auténtico de PowerShell
                return """Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

PS C:\\Users\\Usuario>"""
            
            lines = [
                "Windows PowerShell",
                "Copyright (C) Microsoft Corporation. Todos los derechos reservados.",
                ""
            ]
            
            # Agregar historial de comandos con formato auténtico
            for entry in self.history:
                lines.append(f"PS C:\\Users\\Usuario>{entry['command']}")
                if entry['output']:
                    # Dividir output en líneas y mantener formato
                    output_lines = entry['output'].split('\n')
                    for line in output_lines:
                        if line.strip():  # Solo agregar líneas no vacías
                            lines.append(line)
                lines.append("")  # Línea vacía entre comandos
            
            lines.append("PS C:\\Users\\Usuario>")
            return '\n'.join(lines)

    def _apply_console_styles(self, console_type: str):
        """Aplica estilos auténticos de CMD y PowerShell"""
        if console_type == "cmd":
            st.markdown("""
            <style>
            /* Estilos auténticos para CMD - Negro con texto plata */
            div[data-testid="stCodeBlock"] {
                background-color: #000000 !important;
                border: 2px solid #808080 !important;
                border-radius: 0px !important;
                box-shadow: inset 0 0 10px rgba(0,0,0,0.5) !important;
                margin: 8px 0 !important;
            }
            div[data-testid="stCodeBlock"] code {
                color: #c0c0c0 !important;
                background-color: #000000 !important;
                font-family: 'Consolas', 'Lucida Console', 'Courier New', monospace !important;
                font-size: 12px !important;
                font-weight: normal !important;
                line-height: 1.2 !important;
                white-space: pre-wrap !important;
                padding: 8px 12px !important;
            }
            /* Input auténtico de CMD */
            div[data-testid="stTextInput"] input {
                background-color: #000000 !important;
                color: #c0c0c0 !important;
                border: 1px solid #808080 !important;
                border-radius: 0px !important;
                font-family: 'Consolas', 'Lucida Console', 'Courier New', monospace !important;
                font-size: 12px !important;
                font-weight: normal !important;
                padding: 4px 8px !important;
            }
            div[data-testid="stTextInput"] input:focus {
                border-color: #ffffff !important;
                box-shadow: 0 0 3px rgba(255, 255, 255, 0.4) !important;
            }
            </style>
            """, unsafe_allow_html=True)
        else:  # PowerShell
            st.markdown("""
            <style>
            /* Estilos auténticos para PowerShell - Azul oscuro con texto blanco */
            div[data-testid="stCodeBlock"] {
                background-color: #012456 !important;
                border: 2px solid #1e3a8a !important;
                border-radius: 0px !important;
                box-shadow: inset 0 0 10px rgba(1,36,86,0.7) !important;
                margin: 8px 0 !important;
            }
            div[data-testid="stCodeBlock"] code {
                color: #ffffff !important;
                background-color: #012456 !important;
                font-family: 'Consolas', 'Lucida Console', 'Courier New', monospace !important;
                font-size: 12px !important;
                font-weight: normal !important;
                line-height: 1.2 !important;
                white-space: pre-wrap !important;
                padding: 8px 12px !important;
            }
            /* Input auténtico de PowerShell */
            div[data-testid="stTextInput"] input {
                background-color: #012456 !important;
                color: #ffffff !important;
                border: 1px solid #1e3a8a !important;
                border-radius: 0px !important;
                font-family: 'Consolas', 'Lucida Console', 'Courier New', monospace !important;
                font-size: 12px !important;
                font-weight: normal !important;
                padding: 4px 8px !important;
            }
            div[data-testid="stTextInput"] input:focus {
                border-color: #00ffff !important;
                box-shadow: 0 0 3px rgba(0, 255, 255, 0.5) !important;
            }
            </style>
            """, unsafe_allow_html=True)

    def _render_cmd_console(self, height: int, key_suffix: str):
        self._apply_console_styles("cmd")
        console_text = self._build_console_text("cmd")
        st.code(console_text, language=None)
        command = st.text_input(
            "Escribe un comando CMD:", 
            key=f"cmd_input_{key_suffix}", 
            placeholder="Ej: dir, cd, echo Hola",
            help="Presiona Enter o haz clic en Ejecutar para correr el comando"
        )
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("🚀 Ejecutar", key=f"cmd_execute_{key_suffix}", type="primary") and command:
                self._execute_command(command)
                st.rerun()
        with col2:
            if st.button("🗑️ Limpiar", key=f"cmd_clear_{key_suffix}"):
                self.clear_history()
                st.rerun()

    def _render_ps_console(self, height: int, key_suffix: str):
        self._apply_console_styles("powershell")
        console_text = self._build_console_text("powershell")
        st.code(console_text, language=None)
        command = st.text_input(
            "Escribe un comando PowerShell:", 
            key=f"ps_input_{key_suffix}", 
            placeholder="Ej: Get-ChildItem, Get-Date, Write-Host Hola",
            help="Presiona Enter o haz clic en Ejecutar para correr el comando"
        )
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button("🚀 Ejecutar", key=f"ps_execute_{key_suffix}", type="primary") and command:
                self._execute_command(command)
                st.rerun()
        with col2:
            if st.button("🗑️ Limpiar", key=f"ps_clear_{key_suffix}"):
                self.clear_history()
                st.rerun()

    def render(self, height: int = 400, key_suffix: str = ""):
        """Renderiza el simulador de consola con estilos auténticos"""
        if self.console_type == "cmd":
            st.markdown("### ⬛ Símbolo del sistema (CMD)")
            st.markdown("*Simulación auténtica con colores originales de Windows*")
            self._render_cmd_console(height, key_suffix)
        else:
            st.markdown("### 🔷 Windows PowerShell") 
            st.markdown("*Simulación auténtica con colores originales de PowerShell*")
            self._render_ps_console(height, key_suffix)

    def _execute_command(self, command: str):
        output = self.parser.parse_command(command, self.console_type)
        self.history.append({
            'command': command,
            'output': output
        })
        st.session_state[f'{self.console_type}_history'] = self.history

    def clear_history(self):
        self.history = []
        st.session_state[f'{self.console_type}_history'] = []