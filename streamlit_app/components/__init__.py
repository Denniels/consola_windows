"""
Componentes de la interfaz de usuario para la aplicación Streamlit
"""

# Importar todos los componentes principales
from .ui_components import NavigationComponent, ProgressCard
from .quiz_components import QuizComponent, CommandPracticeComponent
from .console_components import ConsoleSimulator
from .ui_helpers import (
    create_info_box,
    create_code_example,
    create_comparison_table,
    create_learning_objective_card,
    create_tip_card,
    create_dual_console_demo,
    create_command_reference_table,
    render_protected_command,
    render_command_option
)

__all__ = [
    # Componentes principales
    'NavigationComponent',
    'ProgressCard',
    'QuizComponent',
    'CommandPracticeComponent',
    'ConsoleSimulator',
    
    # Funciones auxiliares
    'create_info_box',
    'create_code_example',
    'create_comparison_table',
    'create_learning_objective_card',
    'create_tip_card',
    'create_dual_console_demo',
    'create_command_reference_table',
    'render_protected_command',
    'render_command_option'
]
