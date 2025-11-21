from transformers import pipeline

clf = pipeline("text-classification", model="./ms_pines_funcion_classifier", tokenizer="./ms_pines_funcion_classifier")

print("="*60)
print("PRUEBAS DEL CLASIFICADOR DE PINES POR FUNCIÓN")
print("="*60)

# ========== EJEMPLOS DECORATIVOS ==========
print("\n🎨 PRUEBAS - CATEGORÍA: DECORATIVO")
print("-" * 60)

print("\n1. Pin kawaii:")
print(clf("Pin metálico redondo 3.7cm con diseño de gato kawaii en colores pastel"))

print("\n2. Pin aesthetic:")
print(clf("Pin redondo 3.2cm aesthetic vaporwave con palmeras y sol retro"))

print("\n3. Pin de comida:")
print(clf("Pin metálico 3.7cm con diseño de tacos y burritos mexicanos"))

print("\n4. Pin de animales:")
print(clf("Pin redondo 5.6cm con koala durmiendo en rama de eucalipto"))

print("\n5. Pin retro:")
print(clf("Pin metálico 3.2cm con vinilo tocadiscos música retro años 70"))

# ========== EJEMPLOS COLECCIONABLES ==========
print("\n\n🏆 PRUEBAS - CATEGORÍA: COLECCIONABLE")
print("-" * 60)

print("\n1. Edición limitada:")
print(clf("Pin redondo 3.7cm edición limitada 50 unidades numerado 12/50"))

print("\n2. Exclusivo de convención:")
print(clf("Pin metálico 5.6cm Comic-Con 2024 exclusivo con certificado de autenticidad"))

print("\n3. Firmado por artista:")
print(clf("Pin redondo 3.2cm firmado por artista digital numerado 1/100"))

print("\n4. Error de impresión raro:")
print(clf("Pin metálico 3.7cm error de impresión doble capa considerado pieza rara"))

print("\n5. Exclusivo streaming:")
print(clf("Pin redondo 3.7cm de Twitch streamer para suscriptores tier 3 exclusivo"))

# ========== EJEMPLOS PROMOCIONALES ==========
print("\n\n📢 PRUEBAS - CATEGORÍA: PROMOCIONAL")
print("-" * 60)

print("\n1. Corporativo:")
print(clf("Pin metálico 5.6cm con logo de empresa tecnológica para evento anual"))

print("\n2. Uniforme de empleados:")
print(clf("Pin redondo 3.2cm con logo de cadena de restaurantes para meseros"))

print("\n3. Marca deportiva:")
print(clf("Pin metálico 3.7cm con logo de marca deportiva para maratón 2025"))

print("\n4. Campaña de marketing:")
print(clf("Pin redondo 5.6cm de startup para repartir en feria de emprendimiento"))

print("\n5. Universidad:")
print(clf("Pin metálico 3.2cm universitario para repartir en open house a estudiantes"))

# ========== EJEMPLOS FUNCIONALES ==========
print("\n\n⚙️ PRUEBAS - CATEGORÍA: FUNCIONAL")
print("-" * 60)

print("\n1. Identificación con foto:")
print(clf("Pin redondo 5.6cm con foto y nombre para identificación de empleados"))

print("\n2. Código QR:")
print(clf("Pin metálico 3.7cm con código QR para credencial de evento empresarial"))

print("\n3. Recuerdo de graduación:")
print(clf("Pin redondo 5.6cm con foto de graduación personalizada recuerdo ceremonia 2025"))

print("\n4. Membresía VIP:")
print(clf("Pin metálico 3.2cm con código de descuento para clientes VIP del club"))

print("\n5. Credencial de hospital:")
print(clf("Pin redondo 3.7cm con logo de hospital para personal médico de turno"))

# ========== EJEMPLOS AMBIGUOS (para ver cómo decide el modelo) ==========
print("\n\n❓ PRUEBAS - CASOS AMBIGUOS")
print("-" * 60)

print("\n1. Pin con múltiples características:")
print(clf("Pin metálico 5.6cm edición limitada de empresa con logo corporativo numerado"))

print("\n2. Pin decorativo con función:")
print(clf("Pin redondo 3.7cm con diseño kawaii y código QR en la parte trasera"))

print("\n3. Pin promocional coleccionable:")
print(clf("Pin metálico 3.2cm exclusivo de convención para empleados de la marca"))

print("\n4. Solo especificaciones:")
print(clf("Pin redondo metálico de 3.7cm de diámetro con imagen personalizada"))

print("\n5. Descripción genérica:")
print(clf("Pin metálico redondo con diseño colorido"))

# ========== EJEMPLOS DE CASOS REALES ==========
print("\n\n🛒 PRUEBAS - CASOS DE CLIENTES REALES")
print("-" * 60)

print("\n1. Cliente pidiendo diseño personalizado:")
print(clf("Quiero un pin de 5.6cm con la foto de mi perro para regalar en su cumpleaños"))

print("\n2. Empresa pidiendo merchandising:")
print(clf("Necesito 200 pines de 3.2cm con nuestro logo para la conferencia de marzo"))

print("\n3. Artista independiente:")
print(clf("Pin de 3.7cm con mi ilustración original de dragón para vender en mi tienda"))

print("\n4. Fan coleccionista:")
print(clf("Pin de 3.2cm de mi personaje favorito de anime edición especial numerada"))

print("\n5. Evento social:")
print(clf("Pins de 5.6cm con las fotos de los novios para recuerdo de boda"))

print("\n" + "="*60)
print("FIN DE LAS PRUEBAS")
print("="*60)  

