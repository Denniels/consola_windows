"""
Aplicación principal del Curso Interactivo de Consolas Windows
"""

import streamlit as st
import sys
import os
import importlib.util

# Agregar utils al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))

from progress_tracker import ProgressTracker, NavigationHelper, create_section_header
from ui_components import ProgressCard
from user_manager import UserManager, check_user_registration

def load_css():
    """Carga los estilos CSS personalizados"""
    try:
        # CSS robusto para anti-traducción de comandos
        st.markdown("""
        <meta name="google" content="notranslate">
        <meta name="translate" content="no">
        
        <style>
        /* Protección anti-traducción robusta para todos los elementos de código */
        code, pre, kbd, samp,
        .stCode, .stCodeBlock,
        [data-testid="stCode"],
        [data-testid="stCodeBlock"],
        .quiz-command-protection {
            translate: no !important;
            -webkit-translate: no !important;
            -moz-translate: no !important;
            -ms-translate: no !important;
            font-family: 'Consolas', 'Courier New', monospace !important;
        }
        
        /* Protección específica para elementos de quiz y comandos */
        .quiz-container code,
        .protected-command,
        .language-bash,
        .language-cmd,
        .language-powershell {
            translate: no !important;
            -webkit-translate: no !important;
            -moz-translate: no !important;
            -ms-translate: no !important;
            background-color: #f8f9fa !important;
            border: 1px solid #dee2e6 !important;
            border-radius: 4px !important;
            padding: 8px 12px !important;
            margin: 4px 0 !important;
            font-family: 'Consolas', 'Courier New', monospace !important;
            display: inline-block !important;
            white-space: pre-wrap !important;
        }
        
        /* Protección para tablas y dataframes */
        .stDataFrame, .stTable, table {
            translate: no !important;
            -webkit-translate: no !important;
        }
        
        .stDataFrame code, .stTable code, table code {
            translate: no !important;
            -webkit-translate: no !important;
            font-family: 'Consolas', 'Courier New', monospace !important;
            background-color: #f0f0f0 !important;
            padding: 2px 4px !important;
            border-radius: 3px !important;
        }
        
        /* Protección adicional para elementos específicos */
        [class*="command"], [class*="cmd"], [class*="powershell"] {
            translate: no !important;
            -webkit-translate: no !important;
            font-family: 'Consolas', 'Courier New', monospace !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Cargar archivos CSS adicionales
        css_files = ['main.css', 'console_cmd.css', 'console_ps.css']
        css_dir = os.path.join(os.path.dirname(__file__), 'css')
        
        combined_css = ""
        for css_file in css_files:
            css_path = os.path.join(css_dir, css_file)
            if os.path.exists(css_path):
                with open(css_path, 'r', encoding='utf-8') as f:
                    combined_css += f.read() + "\n"
        
        if combined_css:
            st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error cargando estilos CSS: {e}")

def initialize_session_state():
    """Inicializa el estado de la sesión"""
    if 'progress_tracker' not in st.session_state:
        st.session_state.progress_tracker = ProgressTracker()
    
    if 'navigation_helper' not in st.session_state:
        st.session_state.navigation_helper = NavigationHelper()
    
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "01_intro"
    
    # Inicializar UserManager
    if 'user_manager' not in st.session_state:
        st.session_state.user_manager = UserManager()

def load_page_module(page_name: str):
    """Carga dinámicamente un módulo de página"""
    try:
        pages_dir = os.path.join(os.path.dirname(__file__), 'pages')
        
        # Mapeo de nombres de página a archivos
        page_files = {
            "01_intro": "01_intro.py",
            "02_cmd_basics": "02_cmd_basics.py", 
            "03_powershell_basics": "03_powershell_basics.py",
            "04_intermediate_cmd": "04_intermediate_cmd.py",
            "05_intermediate_ps": "05_intermediate_ps.py",
            "06_advanced_cmd": "06_advanced_cmd.py",
            "07_advanced_ps": "07_advanced_ps.py",
            "08_evaluations": "08_evaluations.py",
            "09_summary": "09_summary.py"
        }
        
        if page_name not in page_files:
            st.error(f"Página no encontrada: {page_name}")
            return
            
        # Cargar módulo dinámicamente
        module_path = os.path.join(pages_dir, page_files[page_name])
        if not os.path.exists(module_path):
            st.error(f"Archivo no encontrado: {module_path}")
            render_placeholder_page(page_name)
            return
            
        spec = importlib.util.spec_from_file_location(page_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Ejecutar la función render_page
        if hasattr(module, 'render_page'):
            module.render_page()
        else:
            st.error(f"Función render_page no encontrada en {page_name}")
        
    except ImportError as e:
        st.error(f"Error importando página {page_name}: {e}")
        render_placeholder_page(page_name)
    except Exception as e:
        st.error(f"Error cargando página {page_name}: {e}")
        render_placeholder_page(page_name)

def render_placeholder_page(page_name: str):
    """Renderiza una página placeholder mientras se desarrollan los módulos"""
    page_info = {
        "01_intro": {"title": "Introducción a las Consolas", "icon": "🏠"},
        "02_cmd_basics": {"title": "Comandos Básicos en CMD", "icon": "⚫"},
        "03_powershell_basics": {"title": "Comandos Básicos en PowerShell", "icon": "🔵"},
        "04_intermediate_cmd": {"title": "Scripts y Variables (CMD)", "icon": "⚫"},
        "05_intermediate_ps": {"title": "Pipes, Objetos y Funciones (PowerShell)", "icon": "🔵"},
        "06_advanced_cmd": {"title": "Automatización y Tareas Programadas (CMD)", "icon": "⚫"},
        "07_advanced_ps": {"title": "Administración del Sistema (PowerShell)", "icon": "🔵"},
        "08_evaluations": {"title": "Evaluaciones Interactivas", "icon": "📊"},
        "09_summary": {"title": "Recursos y Siguientes Pasos", "icon": "📚"}
    }
    
    info = page_info.get(page_name, {"title": "Página", "icon": "📄"})
    
    create_section_header(
        title=info["title"],
        description=f"Módulo en desarrollo - {info['title']}",
        icon=info["icon"]
    )
    
    st.info("🚧 Este módulo está en desarrollo. Próximamente estará disponible con contenido interactivo.")
    
    # Mostrar progreso si está disponible
    if 'progress_tracker' in st.session_state:
        progress_card = ProgressCard(st.session_state.progress_tracker)
        progress_card.render()

def run_app():
    """Función principal que ejecuta la aplicación"""
    
    # Configurar la página
    st.set_page_config(
        page_title="🖥️ Curso Consolas Windows",
        page_icon="🖥️",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Cargar estilos CSS
    load_css()
    
    # Inicializar estado de sesión
    initialize_session_state()
    
    # Verificar si el usuario está registrado, si no mostrar formulario
    if not check_user_registration():
        st.stop()  # Detener ejecución hasta que se registre
    
    # Crear navegación en la barra lateral
    st.session_state.navigation_helper.create_navigation_menu(
        st.session_state.progress_tracker
    )
    
    # Obtener página actual
    current_page = st.session_state.navigation_helper.get_current_page()
    
    # Cargar y renderizar la página actual
    load_page_module(current_page)
    
    # Navegación entre módulos (pie de página)
    st.markdown("---")
    st.session_state.navigation_helper.create_module_navigation(current_page)
    
    # Footer
    st.markdown("""
    ---
    <div style="text-align: center; padding: 2rem; color: #6b7280;">
        <p>
            🖥️ <strong>Curso Interactivo de Consolas Windows</strong><br>
            Desarrollado por Daniel Mardones - Especialista en Python<br>
            📚 Aprende CMD y PowerShell paso a paso
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run_app()
