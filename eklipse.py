import shutil

# Lee la plantilla HTML
with open('template.html', 'r') as file:
    template_content = file.read()

# Guarda el contenido modificado en un nuevo archivo
with open('mapa_urduliz.html', 'w') as file:
    file.write(template_content)

# Mueve el archivo a la carpeta adecuada para servirlo
shutil.move('mapa_urduliz.html', 'docs/mapa_urduliz.html')

print("Mapa generado y guardado como 'docs/mapa_urduliz.html'")
