import folium

# Coordenadas iniciales (Urduliz, Vizcaya, España)
urduliz_coords = [43.3970, -2.9770]

# Coordenadas de un polígono que representa una zona señalada
zona_coords = [
    [43.3980, -2.9790],
    [43.3980, -2.9750],
    [43.3950, -2.9750],
    [43.3950, -2.9790]
]

# Crear un mapa centrado en Urduliz
m = folium.Map(location=urduliz_coords, zoom_start=14)

# Añadir un marcador para Urduliz
folium.Marker(
    location=urduliz_coords,
    popup='Urduliz, Vizcaya, España',
    icon=folium.Icon(icon='cloud')
).add_to(m)

# Añadir un polígono para la zona señalada
folium.Polygon(
    locations=zona_coords,
    color='red',
    fill=True,
    fill_color='red',
    fill_opacity=0.4,
    popup='Zona señalada'
).add_to(m)

# Guardar el mapa en la carpeta 'docs' como 'mapa_urduliz.html'
m.save('docs/mapa_urduliz.html')

print("Mapa generado y guardado como 'docs/mapa_urduliz.html'")
