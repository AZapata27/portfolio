---
version: 1
slug: "src-variants-script-page-astro"
primary_target: "src/variants/script/Page.astro"
related_targets: ["src/pages/script/index.astro","src/pages/es/script/index.astro"]
---

# Surface brief: variante Script (`/script/`, `/es/script/`)

## Scope and mode

Portafolio de una sola página por idioma. Modo **Experience** con cierre Persuade: la persona y su
guion son la obra; el contacto es la salida de escena. Brief pinned por el usuario: el concepto
"conciso / tres voces" de su README (`AZapata27/AZapata27`, rama `docs/readme-conciso`): papel,
máquina de escribir, un guion de trabajo en tres voces (el arquitecto, el constructor, el líder),
retrato posterizado.

## Audience, job, action, proof, constraints

- Audiencia: reclutadores, CTOs y clientes (en/es), escritorio en jornada laboral; a veces móvil.
- Job: conocer a la persona y cómo trabaja en un minuto; encontrar pruebas; contactar.
- Acción primaria: escribir (mailto); secundarias: LinkedIn, GitHub, descargar CV.
- Pruebas: cifras del CV (`profile.metrics`), escenas de experiencia, tomas (proyectos), el escritorio (stack).
- Constraints: contenido sólo desde `src/content`; sin JS obligatorio; AA; reduced motion; tema claro.

## Direction contract

THESIS: Un guion de trabajo en tres voces de un mismo ingeniero. La página se lee como un libreto:
encabezados de escena, nombres de personaje en mayúsculas, parlamentos, acotaciones entre paréntesis
y direcciones de escena en cursiva. La voz manda sobre la caja: no hay tarjetas ni métricas-héroe;
la jerarquía la hace el registro tipográfico de cada voz (ALTO, RÁPIDO, CALMO).

OWN-WORLD: Papel #F4F3EF con grano fino (SVG feTurbulence en data-URI, opacidad ≤ 0.08); tinta
#111111; gris #5A5A5A para acotaciones; reglas #CFCAC1 (1.5px) y una barra vertical de 3px de tinta
como espina estructural. Tres colores de voz que poseen regiones, no sólo palabras: el arquitecto =
tinta (la voz alta: tipografía más grande), el constructor = naranja #FF5A00 (la voz rápida: su acto
invierte a campo naranja con texto papel, el único momento "drenched"), el líder = azul #2340D9 (la
voz calma: más blanco, texto más pequeño, sellos fantasma en azul). Display: Big Shoulders Display
800/900 en mayúsculas, tracking −0.02em, clamp(3.5rem, 9vw, 7rem) para el nombre. Cuerpo: Courier
Prime 400/700 a 17–18px, medida 60–68ch, interlineado 1.6; acotaciones en Courier cursiva gris; cues
de personaje en Big Shoulders 1.25–1.75rem. Retrato: `src/assets/portrait.svg` (tres capas) teñido
por voz vía `fill` (por defecto tinta/grafito/papel-oscuro; en el acto del constructor, naranjas).
Sellos: etiquetas en Courier mayúsculas, rotadas −3° / +2.5° / −90°, como en el README. Radio 0;
sin sombras. Selección de texto naranja sobre tinta; foco visible: subrayado 3px del color de la voz.

STORY: El visitante conoce a una persona (retrato + nombre + reparto de tres voces); lee cómo trabaja
en tres registros (el arquitecto hace que los sistemas se hablen; el constructor mete IA en cada
paso; el líder: metas, no horas); recorre las ESCENAS (experiencia: "ESCENA 8 · INT. FLYPASS · 2024–"),
las TOMAS (proyectos, con su cifra como acotación), EL ESCRITORIO (stack) y la SALIDA (contacto:
"Exit. The team keeps shipping." → escribime / LinkedIn / CV).

FIRST VIEWPORT: Dos columnas separadas por la barra vertical de 3px. Izquierda (~32%): nombre
apilado en Big Shoulders; el reparto con cuadrados de color (■ THE ARCHITECT loud / ■ THE BUILDER
fast / ■ THE LEADER calm) en Courier; "Software architect, 10+ years." en Courier bold; línea de
dominios en gris; botón sellado "WRITE ME" (fondo tinta, texto papel, Big Shoulders) con LinkedIn,
GitHub y CV como enlaces de guion debajo. Derecha: el retrato grande anclado abajo a la derecha, el
sello fantasma "THE LEADER, CALM" en azul arriba (tres capas con opacidad creciente), el sello
"THE ARCHITECT, LOUD" rotado −90° pegado a la barra, y "THE BUILDER, FAST" en naranja rotado 2.5°
cerca del retrato. En móvil (< 768px): nombre, retrato (ancho ~60%, alineado a la derecha, con el
sello azul encima), reparto, botón y enlaces; la barra vertical pasa a ser una regla horizontal.

FORM: "Libreto" (screenplay): la página es un guion continuo con actos numerados; posición 1 de la
lista ordenada (2: cartel de teatro; 3: triálogo a tres columnas; 4: carta mecanografiada). Semilla:
brief-pinned (README `docs/readme-conciso`), sin tirada de dados (usuario ausente; se registra la
sustitución).

MOMENTO MEMORABLE (interacción firmada): al cargar, los cues del reparto se revelan como si una
máquina de escribir los tipeara (clip-path de izquierda a derecha, escalonado) y los sellos
fantasma aparecen con retardo; al pasar el cursor sobre un nombre de voz, el retrato se tiñe con el
color de esa voz. Con `prefers-reduced-motion` todo es estático y completo.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the
verdict, DESIGN.md, and every shipping raster carrying its provenance.

## Unresolved

- Qué variante se publica en `/` (decisión de Andrés).
- Imagen Open Graph (`/og.png`) pendiente hasta elegir variante.
