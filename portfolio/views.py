from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def sobre_mi(request):
    return render(request, "sobre_mi.html")


def proyectos(request):
    context = {
        "proyectos": [
            {
                "titulo": "Gestión de Almacén",
                "descripcion": "Aplicación tipo CRUD para la gestión de stock de un almacén de productos lácteos.",
                "render":"https://jfranciglez.alwaysdata.net/"
            },
            {
                "titulo": "Carta Online",
                "descripcion": "Carta Online de un restaurante con reparto a domicilio donde se puede seleccionar productos y obtener el recibo.",
                "render":"https://ejercicios-php-02-d7b70.wasmer.app/"
            },
            {
                "titulo": "Panaderia Dulce Enigma",
                "descripcion": "Web de una panaderia donde muestra sus productos  y  ofertas, ubicación, contacto."
            },
        ]
    }

    return render(request, "proyectos.html", context)


def habilidades(request):
    context = {
        "habilidades": [  
            {
                "titulo": "Python / Django",
                "descripcion": "Desarrollo backend con Django, incluyendo manejo de vistas, templates y ORM."
            },
            {
                "titulo": "HTML / CSS / JS",
                "descripcion": "Diseño de interfaces web modernas y adaptables."
            },
            {
                "titulo": "Git / GitHub, Docker, AWS",
                "descripcion": "Control de versiones y despliegue de proyectos en la nube."
            },
        ]
    }

    return render(request, "habilidades.html", context)


def contacto(request):
    context = {
        "localizacion": "Málaga, España",
        "contacto": {
            "email": "francicarrillo61@gmail.com",
        }
    }
    return render(request, "contacto.html", context)
