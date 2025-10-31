from django.shortcuts import render


def index(request):
    context = {
        "proyectos": [
            {
                "titulo": "Gestión de Almacén",
                "descripcion": "Aplicación CRUD para controlar stock de productos lácteos.",
                "imagen": "almacen.png",
                "enlace": "https://jfranciglez.alwaysdata.net/"
            },
            {
                "titulo": "Carta Online y Juego Apuesta y Gana",
                "descripcion": "Carta digital para restaurantes con pedidos a domicilio como ejercicio1 y el juego Apuesta y gana como ejercicio2.",
                "imagen": "hamb.png", 
                "enlace": "https://ejercicios-php-02-d7b70.wasmer.app/"
            },
            {
                "titulo": "Panaderia Dulce Enigma",
                "descripcion": "Presencia digital de una tienda donde muestra sus prooductos y ofertas.",
                "imagen": "panad.png",
                "enlace": ""
            },
        ],
        "habilidades": [
                {"titulo": "Python", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg", "nivel": "Avanzado"},
                {"titulo": "Django", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg", "nivel": "Avanzado"},
                {"titulo": "HTML5", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg", "nivel": "Avanzado"},
                {"titulo": "CSS3", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg", "nivel": "Avanzado"},
                {"titulo": "JavaScript", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "nivel": "Avanzado"},
                {"titulo": "PHP", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg", "nivel": "Intermedio"},
                {"titulo": "TailwindCSS", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg", "nivel": "Avanzado"},
                {"titulo": "Angular", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angular/angular-original.svg", "nivel": "Intermedio"},
                {"titulo": "FastAPI", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg", "nivel": "Intermedio"},
                {"titulo": "Docker", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg", "nivel": "Intermedio"},
                {"titulo": "AWS", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg", "nivel": "Básico"},
                {"titulo": "MySQL", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg", "nivel": "Intermedio"},
                {"titulo": "MongoDB", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg", "nivel": "Intermedio"},
                {"titulo": "Java", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", "nivel": "Intermedio"},
            ],
       "contacto": {
            "ubicacion": "Málaga, España",
            "email": "francicarrillo61@gmail.com",
            "linkedin": "https://www.linkedin.com/in/franci-carrillo-b72746382",
            "github": "https://github.com/Jfranciglez",
            "descripcion": "¡Hablemos!.",
       }

        
    }
    return render(request, "index.html", context)
