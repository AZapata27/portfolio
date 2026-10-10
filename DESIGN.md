---
name: andres-zapata.dev
description: Plano de ingeniería de una sola ruta de integración. Papel, tinta, un acento ámbar y azul de dibujo.
colors:
  paper: "#FAFAF7"
  desk: "#ECECE7"
  grid: "#D6D8D4"
  hair: "#C9CBC6"
  ink: "#151515"
  graphite: "#4A4F55"
  amber: "#F2A900"
  amber-deep: "#8A5A00"
  amber-wash: "#F8EAC6"
  drafting-blue: "#1F5FBF"
  blue-wash: "#E4EAF1"
typography:
  display:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(3rem, 8vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(2.25rem, 4.5vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 0.95
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(1.375rem, 2vw, 1.75rem)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Barlow, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "JetBrains Mono, Consolas, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "0.08em"
  mono:
    fontFamily: "JetBrains Mono, Consolas, monospace"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.45
rounded:
  none: "0"
spacing:
  s1: "4px"
  s2: "8px"
  s3: "12px"
  s4: "16px"
  s5: "24px"
  s6: "32px"
  s7: "48px"
  s8: "64px"
components:
  sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "clamp(0.875rem, 2.5vw, 2rem)"
  table-header:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.graphite}"
    typography: "{typography.label}"
    padding: "12px 16px"
  row-contact:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    typography: "{typography.mono}"
    padding: "16px"
  callout:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.ink}"
    rounded: "50%"
    size: "32px"
  callout-bus:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.drafting-blue}"
    rounded: "50%"
    size: "32px"
  link:
    textColor: "{colors.drafting-blue}"
  lang-switch:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.drafting-blue}"
    typography: "{typography.label}"
    padding: "8px 12px"
  prod-block:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
---

# andres-zapata.dev

## Overview

**Norte creativo: "la hoja de dibujo"**. El portafolio es un plano de ingeniería de una sola ruta
de integración (Enterprise Integration Patterns): el problema del visitante entra por un canal, un
*content-based router* lo manda a Arquitectura, Integración o Desarrollo AI-native, un agregador
junta las ramas y sale a producción; el liderazgo corre por encima como *control bus*. Todo lo que
se agregue debe poder existir en una hoja de dibujo técnico: marcos, reglas, tablas, cotas, llamadas
numeradas, bloques de título. Nada de tarjetas, sombras, degradados ni radios.

La implementación vive en `src/variants/blueprint/` (tokens en `tokens.css`, hojas en `sections/`,
piezas del dibujo en `components/`, vocabulario del plano en `labels.ts`). Este archivo resume las
reglas para que un agente pueda añadir una hoja o un componente sin romper el mundo.

## Colors

- **Papel** `#FAFAF7` es la hoja; **mesa** `#ECECE7` es el fondo de la página sobre el que descansan
  las hojas; **grilla** `#D6D8D4` son los puntos cada 24 px; **hairline** `#C9CBC6` separa dentro de
  una tabla sin peso semántico.
- **Tinta** `#151515` para texto, trazos, marcos y el bloque PROD. **Grafito** `#4A4F55` para texto
  secundario (7,9:1 sobre papel).
- **Ámbar** `#F2A900` es el único acento y siempre es relleno, nunca color de texto (1,9:1): sobre del
  mensaje, llamadas ①–③, fila CONTACT, REV actual, selección de texto, anillo de foco.
  **Ámbar profundo** `#8A5A00` sólo para strings de código (5,7:1). **Ámbar lavado** `#F8EAC6` para
  hover de las ramas en móvil.
- **Azul de dibujo** `#1F5FBF` para el control bus (línea punteada), la llamada ④ y todos los enlaces
  (5,8:1). **Azul lavado** `#E4EAF1` para el hover del conmutador de idioma.
- Estrategia: restringida (neutros + un acento + un secundario funcional). No introducir más colores;
  si un estado nuevo necesita énfasis, usar grosor de línea o relleno ámbar.

## Typography

- **Display y títulos**: Barlow Condensed 700/800, siempre en mayúsculas, tracking −0,02 em (nombre)
  a −0,01 em (h3). Nombre `clamp(3rem, 8vw, 6rem)`; título de hoja `clamp(2.25rem, 4.5vw, 3.5rem)`
  con regla inferior de 1,5 px; h3 `clamp(1.375rem, 2vw, 1.75rem)`; h4 1,25 rem.
- **Cuerpo**: Barlow 400/500, 17 px (18 px desde 1280 px), interlínea 1,55, medida 62–66 ch.
- **Etiquetas, tablas, código, sellos**: JetBrains Mono 12–14 px con numerales tabulares; las
  etiquetas en mayúsculas con tracking 0,08 em en grafito.
- Las tres familias se autoalojan con la Fonts API de Astro (`fonts` en `astro.config.ts`;
  `<Font cssVariable=… preload />` en `Page.astro`). No añadir familias.

## Layout

- Hojas (`components/Sheet.astro`) de ancho máximo 1280 px, apiladas con 24 px de separación sobre
  la mesa, con marco exterior de 2 px, banda, marco interior de 1 px, marcas de esquina, grilla de
  puntos y sello `SHEET n/6 · TÍTULO · andres-zapata.route` abajo a la derecha. La hoja 1 lleva
  además reglas de columnas (1–6) y zonas (A–D).
- Escala de espaciado de 4 px (`--s-1` … `--s-8`); gutter `clamp(1rem, 3vw, 2.5rem)`.
- Diagrama de la ruta: SVG (`RouteDiagram`) desde 960 px; flujo vertical en HTML (`RouteFlow`) por
  debajo. Tablas semánticas que se apilan con `display: grid` en móvil (`< 768` logros y lista de
  partes; `< 900` revisiones); el único scroll horizontal permitido es el código de `DETAIL A`.
- Barra superior fija desde 1024 px; debajo se apila y no se fija.

## Elevation & Depth

No hay sombras ni capas: la profundidad es grosor de trazo. `1px` hairline, `1.5px` trazo normal,
`2px` marco. Los estados se expresan con grosor (hover engrosa el cable de la rama) o con relleno
ámbar, nunca con elevación.

## Shapes

Radio 0 en todo salvo las llamadas numeradas (círculos). Esquinas con marcas de registro. Flechas
como chevrones del propio trazo (`stroke-linecap: round`). Iconos EIP y de interfaz a 24×24, trazo
1,75, remates redondos, todos en tinta (los logos de marca también van en tinta, nunca a color).

## Components

- **Sheet**: `<Sheet id number total title drawingName locale labelledby>`; dentro, un `h2.sheet-title`.
- **Tablas** (`.tbl`): `caption` arriba en mono/mayúsculas, `thead th` en grafito, celdas con
  hairlines; en móvil cada fila es un grid con `data-label`.
- **Bloque de título** (`TitleBlock`, hoja 1 y hoja 6): tabla mono; fila CONTACT en ámbar con el
  mailto como acción primaria; LinkedIn, GitHub y CV como enlaces azules.
- **Llamadas** (`.num`): círculo de 2 rem, borde de tinta, relleno ámbar (①–③) o papel con borde y
  número azul (④, control bus).
- **Enlaces**: azul de dibujo, subrayado de 1 px con offset 0,18 em; 2 px en hover.
- **Foco**: contorno ámbar de 2 px con offset 2 px más anillo interior de tinta. **Selección**: ámbar
  sobre tinta. **Scrollbar**: fina, tinta sobre mesa.
- **Motion**: un solo momento, en escritorio y sin `prefers-reduced-motion`: los cables se entintan
  con `stroke-dashoffset` (600 ms, `cubic-bezier(0.16, 1, 0.3, 1)`, escalonados) y el sobre ámbar
  recorre la ruta con `offset-path` (5 s). Con reduced-motion el dibujo está completo y estático.
  Las demás transiciones son de 140–260 ms sobre color y grosor. Sin JavaScript.

## Do's and Don'ts

- Sí: nuevas hojas numeradas, tablas, cotas, llamadas, bloques de título; texto en mayúsculas sólo
  en display y etiquetas; todo el texto desde `src/content/` y `t(locale)`.
- No: tarjetas iguales como estructura, kicker/eyebrow sobre títulos, degradados, sombras, radios,
  `border-left` de color, emoji como iconos, texto en ámbar, colores nuevos, fuentes nuevas,
  animaciones de entrada por sección, JavaScript obligatorio.
- Contraste mínimo AA en todo; comprobar cada par nuevo contra papel y contra ámbar.
