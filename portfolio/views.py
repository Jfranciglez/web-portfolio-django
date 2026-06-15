from django.shortcuts import render


def index(request):
    context = {
        "proyectos": [
            {
                "titulo": "Dental Clinic",
                "subtitulo":"Proyecto académico",
                "descripcion": "Gestión de citas de una clinica dental.",
                "imagen": "dentalclinic.png",
                "enlace": "https://jfranciglez.github.io/trabajo-enfoque-devclient/"
            },
            {
                "titulo": "ShoesRelife",
                "subtitulo":"Proyecto académico",
                "descripcion":"Tienda online de zapatillas.",
                "imagen": "shoesrelife.png", 
                "enlace": "https://ejercicios-php-02-d7b70.wasmer.app/"
            },
            {
                "titulo": "Visitas Virtuales",
                "subtitulo":"Proyecto prácticas",
                "descripcion": "Visistas virtuales de los institutos de Davante.",
                "imagen": "visitas.png", 
                "enlace": "https://visitasvirtuales.dedyn.io/"
            },
            {
                "titulo": "100 Caños",
                "subtitulo":"Proyecto prácticas",
                "descripcion": "Web de reservas de experiencias de oleoturismo en Málaga.",
                "imagen": "100caños.png", 
                "enlace": "https://100canos.com/"
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
                {"titulo": "AWS", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg", "nivel": "Intermedio"},
                {"titulo": "MySQL", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg", "nivel": "Intermedio"},
                {"titulo": "MongoDB", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg", "nivel": "Intermedio"},
                {"titulo": "Java", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg", "nivel": "Intermedio"},
                {"titulo": "React", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg", "nivel": "Intermedio"},
                {"titulo": "Node.js", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg", "nivel": "Intermedio"}, 
                {"titulo": "Express.js", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg", "nivel": "Intermedio"},
                {"titulo": "PostgreSQL", "icono": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg", "nivel": "Intermedio"},
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
