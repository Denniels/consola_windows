#!/usr/bin/env python3
"""
Script de prueba para verificar el funcionamiento del ProgressTracker
"""

import sys
import os

# Agregar paths para imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'streamlit_app', 'utils'))

from progress_tracker import ProgressTracker

def test_progress_tracker():
    """Prueba las funcionalidades del ProgressTracker"""
    print("🧪 Iniciando pruebas del ProgressTracker...")
    
    # Crear instancia del tracker
    tracker = ProgressTracker()
    
    # Simular user_id
    import streamlit as st
    if 'user_id' not in st.session_state:
        st.session_state.user_id = "test_user_debug"
    
    print(f"📋 User ID: {tracker.get_user_id()}")
    
    # Probar agregar quiz scores para diferentes módulos
    quiz_data = [
        ("cmd_basics", 85),
        ("ps_basics", 92),
        ("cmd_intermediate", 78),
        ("ps_intermediate", 65),  # Este no debería contar como completado
        ("cmd_advanced", 88),
        ("ps_advanced", 91)
    ]
    
    print("\n📝 Agregando quiz scores...")
    for module_id, score in quiz_data:
        tracker.add_quiz_score(module_id, score, 100)
        print(f"  ✅ {module_id}: {score}%")
    
    # Verificar progreso general
    print(f"\n📊 Progreso general: {tracker.get_overall_progress():.1f}%")
    
    # Verificar estadísticas
    completed_modules, total_modules = tracker.get_completed_modules_count()
    print(f"📚 Módulos completados: {completed_modules}/{total_modules}")
    
    quizzes_completed = tracker.get_completed_quizzes_count()
    print(f"🎯 Quizzes completados: {quizzes_completed}")
    
    commands_practiced = tracker.get_commands_practiced_count()
    print(f"⌨️ Comandos practicados: {commands_practiced}")
    
    # Mostrar detalle de quiz scores
    print(f"\n🔍 Detalle de quiz scores:")
    for module_id, score in quiz_data:
        scores = tracker.get_quiz_scores(module_id)
        print(f"  {module_id}: {scores}")

if __name__ == "__main__":
    test_progress_tracker()
