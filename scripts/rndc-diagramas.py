"""Diagramas C4 del caso de estudio RNDC: un solo modelo, dos salidas.

- `src/assets/work/rndc/*.svg`: los diagramas que muestra la página del proyecto, dibujados con el trazo
  del plano (papel, tinta, ámbar, azul de dibujo). Son SVG autónomos (se sirven como `<img>`), así que
  usan una familia de sistema (Arial/Helvetica) en vez de las fuentes del sitio.
- `public/casos/rndc/*.drawio`: los mismos diagramas en formato draw.io con las formas C4 estándar
  (paleta azul de la plantilla C4 de diagrams.net), para abrirlos y editarlos.

Uso: `python scripts/rndc-diagramas.py` desde la raíz del repo. Cada diagrama existe en español e inglés.
"""
from __future__ import annotations

import html
import os
from dataclasses import dataclass, field

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "src", "assets", "work", "rndc")
DRAWIO_DIR = os.path.join(ROOT, "public", "casos", "rndc")

# Paleta del plano
PAPER, INK, GRAPHITE, AMBER, AMBER_WASH, BLUE, HAIR, GRID = "#FAFAF7", "#151515", "#4A4F55", "#F2A900", "#F8EAC6", "#1F5FBF", "#C9CBC6", "#D6D8D4"
FONT = "Arial, Helvetica, sans-serif"
CHAR_W = 5.6  # ancho medio de un carácter a 10 px


@dataclass
class Node:
    id: str
    kind: str  # person | system | external | container | component | db | queue | boundary | note
    name: tuple[str, str]
    type: tuple[str, str]
    desc: tuple[str, str]
    x: int
    y: int
    w: int = 200
    h: int = 110
    parent: str | None = None


@dataclass
class Edge:
    src: str
    dst: str
    label: tuple[str, str]
    tech: str = ""
    dashed: bool = False
    points: list[tuple[int, int]] = field(default_factory=list)
    number: int | None = None
    label_side: str = "auto"  # auto | center | below | right | left: dónde va la etiqueta respecto al tramo
    label_seg: int | None = None  # índice del tramo que lleva la etiqueta (por defecto, el más largo)
    label_pos: tuple[int, int] | None = None  # centro explícito de la etiqueta
    wrap_chars: int | None = None  # ancho máximo de línea de la etiqueta en caracteres


@dataclass
class Diagram:
    slug: str
    title: tuple[str, str]
    width: int
    height: int
    nodes: list[Node]
    edges: list[Edge]


L = lambda es, en: (es, en)  # noqa: E731


# ---------------------------------------------------------------------------- modelo
def contexto() -> Diagram:
    nodes = [
        Node("analista", "person", L("Analista de despachos", "Dispatch analyst"), L("Persona", "Person"),
             L("Crea órdenes, remesas y manifiestos; registra cumplidos", "Creates orders, consignment notes and manifests; files proofs of delivery"), 60, 40, 220, 130),
        Node("generador", "person", L("Generador de carga", "Shipper"), L("Persona · cliente", "Person · customer"),
             L("Autoriza a la transportadora, consulta remesas y registra el valor del flete", "Authorises the carrier, checks consignment notes and records the freight value"), 500, 40, 220, 130),
        Node("conductor", "person", L("Conductor / tenedor", "Driver / vehicle holder"), L("Persona", "Person"),
             L("Acepta y porta el manifiesto electrónico", "Accepts and carries the electronic manifest"), 940, 40, 220, 130),
        Node("plataforma", "system", L("Plataforma de despachos", "Dispatch platform"), L("Sistema de software", "Software system"),
             L("Ciclo de vida del despacho orientado a eventos: orden → remesa → manifiesto → cumplido. Valida antes de reportar y concilia fletes.",
               "Event-driven dispatch lifecycle: order → consignment note → manifest → proof of delivery. Validates before filing and reconciles freight."), 380, 290, 460, 140),
        Node("rndc", "external", L("RNDC", "RNDC"), L("Sistema externo · Ministerio de Transporte", "External system · Ministry of Transport"),
             L("Registro Nacional de Despachos de Carga. Servicio web SOAP/XML; recibe, valida y numera cada operación.",
               "National Cargo Dispatch Registry. SOAP/XML web service; receives, validates and numbers every operation."), 60, 540, 240, 130),
        Node("erp", "external", L("ERP / TMS legado", "Legacy ERP / TMS"), L("Sistema existente · Oracle", "Existing system · Oracle"),
             L("Órdenes, clientes, vehículos y terceros. Se mantiene en operación durante la modernización.",
               "Orders, customers, vehicles and third parties. Stays in operation during the modernisation."), 380, 540, 240, 130),
        Node("sicetac", "external", L("SICE-TAC", "SICE-TAC"), L("Sistema externo · Ministerio de Transporte", "External system · Ministry of Transport"),
             L("Costos de referencia del transporte de carga por ruta y configuración.", "Reference freight costs by route and vehicle configuration."), 700, 540, 240, 130),
        Node("app", "external", L("App RNDC Transportador", "RNDC Carrier app"), L("Sistema externo · Ministerio", "External system · Ministry"),
             L("Donde el conductor acepta el manifiesto expedido.", "Where the driver accepts the issued manifest."), 960, 540, 220, 130),
    ]
    edges = [
        Edge("analista", "plataforma", L("Registra despachos y consulta estados", "Registers dispatches and checks status"), "HTTPS"),
        Edge("generador", "plataforma", L("Autoriza, consulta y registra fletes", "Authorises, checks and records freight"), "HTTPS"),
        Edge("conductor", "app", L("Acepta y porta el manifiesto", "Accepts and carries the manifest"), "App móvil"),
        Edge("plataforma", "rndc", L("Reporta remesas, manifiestos y cumplidos; recibe ingresoid o error", "Files consignment notes, manifests and proofs; gets ingresoid or error"), "SOAP/XML"),
        Edge("plataforma", "erp", L("Lee órdenes y maestros; devuelve fletes conciliados", "Reads orders and master data; returns reconciled freight"), "CDC · Debezium"),
        Edge("plataforma", "sicetac", L("Consulta costos de referencia", "Looks up reference costs"), "HTTP"),
        Edge("rndc", "app", L("Publica el manifiesto expedido", "Publishes the issued manifest"), "", dashed=True, points=[(180, 705), (1070, 705)], label_side="below"),
    ]
    return Diagram("c1-contexto", L("Nivel 1 · Contexto", "Level 1 · Context"), 1240, 780, nodes, edges)


def contenedores() -> Diagram:
    B = "plataforma"
    nodes = [
        Node("analista", "person", L("Analista de despachos", "Dispatch analyst"), L("Persona", "Person"), L("", ""), 60, 20, 200, 90),
        Node("generador", "person", L("Generador de carga", "Shipper"), L("Persona", "Person"), L("", ""), 340, 20, 200, 90),
        Node(B, "boundary", L("Plataforma de despachos", "Dispatch platform"), L("Sistema de software", "Software system"), L("", ""), 40, 160, 1320, 570),
        Node("web", "container", L("Web de despachos", "Dispatch web app"), L("Contenedor · Angular", "Container · Angular"),
             L("Órdenes, remesas, manifiestos, cumplidos y estado de cada reporte", "Orders, consignment notes, manifests, proofs and the status of every filing"), 60, 200, 200, 120, B),
        Node("api", "container", L("API de despachos", "Dispatch API"), L("Contenedor · Quarkus REST", "Container · Quarkus REST"),
             L("Comandos del ciclo de vida; escribe el evento en la outbox en la misma transacción", "Lifecycle commands; writes the event to the outbox in the same transaction"), 340, 200, 200, 120, B),
        Node("pg", "db", L("PostgreSQL", "PostgreSQL"), L("Contenedor · base de datos", "Container · database"),
             L("Despachos, estado de cada reporte, idempotencia, outbox", "Dispatches, filing status, idempotency, outbox"), 620, 200, 200, 120, B),
        Node("keycloak", "container", L("Keycloak", "Keycloak"), L("Contenedor · IAM", "Container · IAM"),
             L("OAuth2/OIDC; reemplazó al LDAP", "OAuth2/OIDC; replaced LDAP"), 1160, 200, 180, 120, B),
        Node("motor", "container", L("Motor de validación", "Validation engine"), L("Contenedor · Camel", "Container · Camel"),
             L("Reglas del Ministerio antes de salir: pesos, SOAT/RTM, flete mínimo, ICA, catálogos DANE", "Ministry rules before leaving: weights, insurance/inspection, minimum freight, ICA, DANE catalogues"), 340, 370, 200, 120, B),
        Node("kafka", "queue", L("Kafka", "Kafka"), L("Contenedor · Confluent", "Container · Confluent"),
             L("despacho.orden · remesa · manifiesto · cumplido · rndc.resultado", "dispatch.order · consignment · manifest · proof · rndc.result"), 620, 370, 200, 120, B),
        Node("integrador", "container", L("Integrador RNDC", "RNDC integrator"), L("Contenedor · Camel + CXF", "Container · Camel + CXF"),
             L("Mapea a XML, llama al servicio SOAP, interpreta ingresoid/errores, reintenta y difiere", "Maps to XML, calls the SOAP service, reads ingresoid/errors, retries and defers"), 900, 370, 200, 120, B),
        Node("obs", "container", L("Observabilidad", "Observability"), L("Contenedor · OTel · Grafana", "Container · OTel · Grafana"),
             L("Trazas por despacho, métricas de rechazo por código", "Traces per dispatch, rejection metrics by code"), 1160, 370, 180, 120, B),
        Node("debezium", "container", L("Debezium", "Debezium"), L("Contenedor · Kafka Connect", "Container · Kafka Connect"),
             L("CDC desde Oracle: órdenes y maestros del legado", "CDC from Oracle: legacy orders and master data"), 60, 540, 200, 120, B),
        Node("conciliador", "container", L("Conciliador de fletes", "Freight reconciler"), L("Contenedor · Kafka Streams", "Container · Kafka Streams"),
             L("Flete pactado vs. SICE-TAC vs. factura; alimenta al ERP", "Agreed freight vs. SICE-TAC vs. invoice; feeds the ERP"), 620, 540, 200, 120, B),
        Node("sim", "container", L("Simulador RNDC", "RNDC simulator"), L("Contenedor · WireMock (pruebas)", "Container · WireMock (tests)"),
             L("Contratos de ejemplo: ingresoid, errores MAN/REM, latencia", "Sample contracts: ingresoid, MAN/REM errors, latency"), 900, 540, 200, 120, B),
        Node("oracle", "external", L("Oracle legado", "Legacy Oracle"), L("Sistema existente", "Existing system"), L("", ""), 60, 780, 200, 90),
        Node("sicetac", "external", L("SICE-TAC", "SICE-TAC"), L("Sistema externo", "External system"), L("", ""), 620, 780, 200, 90),
        Node("rndc", "external", L("RNDC · servicio web", "RNDC · web service"), L("Sistema externo · SOAP/XML", "External system · SOAP/XML"), L("", ""), 900, 780, 200, 90),
    ]
    edges = [
        Edge("analista", "web", L("Usa", "Uses"), "HTTPS"),
        Edge("generador", "web", L("Usa", "Uses"), "HTTPS"),
        Edge("web", "api", L("Llama", "Calls"), "REST · OIDC"),
        Edge("api", "keycloak", L("Valida tokens", "Validates tokens"), "OIDC", points=[(440, 180), (1250, 180)]),
        Edge("api", "pg", L("Lee y escribe; outbox", "Reads and writes; outbox"), "JDBC"),
        Edge("pg", "kafka", L("Outbox → eventos", "Outbox → events"), "Debezium outbox"),
        Edge("kafka", "motor", L("Eventos del despacho", "Dispatch events"), "", points=[(620, 410), (540, 410)]),
        Edge("motor", "kafka", L("Validado o rechazado", "Validated or rejected"), "", points=[(540, 455), (620, 455)]),
        Edge("kafka", "integrador", L("Remesa · manifiesto · cumplido validados", "Validated consignment · manifest · proof"), ""),
        Edge("integrador", "kafka", L("rndc.resultado", "rndc.result"), "", points=[(1000, 490), (1000, 510), (780, 510), (780, 490)]),
        Edge("integrador", "rndc", L("Reporta y consulta", "Files and queries"), "SOAP/XML · HTTPS", points=[(1130, 470), (1130, 760), (1050, 760)], label_pos=(1130, 700)),
        Edge("integrador", "sim", L("En pruebas y demos", "In tests and demos"), "", dashed=True),
        Edge("debezium", "oracle", L("Captura cambios", "Captures changes"), "LogMiner"),
        Edge("debezium", "kafka", L("Órdenes y maestros como eventos", "Orders and master data as events"), "", points=[(260, 580), (580, 580), (580, 465), (620, 465)]),
        Edge("kafka", "conciliador", L("Remesas y cumplidos", "Consignments and proofs"), "", points=[(700, 490), (700, 540)]),
        Edge("conciliador", "sicetac", L("Costos de referencia", "Reference costs"), "HTTP"),
        Edge("integrador", "obs", L("Trazas y métricas", "Traces and metrics"), "OTLP", dashed=True),
    ]
    return Diagram("c2-contenedores", L("Nivel 2 · Contenedores", "Level 2 · Containers"), 1400, 900, nodes, edges)


def componentes() -> Diagram:
    B = "integrador"
    nodes = [
        Node("kafka-in", "queue", L("Kafka", "Kafka"), L("Contenedor", "Container"), L("Eventos validados", "Validated events"), 40, 40, 180, 90),
        Node("rndc", "external", L("RNDC · servicio web", "RNDC · web service"), L("Sistema externo · SOAP/XML", "External system · SOAP/XML"), L("", ""), 960, 40, 290, 90),
        Node(B, "boundary", L("Integrador RNDC", "RNDC integrator"), L("Contenedor · Camel sobre Quarkus", "Container · Camel on Quarkus"), L("", ""), 40, 170, 1240, 560),
        Node("consumer", "component", L("Consumidor de eventos", "Event consumer"), L("Componente · Camel Kafka", "Component · Camel Kafka"),
             L("Una ruta por tipo: remesa, manifiesto, cumplido, anulación", "One route per type: consignment, manifest, proof, cancellation"), 60, 210, 210, 110, B),
        Node("prevalid", "component", L("Validador previo", "Pre-validator"), L("Componente · reglas", "Component · rules"),
             L("Peso total ≤ capacidad de la configuración; SOAT/RTM vigentes a la fecha de descargue; flete ≥ mínimo; ICA del municipio; códigos DANE y Sistema Armonizado",
               "Total weight ≤ configuration capacity; insurance/inspection valid at unloading date; freight ≥ minimum; municipality ICA; DANE and Harmonised System codes"), 340, 210, 250, 150, B),
        Node("catalogos", "component", L("Catálogos maestros", "Master catalogues"), L("Componente · caché", "Component · cache"),
             L("Municipios, configuraciones vehiculares, tarifas ICA, naturaleza de carga; se refrescan desde el RNDC", "Municipalities, vehicle configurations, ICA rates, cargo nature; refreshed from the RNDC"), 340, 400, 250, 110, B),
        Node("idem", "component", L("Registro de idempotencia y estado", "Idempotency and status register"), L("Componente · PostgreSQL", "Component · PostgreSQL"),
             L("Consecutivo único por operación; estados: pendiente, enviado, aceptado, rechazado, diferido", "Unique consecutive per operation; states: pending, sent, accepted, rejected, deferred"), 340, 540, 250, 120, B),
        Node("mapper", "component", L("Mapeador XML", "XML mapper"), L("Componente · plantillas", "Component · templates"),
             L("Una plantilla por procesoid; nunca se construye XML a mano en las rutas", "One template per procesoid; routes never build XML by hand"), 660, 210, 230, 110, B),
        Node("parser", "component", L("Intérprete de respuestas", "Response interpreter"), L("Componente", "Component"),
             L("ingresoid → aceptado; ErrorMSG → código (MAN071, REM139…) clasificado en corregible, reintentable o definitivo",
               "ingresoid → accepted; ErrorMSG → code (MAN071, REM139…) classified as fixable, retryable or final"), 660, 380, 230, 130, B),
        Node("publisher", "component", L("Publicador de resultados", "Result publisher"), L("Componente · Kafka", "Component · Kafka"),
             L("rndc.resultado con ingresoid o error; alimenta estado, web y conciliación", "rndc.result with ingresoid or error; feeds status, web and reconciliation"), 660, 540, 230, 120, B),
        Node("soap", "component", L("Cliente SOAP RNDC", "RNDC SOAP client"), L("Componente · CXF", "Component · CXF"),
             L("Credenciales por empresa, timeouts, reintentos con backoff y circuit breaker", "Per-company credentials, timeouts, backoff retries and circuit breaker"), 960, 210, 290, 120, B),
        Node("diferida", "component", L("Cola diferida (contingencia)", "Deferred queue (contingency)"), L("Componente · Kafka", "Component · Kafka"),
             L("Si el RNDC no responde: reintento programado dentro de la ventana de contingencia; alerta si vence", "If the RNDC is down: scheduled retry within the contingency window; alert if it expires"), 960, 380, 290, 120, B),
        Node("telemetria", "component", L("Telemetría", "Telemetry"), L("Componente · OpenTelemetry", "Component · OpenTelemetry"),
             L("Traza por despacho; métricas por código de error y por empresa", "Trace per dispatch; metrics by error code and company"), 960, 540, 290, 110, B),
        Node("kafka-out", "queue", L("Kafka", "Kafka"), L("Contenedor", "Container"), L("rndc.resultado", "rndc.result"), 660, 780, 230, 80),
    ]
    edges = [
        Edge("kafka-in", "consumer", L("Consume", "Consumes"), ""),
        Edge("consumer", "idem", L("¿Ya se envió? Marca en curso", "Already sent? Marks in progress"), "", points=[(165, 600)]),
        Edge("consumer", "prevalid", L("Operación a reportar", "Operation to file"), ""),
        Edge("prevalid", "catalogos", L("Consulta", "Looks up"), ""),
        Edge("prevalid", "mapper", L("Operación válida", "Valid operation"), ""),
        Edge("mapper", "soap", L("XML del procesoid", "procesoid XML"), ""),
        Edge("soap", "rndc", L("AtenderMensajeRNDC", "AtenderMensajeRNDC"), "SOAP/XML"),
        Edge("soap", "parser", L("Respuesta XML", "XML response"), ""),
        Edge("parser", "diferida", L("Reintentar o sin respuesta", "Retryable or no answer"), ""),
        Edge("diferida", "soap", L("Reintenta", "Retries"), "", dashed=True),
        Edge("parser", "publisher", L("Aceptado o definitivo", "Accepted or final"), ""),
        Edge("publisher", "idem", L("Actualiza estado", "Updates status"), ""),
        Edge("publisher", "kafka-out", L("Publica", "Publishes"), ""),
        Edge("prevalid", "publisher", L("Rechazo con causa", "Rejection with cause"), "", dashed=True, points=[(620, 330), (620, 580)], wrap_chars=9),
        Edge("parser", "telemetria", L("Métricas por código de error", "Metrics by error code"), "", dashed=True),
    ]
    return Diagram("c3-componentes", L("Nivel 3 · Componentes del integrador", "Level 3 · Integrator components"), 1300, 900, nodes, edges)


def dinamica() -> Diagram:
    nodes = [
        Node("analista", "person", L("Analista", "Analyst"), L("Persona", "Person"), L("", ""), 40, 40, 170, 90),
        Node("web", "container", L("Web de despachos", "Dispatch web app"), L("Angular", "Angular"), L("", ""), 310, 40, 190, 90),
        Node("api", "container", L("API de despachos", "Dispatch API"), L("Quarkus", "Quarkus"), L("", ""), 600, 40, 190, 90),
        Node("kafka", "queue", L("Kafka", "Kafka"), L("Confluent", "Confluent"), L("", ""), 890, 40, 190, 90),
        Node("motor", "container", L("Motor de validación", "Validation engine"), L("Camel", "Camel"), L("", ""), 1180, 40, 200, 90),
        Node("conciliador", "container", L("Conciliador de fletes", "Freight reconciler"), L("Kafka Streams", "Kafka Streams"), L("", ""), 310, 260, 190, 90),
        Node("integrador", "container", L("Integrador RNDC", "RNDC integrator"), L("Camel + CXF", "Camel + CXF"), L("", ""), 890, 260, 190, 90),
        Node("erp", "external", L("ERP legado", "Legacy ERP"), L("Oracle", "Oracle"), L("", ""), 40, 470, 170, 90),
        Node("rndc", "external", L("RNDC", "RNDC"), L("Ministerio de Transporte", "Ministry of Transport"), L("", ""), 890, 470, 190, 90),
        Node("app", "external", L("App RNDC Transportador", "RNDC Carrier app"), L("Conductor", "Driver"), L("", ""), 1170, 470, 190, 90),
        Node("nota", "note", L("Plazos que gobiernan el ciclo", "Deadlines that govern the cycle"), L("", ""),
             L("Cumplido a más tardar 72 h después de terminar el viaje. Con más del 20 % de operaciones pendientes el RNDC bloquea nuevos registros. Contingencia: reporte electrónico dentro de 24 h.",
               "Proof of delivery no later than 72 h after the trip ends. With more than 20% of operations pending the RNDC blocks new filings. Contingency: electronic filing within 24 h."), 40, 650, 650, 90),
    ]
    edges = [
        Edge("analista", "web", L("Crea la orden y la remesa", "Creates the order and consignment note"), "", number=1),
        Edge("web", "api", L("POST /remesas", "POST /consignments"), "", number=2),
        Edge("api", "kafka", L("Outbox → despacho.remesa", "Outbox → dispatch.consignment"), "", number=3),
        Edge("kafka", "motor", L("Valida reglas del Ministerio", "Validates Ministry rules"), "", number=4),
        Edge("motor", "integrador", L("Remesa validada", "Validated consignment"), "", number=5, points=[(1280, 130), (1280, 305), (1080, 305)]),
        Edge("integrador", "rndc", L("Registra remesa → ingresoid", "Files consignment → ingresoid"), "SOAP", number=6, label_side="left", wrap_chars=18),
        Edge("integrador", "rndc", L("Expide el manifiesto con sus remesas → número de manifiesto", "Issues the manifest with its consignments → manifest number"), "SOAP", number=7,
             points=[(830, 320), (830, 490)], label_side="left", wrap_chars=24),
        Edge("rndc", "app", L("Publica el manifiesto; el conductor lo acepta", "Publishes the manifest; the driver accepts it"), "", number=8, points=[(985, 590), (1265, 590)]),
        Edge("integrador", "rndc", L("Cumplido de remesa y de manifiesto (≤ 72 h)", "Consignment and manifest proof of delivery (≤ 72 h)"), "SOAP", number=9,
             points=[(1120, 320), (1120, 490)], wrap_chars=22),
        Edge("integrador", "kafka", L("rndc.resultado por cada paso", "rndc.result after each step"), "", number=10, points=[(1020, 260), (1020, 130)]),
        Edge("kafka", "conciliador", L("Remesas cumplidas", "Delivered consignments"), "", number=11, points=[(910, 130), (910, 200), (405, 200), (405, 260)]),
        Edge("conciliador", "erp", L("Flete conciliado contra SICE-TAC y factura", "Freight reconciled against SICE-TAC and invoice"), "", number=12),
    ]
    return Diagram("c4-dinamica", L("Dinámica · ciclo de un despacho", "Dynamic · lifecycle of a dispatch"), 1420, 770, nodes, edges)


def despliegue() -> Diagram:
    K, C, O = "k8s", "confluent", "onprem"
    nodes = [
        Node("navegador", "external", L("Navegador del analista", "Analyst's browser"), L("Nodo", "Node"), L("", ""), 40, 40, 220, 80),
        Node(K, "boundary", L("Kubernetes (clúster de la transportadora)", "Kubernetes (carrier's cluster)"), L("Nodo de despliegue", "Deployment node"), L("", ""), 40, 170, 760, 500),
        Node("ingress", "container", L("Ingress + web", "Ingress + web"), L("nginx", "nginx"), L("TLS, archivos estáticos de Angular", "TLS, Angular static files"), 60, 210, 220, 100, K),
        Node("api", "container", L("API de despachos", "Dispatch API"), L("Quarkus · 2 réplicas", "Quarkus · 2 replicas"), L("", ""), 310, 210, 220, 100, K),
        Node("keycloak", "container", L("Keycloak", "Keycloak"), L("IAM", "IAM"), L("", ""), 560, 210, 220, 100, K),
        Node("pg", "db", L("PostgreSQL", "PostgreSQL"), L("Operador · primario + réplica", "Operator · primary + replica"), L("", ""), 60, 350, 220, 100, K),
        Node("integrador", "container", L("Integrador RNDC", "RNDC integrator"), L("Camel + CXF · 2 réplicas", "Camel + CXF · 2 replicas"), L("Salida a internet por IP fija (allowlist del Ministerio)", "Internet egress through a fixed IP (Ministry allowlist)"), 310, 350, 220, 100, K),
        Node("sim", "container", L("Simulador RNDC", "RNDC simulator"), L("WireMock · sólo pruebas", "WireMock · tests only"), L("", ""), 560, 350, 220, 100, K),
        Node("motor", "container", L("Motor de validación", "Validation engine"), L("Camel · 2 réplicas", "Camel · 2 replicas"), L("", ""), 60, 490, 220, 100, K),
        Node("obs", "container", L("Observabilidad", "Observability"), L("Prometheus · Grafana · Tempo · Loki", "Prometheus · Grafana · Tempo · Loki"), L("", ""), 310, 490, 220, 100, K),
        Node("conciliador", "container", L("Conciliador", "Reconciler"), L("Kafka Streams", "Kafka Streams"), L("", ""), 560, 490, 220, 100, K),
        Node(C, "boundary", L("Clúster Kafka (Confluent)", "Kafka cluster (Confluent)"), L("Nodo de despliegue", "Deployment node"), L("", ""), 840, 170, 360, 300),
        Node("brokers", "queue", L("3 brokers", "3 brokers"), L("Particiones y réplicas por tema", "Partitions and replicas per topic"), L("", ""), 860, 210, 320, 90, C),
        Node("connect", "container", L("Kafka Connect", "Kafka Connect"), L("Debezium Oracle · outbox", "Debezium Oracle · outbox"), L("", ""), 860, 330, 150, 110, C),
        Node("mm2", "container", L("MirrorMaker 2", "MirrorMaker 2"), L("Réplica al clúster de DR", "Replication to the DR cluster"), L("", ""), 1030, 330, 150, 110, C),
        Node(O, "boundary", L("Centro de datos de la transportadora", "Carrier's data centre"), L("Nodo de despliegue · on-prem", "Deployment node · on-prem"), L("", ""), 840, 510, 360, 160),
        Node("oracle", "db", L("Oracle legado", "Legacy Oracle"), L("ERP / TMS", "ERP / TMS"), L("", ""), 860, 550, 320, 100, O),
        Node("rndc", "external", L("RNDC · Ministerio de Transporte", "RNDC · Ministry of Transport"), L("Internet · SOAP/XML", "Internet · SOAP/XML"), L("", ""), 40, 730, 300, 80),
        Node("sicetac", "external", L("SICE-TAC", "SICE-TAC"), L("Internet · HTTP", "Internet · HTTP"), L("", ""), 380, 730, 300, 80),
    ]
    edges = [
        Edge("navegador", "ingress", L("HTTPS", "HTTPS"), ""),
        Edge("ingress", "api", L("REST", "REST"), ""),
        Edge("api", "keycloak", L("OIDC", "OIDC"), ""),
        Edge("api", "pg", L("JDBC", "JDBC"), "", points=[(420, 310), (420, 330), (295, 330), (295, 400), (280, 400)], label_seg=1),
        Edge("integrador", "rndc", L("SOAP/XML por IP fija", "SOAP/XML through fixed IP"), "", points=[(295, 420), (295, 710), (190, 710), (190, 730)], label_seg=2),
        Edge("integrador", "sim", L("", ""), "", dashed=True),
        Edge("conciliador", "sicetac", L("HTTP", "HTTP"), "", points=[(670, 590), (670, 710), (530, 710), (530, 730)]),
        Edge("connect", "oracle", L("LogMiner", "LogMiner"), ""),
        Edge("brokers", "connect", L("", ""), ""),
        Edge("brokers", "mm2", L("", ""), ""),
        Edge("api", "brokers", L("Eventos", "Events"), "", points=[(420, 210), (420, 190), (820, 190), (820, 255), (860, 255)]),
        Edge("integrador", "brokers", L("Consume y publica", "Consumes and publishes"), "", points=[(530, 380), (545, 380), (545, 330), (820, 330), (820, 270), (860, 270)]),
    ]
    return Diagram("c5-despliegue", L("Despliegue", "Deployment"), 1240, 840, nodes, edges)


DIAGRAMS = [contexto(), contenedores(), componentes(), dinamica(), despliegue()]


# ---------------------------------------------------------------------------- SVG
def wrap(text: str, max_chars: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def center(n: Node) -> tuple[float, float]:
    return n.x + n.w / 2, n.y + n.h / 2


def anchor(n: Node, towards: tuple[float, float]) -> tuple[float, float]:
    """Punto del borde del nodo en la dirección de `towards` (recorte rectangular)."""
    cx, cy = center(n)
    tx, ty = towards
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (n.w / 2) / abs(dx) if dx else float("inf")
    sy = (n.h / 2) / abs(dy) if dy else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def svg_text(x: float, y: float, lines: list[str], size: float, weight: str = "normal", color: str = INK, anchor_: str = "middle", italic: bool = False, lh: float | None = None) -> str:
    lh = lh or size * 1.25
    out = []
    for i, line in enumerate(lines):
        style = f"font-family:{FONT};font-size:{size}px;font-weight:{weight};fill:{color}" + (";font-style:italic" if italic else "")
        out.append(f'<text x="{x:.1f}" y="{y + i * lh:.1f}" text-anchor="{anchor_}" style="{style}">{html.escape(line)}</text>')
    return "".join(out)


def svg_node(n: Node, lang: int) -> str:
    name, typ, desc = n.name[lang], n.type[lang], n.desc[lang]
    x, y, w, h = n.x, n.y, n.w, n.h
    parts = []
    if n.kind == "boundary":
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{GRAPHITE}" stroke-width="1.2" stroke-dasharray="6 5"/>')
        parts.append(svg_text(x + 10, y + 17, [name], 13, "bold", GRAPHITE, "start"))
        parts.append(svg_text(x + 10, y + 31, [f"[{typ}]"], 10, "normal", GRAPHITE, "start"))
        return "".join(parts)
    if n.kind == "note":
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{AMBER_WASH}" stroke="{INK}" stroke-width="1"/>')
        parts.append(svg_text(x + 12, y + 20, [name], 12, "bold", INK, "start"))
        parts.append(svg_text(x + 12, y + 38, wrap(desc, int((w - 24) / CHAR_W)), 10.5, "normal", INK, "start", lh=14))
        return "".join(parts)
    stroke_w = 2 if n.kind in ("system",) else 1.5
    dash = ' stroke-dasharray="7 5"' if n.kind == "external" else ""
    fill = AMBER if n.kind == "system" else PAPER
    if n.kind == "db":
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{INK}" stroke-width="{stroke_w}"/>')
        parts.append(f'<path d="M{x} {y + 9} H{x + w}" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    elif n.kind == "queue":
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{INK}" stroke-width="{stroke_w}"/>')
        parts.append(f'<path d="M{x + 8} {y} V{y + h} M{x + w - 8} {y} V{y + h}" stroke="{INK}" stroke-width="1" fill="none"/>')
    elif n.kind == "person":
        cx = x + w / 2
        parts.append(f'<rect x="{x}" y="{y + 16}" width="{w}" height="{h - 16}" rx="10" fill="{fill}" stroke="{INK}" stroke-width="{stroke_w}"/>')
        parts.append(f'<circle cx="{cx}" cy="{y + 16}" r="14" fill="{PAPER}" stroke="{INK}" stroke-width="{stroke_w}"/>')
        parts.append(f'<circle cx="{cx}" cy="{y + 12}" r="4" fill="{INK}"/><path d="M{cx - 7} {y + 25} q7 -9 14 0" stroke="{INK}" stroke-width="1.5" fill="none"/>')
    else:
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{INK}" stroke-width="{stroke_w}"{dash}/>')
    top = y + (46 if n.kind == "person" else 20)
    cx = x + w / 2
    name_lines = wrap(name, int((w - 20) / 7.2))
    parts.append(svg_text(cx, top, name_lines, 13, "bold", INK, lh=16))
    yy = top + len(name_lines) * 16
    if typ:
        parts.append(svg_text(cx, yy, [f"[{typ}]"], 10, "normal", GRAPHITE if n.kind != "system" else INK, italic=True))
        yy += 15
    if desc:
        parts.append(svg_text(cx, yy + 2, wrap(desc, int((w - 20) / 5.4)), 10.5, "normal", INK, lh=13.5))
    return "".join(parts)


def svg_edge(e: Edge, nodes: dict[str, Node], lang: int) -> tuple[str, str]:
    """Devuelve (trazo, etiqueta). Las etiquetas se pintan en una capa superior para que ningún nodo las tape."""
    a, b = nodes[e.src], nodes[e.dst]
    if e.points:
        p0 = anchor(a, e.points[0])
        p1 = anchor(b, e.points[-1])
        pts = [p0, *[(float(px), float(py)) for px, py in e.points], p1]
    else:
        p0 = anchor(a, center(b))
        p1 = anchor(b, center(a))
        pts = [p0, p1]
    d = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    dash = ' stroke-dasharray="5 4"' if e.dashed else ""
    path = f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="1.5" marker-end="url(#arrow)"{dash}/>'

    # tramo que lleva la etiqueta: el indicado o el más largo
    segs = list(zip(pts, pts[1:]))
    if e.label_seg is not None:
        (x1, y1), (x2, y2) = segs[e.label_seg]
    else:
        (x1, y1), (x2, y2) = max(segs, key=lambda s: abs(s[1][0] - s[0][0]) + abs(s[1][1] - s[0][1]))
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    horizontal = abs(x2 - x1) >= abs(y2 - y1)
    seg_len = abs(x2 - x1) + abs(y2 - y1)

    label = e.label[lang]
    if e.wrap_chars:
        max_chars = e.wrap_chars
    elif horizontal and e.label_side in ("auto", "center") and e.number is None and len(pts) == 2:
        # tramo corto entre dos cajas vecinas: la etiqueta debe caber en el hueco
        max_chars = max(8, min(30, int((seg_len - 10) / CHAR_W)))
    else:
        max_chars = 30
    lines = wrap(label, max_chars) if label else []
    if e.tech:
        lines.append(f"[{e.tech}]")
    out = []
    if lines:
        wmax = max(len(s) for s in lines) * CHAR_W + 12
        hgt = len(lines) * 12.5 + 6
        side = e.label_side
        if side == "auto":
            side = "center" if e.number is None else ("below" if horizontal else "right")
        if e.label_pos:
            lx, ly, text_anchor = e.label_pos[0], e.label_pos[1], "middle"
        elif side == "center":
            lx, ly, text_anchor = mx, my, "middle"
        elif side == "below":
            lx, ly, text_anchor = mx, my + 14 + hgt / 2, "middle"
        elif side == "right":
            lx, ly, text_anchor = mx + 16 + wmax / 2, my, "middle"
        else:  # left
            lx, ly, text_anchor = mx - 16 - wmax / 2, my, "middle"
        out.append(f'<rect x="{lx - wmax / 2:.1f}" y="{ly - hgt / 2 - 1:.1f}" width="{wmax:.1f}" height="{hgt:.1f}" fill="{PAPER}" fill-opacity="0.94"/>')
        out.append(svg_text(lx, ly - hgt / 2 + 11, lines, 10, "normal", GRAPHITE, text_anchor, lh=12.5))
    if e.number is not None:
        out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="11" fill="{AMBER}" stroke="{INK}" stroke-width="1.5"/>')
        out.append(svg_text(mx, my + 4, [str(e.number)], 11, "bold", INK))
    return path, "".join(out)


def write_svg(dg: Diagram, lang: int, path: str) -> None:
    nodes = {n.id: n for n in dg.nodes}
    body = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {dg.width} {dg.height}" width="{dg.width}" height="{dg.height}" role="img" aria-label="{html.escape(dg.title[lang])}">',
        f'<title>{html.escape(dg.title[lang])}</title>',
        f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"/></marker>'
        f'<pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{GRID}"/></pattern></defs>',
        f'<rect width="{dg.width}" height="{dg.height}" fill="{PAPER}"/><rect width="{dg.width}" height="{dg.height}" fill="url(#grid)"/>',
    ]
    body += [svg_node(n, lang) for n in dg.nodes if n.kind == "boundary"]
    edges = [svg_edge(e, nodes, lang) for e in dg.edges]
    body += [p for p, _ in edges]
    body += [svg_node(n, lang) for n in dg.nodes if n.kind != "boundary"]
    body += [lbl for _, lbl in edges]
    body.append(svg_text(dg.width - 12, dg.height - 10, [dg.title[lang].upper()], 10, "bold", GRAPHITE, "end"))
    body.append("</svg>\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(body))


# ---------------------------------------------------------------------------- draw.io
C4_STYLE = {
    "person": "html=1;fontSize=11;dashed=0;whiteSpace=wrap;fillColor=#083F75;strokeColor=#06315C;fontColor=#ffffff;shape=mxgraph.c4.person2;align=center;metaEdit=1;points=[[0.5,0,0],[1,0.5,0],[1,0.75,0],[0.75,1,0],[0.5,1,0],[0.25,1,0],[0,0.75,0],[0,0.5,0]];resizable=0;",
    "system": "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#1061B0;strokeColor=#0D5091;fontColor=#ffffff;align=center;arcSize=10;strokeWidth=1;metaEdit=1;resizable=0;",
    "external": "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#8C8496;strokeColor=#736782;fontColor=#ffffff;align=center;arcSize=10;strokeWidth=1;metaEdit=1;resizable=0;",
    "container": "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#23A2D9;fontColor=#ffffff;align=center;arcSize=10;strokeColor=#0E7DAD;metaEdit=1;resizable=0;",
    "component": "rounded=1;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#63BEF2;fontColor=#ffffff;align=center;arcSize=6;strokeColor=#2086C9;metaEdit=1;resizable=0;",
    "db": "shape=cylinder3;size=15;whiteSpace=wrap;html=1;boundedLbl=1;rounded=0;labelBackgroundColor=none;fillColor=#23A2D9;fontSize=12;fontColor=#ffffff;align=center;strokeColor=#0E7DAD;metaEdit=1;",
    "queue": "shape=mxgraph.c4.container;whiteSpace=wrap;html=1;labelBackgroundColor=none;fillColor=#23A2D9;fontColor=#ffffff;align=center;strokeColor=#0E7DAD;metaEdit=1;",
    "boundary": "rounded=1;fontSize=11;whiteSpace=wrap;html=1;dashed=1;arcSize=20;fillColor=none;strokeColor=#666666;fontColor=#333333;labelBackgroundColor=none;align=left;verticalAlign=bottom;labelBorderColor=none;spacingTop=0;spacing=10;dashPattern=8 4;metaEdit=1;rotatable=0;perimeter=rectanglePerimeter;noLabel=0;labelPadding=0;allowArrows=0;connectable=0;expand=0;recursiveResize=0;editable=1;pointerEvents=0;absoluteArcSize=1;",
    "note": "shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#fff2cc;strokeColor=#d6b656;size=20;align=left;verticalAlign=top;spacing=8;",
}
EDGE_STYLE = "endArrow=blockThin;html=1;fontSize=10;fontColor=#404040;strokeWidth=1;endFill=1;strokeColor=#828282;elbow=vertical;metaEdit=1;endSize=14;startSize=14;jumpStyle=arc;jumpSize=16;rounded=0;edgeStyle=orthogonalEdgeStyle;"


def drawio_label(n: Node, lang: int) -> str:
    name, typ, desc = n.name[lang], n.type[lang], n.desc[lang]
    if n.kind == "boundary":
        return f"<b>{html.escape(name)}</b><div>[{html.escape(typ)}]</div>"
    if n.kind == "note":
        return f"<b>{html.escape(name)}</b><br>{html.escape(desc)}"
    label = f"<b>{html.escape(name)}</b><div>[{html.escape(typ)}]</div>"
    if desc:
        label += f'<br><div><font style="font-size: 11px">{html.escape(desc)}</font></div>'
    return label


def write_drawio(dg: Diagram, lang: int, path: str) -> None:
    cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
    for n in dg.nodes:
        style = C4_STYLE[n.kind]
        parent = "1"
        x, y = n.x, n.y
        if n.parent:
            p = next(m for m in dg.nodes if m.id == n.parent)
            parent = p.id
            x, y = n.x - p.x, n.y - p.y
        cells.append(
            f'<mxCell id="{n.id}" value="{html.escape(drawio_label(n, lang), quote=True)}" style="{style}" vertex="1" parent="{parent}">'
            f'<mxGeometry x="{x}" y="{y}" width="{n.w}" height="{n.h}" as="geometry"/></mxCell>'
        )
    for i, e in enumerate(dg.edges):
        label = e.label[lang]
        if e.number is not None:
            label = f"{e.number}. {label}"
        value = f'<div style="text-align: center"><b>{html.escape(label)}</b></div>' + (f'<div style="text-align: center">[{html.escape(e.tech)}]</div>' if e.tech else "")
        style = EDGE_STYLE + ("dashed=1;" if e.dashed else "")
        pts = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in e.points)
        geom = f'<mxGeometry relative="1" as="geometry">{("<Array as=\"points\">" + pts + "</Array>") if pts else ""}</mxGeometry>'
        cells.append(f'<mxCell id="e{i}" value="{html.escape(value, quote=True)}" style="{style}" edge="1" parent="1" source="{e.src}" target="{e.dst}">{geom}</mxCell>')
    xml = (
        '<mxfile host="app.diagrams.net" agent="rndc-diagramas.py" version="24.0.0">'
        f'<diagram id="{dg.slug}" name="{html.escape(dg.title[lang], quote=True)}">'
        f'<mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1654" pageHeight="1169" math="0" shadow="0">'
        f'<root>{"".join(cells)}</root></mxGraphModel></diagram></mxfile>\n'
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(xml)


def main() -> None:
    os.makedirs(SVG_DIR, exist_ok=True)
    os.makedirs(DRAWIO_DIR, exist_ok=True)
    for dg in DIAGRAMS:
        for lang, code in ((0, "es"), (1, "en")):
            write_svg(dg, lang, os.path.join(SVG_DIR, f"{dg.slug}.{code}.svg"))
            write_drawio(dg, lang, os.path.join(DRAWIO_DIR, f"{dg.slug}.{code}.drawio"))
        print("ok", dg.slug)


if __name__ == "__main__":
    main()
