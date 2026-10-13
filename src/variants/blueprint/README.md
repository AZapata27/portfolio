# Variante "blueprint": la trayectoria como ruta de integración

Rutas: `/` (español, idioma por defecto) y `/en/` (inglés). Fuente de verdad del contenido:
`src/content/` y `src/lib/i18n.ts`; esta carpeta sólo decide cómo se ve. Es la variante elegida
el 2026-10-10 (la alternativa "script" se eliminó).

## Idea

La página **es un plano de ingeniería** de una sola ruta EIP: el problema del visitante entra por un
canal, un *content-based router* lo manda a Arquitectura, Integración o Desarrollo AI-native, un
agregador junta las ramas y sale a producción; el liderazgo corre por encima como *control bus*.
No hay tarjetas ni grilla de skills: hay un **juego de seis hojas de dibujo** numeradas
(`SHEET 1/6 … 6/6`), cada una con marco doble, marcas de esquina, grilla de puntos y sello.

| Hoja | Id (`#`)        | Qué es                                                                                   |
| ---- | --------------- | ---------------------------------------------------------------------------------------- |
| 1    | `route`         | Nombre, diagrama de la ruta (SVG), `DETAIL A · Route.java`, bloque de título con contacto |
| 2    | `capabilities`  | NOTES ①–④ (las cuatro capacidades), resumen y tabla de LOGROS (`profile.achievements`)   |
| 3    | `experience`    | PERFIL LONGITUDINAL: la trayectoria como línea de tiempo sin fechas (empresa, relación, cargo, una línea, stack superficial); el detalle queda en el CV |
| 4    | `work`          | DETAILS B–Q: los proyectos tangibles agrupados por dominio; los que tienen cifra la llevan como cota |
| 5    | `stack`         | PARTS LIST: `ITEM / GROUP / PARTS` con logos de simple-icons en tinta                     |
| 6    | `contact`       | TITLE BLOCK: mailto en ámbar, LinkedIn, GitHub, CV, ubicación, disponibilidad, idiomas, notas generales |

`DETAIL A` es el código; por eso los proyectos empiezan en `DETAIL B`.

## Paleta

| Token           | Hex       | Uso                                                                    |
| --------------- | --------- | ---------------------------------------------------------------------- |
| `--paper`       | `#FAFAF7` | Papel de cada hoja (con grilla de puntos `--grid`)                     |
| `--desk`        | `#ECECE7` | Mesa sobre la que descansan las hojas (fondo de página)                |
| `--grid`        | `#D6D8D4` | Puntos de la grilla, cada 24 px                                        |
| `--hair`        | `#C9CBC6` | Separadores secundarios (sólo decorativos)                             |
| `--ink`         | `#151515` | Tinta: texto, trazos, bloque PROD                                      |
| `--graphite`    | `#4A4F55` | Secundario (7,9:1 sobre papel)                                         |
| `--amber`       | `#F2A900` | Único acento: sobre del mensaje, llamadas ①–③, fila CONTACT, REV actual, selección de texto. Nunca como color de texto (1,9:1) |
| `--amber-deep`  | `#8A5A00` | Strings del código (5,7:1)                                             |
| `--amber-wash`  | `#F8EAC6` | Hover de las ramas en móvil                                            |
| `--blue`        | `#1F5FBF` | Control bus (línea punteada), llamada ④ y enlaces (5,8:1)              |
| `--blue-wash`   | `#E4EAF1` | Hover del conmutador de idioma                                         |

Sin sombras ni radios: la profundidad es grosor de línea (`1px` hairline, `1.5px` trazo, `2px` marco).

## Tipografía

- **Display**: Barlow Condensed 700/800, mayúsculas, tracking −0,02 em. Nombre
  `clamp(3rem, 8vw, 6rem)`; títulos de hoja `clamp(2.25rem, 4.5vw, 3.5rem)`; h3
  `clamp(1.375rem, 2vw, 1.75rem)`.
- **Cuerpo**: Barlow 400/500, 17 px (18 px desde 1280 px), interlínea 1,55, medidas de 62–66 ch.
- **Etiquetas, tablas y código**: JetBrains Mono 12–14 px con numerales tabulares; etiquetas en
  mayúsculas con tracking 0,08 em.

Las tres familias se autoalojan con la Fonts API de Astro (`<Font cssVariable=… preload />` en
`Page.astro`).

## Espaciado y hojas

Escala de 4 px (`--s-1` … `--s-8`). Cada hoja (`components/Sheet.astro`) tiene marco exterior de
2 px, banda (8 px; 14–22 px en la hoja 1 para las reglas 1–6 y A–D), marco interior de 1 px,
marcas de esquina dibujadas con gradientes de fondo y el sello `SHEET n/6 · TÍTULO` (sin nombre de plano: decisión de Andrés, 2026-10-12)
pegado a la esquina inferior derecha. Ancho máximo 1280 px; separación entre hojas 24 px.

## Diagrama de la ruta

- **Escritorio (≥ 960 px)**: `components/RouteDiagram.astro`, un SVG con `viewBox 0 0 1080 318`
  (máx. 1040 px de ancho). Línea principal en y=180, ramas en 90/180/270, control bus en y=24.
  Cables con `vector-effect: non-scaling-stroke` y puntas de flecha como chevrones del propio trazo.
  Cada rama es un `<a>` a su nota (`#capabilities-<id>`); al pasar el cursor se engrosan su cable y
  su caja y se rellena su llamada en ámbar.
- **Móvil y tablet (< 960 px)**: `components/RouteFlow.astro`, la misma ruta en vertical con cajas
  HTML y conectores en CSS. Sin animación.
- Los iconos EIP (canal, router, agregador, endpoint, sobre, bus, y los tres glifos de rama) viven
  una sola vez en `components/EipSprite.astro` (24×24, trazo 1,75, remates redondos: el mismo peso
  que `src/components/Icon.astro`) y se reutilizan con `<use href="#eip-…">`.
- `DETAIL A` (`components/DetailA.astro`) genera el DSL de Camel a partir de `capabilities`: los ids
  son los `needs("…")`, los dos primeros `parts` de cada rama forman el endpoint y la primera
  parte del control bus el `wireTap`. Así el código y el dibujo no se desincronizan.

## Perfil longitudinal (hoja 3)

La experiencia no se duplica del CV: es una **línea de tiempo sin fechas** con empresa, relación
(`client`: "Contratista", cliente final), cargo, un resumen de una línea (`short`) y hasta cuatro
tecnologías (`tags`). El orden es el de `getExperience`: puestos actuales primero (Avianca como
contratista, luego Quind) y después del más reciente al más antiguo; la línea nace en el bloque HOY
(tinta, como PROD) y se aleja hacia el pasado. Decisión de Andrés del 2026-10-12: sin fechas y sin
el nodo del contratista independiente.

- **Escritorio (≥ 960 px)**: horizontal, HOY a la izquierda. Grilla de `max-content` (HOY) más
  `n + 1` columnas; cada estación ocupa dos columnas y alterna arriba y abajo de la línea, con su
  línea de llamada vertical y un marcador circular (ámbar si el puesto es actual).
- **Móvil y tablet (< 960 px)**: vertical, HOY arriba, marcadores sobre una línea a la izquierda.
- El trabajo como **contratista independiente** (`type: freelance`) no se dibuja: sus proyectos
  están en la hoja 4.

## Detalles (hoja 4)

Es la hoja con más peso. Los proyectos se agrupan por `domain` (texto exacto, en el orden en que
aparece cada dominio según `order`); cada grupo lleva el rango de detalles (`DETALLES B–E`), el
nombre del dominio y la cantidad. Las tarjetas son todas iguales (`auto-fill` de 272 px, cuatro en
la hoja completa); las que tienen `metric` llevan la cifra como cota y marco de 1,5 px, el resto
marco hairline. Letras continuas B, C, D… a través de los grupos.

## Momento memorable (motion)

Al cargar, en escritorio y sólo con `prefers-reduced-motion: no-preference`:

1. Los cables y las cajas se **entintan** con `stroke-dashoffset` (cada path lleva
   `pathLength="1"`, `stroke-dasharray: 1 1.2`; el hueco mayor que el trazo evita que asome el
   remate redondo antes de tiempo). Retardos escalonados de 0,15 s a 4,4 s, 600 ms cada uno,
   `cubic-bezier(0.16, 1, 0.3, 1)`.
2. El **sobre ámbar recorre la ruta** con `offset-path` (5 s, desde 0,4 s): entra al router, se
   "absorbe" (escala 0,15), sale por la rama de arquitectura, cruza la caja, baja al agregador y
   descansa en el canal de salida.
3. Las llamadas ①–④ se estampan (escala 0,6 → 1) cuando el sobre pasa; el control bus pasa de
   35 % a 100 % de opacidad al final.

Con `prefers-reduced-motion: reduce` no hay `dasharray` ni `offset-path`: el dibujo está completo y
el sobre descansa en el canal de entrada. Sin JavaScript en ninguna de las dos situaciones.

## Accesibilidad

Un solo `h1`; `header` / `nav` / `main#main` / `footer`; cada hoja es una `section` con
`aria-labelledby`. Contraste AA en todo el texto (ver tabla de paleta). Foco visible: contorno
ámbar de 2 px con offset 2 px más anillo interior de tinta (para que el foco contraste también
sobre el papel). Selección ámbar sobre tinta. Scrollbar tematizada. Las tablas son `<table>`
semánticas con `caption`, `th scope` y, en móvil, cada fila se apila con `display: grid`
(`thead` oculto visualmente) sin scroll horizontal; el único bloque que desplaza es el código de
`DETAIL A`, que además en móvil pone las llamadas a la izquierda para que no desaparezcan.

## Responsivo

- `< 640`: bloques de título y detalles en una columna; etiqueta `DETAIL x` sobre el título.
- `< 640`: detalles (proyectos) en una columna; desde 640, tantas columnas de 272 px como quepan.
- `< 768`: LOGROS y PARTS LIST apiladas. `< 900`: contacto en una columna.
- `< 960`: ruta vertical en vez del SVG; el bloque de título pasa antes del código; la línea de
  tiempo pasa de horizontal a vertical.
- `< 1024`: barra superior sin fijar (`AZ` + idioma arriba, navegación debajo). Desde 1024 se fija.

Probado a 390, 768 y 1440 px (capturas en `screenshots/`).

## Qué se descartó y por qué

- **Tarjetas iguales como estructura y la plantilla "cifra grande + etiqueta"**: los logros van en
  una tabla LOGROS y, en los proyectos, la cifra como cota (línea de dimensión), que es lo que un
  plano usa para medir.
- **Kicker/eyebrow sobre los títulos**: el número de hoja va en el sello inferior, no encima del h2.
- **Un segundo SVG para móvil**: el texto envuelto en HTML es más robusto en español que en SVG.
- **Iconos de marca a color**: en una lista de partes todo va en tinta.
- **Pasar `class` a los componentes de diagrama** desde `Hero.astro`: los estilos scoped del padre
  no llegan a la raíz del hijo, por eso cada diagrama va envuelto en un `div` propio.

## Para extender

- Nueva hoja: `sections/<Nombre>.astro` envuelta en `<Sheet …>`, incluirla en `Page.astro` y subir
  `total`.
- Nuevo proyecto: `src/content/projects/{en,es}/<slug>.md` con un `domain` ya existente (o uno nuevo
  en los dos idiomas) y un `order` contiguo a los de su dominio; la letra del detalle sale sola.
- Nuevo puesto en la línea de tiempo: `src/content/experience/{en,es}/<slug>.md` con `short` y
  `tags` (hasta cuatro); `type: freelance` no se dibuja. Nueva etiqueta de interfaz del mundo "plano": `labels.ts` (en y es).
- El DSL de `DETAIL A` y el diagrama leen `capabilities` por `id`; si se agrega una capacidad hay que
  decidir en qué rama va (el orden fijo está en `capabilityOrder`).
