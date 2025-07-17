"""
Parser de comandos para simular CMD y PowerShell
"""

import re
import random
from typing import Dict, List, Tuple, Optional
from datetime import datetime

class CommandParser:
    """Parser principal para detectar y procesar comandos"""
    
    def __init__(self):
        self.cmd_commands = self._load_cmd_commands()
        self.ps_commands = self._load_ps_commands()
        self.common_errors = self._load_common_errors()
    
    def detect_console_type(self, command: str) -> str:
        """Detecta si el comando es CMD o PowerShell"""
        command = command.strip().lower()
        
        # Verificar comandos específicos de PowerShell
        ps_indicators = [
            'get-', 'set-', 'new-', 'remove-', 'start-', 'stop-',
            'test-', 'invoke-', 'import-', 'export-', 'select-',
            'where-', 'foreach-', 'measure-', 'sort-', 'group-'
        ]
        
        if any(command.startswith(indicator) for indicator in ps_indicators):
            return "powershell"
        
        # Verificar sintaxis de PowerShell
        if '-' in command and not command.startswith('cd '):
            return "powershell"
        
        # Por defecto, asumir CMD
        return "cmd"
    
    def parse_command(self, command: str, console_type: str = None) -> str:
        """Analiza y procesa un comando y retorna solo el output"""
        if console_type is None:
            console_type = self.detect_console_type(command)
        
        command_clean = command.strip()
        
        # Crear estructura de resultado temporal
        result = {
            'console_type': console_type,
            'original_command': command,
            'clean_command': command_clean,
            'is_valid': False,
            'output': '',
            'error': '',
            'suggestions': [],
            'educational_note': ''
        }
        
        if console_type == "cmd":
            result = self._parse_cmd_command(result)
        else:
            result = self._parse_ps_command(result)
        
        # Retornar solo el output o error
        if result['is_valid']:
            return result['output']
        else:
            return result['error']
    
    def _parse_cmd_command(self, result: Dict) -> Dict:
        """Procesa comandos de CMD"""
        command = result['clean_command'].lower()
        
        # Dividir comando y argumentos
        parts = command.split()
        if not parts:
            result['error'] = "No se ha introducido ningún comando"
            return result
        
        cmd_name = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd_name in self.cmd_commands:
            cmd_info = self.cmd_commands[cmd_name]
            result['is_valid'] = True
            result['output'] = self._simulate_cmd_output(cmd_name, args)
            result['educational_note'] = cmd_info.get('description', '')
        else:
            result['error'] = f"'{cmd_name}' no se reconoce como un comando interno o externo"
            result['suggestions'] = self._get_cmd_suggestions(cmd_name)
        
        return result
    
    def _parse_ps_command(self, result: Dict) -> Dict:
        """Procesa comandos de PowerShell"""
        command = result['clean_command']
        
        # Dividir comando y argumentos
        parts = command.split()
        if not parts:
            result['error'] = "No se ha introducido ningún comando"
            return result
        
        cmd_name = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd_name in self.ps_commands:
            cmd_info = self.ps_commands[cmd_name]
            result['is_valid'] = True
            result['output'] = self._simulate_ps_output(cmd_name, args)
            result['educational_note'] = cmd_info.get('description', '')
        else:
            result['error'] = f"El término '{parts[0]}' no se reconoce como nombre de un cmdlet"
            result['suggestions'] = self._get_ps_suggestions(cmd_name)
        
        return result
    
    def _simulate_cmd_output(self, cmd_name: str, args: List[str]) -> str:
        """Simula la salida de comandos CMD"""
        
        outputs = {
            'dir': self._simulate_dir_output(),
            'cd': self._simulate_cd_output(args),
            'cls': '',  # cls borra la pantalla
            'echo': ' '.join(args) if args else '',
            'type': self._simulate_type_output(args),
            'copy': f"        1 archivo(s) copiado(s)." if args else "La sintaxis del comando no es correcta.",
            'del': f"" if args else "La sintaxis del comando no es correcta.",
            'mkdir': f"" if args else "La sintaxis del comando no es correcta.",
            'rmdir': f"" if args else "La sintaxis del comando no es correcta.",
            'help': self._simulate_help_output(args),
            'ver': "Microsoft Windows [Versión 10.0.19045.3693]",
            'date': f"Fecha actual: {datetime.now().strftime('%d/%m/%Y')}",
            'time': f"Hora actual: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}",
            'ipconfig': self._simulate_ipconfig_output(),
            'tasklist': self._simulate_tasklist_output(),
            'netstat': self._simulate_netstat_output()
        }
        
        return outputs.get(cmd_name, f"Comando {cmd_name} ejecutado correctamente.")
    
    def _simulate_ps_output(self, cmd_name: str, args: List[str]) -> str:
        """Simula la salida de comandos PowerShell"""
        
        outputs = {
            'get-process': self._simulate_get_process_output(),
            'get-service': self._simulate_get_service_output(),
            'get-childitem': self._simulate_get_childitem_output(),
            'set-location': '',
            'clear-host': '',
            'write-output': ' '.join(args) if args else '',
            'get-help': self._simulate_get_help_output(args),
            'get-command': self._simulate_get_command_output(args),
            'get-content': self._simulate_get_content_output(args),
            'test-connection': self._simulate_test_connection_output(args),
            'get-date': datetime.now().strftime('%A, %B %d, %Y %I:%M:%S %p'),
            'get-location': "C:\\Users\\Usuario",
            'get-host': self._simulate_get_host_output()
        }
        
        return outputs.get(cmd_name, f"Cmdlet {cmd_name} ejecutado correctamente.")
    
    def _simulate_dir_output(self) -> str:
        """Simula la salida del comando dir"""
        return """ El volumen de la unidad C es Windows
 El número de serie del volumen es: A1B2-C3D4

 Directorio de C:\\Users\\Usuario

22/12/2024  14:30    <DIR>          .
22/12/2024  14:30    <DIR>          ..
22/12/2024  10:15    <DIR>          Desktop
22/12/2024  09:45    <DIR>          Documents
22/12/2024  11:20    <DIR>          Downloads
22/12/2024  08:30    <DIR>          Pictures
21/12/2024  16:45            2,048 archivo.txt
20/12/2024  12:30           15,872 datos.xlsx
               2 archivo(s)        17,920 bytes
               6 dirs  25,789,456,384 bytes libres"""
    
    def _simulate_cd_output(self, args: List[str]) -> str:
        """Simula la salida del comando cd"""
        if not args:
            return "C:\\Users\\Usuario"
        return ""
    
    def _simulate_type_output(self, args: List[str]) -> str:
        """Simula la salida del comando type"""
        if not args:
            return "La sintaxis del comando no es correcta."
        return f"Contenido del archivo {args[0]}:\nEste es un archivo de ejemplo.\nContiene texto simulado para el curso."
    
    def _simulate_help_output(self, args: List[str]) -> str:
        """Simula la salida del comando help"""
        if not args:
            return """Para obtener más información acerca de un comando específico, escriba HELP nombre-comando
ATTRIB          Muestra o cambia los atributos del archivo.
CD              Muestra el nombre del directorio actual o cambia a otro directorio.
CHDIR           Muestra el nombre del directorio actual o cambia a otro directorio.
CLS             Borra la pantalla.
COPY            Copia uno o más archivos en otra ubicación.
DATE            Muestra o establece la fecha.
DEL             Elimina uno o más archivos.
DIR             Muestra una lista de archivos y subdirectorios en un directorio.
ECHO            Muestra mensajes, o activa y desactiva el eco del comando.
EXIT            Sale del programa CMD.EXE (intérprete de comandos).
HELP            Proporciona información de ayuda para los comandos de Windows.
MD              Crea un directorio.
MKDIR           Crea un directorio.
MOVE            Mueve archivos y cambia el nombre a archivos y directorios.
RD              Elimina un directorio.
REN             Cambia el nombre de uno o más archivos.
RENAME          Cambia el nombre de uno o más archivos.
RMDIR           Elimina un directorio.
TIME            Muestra o establece la hora del sistema.
TYPE            Muestra el contenido de un archivo de texto.
VER             Muestra la versión de Windows."""
        return f"Ayuda para el comando {args[0].upper()}..."
    
    def _simulate_ipconfig_output(self) -> str:
        """Simula la salida del comando ipconfig"""
        return """
Configuración IP de Windows

Adaptador de Ethernet Ethernet:

   Estado de los medios. . . . . . . . . . . : medios desconectados
   Sufijo DNS específico para la conexión. . :

Adaptador de LAN inalámbrica Wi-Fi:

   Sufijo DNS específico para la conexión. . : 
   Dirección IPv6 de vínculo local. . . . . .: fe80::1234:5678:9abc:def0%12
   Dirección IPv4. . . . . . . . . . . . . . .: 192.168.1.100
   Máscara de subred . . . . . . . . . . . . .: 255.255.255.0
   Puerta de enlace predeterminada . . . . . .: 192.168.1.1
"""
    
    def _simulate_tasklist_output(self) -> str:
        """Simula la salida del comando tasklist"""
        return """
Nombre de imagen                     PID Nombre de sesión       Núm. de ses Uso de memoria
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0      2,124 K
smss.exe                       532 Services                   0      1,024 K
csrss.exe                      612 Services                   0      4,096 K
winlogon.exe                   668 Services                   0      3,072 K
services.exe                   716 Services                   0      5,120 K
lsass.exe                      728 Services                   0      8,192 K
svchost.exe                    912 Services                   0     15,360 K
svchost.exe                    980 Services                   0     12,288 K
explorer.exe                 1,234 Console                    1     35,840 K
notepad.exe                  2,468 Console                    1      8,192 K
"""
    
    def _simulate_netstat_output(self) -> str:
        """Simula la salida del comando netstat"""
        return """
Conexiones activas

  Proto  Dirección local          Dirección remota         Estado
  TCP    127.0.0.1:445           0.0.0.0:0                LISTENING
  TCP    192.168.1.100:139       0.0.0.0:0                LISTENING
  TCP    192.168.1.100:1234      google.com:443           ESTABLISHED
  TCP    192.168.1.100:5678      microsoft.com:80         TIME_WAIT
  UDP    127.0.0.1:53            *:*                      
  UDP    192.168.1.100:137       *:*                      
"""
    
    def _simulate_get_process_output(self) -> str:
        """Simula la salida del cmdlet Get-Process"""
        return """
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    463      25    15,840     23,456       1.23    832   1 explorer
    234      12     8,192     12,288       0.45   1234   1 notepad
    156       8     4,096      6,144       0.12   2468   0 services
    892      45    32,768     45,056       5.67   3692   1 chrome
    345      18    12,288     18,432       2.34   4567   1 winword
"""
    
    def _simulate_get_service_output(self) -> str:
        """Simula la salida del cmdlet Get-Service"""
        return """
Status   Name               DisplayName                           
------   ----               -----------                           
Running  AudioEndpointBu... Windows Audio Endpoint Builder       
Stopped  BthAvctpSvc        AVCTP service                         
Running  BITS               Background Intelligent Transfer Ser...
Running  BrokerInfrastru... Background Tasks Infrastructure Ser...
Running  Browser            Computer Browser                      
Running  BFE                Base Filtering Engine                 
Running  CertPropSvc        Certificate Propagation              
Running  CryptSvc           Cryptographic Services               
Running  DcomLaunch         DCOM Server Process Launcher         
Running  Dhcp               DHCP Client                           
"""
    
    def _simulate_get_childitem_output(self) -> str:
        """Simula la salida del cmdlet Get-ChildItem"""
        return """
    Directorio: C:\\Users\\Usuario

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        22/12/2024     14:30                Desktop
d-----        22/12/2024      9:45                Documents
d-----        22/12/2024     11:20                Downloads
d-----        22/12/2024      8:30                Pictures
-a----        21/12/2024     16:45           2048 archivo.txt
-a----        20/12/2024     12:30          15872 datos.xlsx
"""
    
    def _simulate_get_help_output(self, args: List[str]) -> str:
        """Simula la salida del cmdlet Get-Help"""
        if not args:
            return """
TEMA
    about_PowerShell

DESCRIPCIÓN BREVE
    PowerShell es un shell de línea de comandos y lenguaje de scripting.

DESCRIPCIÓN LARGA
    PowerShell es una solución de automatización multiplataforma compuesta por un 
    shell de línea de comandos, un lenguaje de scripting y un marco de administración
    de configuración.

VÍNCULOS RELACIONADOS
    Online version: https://docs.microsoft.com/powershell/
    Get-Command
    Get-Member
"""
        return f"""
NOMBRE
    {args[0]}

SINOPSIS
    Ayuda para el cmdlet {args[0]}

DESCRIPCIÓN
    Este cmdlet realiza operaciones específicas del sistema.

PARÁMETROS
    Para ver los parámetros, use: Get-Help {args[0]} -Detailed
"""
    
    def _simulate_get_command_output(self, args: List[str]) -> str:
        """Simula la salida del cmdlet Get-Command"""
        return """
CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Alias           % -> ForEach-Object                                           
Alias           ? -> Where-Object                                             
Alias           ac -> Add-Content                                             
Alias           asnp -> Add-PSSnapin                                          
Alias           cat -> Get-Content                                            
Alias           cd -> Set-Location                                            
Alias           chdir -> Set-Location                                         
Alias           clc -> Clear-Content                                          
Alias           clear -> Clear-Host                                           
Alias           clhy -> Clear-History                                         
Alias           cli -> Clear-Item                                             
Alias           clp -> Clear-ItemProperty                                     
Alias           cls -> Clear-Host                                             
Function        A:                                                            
Function        B:                                                            
Function        C:                                                            
Function        Clear-Host                                                    
Cmdlet          Add-Computer                               3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Add-Content                                3.1.0.0    Microsoft.PowerShell.Management
Cmdlet          Add-History                                3.0.0.0    Microsoft.PowerShell.Core
"""
    
    def _simulate_get_content_output(self, args: List[str]) -> str:
        """Simula la salida del cmdlet Get-Content"""
        if not args:
            return "Get-Content : Falta un argumento para el parámetro 'Path'."
        return f"""Línea 1 del archivo {args[0]}
Línea 2 del archivo {args[0]}
Línea 3 del archivo {args[0]}
Esta es una simulación del contenido del archivo.
Línea final del archivo."""
    
    def _simulate_test_connection_output(self, args: List[str]) -> str:
        """Simula la salida del cmdlet Test-Connection"""
        if not args:
            return "Test-Connection : Falta un argumento para el parámetro 'ComputerName'."
        
        target = args[0]
        return f"""
Source        Destination     IPV4Address      IPV6Address                              Bytes    Time(ms)
------        -----------     -----------      -----------                              -----    --------
MIPC          {target}       8.8.8.8                                                   32       15      
MIPC          {target}       8.8.8.8                                                   32       12      
MIPC          {target}       8.8.8.8                                                   32       18      
MIPC          {target}       8.8.8.8                                                   32       14      
"""
    
    def _simulate_get_host_output(self) -> str:
        """Simula la salida del cmdlet Get-Host"""
        return """
Name             : ConsoleHost
Version          : 5.1.19041.3693
InstanceId       : 12345678-abcd-1234-efgh-123456789012
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : es-ES
CurrentUICulture : es-ES
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
DebuggerEnabled  : True
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace
"""
    
    def _get_cmd_suggestions(self, cmd_name: str) -> List[str]:
        """Obtiene sugerencias para comandos CMD no reconocidos"""
        suggestions = []
        
        # Sugerencias basadas en similitud
        similar_commands = {
            'ls': ['dir'],
            'cat': ['type'],
            'rm': ['del'],
            'mv': ['move'],
            'cp': ['copy'],
            'pwd': ['cd'],
            'clear': ['cls'],
            'mkdir': ['md'],
            'rmdir': ['rd']
        }
        
        if cmd_name in similar_commands:
            suggestions.extend(similar_commands[cmd_name])
        
        # Sugerencias por errores comunes
        if 'echo' in cmd_name:
            suggestions.append('echo')
        if 'dir' in cmd_name:
            suggestions.append('dir')
        if 'help' in cmd_name:
            suggestions.append('help')
        
        return suggestions[:3]  # Máximo 3 sugerencias
    
    def _get_ps_suggestions(self, cmd_name: str) -> List[str]:
        """Obtiene sugerencias para cmdlets PowerShell no reconocidos"""
        suggestions = []
        
        # Sugerencias basadas en verbos comunes
        if cmd_name.startswith('get'):
            suggestions.extend(['Get-Process', 'Get-Service', 'Get-ChildItem'])
        elif cmd_name.startswith('set'):
            suggestions.extend(['Set-Location', 'Set-Content', 'Set-Variable'])
        elif cmd_name.startswith('new'):
            suggestions.extend(['New-Item', 'New-Object', 'New-Variable'])
        
        # Sugerencias por alias comunes
        alias_suggestions = {
            'ls': ['Get-ChildItem'],
            'dir': ['Get-ChildItem'],
            'cat': ['Get-Content'],
            'pwd': ['Get-Location'],
            'cd': ['Set-Location'],
            'clear': ['Clear-Host'],
            'cls': ['Clear-Host']
        }
        
        if cmd_name in alias_suggestions:
            suggestions.extend(alias_suggestions[cmd_name])
        
        return suggestions[:3]  # Máximo 3 sugerencias
    
    def _load_cmd_commands(self) -> Dict:
        """Carga la base de datos de comandos CMD"""
        return {
            'dir': {'description': 'Muestra una lista de archivos y subdirectorios en un directorio'},
            'cd': {'description': 'Muestra el nombre del directorio actual o cambia a otro directorio'},
            'cls': {'description': 'Borra la pantalla'},
            'copy': {'description': 'Copia uno o más archivos en otra ubicación'},
            'del': {'description': 'Elimina uno o más archivos'},
            'type': {'description': 'Muestra el contenido de un archivo de texto'},
            'echo': {'description': 'Muestra mensajes, o activa y desactiva el eco del comando'},
            'mkdir': {'description': 'Crea un directorio'},
            'md': {'description': 'Crea un directorio'},
            'rmdir': {'description': 'Elimina un directorio'},
            'rd': {'description': 'Elimina un directorio'},
            'move': {'description': 'Mueve archivos y cambia el nombre a archivos y directorios'},
            'help': {'description': 'Proporciona información de ayuda para los comandos de Windows'},
            'ver': {'description': 'Muestra la versión de Windows'},
            'date': {'description': 'Muestra o establece la fecha'},
            'time': {'description': 'Muestra o establece la hora del sistema'},
            'ipconfig': {'description': 'Muestra la configuración IP de Windows'},
            'tasklist': {'description': 'Muestra las tareas que se ejecutan actualmente'},
            'taskkill': {'description': 'Termina o detiene un proceso o aplicación en ejecución'},
            'netstat': {'description': 'Muestra conexiones de red, tablas de enrutamiento e interfaces'},
            'ping': {'description': 'Envía solicitudes de eco ICMP a un host de red'},
            'find': {'description': 'Busca una cadena de texto en uno o varios archivos'},
            'findstr': {'description': 'Busca cadenas en archivos'},
            'xcopy': {'description': 'Copia archivos y árboles de directorios'},
            'attrib': {'description': 'Muestra o cambia los atributos del archivo'},
            'chkdsk': {'description': 'Comprueba un disco y muestra un informe de estado'},
            'set': {'description': 'Muestra, establece o quita variables de entorno'},
            'path': {'description': 'Muestra o establece una ruta de búsqueda para archivos ejecutables'},
            'start': {'description': 'Inicia una ventana independiente para ejecutar un programa o comando'},
            'call': {'description': 'Llama a un programa por lotes desde otro'},
            'exit': {'description': 'Sale del programa CMD.EXE (intérprete de comandos)'}
        }
    
    def _load_ps_commands(self) -> Dict:
        """Carga la base de datos de cmdlets PowerShell"""
        return {
            'get-process': {'description': 'Obtiene los procesos que se ejecutan en el equipo local'},
            'get-service': {'description': 'Obtiene los servicios en el equipo'},
            'get-childitem': {'description': 'Obtiene elementos en una o más ubicaciones especificadas'},
            'set-location': {'description': 'Establece la ubicación de trabajo actual en una ubicación especificada'},
            'get-location': {'description': 'Obtiene información sobre la ubicación de trabajo actual'},
            'clear-host': {'description': 'Borra la pantalla en el programa host'},
            'write-output': {'description': 'Envía los objetos especificados al siguiente comando en la canalización'},
            'new-item': {'description': 'Crea un nuevo elemento'},
            'remove-item': {'description': 'Elimina los elementos especificados'},
            'copy-item': {'description': 'Copia un elemento de una ubicación a otra'},
            'move-item': {'description': 'Mueve un elemento de una ubicación a otra'},
            'get-content': {'description': 'Obtiene el contenido del elemento en la ubicación especificada'},
            'set-content': {'description': 'Escribe contenido nuevo o reemplaza contenido existente en un archivo'},
            'get-help': {'description': 'Muestra información sobre comandos y conceptos de PowerShell'},
            'get-command': {'description': 'Obtiene todos los comandos'},
            'get-member': {'description': 'Obtiene las propiedades y métodos de objetos'},
            'select-object': {'description': 'Selecciona objetos o propiedades de objetos'},
            'where-object': {'description': 'Selecciona objetos de una colección basándose en sus valores de propiedad'},
            'foreach-object': {'description': 'Realiza una operación en cada elemento de una colección de objetos de entrada'},
            'sort-object': {'description': 'Ordena objetos por valores de propiedad'},
            'group-object': {'description': 'Agrupa objetos que contienen el mismo valor para propiedades especificadas'},
            'measure-object': {'description': 'Calcula las propiedades numéricas de objetos'},
            'start-process': {'description': 'Inicia uno o más procesos en el equipo local'},
            'stop-process': {'description': 'Detiene uno o más procesos en ejecución'},
            'get-eventlog': {'description': 'Obtiene los eventos de un registro de eventos'},
            'test-connection': {'description': 'Envía paquetes de solicitud de eco ICMP a uno o más equipos'},
            'invoke-webrequest': {'description': 'Obtiene contenido de una página web en Internet'},
            'get-date': {'description': 'Obtiene la fecha y hora actuales'},
            'get-host': {'description': 'Obtiene un objeto que representa el programa host actual'},
            'get-variable': {'description': 'Obtiene las variables en la consola actual'},
            'set-variable': {'description': 'Establece el valor de una variable'},
            'new-variable': {'description': 'Crea una nueva variable'},
            'remove-variable': {'description': 'Elimina una variable y su valor'},
            'import-module': {'description': 'Agrega módulos a la sesión actual'},
            'get-module': {'description': 'Obtiene los módulos que se han importado o que se pueden importar'},
            'export-csv': {'description': 'Convierte objetos en una serie de cadenas de valores separados por comas'},
            'import-csv': {'description': 'Crea objetos personalizados tipo tabla a partir de elementos de un archivo CSV'}
        }
    
    def _load_common_errors(self) -> Dict:
        """Carga errores comunes y sus explicaciones"""
        return {
            'cmd': {
                'syntax_errors': [
                    "Olvidar comillas en rutas con espacios",
                    "Usar barras diagonales (/) en lugar de barras invertidas (\\)",
                    "No especificar la extensión del archivo",
                    "Usar comandos de Linux en Windows"
                ],
                'permission_errors': [
                    "Intentar acceder a archivos del sistema sin permisos",
                    "Ejecutar comandos que requieren administrador",
                    "Modificar archivos en uso por otros procesos"
                ],
                'path_errors': [
                    "Ruta no encontrada",
                    "Archivo o directorio no existe",
                    "Usar rutas relativas incorrectas"
                ]
            },
            'powershell': {
                'syntax_errors': [
                    "No usar el guión (-) en parámetros",
                    "Olvidar comillas en cadenas con espacios",
                    "Usar comandos CMD en lugar de cmdlets",
                    "No respetar mayúsculas en nombres de variables"
                ],
                'execution_errors': [
                    "Política de ejecución restringida",
                    "Cmdlet no reconocido",
                    "Parámetros incorrectos o faltantes"
                ],
                'pipeline_errors': [
                    "Pipes mal formados",
                    "Objetos incompatibles en pipeline",
                    "Filtros incorrectos"
                ]
            }
        }
