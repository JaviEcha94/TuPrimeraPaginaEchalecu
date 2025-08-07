# TuPrimeraPaginaEchalecu

Proyecto web desarrollado en Django siguiendo el patrón MVT como parte del curso de Python en Coderhouse.

## 🎯 Objetivo

Crear una aplicación web básica que permita:
- Agregar personas mediante un formulario.
- Ver el listado de personas.
- Buscar personas por nombre o email.
- Usar herencia de templates para reutilizar estructura HTML.

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Django 4
- SQLite3 (base de datos por defecto)

---

## 📦 Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/JaviEcha94/TuPrimeraPaginaEchalecu.git
cd TuPrimeraPaginaEchalecu
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv env
source env/bin/activate  # Mac/Linux
.\env\Scriptsctivate   # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear base de datos y migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Iniciar el servidor

```bash
python manage.py runserver
```

Luego ingresá en tu navegador a:  
👉 http://127.0.0.1:8000/

---

## 🚀 Funcionalidades

- **Página principal**: muestra el listado de personas (`/`)
- **Formulario**: para agregar personas nuevas (`/agregar/`)
- **Búsqueda**: en el listado por nombre o email
- **Templates**: uso de herencia (`base.html`, `listado.html`, `formulario.html`)
- **Navegación**: menú de navegación entre vistas

---

## 📁 Estructura del proyecto

```
TuPrimeraPaginaEchalecu/
├── personas/
│   ├── models.py          # Modelo Persona
│   ├── forms.py           # Formulario para agregar personas
│   ├── views.py           # Vistas de listado y formulario
│   ├── urls.py            # Rutas de la app
│   └── templates/
│       ├── base.html      # Template base
│       ├── listado.html   # Listado con búsqueda
│       └── formulario.html# Formulario para crear
├── miproyecto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

---
