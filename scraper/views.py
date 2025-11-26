import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def buscar(request):
    resultados = []

    if request.method == "POST":
        termino = request.POST.get("termino")

        # URL de búsqueda en Wikipedia (español)
        url = f"https://es.wikipedia.org/w/index.php?search={termino}&title=Especial:Buscar&fulltext=1"
        headers = {"User-Agent": "Mozilla/5.0"}
        respuesta = requests.get(url, headers=headers)

        # Revisar que la respuesta sea correcta
        if respuesta.status_code == 200:
            soup = BeautifulSoup(respuesta.text, "html.parser")

            # Extraer resultados de búsqueda
            search_items = soup.select("li.mw-search-result")
            if not search_items:
                # Si hay un artículo directo, sacar el título y párrafo inicial
                titulo_tag = soup.select_one("h1#firstHeading")
                parrafo_tag = soup.select_one("div.mw-parser-output > p")
                if titulo_tag and parrafo_tag:
                    resultados.append({
                        "titulo": titulo_tag.text,
                        "link": request.build_absolute_uri(respuesta.url),
                        "resumen": parrafo_tag.text.strip()
                    })
            else:
                # Extraer múltiples resultados
                for item in search_items[:5]:  # solo 5 primeros
                    titulo_tag = item.select_one("div.mw-search-result-heading a")
                    resumen_tag = item.select_one("div.searchresult")
                    titulo = titulo_tag.text if titulo_tag else "Sin título"
                    link = "https://es.wikipedia.org" + titulo_tag["href"] if titulo_tag else "#"
                    resumen = resumen_tag.text if resumen_tag else ""
                    resultados.append({"titulo": titulo, "link": link, "resumen": resumen})

    return render(request, "scraper/buscar.html", {"resultados": resultados})
