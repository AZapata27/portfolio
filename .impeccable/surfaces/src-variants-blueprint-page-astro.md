---
version: 1
slug: "src-variants-blueprint-page-astro"
primary_target: "src/variants/blueprint/Page.astro"
related_targets: ["src/pages/blueprint/index.astro","src/pages/es/blueprint/index.astro"]
---

# Surface brief: variante Blueprint (`/blueprint/`, `/es/blueprint/`)

## Scope and mode

Portafolio de una sola página por idioma. Modo **Experience** con cierre Persuade: el dibujo es la
obra; el contacto es la acción. Brief pinned por el usuario: el concepto "ruta EIP" de su README
(`AZapata27/AZapata27`, rama `docs/readme-ruta-eip`): plano técnico, grilla, bloque de título,
ruta de integración con router, ramas, agregador y control bus.

## Audience, job, action, proof, constraints

- Audiencia: reclutadores, CTOs y clientes (en/es), escritorio en jornada laboral; a veces móvil.
- Job: entender en un viewport qué hace Andrés y por qué es distinto; encontrar pruebas; contactar.
- Acción primaria: escribir (mailto); secundarias: LinkedIn, GitHub, descargar CV.
- Pruebas: cifras del CV (`profile.metrics`), tabla de experiencia, casos (`projects`), stack.
- Constraints: contenido sólo desde `src/content`; sin JS obligatorio; AA; reduced motion; tema claro.

## Direction contract

THESIS: La página ES un plano de ingeniería de una sola ruta: el problema del visitante entra por un
canal, un content-based router lo manda a Arquitectura, Integración o AI-native, un agregador junta
las ramas y sale a producción; el liderazgo corre como control bus. Rechaza el arreglo por defecto de
la categoría (foto + tarjetas iguales + grilla de skills): no hay tarjetas, hay hojas de dibujo con
marco, reglas de zona, bloque de título, tabla de revisiones, lista de partes y detalles numerados.

OWN-WORLD: Papel #FAFAF7 con grilla de puntos tenue #D6D8D4; tinta #151515; grafito #4A4F55 para
secundario; ámbar #F2A900 como único acento (marcadores, llamadas numeradas ①–④, el sobre del
mensaje, la fila de acción primaria) y ámbar oscuro #8A5A00 para strings de código; azul de dibujo
#1F5FBF para el control bus (línea punteada) y los enlaces. Display: Barlow Condensed 700/800 en
mayúsculas, tracking −0.02em, grande. Cuerpo: Barlow 400/500, 17–18px, medida 60–72ch. Etiquetas,
tablas y código: JetBrains Mono 12–14px, etiquetas en mayúsculas con tracking 0.08em. Líneas de
1.5–2px de tinta; hojas con borde 1px y marcas de esquina; radio 0; sin sombras (la profundidad es
grosor de línea, no elevación). Iconos de marca de simple-icons en tinta (monocromo) dentro de la
lista de partes; iconos EIP (canal, router, agregador, endpoint) dibujados en SVG a mano con el mismo
trazo. Selección de texto ámbar sobre tinta; foco visible: contorno 2px ámbar con offset 2px.

STORY: El visitante ve un plano titulado con el nombre y "software architect"; entiende que el
oficio es enrutar problemas a la disciplina correcta; lo cree por la tabla REVISIONS (experiencia
como filas REV / FECHA / DESCRIPCIÓN / BY), las hojas DETAIL A–G (proyectos con su cifra como cota)
y la PARTS LIST (stack con logos); actúa desde el bloque de título, que es también el bloque de
contacto (email en fila ámbar, LinkedIn, GitHub, CV).

FIRST VIEWPORT: Una hoja a todo el ancho con marco, regla de columnas (1–6) arriba y zonas (A–D) a
la izquierda. Arriba a la izquierda: nombre en Barlow Condensed clamp(3rem, 8vw, 6rem) en
mayúsculas; debajo, en Barlow, "Software architect, 10+ years. Fintech, banking, logistics and
transportation, integrations." En el centro: el diagrama de la ruta como SVG responsivo: canal de
entrada ("inbound · your problem", con el sobre ámbar) → content-based router → tres cajas de rama
(ARCHITECTURE / INTEGRATION / AI-NATIVE DEVELOPER, cada una con su icono EIP y sus `parts` en mono)
→ agregador → "outbound · production" → bloque negro PROD; el control bus en azul punteado por
encima con "teams · 200+ people led · AI trainings". Abajo a la izquierda: DETAIL A `Route.java`
con la ruta en DSL de Camel (strings en ámbar oscuro). Abajo a la derecha: el bloque de título como
tabla mono (DRAWING andres-zapata.route · ROLE · EXPERIENCE · DOMAINS · SCOPE · CONTACT) donde la
fila CONTACT lleva el mailto resaltado en ámbar, y LinkedIn / GitHub / CV como filas. En móvil (<
768px): nombre, luego el diagrama apilado en vertical (ramas en columna, conectores verticales),
luego el bloque de título como lista; el DETAIL A se oculta o se muestra como bloque de código con
scroll horizontal.

FORM: "Juego de hojas de dibujo" (sheet set): cada sección es una hoja numerada (SHEET 1/5 …) con
su propio bloque de título mínimo; posición 1 de la lista ordenada (2: una sola hoja larga; 3:
pestañas por hoja; 4: póster esquemático). Semilla: brief-pinned (README `docs/readme-ruta-eip`),
sin tirada de dados (usuario ausente; se registra la sustitución).

MOMENTO MEMORABLE (interacción firmada): al cargar, el sobre ámbar recorre la ruta (offset-path /
stroke-dashoffset) y las ramas se "entintan" con retardo; al pasar el cursor por una rama se
resalta su cable y su nota numerada. Con `prefers-reduced-motion` todo es estático y completo.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the
verdict, DESIGN.md, and every shipping raster carrying its provenance.

## Unresolved

- Qué variante se publica en `/` (decisión de Andrés).
- Imagen Open Graph (`/og.png`) pendiente hasta elegir variante.
