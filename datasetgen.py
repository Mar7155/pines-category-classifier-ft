import csv
import random

# Configuración
NUM_SAMPLES = 2000
SAMPLES_PER_CATEGORY = NUM_SAMPLES // 4  # 500 por categoría

# Componentes para generar descripciones variadas
tamanos = ["3.2cm", "3.7cm", "5.6cm"]

# Temas y diseños por categoría
decorativos = {
    "animales": ["gato", "perro", "koala", "panda", "zorro", "búho", "conejo", "hamster", "perezoso", "erizo", "llama", "unicornio", "dragón", "ballena", "delfín", "oso polar", "pingüino", "camaleón", "libélula", "mariposa"],
    "comida": ["sushi", "ramen", "tacos", "pizza", "café", "té matcha", "bubble tea", "donut", "helado", "aguacate", "hamburguesa", "burrito", "cupcake", "macaron", "waffle", "croissant", "hot dog", "bento box"],
    "naturaleza": ["montañas", "bosque", "océano", "flores", "cactus", "suculentas", "palmeras", "luna", "estrellas", "sol", "arcoíris", "nubes", "cascada", "lago", "volcán", "desierto", "aurora boreal", "atardecer"],
    "objetos": ["cámara vintage", "vinilo", "cassette", "máquina de escribir", "teléfono retatorio", "bicicleta", "patines", "guitarra", "telescopio", "brújula", "faro", "globo aerostático", "cohete", "robot", "paraguas", "maleta vintage", "tostadora"],
    "estilos": ["kawaii", "aesthetic", "minimalista", "retro", "vaporwave", "pixel art", "line art", "acuarela", "geométrico", "boho", "cyberpunk", "steampunk", "art deco", "pop art", "grunge"]
}

coleccionables = {
    "tipo": ["edición limitada", "exclusivo", "variant holográfico", "chase metallic", "error de impresión", "prototype sample", "primera edición", "edición aniversario", "variant glow in the dark"],
    "evento": ["Comic-Con", "E3", "convención anime", "festival de cine", "Crunchyroll Expo", "PAX", "BlizzCon", "TwitchCon", "VidCon", "Dragon Con"],
    "numeracion": ["numerado 1/50", "numerado 12/100", "numerado 25/500", "#5/25", "#142/200", "edición de 100 unidades", "solo 25 piezas", "edición de 75"],
    "artista": ["firmado por artista", "diseñado por ilustrador independiente", "colaboración con artista digital", "creado por animator", "artwork original de diseñador", "ilustración exclusiva"],
    "plataforma": ["Kickstarter backer reward", "Patreon tier exclusivo", "Etsy edición limitada", "DeviantArt exclusive", "Instagram artist series", "TikTok milestone"]
}

promocionales = {
    "empresas": ["startup tecnológica", "empresa de software", "compañía de seguros", "banco", "aerolínea", "hotel boutique", "cadena de restaurantes", "cervecería artesanal", "marca de ropa", "marca deportiva", "farmacéutica", "automotriz", "inmobiliaria", "consultora"],
    "eventos": ["conferencia", "congreso", "maratón", "festival", "hackathon", "feria de emprendimiento", "open house", "evento anual", "campaña electoral", "lanzamiento de producto"],
    "uso": ["uniforme de empleados", "identificación de personal", "merchandising oficial", "programa de afiliados", "campaña de marketing", "regalo corporativo", "bienvenida nuevos empleados"],
    "sector": ["tecnología", "salud", "educación", "deportes", "entretenimiento", "gastronomía", "moda", "finanzas", "turismo", "medios"]
}

funcionales = {
    "identificacion": ["con foto y nombre", "con código de empleado", "con logo y departamento", "credencial de acceso", "identificación de personal", "badge de seguridad"],
    "eventos_personales": ["graduación", "boda", "quinceañera", "baby shower", "aniversario", "cumpleaños", "bautizo", "primera comunión"],
    "membresia": ["membresía VIP", "club de fans", "programa de lealtad", "suscripción premium", "acceso exclusivo", "pase backstage"],
    "tecnologia": ["código QR", "código de descuento", "QR menú digital", "acceso área restringida", "código de vestidor"],
    "lugares": ["hospital", "escuela", "universidad", "biblioteca", "museo", "zoo", "gimnasio", "spa", "teatro", "laboratorio", "veterinaria", "restaurante", "cafetería", "oficina"]
}

descriptores = ["diseño", "ilustración", "imagen", "artwork", "gráfico", "estampado", "dibujo", "representación"]
colores = ["colores pastel", "colores vibrantes", "dorado", "plateado", "negro y blanco", "arcoíris", "metálico", "brillante", "mate", "holográfico"]
estilos_visuales = ["minimalista", "detallado", "cartoon", "realista", "abstracto", "vintage", "moderno", "elegante", "divertido", "sofisticado"]

def generar_decorativo():
    tamano = random.choice(tamanos)
    categoria_tema = random.choice(list(decorativos.keys()))
    tema = random.choice(decorativos[categoria_tema])
    descriptor = random.choice(descriptores)
    detalle = random.choice(colores + estilos_visuales)
    
    templates = [
        f"Pin metálico redondo {tamano} con {descriptor} de {tema} {detalle}",
        f"Pin redondo {tamano} {tema} estilo {detalle}",
        f"Pin metálico {tamano} con {tema} {descriptor} {detalle}",
        f"Pin redondo metálico {tamano} de {tema} con acabado {detalle}",
        f"Pin {tamano} con ilustración de {tema} {detalle}"
    ]
    return random.choice(templates)

def generar_coleccionable():
    tamano = random.choice(tamanos)
    tipo = random.choice(coleccionables["tipo"])
    detalle = random.choice(coleccionables["numeracion"] + coleccionables["evento"] + coleccionables["artista"] + coleccionables["plataforma"])
    
    templates = [
        f"Pin metálico redondo {tamano} {tipo} {detalle}",
        f"Pin redondo {tamano} {detalle} {tipo}",
        f"Pin metálico {tamano} {tipo} con certificado de autenticidad {detalle}",
        f"Pin redondo {tamano} exclusivo {detalle}",
        f"Pin metálico {tamano} {tipo} colección {detalle}"
    ]
    return random.choice(templates)

def generar_promocional():
    tamano = random.choice(tamanos)
    empresa = random.choice(promocionales["empresas"])
    uso = random.choice(promocionales["uso"])
    evento = random.choice(promocionales["eventos"])
    
    templates = [
        f"Pin metálico redondo {tamano} con logo de {empresa} para {uso}",
        f"Pin redondo {tamano} de {empresa} para {evento}",
        f"Pin metálico {tamano} corporativo de {empresa} {uso}",
        f"Pin redondo {tamano} promocional con logo {empresa} para {evento}",
        f"Pin metálico {tamano} de {empresa} para {uso} en {evento}"
    ]
    return random.choice(templates)

def generar_funcional():
    tamano = random.choice(tamanos)
    funcion = random.choice(funcionales["identificacion"] + funcionales["tecnologia"])
    lugar = random.choice(funcionales["lugares"])
    evento = random.choice(funcionales["eventos_personales"])
    
    templates = [
        f"Pin metálico redondo {tamano} {funcion} para {lugar}",
        f"Pin redondo {tamano} con foto personalizada recuerdo de {evento}",
        f"Pin metálico {tamano} {funcion} para personal de {lugar}",
        f"Pin redondo {tamano} con {funcion} para evento de {evento}",
        f"Pin metálico {tamano} {funcion} {lugar} identificación"
    ]
    return random.choice(templates)

# Generar dataset
dataset = []

print("Generando dataset de 2000 ejemplos...")
print(f"- Decorativos: {SAMPLES_PER_CATEGORY}")
print(f"- Coleccionables: {SAMPLES_PER_CATEGORY}")
print(f"- Promocionales: {SAMPLES_PER_CATEGORY}")
print(f"- Funcionales: {SAMPLES_PER_CATEGORY}")

for _ in range(SAMPLES_PER_CATEGORY):
    dataset.append(("decorativo", generar_decorativo()))
    dataset.append(("coleccionable", generar_coleccionable()))
    dataset.append(("promocional", generar_promocional()))
    dataset.append(("funcional", generar_funcional()))

# Mezclar el dataset
random.shuffle(dataset)

# Guardar en CSV
filename = "./datasets/ms_pines_funcion_2000ejemplos.csv"
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['v1', 'v2'])
    writer.writerows(dataset)

print(f"\n✅ Dataset generado exitosamente: {filename}")
print(f"📊 Total de ejemplos: {len(dataset)}")
print(f"\n🔍 Primeros 5 ejemplos:")
for i in range(5):
    print(f"  {i+1}. {dataset[i][0]}: {dataset[i][1]}")
print(f"\n🔍 Últimos 5 ejemplos:")
for i in range(-5, 0):
    print(f"  {2000+i+1}. {dataset[i][0]}: {dataset[i][1]}")