from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def sobre_mi(request):
    return render(request, "sobre_mi.html")

def proyectos(request):
    context = {
    "proyectos": [
        {
            "titulo": "",
            "descripcion": ""
        },
        {
            "titulo": "",
            "descripcion": ""
        },
        {
            "titulo": "",
            "descripcion": ""
        },
    ]
}

    return render(request, "proyectos.html")

def habilidades(request):
    context = {
    "proyectos": [
        {
            "titulo": "",
            "descripcion": ""
        },
        {
            "titulo": "",
            "descripcion": ""
        },
        {
            "titulo": "",
            "descripcion": ""
        },
    ]
}

    return render(request, "habilidades.html")

def contacto(request):
    context = {
        "localizacion": "Málaga, España.",

        "contacto": {
            "email": "francicarrillo61@gmail.com"
        }
    } 
    return render(request, "contacto.html", context=context)