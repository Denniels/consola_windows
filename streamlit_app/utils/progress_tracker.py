"""
Utilidades para manejar el progreso del usuario y navegación
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import streamlit as st

class ProgressTracker:
    """Maneja el progreso del usuario a través del curso"""
    
    def __init__(self, data_file: str = "data/progress_tracker.json"):
        self.data_file = data_file
        self.progress_data = self._load_progress_data()
    
    def _load_progress_data(self) -> Dict:
        """Carga los datos de progreso desde el archivo JSON"""
        try:
            # Obtener la ruta absoluta relativa al directorio del proyecto
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            file_path = os.path.join(base_dir, self.data_file)
            
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            st.error(f"Error cargando datos de progreso: {e}")
        
        # Retornar estructura por defecto si hay error
        return {
            "user_progress": {},
            "module_completion": {
                "01_intro": [],
                "02_cmd_basics": [],
                "03_powershell_basics": [],
                "04_intermediate_cmd": [],
                "05_intermediate_ps": [],
                "06_advanced_cmd": [],
                "07_advanced_ps": [],
                "08_evaluations": [],
                "09_summary": []
            },
            "quiz_scores": {},
            "last_accessed": {},
            "total_time_spent": {},
            "commands_practiced": {}
        }
    
    def _save_progress_data(self):
        """Guarda los datos de progreso al archivo JSON"""
        try:
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            file_path = os.path.join(base_dir, self.data_file)
            
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            st.error(f"Error guardando datos de progreso: {e}")
    
    def get_user_id(self) -> str:
        """Obtiene o crea un ID de usuario único y persistente"""
        if 'user_id' not in st.session_state:
            # Crear un ID más estable para la sesión
            import hashlib
            
            # Usar una combinación de fecha + hash de la sesión de Streamlit
            session_hash = hashlib.md5(str(id(st.session_state)).encode()).hexdigest()[:8]
            today = datetime.now().strftime('%Y%m%d')
            
            # Crear un ID basado en la fecha de hoy + hash de sesión
            temp_id = f"user_{today}_{session_hash}"
            
            st.session_state.user_id = temp_id
        return st.session_state.user_id
    
    def update_module_progress(self, module_id: str, section: str, completed: bool = True):
        """Actualiza el progreso de un módulo específico"""
        user_id = self.get_user_id()
        
        if user_id not in self.progress_data["user_progress"]:
            self.progress_data["user_progress"][user_id] = {}
        
        if module_id not in self.progress_data["user_progress"][user_id]:
            self.progress_data["user_progress"][user_id][module_id] = {
                "sections_completed": [],
                "quiz_scores": [],
                "time_spent": 0,
                "last_accessed": None
            }
        
        module_progress = self.progress_data["user_progress"][user_id][module_id]
        
        if completed and section not in module_progress["sections_completed"]:
            module_progress["sections_completed"].append(section)
        
        module_progress["last_accessed"] = datetime.now().isoformat()
        
        self._save_progress_data()
    
    def get_module_progress(self, module_id: str) -> Dict:
        """Obtiene el progreso de un módulo específico"""
        user_id = self.get_user_id()
        
        if (user_id in self.progress_data["user_progress"] and 
            module_id in self.progress_data["user_progress"][user_id]):
            return self.progress_data["user_progress"][user_id][module_id]
        
        return {
            "sections_completed": [],
            "quiz_scores": [],
            "time_spent": 0,
            "last_accessed": None
        }
    
    def calculate_overall_progress(self) -> float:
        """Calcula el progreso general del usuario"""
        user_id = self.get_user_id()
        
        if user_id not in self.progress_data["user_progress"]:
            return 0.0
        
        total_modules = 9
        completed_modules = 0
        
        for module_id in self.progress_data["module_completion"].keys():
            module_progress = self.get_module_progress(module_id)
            if len(module_progress["sections_completed"]) > 0:
                completed_modules += 1
        
        return (completed_modules / total_modules) * 100
    
    def get_overall_progress(self) -> float:
        """Calcula el progreso general del usuario basado en quizzes completados"""
        user_id = self.get_user_id()
        
        if ("user_progress" not in self.progress_data or 
            user_id not in self.progress_data["user_progress"]):
            return 0.0
        
        user_modules = self.progress_data["user_progress"][user_id]
        
        # Módulos principales que deben contar para el progreso
        main_modules = [
            "02_cmd_basics", "03_powershell_basics", 
            "04_intermediate_cmd", "05_intermediate_ps",
            "06_advanced_cmd", "07_advanced_ps",
            "08_evaluations", "08_evaluations_cmd", "08_evaluations_ps"
        ]
        
        total_progress = 0.0
        modules_with_progress = 0
        
        for module_id, module_data in user_modules.items():
            # Mapear nombres de módulos a nombres estándar
            if module_id in main_modules:
                current_module = module_id
            else:
                current_module = self._map_module_name(module_id)
            
            if current_module in main_modules:
                modules_with_progress += 1
                
                # Si tiene quiz scores, calcular progreso basado en la mejor puntuación
                quiz_scores = module_data.get("quiz_scores", [])
                if quiz_scores:
                    best_score = max([qs.get("percentage", 0) for qs in quiz_scores])
                    # Si obtuvo >= 70%, contar como completado (100%), sino usar el porcentaje
                    module_progress = 100.0 if best_score >= 70 else best_score
                    total_progress += module_progress
                # Si no tiene quiz pero tiene secciones completadas, dar progreso parcial
                elif module_data.get("sections_completed"):
                    total_progress += 25.0  # Progreso parcial por ver contenido
        
        if modules_with_progress == 0:
            return 0.0
        
        return total_progress / len(main_modules)
    
    def _map_module_name(self, module_id: str) -> str:
        """Mapea nombres de módulos a nombres estándar"""
        mapping = {
            "02_cmd_basics": "cmd_basics",
            "03_powershell_basics": "ps_basics",
            "04_intermediate_cmd": "cmd_intermediate", 
            "05_intermediate_ps": "ps_intermediate",
            "06_advanced_cmd": "cmd_advanced",
            "07_advanced_ps": "ps_advanced",
            "08_evaluations": "evaluations"
        }
        return mapping.get(module_id, module_id)
    
    def get_completed_modules_count(self) -> tuple:
        """Retorna (módulos_completados, total_módulos)"""
        user_id = self.get_user_id()
        
        if ("user_progress" not in self.progress_data or 
            user_id not in self.progress_data["user_progress"]):
            return (0, 6)  # 6 módulos principales
        
        user_modules = self.progress_data["user_progress"][user_id]
        main_modules = [
            "02_cmd_basics", "03_powershell_basics", 
            "04_intermediate_cmd", "05_intermediate_ps",
            "06_advanced_cmd", "07_advanced_ps",
            "08_evaluations", "08_evaluations_cmd", "08_evaluations_ps"
        ]
        
        completed = 0
        for module_id, module_data in user_modules.items():
            # Si el module_id ya está en el formato correcto o es uno de los principales
            if module_id in main_modules:
                quiz_scores = module_data.get("quiz_scores", [])
                if quiz_scores:
                    best_score = max([qs.get("percentage", 0) for qs in quiz_scores])
                    if best_score >= 70:
                        completed += 1
            else:
                # Usar el mapeo tradicional para compatibilidad
                standard_module = self._map_module_name(module_id)
                if standard_module in main_modules:
                    quiz_scores = module_data.get("quiz_scores", [])
                    if quiz_scores:
                        best_score = max([qs.get("percentage", 0) for qs in quiz_scores])
                        if best_score >= 70:
                            completed += 1
        
        return (completed, len(main_modules))
    
    def get_completed_quizzes_count(self) -> int:
        """Retorna el número de quizzes completados exitosamente"""
        user_id = self.get_user_id()
        
        if ("user_progress" not in self.progress_data or 
            user_id not in self.progress_data["user_progress"]):
            return 0
        
        user_modules = self.progress_data["user_progress"][user_id]
        completed_quizzes = 0
        
        for module_id, module_data in user_modules.items():
            quiz_scores = module_data.get("quiz_scores", [])
            if quiz_scores:
                best_score = max([qs.get("percentage", 0) for qs in quiz_scores])
                if best_score >= 70:
                    completed_quizzes += 1
        
        return completed_quizzes
    
    def get_commands_practiced_count(self) -> int:
        """Retorna el número de comandos únicos practicados"""
        commands_practiced = self.progress_data.get("commands_practiced", {})
        return len(commands_practiced)
    
    def add_command_practice(self, command: str, metadata: Dict, success: bool = True):
        """Registra la práctica de un comando"""
        timestamp = datetime.now().isoformat()
        
        if "commands_practiced" not in self.progress_data:
            self.progress_data["commands_practiced"] = {}
        
        if command not in self.progress_data["commands_practiced"]:
            self.progress_data["commands_practiced"][command] = []
        
        practice_entry = {
            "timestamp": timestamp,
            "success": success,
            "metadata": metadata
        }
        
        self.progress_data["commands_practiced"][command].append(practice_entry)
        self._save_progress_data()
    
    def get_practiced_commands(self) -> Dict:
        """Retorna estadísticas de comandos practicados"""
        commands_data = {}
        commands_practiced = self.progress_data.get("commands_practiced", {})
        
        for command, practices in commands_practiced.items():
            # Asegurar que practices es una lista
            if not isinstance(practices, list):
                practices = []
            
            total_attempts = len(practices)
            successful_attempts = 0
            
            # Contar intentos exitosos de forma segura
            for practice in practices:
                if isinstance(practice, dict) and practice.get("success", False):
                    successful_attempts += 1
                elif isinstance(practice, str):
                    # Si es string, asumir que es exitoso (formato anterior)
                    successful_attempts += 1
            
            commands_data[command] = {
                "attempts": total_attempts,
                "successes": successful_attempts,
                "success_rate": successful_attempts / total_attempts if total_attempts > 0 else 0,
                "last_practiced": None  # Por ahora simplificamos
            }
        
        return commands_data
    
    @property
    def module_progress(self) -> Dict:
        """Retorna el progreso de módulos"""
        return self.progress_data.get("module_completion", {})
    
    @property
    def command_history(self) -> Dict:
        """Retorna el historial de comandos practicados"""
        return self.progress_data.get("commands_practiced", {})
    
    @property
    def quiz_scores(self) -> Dict:
        """Retorna las puntuaciones de los quizzes"""
        return self.progress_data.get("quiz_scores", {})
    
    def reset_progress(self):
        """Reinicia todo el progreso del usuario"""
        self.progress_data = {
            "user_progress": {},
            "module_completion": {
                "01_intro": [],
                "02_cmd_basics": [],
                "03_powershell_basics": [],
                "04_intermediate_cmd": [],
                "05_intermediate_ps": [],
                "06_advanced_cmd": [],
                "07_advanced_ps": [],
                "08_evaluations": [],
                "09_summary": []
            },
            "quiz_scores": {},
            "last_accessed": {},
            "total_time_spent": {},
            "commands_practiced": {}
        }
        self._save_progress_data()
    
    def add_quiz_score(self, module_id: str, score: float, max_score: float):
        """Registra el resultado de un quiz"""
        user_id = self.get_user_id()
        
        # Asegurar que la estructura existe
        if "user_progress" not in self.progress_data:
            self.progress_data["user_progress"] = {}
        
        if user_id not in self.progress_data["user_progress"]:
            self.progress_data["user_progress"][user_id] = {}
        
        if module_id not in self.progress_data["user_progress"][user_id]:
            self.progress_data["user_progress"][user_id][module_id] = {
                "sections_completed": [],
                "quiz_scores": [],
                "time_spent": 0,
                "last_accessed": datetime.now().isoformat()
            }
        
        quiz_result = {
            "score": score,
            "max_score": max_score,
            "percentage": (score / max_score) * 100,
            "date": datetime.now().isoformat()
        }
        
        # Agregar el resultado del quiz a la estructura correcta
        self.progress_data["user_progress"][user_id][module_id]["quiz_scores"].append(quiz_result)
        
        # Actualizar última vez accedido
        self.progress_data["user_progress"][user_id][module_id]["last_accessed"] = datetime.now().isoformat()
        
        self._save_progress_data()
    
    def get_quiz_scores(self, module_id: str) -> List[Dict]:
        """Obtiene los resultados de quiz de un módulo"""
        user_id = self.get_user_id()
        
        if ("user_progress" in self.progress_data and 
            user_id in self.progress_data["user_progress"] and 
            module_id in self.progress_data["user_progress"][user_id] and
            "quiz_scores" in self.progress_data["user_progress"][user_id][module_id]):
            return self.progress_data["user_progress"][user_id][module_id]["quiz_scores"]
        
        return []
    
    def get_recommendations(self) -> List[str]:
        """Genera recomendaciones basadas en el progreso del usuario"""
        user_id = self.get_user_id()
        recommendations = []
        
        if user_id not in self.progress_data["user_progress"]:
            recommendations.append("¡Comienza con la Introducción a las Consolas!")
            return recommendations
        
        # Analizar progreso por módulo
        modules_info = {
            "01_intro": "Introducción a las Consolas",
            "02_cmd_basics": "Comandos Básicos en CMD",
            "03_powershell_basics": "Comandos Básicos en PowerShell",
            "04_intermediate_cmd": "Scripts y Variables (CMD)",
            "05_intermediate_ps": "Pipes, Objetos y Funciones (PowerShell)",
            "06_advanced_cmd": "Automatización y Tareas Programadas (CMD)",
            "07_advanced_ps": "Administración del Sistema (PowerShell)",
            "08_evaluations": "Evaluaciones Interactivas",
            "09_summary": "Recursos y Siguientes Pasos"
        }
        
        user_progress = self.progress_data["user_progress"][user_id]
        
        # Encontrar el siguiente módulo recomendado
        for module_id, module_name in modules_info.items():
            if module_id not in user_progress or len(user_progress[module_id]["sections_completed"]) == 0:
                recommendations.append(f"Continúa con: {module_name}")
                break
        
        # Analizar comandos practicados
        practiced_commands = self.get_practiced_commands()
        if practiced_commands:
            cmd_success_rates = {}
            for cmd_key, cmd_data in practiced_commands.items():
                if cmd_data["attempts"] > 0:
                    success_rate = cmd_data["successes"] / cmd_data["attempts"]
                    if success_rate < 0.7:  # Menos del 70% de éxito
                        console_type, command = cmd_key.split(":", 1)
                        cmd_success_rates[cmd_key] = success_rate
            
            if cmd_success_rates:
                worst_cmd = min(cmd_success_rates, key=cmd_success_rates.get)
                console_type, command = worst_cmd.split(":", 1)
                recommendations.append(f"Práctica más el comando '{command}' en {console_type.upper()}")
        
        # Recomendaciones de quiz
        quiz_scores = self.progress_data["quiz_scores"].get(user_id, {})
        for module_id, scores in quiz_scores.items():
            if scores:
                latest_score = scores[-1]
                if latest_score["percentage"] < 70:
                    module_name = modules_info.get(module_id, module_id)
                    recommendations.append(f"Repasa el módulo: {module_name}")
        
        if not recommendations:
            recommendations.append("¡Excelente progreso! Considera repasar los conceptos avanzados.")
        
        return recommendations[:3]  # Máximo 3 recomendaciones


class NavigationHelper:
    """Ayuda con la navegación entre páginas y módulos"""
    
    def __init__(self):
        self.modules = [
            {"id": "01_intro", "title": "Introducción", "icon": "🏠"},
            {"id": "02_cmd_basics", "title": "CMD Básico", "icon": "⚫"},
            {"id": "03_powershell_basics", "title": "PowerShell Básico", "icon": "🔵"},
            {"id": "04_intermediate_cmd", "title": "CMD Intermedio", "icon": "⚫"},
            {"id": "05_intermediate_ps", "title": "PowerShell Intermedio", "icon": "🔵"},
            {"id": "06_advanced_cmd", "title": "CMD Avanzado", "icon": "⚫"},
            {"id": "07_advanced_ps", "title": "PowerShell Avanzado", "icon": "🔵"},
            {"id": "08_evaluations", "title": "Evaluaciones", "icon": "📊"},
            {"id": "09_summary", "title": "Resumen", "icon": "📚"}
        ]
    
    def get_module_info(self, module_id: str) -> Optional[Dict]:
        """Obtiene información de un módulo específico"""
        for module in self.modules:
            if module["id"] == module_id:
                return module
        return None
    
    def get_next_module(self, current_module_id: str) -> Optional[Dict]:
        """Obtiene el siguiente módulo en la secuencia"""
        for i, module in enumerate(self.modules):
            if module["id"] == current_module_id and i < len(self.modules) - 1:
                return self.modules[i + 1]
        return None
    
    def get_previous_module(self, current_module_id: str) -> Optional[Dict]:
        """Obtiene el módulo anterior en la secuencia"""
        for i, module in enumerate(self.modules):
            if module["id"] == current_module_id and i > 0:
                return self.modules[i - 1]
        return None
    
    def create_navigation_menu(self, progress_tracker: ProgressTracker):
        """Crea un menú de navegación en la barra lateral"""
        st.sidebar.title("📚 Módulos del Curso")
        
        # Mostrar progreso general
        overall_progress = progress_tracker.calculate_overall_progress()
        st.sidebar.progress(overall_progress / 100)
        st.sidebar.caption(f"Progreso general: {overall_progress:.1f}%")
        
        st.sidebar.markdown("---")
        
        # Menú de módulos
        for module in self.modules:
            module_progress = progress_tracker.get_module_progress(module["id"])
            
            # Determinar estado del módulo
            if len(module_progress["sections_completed"]) > 0:
                status_icon = "✅"
                status_text = "Completado"
            elif module_progress["last_accessed"]:
                status_icon = "🔄"
                status_text = "En progreso"
            else:
                status_icon = "⭕"
                status_text = "No iniciado"
            
            # Crear botón de navegación
            button_text = f"{module['icon']} {module['title']}"
            if st.sidebar.button(button_text, key=f"nav_{module['id']}"):
                st.session_state.current_page = module["id"]
                st.rerun()
            
            # Mostrar estado
            st.sidebar.caption(f"{status_icon} {status_text}")
        
        st.sidebar.markdown("---")
        
        # Mostrar recomendaciones
        recommendations = progress_tracker.get_recommendations()
        if recommendations:
            st.sidebar.markdown("### 💡 Recomendaciones")
            for rec in recommendations:
                st.sidebar.info(rec)
    
    def create_module_navigation(self, current_module_id: str):
        """Crea navegación entre módulos (anterior/siguiente)"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            prev_module = self.get_previous_module(current_module_id)
            if prev_module:
                if st.button(f"⬅️ {prev_module['title']}", key="prev_module"):
                    st.session_state.current_page = prev_module["id"]
                    st.rerun()
        
        with col3:
            next_module = self.get_next_module(current_module_id)
            if next_module:
                if st.button(f"{next_module['title']} ➡️", key="next_module"):
                    st.session_state.current_page = next_module["id"]
                    st.rerun()
    
    def get_current_page(self) -> str:
        """Obtiene la página actual desde session_state"""
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "01_intro"
        return st.session_state.current_page
    
    def set_current_page(self, page_id: str):
        """Establece la página actual"""
        st.session_state.current_page = page_id


def create_section_header(title: str, description: str, icon: str = "📖"):
    """Crea un header estilizado para secciones"""
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    ">
        <h2 style="margin: 0; font-size: 1.8rem;">
            {icon} {title}
        </h2>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)


def create_info_card(title: str, content: str, icon: str = "ℹ️", color: str = "blue"):
    """Crea una tarjeta informativa estilizada"""
    color_map = {
        "blue": {"bg": "#dbeafe", "border": "#3b82f6", "text": "#1e3a8a"},
        "green": {"bg": "#d1fae5", "border": "#10b981", "text": "#065f46"},
        "yellow": {"bg": "#fef3c7", "border": "#f59e0b", "text": "#92400e"},
        "red": {"bg": "#fee2e2", "border": "#ef4444", "text": "#991b1b"}
    }
    
    colors = color_map.get(color, color_map["blue"])
    
    st.markdown(f"""
    <div style="
        background: {colors['bg']};
        border-left: 4px solid {colors['border']};
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    ">
        <h4 style="
            color: {colors['text']};
            margin: 0 0 0.5rem 0;
            font-size: 1.2rem;
        ">
            {icon} {title}
        </h4>
        <p style="
            color: {colors['text']};
            margin: 0;
            line-height: 1.5;
        ">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)
