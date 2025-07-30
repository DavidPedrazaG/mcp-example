# 🧠 MCP Central AI Ops

**MCP Central AI Ops** es una arquitectura modular basada en el patrón **Host → Clientes → Servidores** inspirada en el [Model Context Protocol](https://modelcontextprotocol.io). Este proyecto simula un sistema de **inteligencia artificial operativa distribuida**, donde una IA central coordina múltiples módulos especializados que interactúan con sus propios backends.

## 🎯 Objetivos

- Modelar una arquitectura MCP realista y extensible
- Simular flujos de trabajo inteligentes con clientes especializados
- Modularizar clientes y servidores para simular microservicios
- Usar sockets y JSON como base de comunicación simple pero poderosa

## 🏗️ Arquitectura General

```
         [ tasks.json ]
               |
             [HOST]
               |
  ┌────────────┼────────────┐
  ▼            ▼            ▼
[Client1]    [Client2]    [Client3]
 Monitor      FileMgr        DB
   |            |            |
   ▼            ▼            ▼
[Server1]    [Server2]    [Server3]
  7001         7002         7003
```

- El Host lee una lista de tareas y las asigna a los clientes adecuados
- Cada cliente se conecta directamente a su servidor por socket
- La comunicación se realiza en formato JSON

## 🗂️ Estructura del Proyecto

```
/mcp_ai_ops/
├── host.py                    # Orquestador central
├── tasks.json                 # Lista de tareas a ejecutar
├── shared/
│   └── protocol.py            # Funciones para comunicación JSON por sockets
├── clients/
│   ├── base.py                # Clase base común para todos los clientes
│   ├── monitor_client.py      # Cliente de métricas
│   ├── file_client.py         # Cliente de archivos
│   └── db_client.py           # Cliente de base de datos
└── servers/
    ├── monitor_server.py      # Servidor de métricas
    ├── file_server.py         # Servidor de archivos
    └── db_server.py           # Servidor de base de datos
```

## 🔄 Flujo de Ejecución

1. El usuario ejecuta los servidores (cada uno en su terminal)
2. El host se ejecuta, lee `tasks.json`, y despacha tareas
3. Cada cliente se conecta al puerto correspondiente y envía su tarea
4. El servidor procesa la tarea y devuelve un resultado
5. El cliente imprime la respuesta, y el host continúa con la siguiente tarea

## ⚙️ Uso

### 🛠️ 1. Ejecutar los servidores

En tres terminales distintas:

```bash
python python -m servers.monitor_server
python python -m servers.file_server
python python -m servers.db_server
```

### 🚀 2. Ejecutar el host

```bash
python -m host
```

### 📄 3. Tareas ejecutadas

```json
[
  {
    "type": "monitor",
    "action": "get_metrics",
    "params": {"cpu": true, "mem": true}
  },
  {
    "type": "file",
    "action": "read",
    "params": {"path": "/logs/app.log"}
  },
  {
    "type": "db",
    "action": "insert",
    "params": {
      "table": "events",
      "data": {"level": "info", "msg": "todo ok"}
    }
  }
]
```

## ✅ Resultado Esperado

- El host imprime en consola el resultado de cada tarea enviada
- Cada cliente conecta y procesa su mensaje
- Los servidores simulan las operaciones como si fueran servicios reales

## 🧠 Ideas para Expandir

- Autenticación con tokens en el protocolo JSON
- Persistencia real en `db_server` con SQLite
- UI web (Flask o Streamlit) para visualizar resultados
- Soporte a múltiples tareas concurrentes con threading o asyncio
- Logs estructurados por cliente y servidor