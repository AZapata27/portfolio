# Analítica

El sitio usa **Vercel Web Analytics** (vistas de página, sin cookies, sin identificar personas) y
**Vercel Speed Insights** (experiencia real de carga), ambos en el plan Hobby, que es gratuito dentro
de estos límites (documentación de Vercel, 2026-10):

| | Web Analytics (Hobby) | Speed Insights (gratis en todos los planes) |
| --- | --- | --- |
| Incluido | 50.000 eventos al mes (una vista de página = un evento) | 10.000 eventos en una ventana móvil de 30 días |
| Historial visible | 1 mes | 24 horas y 7 días |
| Al pasarse | 3 días de gracia y se pausa la recolección hasta el siguiente ciclo; nunca cobra | Pausa de al menos 14 días; nunca cobra |
| No incluye | Eventos personalizados (clics, descargas) ni panel de parámetros UTM: son de Pro / Plus | Core Web Vitals detallados y entradas "Poor": son de Plus |

Un portafolio personal está lejísimos de esos límites (50.000 vistas al mes son más de 1.600 al día).

## Cómo está integrado

- Los dos componentes se montan una sola vez en `src/layouts/Base.astro` (`<Analytics />` y
  `<SpeedInsights />` de `@vercel/analytics/astro` y `@vercel/speed-insights/astro`), así que todas las
  páginas (portada en es/en y cada `/proyectos/<slug>/`) quedan cubiertas.
- Es la única excepción a "sin JavaScript en cliente": un script pequeño que Vercel sirve desde el
  propio dominio (`/_vercel/insights/*`). No usa cookies ni almacena datos personales (no aplica la
  Ley 1581 ni hace falta aviso de cookies).
- En desarrollo (`astro dev`) no envía nada: el paquete lo detecta solo.
- El adaptador `@astrojs/vercel` tiene una opción `webAnalytics` antigua; se deja apagada (por
  defecto) porque desde `@vercel/analytics` 1.4 la vía oficial es el componente.

## Activación en el dashboard (una vez, lo hace Andrés)

1. https://vercel.com → proyecto **portfolio** → pestaña **Analytics** → botón **Enable**.
2. Misma pantalla, pestaña **Speed Insights** → **Enable**.
3. El siguiente despliegue de `master` empieza a recolectar. Comprobación: en el navegador, en
   https://www.andres-zapata.dev, la pestaña Red debe mostrar una petición a `/_vercel/insights/view`.
4. Settings → Notifications → activar los avisos de uso ("usage notifications") para enterarse si
   algún mes se acerca al límite.

## Qué se puede ver en el plan Hobby

- **Visitors** y **Page views** por día, con comparación contra el periodo anterior.
- **Pages**: qué rutas se abren (`/`, `/en/`, `/proyectos/iprev/`…). Es la medida directa de qué
  proyectos despiertan interés.
- **Referrers**: de dónde llegan (linkedin.com, github.com, google.com, directo). Es el "flujo de
  entrada".
- **Countries**, **Devices** (escritorio/móvil), **Operating systems**, **Browsers**.
- Todos los paneles se pueden **filtrar y cruzar**: por ejemplo, referrer = linkedin.com → qué páginas
  ven; país = Colombia → móvil o escritorio. Ese cruce es lo más parecido a un embudo que da el plan.
- Speed Insights: un **Real Experience Score** por ruta con entradas "Great" y "Needs improvement".

Lo que **no** da el plan y cómo suplirlo sin pagar:

| Quiero saber | Por qué no está | Alternativa gratis |
| --- | --- | --- |
| Clics en "Escribime", LinkedIn, GitHub, "Descargar CV" | Eventos personalizados son de Pro | Para el CV: una página `/cv/` propia que cuente como vista y redirija al PDF. Para correo y LinkedIn no hay forma sin eventos; se mide por el otro lado (mensajes recibidos, visitas al perfil de LinkedIn). |
| Qué enlace de LinkedIn trajo la visita (perfil, un post, un proyecto) | El panel UTM es de Web Analytics Plus | Enlazar cada proyecto de LinkedIn a su página `/proyectos/<slug>/`: la ruta de entrada en **Pages** con referrer linkedin.com ya dice qué proyecto abrieron. |
| Qué buscan en Google para llegar | No lo mide ningún plan de Vercel | **Google Search Console** (gratis): consultas, impresiones, CTR y posición por página; el sitio ya publica `sitemap-index.xml`. Bing Webmaster Tools hace lo mismo para Bing/DuckDuckGo. |
| Historial de más de un mes | Ventana de 1 mes en Hobby | Anotar cada mes las cifras clave en `personal/portafolio/analitica.md` del workspace de gestión (5 minutos). |
| Interés en el código | Fuera del sitio | GitHub → repositorio → **Insights → Traffic** (visitas y clones de 14 días) y las estadísticas de LinkedIn ("quién vio tu perfil", impresiones de publicaciones). |

## Cómo leerla para mejorar el sitio (rutina mensual)

1. **Entrada**: Referrers. Si LinkedIn domina, lo que importa es que el primer viewport responda en
   10 segundos; si aparece Google, mirar en Search Console con qué consultas y reforzar esas páginas.
2. **Interés**: Pages filtrado por referrer. Qué proyectos abren más → esos merecen caso de estudio
   profundo; los que nadie abre, revisar título, lámina y resumen en la galería.
3. **Alcance**: visitas a `/en/` frente a `/`. Si el inglés crece, considerar inglés por defecto o
   reforzar el contenido en inglés.
4. **Dispositivo**: si el móvil supera el 40 %, priorizar la revisión móvil de cada cambio.
5. **Rendimiento**: Speed Insights; cualquier ruta en "Needs improvement" se revisa (casi siempre
   imágenes o fuentes).
6. **Decisión**: una sola mejora por mes a partir de estos datos, anotada en el workspace con la cifra
   de partida para comparar al mes siguiente.
