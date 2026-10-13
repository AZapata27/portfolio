---
version: 1
slug: "src-variants-blueprint-projectpage-astro"
primary_target: "src/variants/blueprint/ProjectPage.astro"
related_targets: ["src/pages/proyectos/[slug].astro","src/pages/en/work/[slug].astro","src/variants/blueprint/sections/Work.astro"]
---

---
version: 1
slug: "src-variants-blueprint-projectpage-astro"
primary_target: "src/variants/blueprint/ProjectPage.astro"
related_targets: ["src/pages/proyectos/[slug].astro","src/pages/en/work/[slug].astro","src/variants/blueprint/sections/Work.astro","src/variants/blueprint/components/Plate.astro","src/variants/blueprint/components/Schematic.astro"]
---

# Surface brief: página de proyecto (`/proyectos/<slug>/`, `/en/work/<slug>/`) y galería de la hoja 4

## Scope and mode

Modo **Experience** con cierre Persuade: la obra (captura real del sitio o esquema de arquitectura)
lleva la página; el texto acompaña. Dos superficies en una decisión: la hoja 4 pasa de 16 cajas de
texto a una galería de láminas, y cada lámina abre una página propia (decisión de Andrés del
2026-10-12: página por proyecto, no modal; capturas reales más esquemas; galería agrupada por dominio;
sin numeración "Detalle/Lámina nn" ni pies "FIG.": el único feedback de enlace es el hover).

## Audience, job, action, proof, constraints

- Audiencia: reclutador o CTO que llega desde LinkedIn o desde el índice; quiere ver "qué construyó"
  en diez segundos y tener una URL para compartir.
- Job: reconocer el sistema (logo, pantalla, cliente), leer la cifra, el rol y el stack; volver al índice
  o pasar al siguiente detalle.
- Pruebas: captura real del sitio público (Colpass, RUNT, Flypass, Emtelco) rotulada con dominio y fecha;
  esquema de arquitectura dibujado con los datos del contenido para lo que no tiene pantalla pública.
- Constraints: mundo blueprint intacto (`DESIGN.md`); contenido en es y en; sin JavaScript; AA;
  `prefers-reduced-motion`; nada de capturas de sistemas internos ni datos de usuarios finales. Las
  páginas del Banco de la República no se capturan (anti-bot con captcha): van con esquema.

## Direction contract

THESIS: cada proyecto es una **hoja de detalle** del mismo juego de planos (sello "PROYECTO · dominio"), no una
"página de caso de estudio" con hero, tarjetas de métricas y galería de tabs. La lámina (captura o
esquema) es la pieza dibujada; el resto es bloque de datos, cota y notas, como en cualquier plano.

OWN-WORLD: papel, tinta, ámbar, azul de dibujo y las tres familias del mundo; marco de lámina con
marcas de esquina; en la página de proyecto la captura lleva pie "Captura de colpass.mintransporte.gov.co · 2026-10"
(los esquemas no llevan pie; en la galería no hay pies); sello ámbar con
la cifra pegado a la esquina de la lámina en la galería; esquemas con el mismo trazo de 1,5 px, cajas,
canales con extremos redondeados, bases de datos con tapa, líneas de control azules discontinuas y
bloque PROD en tinta; tabla mono de datos como el bloque de título de la hoja 1.

STORY: en el índice el visitante ve 16 láminas agrupadas por dominio y entiende de un vistazo que hay
obra real (pantallas de sistemas nacionales) y arquitectura (esquemas); abre una, reconoce el sistema,
lee cifra, cliente, rol y stack, baja a las notas y sigue al detalle siguiente o vuelve al índice.

FIRST VIEWPORT (detalle, 1440): barra superior; una hoja con sello "PROYECTO · dominio". Arriba, fila
mono: "← Todos los proyectos · dominio". Título en display `clamp(2.25rem, 4.5vw, 3.5rem)`
en mayúsculas, debajo el resumen a 62 ch, regla de 1,5 px. Debajo, dos columnas 7/5: izquierda la
lámina a sangre con pie; derecha la cota grande (cifra con línea de dimensión) y la tabla mono
CLIENTE / PERIODO / ROL / DOMINIO / STACK / ENLACES. Más abajo, "NOTAS" en 66 ch y la paginación
anterior/siguiente. En móvil todo se apila: lámina, cota, tabla, notas, paginación.

FORM: "hoja de detalle del plano" (detail sheet); posición 1 de la lista (2: panel lateral sobre el
índice; 3: modal centrado; 4: acordeón en la propia hoja). Decisión de Andrés por pregunta
estructurada el 2026-10-12; sin tirada de dados: extensión de una superficie establecida.

SIGNATURE INTERACTION: en la galería, al pasar el cursor la lámina engrosa su marco (anillo interior de
1 px) el título se subraya y la acción "Ver proyecto" se rellena de ámbar con la flecha desplazada 3 px;
sin motion de entrada. Sin JavaScript.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the
verdict, DESIGN.md, and every shipping raster carrying its provenance.

## Unresolved

- Capturas del Banco de la República (SEC, citas de Tesorería): el sitio responde con captcha a los
  navegadores automatizados; si Andrés las toma a mano se añaden como `plate` en el contenido.
- Si conviene una captura de la pantalla real del RNDC (hoy sólo esquema: el portal muestra un marco vacío sin login).
