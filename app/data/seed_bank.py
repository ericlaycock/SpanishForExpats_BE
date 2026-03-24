"""Central seed bank — single source of truth for all word and situation data.

All encounter words, high-frequency words, situations, and their links
are defined here. Grammar situations are in grammar_situations.py.
The seed script (scripts/seed_qa.py) reads from this module.

Structure: _SUB_SITUATIONS defines compact word data as (spanish, english, catalan) tuples.
ENCOUNTER_WORDS, SITUATIONS, and SITUATION_WORDS are generated at import time.
"""

from app.data.hf_words import HIGH_FREQUENCY_WORDS  # noqa: F401 — re-exported

# --- Animation type display names (used by API and onboarding) ---

ANIMATION_NAMES = {
    "airport": "Airport",
    "banking": "Banking",
    "clothing": "Clothing Shopping",
    "internet": "Internet",
    "small_talk": "Small Talk",
    "contractor": "Home Renovation",
    "groceries": "Groceries",
    "mechanic": "Mechanic",
    "police": "Police Stop",
    "restaurant": "Eating Out",
}

# --- Compact sub-situation definitions ---
# Each sub-situation has 50 encounters × 3 words = 150 (spanish, english) tuples.
# Words progress from basic/essential (early encounters) to specialized (later).

_SUB_SITUATIONS = {
    "airport": [
        {
            "title": "Checking In",
            "goal": "Complete the airport check-in process with the airline agent",
            "word_prefix": "air",
            "words": [
                ("billete", "ticket", ""), ("reserva", "reservation", ""), ("confirmación", "confirmation", ""),  # Encounter 1
                ("número de reserva", "reservation number", ""), ("pasajero", "passenger", ""), ("apellido", "last name", ""),  # Encounter 2
                ("documento", "document", ""), ("identificación", "identification", ""), ("permiso de entrada", "entry permit", ""),  # Encounter 3
                ("permiso", "permission", ""), ("documentos de viaje", "travel documents", ""), ("fecha de vencimiento", "expiration date", ""),  # Encounter 4
                ("a nombre de", "in the name of", ""), ("¿tiene reserva?", "Do you have a reservation?", ""), ("¿me muestra el pasaporte?", "Show passport?", ""),  # Encounter 5
                ("¿a qué nombre?", "under what name?", ""), ("vuelo", "flight", ""), ("número de vuelo", "flight number", ""),  # Encounter 6
                ("destino", "destination", ""), ("destino final", "final destination", ""), ("origen", "origin", ""),  # Encounter 7
                ("conexión", "connection", ""), ("vuelo de conexión", "connecting flight", ""), ("vuelo directo", "direct flight", ""),  # Encounter 8
                ("vuelo lleno", "full flight", ""), ("vuelo anterior", "previous flight", ""), ("vuelo siguiente", "next flight", ""),  # Encounter 9
                ("¿va directo a…?", "Are you going directly to...?", ""), ("¿hasta dónde va?", "How far going?", ""), ("¿sale hoy?", "Does it leave today?", ""),  # Encounter 10
                ("¿sale mañana?", "Does it leave tomorrow?", ""), ("salida", "exit", ""), ("llegada", "arrival", ""),  # Encounter 11
                ("embarque", "boarding", ""), ("hora de embarque", "boarding time", ""), ("hora de salida", "departure time", ""),  # Encounter 12
                ("entrada", "entrance", ""), ("número de puerta", "gate number", ""), ("puerta de embarque", "boarding gate", ""),  # Encounter 13
                ("zona de embarque", "boarding area", ""), ("preembarque", "pre-boarding", ""), ("prioridad", "priority", ""),  # Encounter 14
                ("a tiempo", "on time", ""), ("retraso", "delay", ""), ("demora", "delay", ""),  # Encounter 15
                ("cambio de puerta", "door change", ""), ("¿cuál es la puerta?", "which gate?", ""), ("aparece en las pantallas", "appears on screens", ""),  # Encounter 16
                ("aparece en la app", "appears in app", ""), ("no está asignada", "not assigned", ""), ("asiento", "seat", ""),  # Encounter 17
                ("número de asiento", "seat number", ""), ("fila", "line", ""), ("puerta de embarque", "boarding gate", ""),  # Encounter 18
                ("pasillo del avión", "airplane aisle", ""), ("asiento del medio", "middle seat", ""), ("asiento de ventana", "window seat", ""),  # Encounter 19
                ("asiento de pasillo", "aisle seat", ""), ("salida de emergencia", "emergency exit", ""), ("juntos", "together", ""),  # Encounter 20
                ("separados", "separated", ""), ("¿prefiere ventana o pasillo?", "Window or aisle?", ""), ("¿hay asientos juntos?", "Seats together?", ""),  # Encounter 21
                ("¿hay otro asiento?", "Another seat?", ""), ("cambio de asiento", "seat change", ""), ("asignado", "assigned", ""),  # Encounter 22
                ("valijas", "suitcases", ""), ("maleta", "suitcase", ""), ("equipaje de mano", "carry-on luggage", ""),  # Encounter 23
                ("equipaje facturado", "checked luggage", ""), ("maleta de cabina", "carry-on", ""), ("artículo personal", "personal item", ""),  # Encounter 24
                ("primera maleta", "first suitcase", ""), ("segunda maleta", "second suitcase", ""), ("tarifa aérea", "air fare", ""),  # Encounter 25
                ("recibo de equipaje", "baggage receipt", ""), ("cinta transportadora", "conveyor belt", ""), ("recogida de equipaje", "baggage pickup", ""),  # Encounter 26
                ("¿va a facturar equipaje?", "Are you checking luggage?", ""), ("¿lleva equipaje?", "Carry luggage?", ""), ("balanza", "scale", ""),  # Encounter 27
                ("tarifa", "rate", ""), ("límite", "limit", ""), ("exceso", "excess", ""),  # Encounter 28
                ("sobrepeso", "overweight", ""), ("medidas", "measurements", ""), ("medidas permitidas", "allowed measurements", ""),  # Encounter 29
                ("está demasiado pesado", "too heavy", ""), ("está demasiado grande", "too big", ""), ("póngalo en la balanza", "put on scale", ""),  # Encounter 30
                ("¿cuál es el límite?", "what is the limit?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""), ("facturo el equipaje", "I check luggage", ""),  # Encounter 31
                ("etiquetan el equipaje", "tag luggage", ""), ("abre la maleta", "opens the suitcase", ""), ("saca los objetos", "take out objects", ""),  # Encounter 32
                ("pasa algunas cosas a la mochila", "put some things in backpack", ""), ("lo lleva con usted", "take with you", ""), ("no puede ir en la maleta", "can't go in suitcase", ""),  # Encounter 33
                ("¿puede facturarlo?", "Can check in?", ""), ("¿puede llevarlo con usted?", "Can carry with you?", ""), ("líquidos", "liquids", ""),  # Encounter 34
                ("batería portátil", "portable battery", ""), ("cargador", "charger", ""), ("tableta", "tablet", ""),  # Encounter 35
                ("objetos de valor", "valuables", ""), ("medicinas", "medicines", ""), ("¿lleva líquidos?", "Carry liquids?", ""),  # Encounter 36
                ("¿lleva baterías?", "Carry batteries?", ""), ("no está permitido", "not allowed", ""), ("está permitido", "allowed", ""),  # Encounter 37
                ("control de seguridad", "security checkpoint", ""), ("revisión", "inspection", ""), ("revisión adicional", "additional inspection", ""),  # Encounter 38
                ("selección aleatoria", "random selection", ""), ("inspección", "inspection", ""), ("seguridad", "security", ""),  # Encounter 39
                ("terminal", "terminal", ""), ("aeropuerto", "airport", ""), ("aerolínea", "airline", ""),  # Encounter 40
                ("mostrador", "counter", ""), ("equipo electrónico", "electronic equipment", ""), ("no funciona", "does not work", ""),  # Encounter 41
                ("exceso de equipaje", "excess baggage", ""), ("paga el exceso", "pays excess", ""), ("con tarjeta", "by card", ""),  # Encounter 42
                ("en efectivo", "in cash", ""), ("sin costo", "free", ""), ("tarifa", "rate", ""),  # Encounter 43
                ("tarifa", "rate", ""), ("embarque", "boarding", ""), ("pasajero", "passenger", ""),  # Encounter 44
                ("pasajeros", "passengers", ""), ("niño", "boy", ""), ("niña", "girl", ""),  # Encounter 45
                ("coche de bebé", "baby stroller", ""), ("hasta la puerta", "to the door", ""), ("tarjeta de embarque", "boarding pass", ""),  # Encounter 46
                ("imprimen la tarjeta de embarque", "print boarding pass", ""), ("equipaje de mano", "carry-on luggage", ""), ("control de seguridad", "security checkpoint", ""),  # Encounter 47
                ("confirmación por correo", "email confirmation", ""), ("hay espacio", "there is space", ""), ("no hay espacio", "no space", ""),  # Encounter 48
                ("conexión corta", "short connection", ""), ("conexión larga", "long connection", ""), ("control de pasaportes", "passport control", ""),  # Encounter 49
                ("migración", "migration", ""), ("control migratorio", "immigration control", ""), ("formulario de aduana", "customs form", ""),  # Encounter 50
            ],
        },
    ],
    "banking": [
        {
            "title": "Banking",
            "goal": "Handle banking tasks including accounts, transfers, cards, and loans",
            "word_prefix": "bank",
            "words": [
                ("banco", "bench/bank", ""), ("cajero", "cashier", ""), ("cliente", "customer", ""),  # Encounter 1
                ("tarjeta bancaria", "bank card", ""), ("cuenta bancaria", "bank account", ""), ("saldo", "balance", ""),  # Encounter 2
                ("saldo disponible", "available balance", ""), ("saldo actual", "current balance", ""), ("tarjeta", "card", ""),  # Encounter 3
                ("tarjeta de débito", "debit card", ""), ("tarjeta de crédito", "credit card", ""), ("tarjeta bloqueada", "blocked card", ""),  # Encounter 4
                ("tarjeta nueva", "new card", ""), ("PIN", "PIN", ""), ("clave", "key", ""),  # Encounter 5
                ("contraseña", "password", ""), ("número de cuenta", "account number", ""), ("número incorrecto", "wrong number", ""),  # Encounter 6
                ("transferencia", "transfer", ""), ("transferencia enviada", "transfer sent", ""), ("transferencia recibida", "transfer received", ""),  # Encounter 7
                ("no llegó", "didn't arrive", ""), ("llegó tarde", "arrived late", ""), ("comprobante", "receipt", ""),  # Encounter 8
                ("muestro el comprobante", "show receipt", ""), ("reviso la cuenta", "I check the account", ""), ("revisan los movimientos", "check the movements", ""),  # Encounter 9
                ("movimientos", "movements", ""), ("cargo", "charge", ""), ("cargos extra", "extra charges", ""),  # Encounter 10
                ("no lo reconozco", "don't recognize it", ""), ("cargo sospechoso", "suspicious charge", ""), ("intento sospechoso", "suspicious attempt", ""),  # Encounter 11
                ("bloqueo", "blockage", ""), ("se bloqueó", "locked", ""), ("desbloquean la tarjeta", "unlock the card", ""),  # Encounter 12
                ("activan la tarjeta", "activate the card", ""), ("emiten la tarjeta", "issue card", ""), ("funciona ahora", "works now", ""),  # Encounter 13
                ("no funciona", "does not work", ""), ("rechazada", "rejected", ""), ("pago rechazado", "payment rejected", ""),  # Encounter 14
                ("hago el pago", "I make payment", ""), ("pago aprobado", "payment approved", ""), ("pago pendiente", "pending payment", ""),  # Encounter 15
                ("monto", "amount", ""), ("monto total", "total amount", ""), ("cantidad total", "total amount", ""),  # Encounter 16
                ("deposito dinero", "deposit money", ""), ("retiro", "withdrawal", ""), ("retiro dinero", "withdraw money", ""),  # Encounter 17
                ("efectivo", "cash", ""), ("con tarjeta", "by card", ""), ("cajero automático", "ATM", ""),  # Encounter 18
                ("retiro en el cajero", "ATM withdrawal", ""), ("saldo insuficiente", "insufficient balance", ""), ("no hay fondos", "no funds", ""),  # Encounter 19
                ("hay fondos", "there are funds", ""), ("abro una cuenta", "I open an account", ""), ("abro una cuenta nueva", "I open a new account", ""),  # Encounter 20
                ("cierro la cuenta", "close account", ""), ("cambio de cuenta", "account change", ""), ("tipo de cuenta", "account type", ""),  # Encounter 21
                ("cuenta principal", "main account", ""), ("cuenta de ahorros", "savings account", ""), ("cuenta corriente", "checking account", ""),  # Encounter 22
                ("comisión", "commission", ""), ("cobran comisión", "charge commission", ""), ("sin comisión", "no commission", ""),  # Encounter 23
                ("comisión mensual", "monthly commission", ""), ("eliminan la comisión", "remove commission", ""), ("tasa de interés", "interest rate", ""),  # Encounter 24
                ("condiciones", "conditions", ""), ("saldo mínimo", "minimum balance", ""), ("requiere saldo mínimo", "requires minimum balance", ""),  # Encounter 25
                ("requiere depósitos", "requires deposits", ""), ("historial", "history", ""), ("historial crediticio", "credit history", ""),  # Encounter 26
                ("crédito", "credit", ""), ("buen crédito", "good credit", ""), ("mal crédito", "bad credit", ""),  # Encounter 27
                ("préstamo", "loan", ""), ("solicito un préstamo", "I request a loan", ""), ("monto del préstamo", "loan amount", ""),  # Encounter 28
                ("aprueban el préstamo", "loan approved", ""), ("rechazan el préstamo", "loan denied", ""), ("aprobación", "approval", ""),  # Encounter 29
                ("está en proceso", "in process", ""), ("petición", "request", ""), ("envío la solicitud", "I send the request", ""),  # Encounter 30
                ("documentos", "documents", ""), ("falta un documento", "missing document", ""), ("envío los documentos", "I send the documents", ""),  # Encounter 31
                ("comprobante de ingresos", "income proof", ""), ("revisan el sistema", "check the system", ""), ("el sistema falla", "system fails", ""),  # Encounter 32
                ("el sistema está lento", "system is slow", ""), ("error del sistema", "system error", ""), ("abren un caso", "open a case", ""),  # Encounter 33
                ("número de caso", "case number", ""), ("seguimiento del caso", "case tracking", ""), ("tarda unos días", "takes a few days", ""),  # Encounter 34
                ("tiempo estimado", "estimated time", ""), ("depende del sistema", "depends on system", ""), ("espero la respuesta", "I await reply", ""),  # Encounter 35
                ("hoy no", "not today", ""), ("mañana sí", "yes tomorrow", ""), ("llamo al banco", "I call bank", ""),  # Encounter 36
                ("atención al cliente", "customer service", ""), ("hablo con un agente", "speak to agent", ""), ("verifican mi identidad", "verify my identity", ""),  # Encounter 37
                ("confirman mis datos", "confirm my data", ""), ("fecha de nacimiento", "birth date", ""), ("dirección", "address", ""),  # Encounter 38
                ("número de teléfono", "phone number", ""), ("correo electrónico", "email", ""), ("actualizan mis datos", "update my data", ""),  # Encounter 39
                ("datos incorrectos", "incorrect data", ""), ("cambio mis datos", "update data", ""), ("código de seguridad", "security code", ""),  # Encounter 40
                ("envían el código", "they send the code", ""), ("ingreso el código", "enter code", ""), ("código válido", "valid code", ""),  # Encounter 41
                ("código inválido", "invalid code", ""), ("acceso a la cuenta", "account access", ""), ("no tengo acceso", "no access", ""),  # Encounter 42
                ("recupero el acceso", "regain access", ""), ("restablecen la clave", "reset the password", ""), ("cambio la clave", "change password", ""),  # Encounter 43
                ("bloquean el acceso", "block access", ""), ("acceso activo", "active access", ""), ("sigue igual", "stays same", ""),  # Encounter 44
                ("mejora un poco", "improves a bit", ""), ("no mejora", "doesn't improve", ""), ("¿qué pasó?", "What happened?", ""),  # Encounter 45
                ("¿qué hago?", "What do?", ""), ("¿cuánto tarda?", "how long does it take?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""),  # Encounter 46
                ("no entiendo", "do not understand", ""), ("¿puede repetir?", "Can repeat?", ""), ("más despacio", "slower", ""),  # Encounter 47
                ("oficina bancaria", "bank office", ""), ("ejecutivo", "executive", ""), ("ventanilla", "window", ""),  # Encounter 48
                ("firma registrada", "registered signature", ""), ("la firma no coincide", "signature mismatch", ""), ("transferencia internacional", "international transfer", ""),  # Encounter 49
                ("tipo de cambio", "exchange rate", ""), ("comisión por transferencia", "transfer commission", ""), ("fondos retenidos", "withheld funds", ""),  # Encounter 50
            ],
        },
    ],
    "clothing": [
        {
            "title": "Clothing Shopping",
            "goal": "Navigate a clothing store, find your size, make a purchase, and handle returns",
            "word_prefix": "cloth",
            "words": [
                ("vendedor", "seller", ""), ("cliente", "customer", ""), ("boutique", "boutique", ""),  # Encounter 1
                ("ropa", "clothes", ""), ("camisa", "shirt", ""), ("pantalón", "pants", ""),  # Encounter 2
                ("chaqueta", "jacket", ""), ("vestido", "dress", ""), ("falda", "skirt", ""),  # Encounter 3
                ("talla", "size", ""), ("¿qué talla usa?", "What size?", ""), ("le queda bien", "fits well", ""),  # Encounter 4
                ("le queda grande", "too big", ""), ("le queda pequeño", "too small", ""), ("no le queda", "does not fit", ""),  # Encounter 5
                ("otra talla", "another size", ""), ("más grande", "bigger", ""), ("más pequeño", "smaller", ""),  # Encounter 6
                ("probador", "fitting room", ""), ("usa el probador", "use tester", ""), ("espere su turno", "wait your turn", ""),  # Encounter 7
                ("hay fila", "there is line", ""), ("prenda", "garment", ""), ("mismo modelo", "same model", ""),  # Encounter 8
                ("modelo diferente", "different model", ""), ("color", "color", ""), ("otro color", "another color", ""),  # Encounter 9
                ("no hay talla", "no size", ""), ("no hay stock", "out of stock", ""), ("está agotado", "is sold out", ""),  # Encounter 10
                ("reviso el stock", "I check the stock", ""), ("reviso el sistema", "I check the system", ""), ("hay en otra sucursal", "in another branch", ""),  # Encounter 11
                ("otra sucursal", "another branch", ""), ("lo pueden pedir", "can order", ""), ("llega en unos días", "arrives in days", ""),  # Encounter 12
                ("tarda unos días", "takes a few days", ""), ("lo aparto", "set aside", ""), ("apartado", "section", ""),  # Encounter 13
                ("tarifa", "rate", ""), ("precio normal", "regular price", ""), ("precio de oferta", "offer price", ""),  # Encounter 14
                ("descuento", "discount", ""), ("el descuento aplica", "discount applies", ""), ("no aplica", "not applicable", ""),  # Encounter 15
                ("promoción", "promotion", ""), ("talla", "size", ""), ("con membresía", "with membership", ""),  # Encounter 16
                ("sin membresía", "no membership", ""), ("registro", "registration", ""), ("no quiero registrarme", "don't want to check in", ""),  # Encounter 17
                ("el sistema marca otro precio", "system shows different price", ""), ("no coincide", "does not match", ""), ("reviso el precio", "I check the price", ""),  # Encounter 18
                ("corrigen el precio", "they correct the price", ""), ("ajuste manual", "manual adjustment", ""), ("talla", "size", ""),  # Encounter 19
                ("mal etiquetado", "mislabeling", ""), ("letrero", "sign", ""), ("política de la tienda", "store policy", ""),  # Encounter 20
                ("no aceptamos devoluciones", "no returns", ""), ("solo damos crédito de tienda", "we only give store credit", ""), ("crédito de tienda", "store credit", ""),  # Encounter 21
                ("devolución", "refund", ""), ("procesan la devolución", "they process the return", ""), ("cambio de producto", "product exchange", ""),  # Encounter 22
                ("producto defectuoso", "defective product", ""), ("está roto", "broken", ""), ("costura rota", "torn seam", ""),  # Encounter 23
                ("recibo", "receipt", ""), ("tiene recibo", "has receipt", ""), ("sin recibo", "no receipt", ""),  # Encounter 24
                ("dentro del plazo", "within the deadline", ""), ("fuera del plazo", "overdue", ""), ("quiero hablar con la gerente", "want to speak manager", ""),  # Encounter 25
                ("gerente", "manager", ""), ("excepción", "exception", ""), ("aprueban la excepción", "exception approved", ""),  # Encounter 26
                ("caja", "box", ""), ("prenda", "garment", ""), ("monto total", "total amount", ""),  # Encounter 27
                ("pago", "payment", ""), ("inserta la tarjeta", "insert card", ""), ("acerca la tarjeta", "bring the card closer", ""),  # Encounter 28
                ("pasa la tarjeta", "swipe card", ""), ("no pasa", "doesn't happen", ""), ("inténtalo otra vez", "try again", ""),  # Encounter 29
                ("pago aprobado", "payment approved", ""), ("pago rechazado", "payment rejected", ""), ("otra tarjeta", "another card", ""),  # Encounter 30
                ("efectivo", "cash", ""), ("pago en efectivo", "cash payment", ""), ("firma aquí", "sign here", ""),  # Encounter 31
                ("bolsa", "bag", ""), ("¿quiere bolsa?", "Want bag?", ""), ("bolsa grande", "large bag", ""),  # Encounter 32
                ("bolsa pequeña", "small bag", ""), ("sin bolsa", "no bag", ""), ("lo empacan", "pack it", ""),  # Encounter 33
                ("fila larga", "long line", ""), ("mucha gente", "many people", ""), ("espera larga", "long wait", ""),  # Encounter 34
                ("tarda mucho", "takes long", ""), ("servicio lento", "slow service", ""), ("está abierto", "is open", ""),  # Encounter 35
                ("está cerrado", "is closed", ""), ("horario", "schedule", ""), ("identificación", "identification", ""),  # Encounter 36
                ("muestra su identificación", "shows ID", ""), ("alarma", "alarm", ""), ("sensor", "sensor", ""),  # Encounter 37
                ("quitan el sensor", "remove sensor", ""), ("sensor activo", "active sensor", ""), ("la alarma suena", "alarm sounds", ""),  # Encounter 38
                ("revisan la compra", "check the purchase", ""), ("el código escanea", "code scans", ""), ("el código no escanea", "code doesn’t scan", ""),  # Encounter 39
                ("ingreso manual", "manual entry", ""), ("código manual", "manual code", ""), ("problema del sistema", "system problem", ""),  # Encounter 40
                ("ya quedó", "it's done", ""), ("sigue igual", "stays same", ""), ("talla correcta", "correct size", ""),  # Encounter 41
                ("talla incorrecta", "incorrect size", ""), ("se lo traigo", "I'll bring it", ""), ("no le queda bien", "doesn't fit", ""),  # Encounter 42
                ("le queda mejor", "fits better", ""), ("me lo llevo", "I'll take it", ""), ("devolución parcial", "partial refund", ""),  # Encounter 43
                ("monto reembolsado", "refunded amount", ""), ("te lo cambio", "I exchange it for you", ""), ("te hago un descuento", "I give you a discount", ""),  # Encounter 44
                ("caja abierta", "open box", ""), ("caja cerrada", "closed box", ""), ("precio final", "final price", ""),  # Encounter 45
                ("cupón", "coupon", ""), ("el cupón vence hoy", "coupon expires today", ""), ("temporada", "season", ""),  # Encounter 46
                ("colección nueva", "new collection", ""), ("prenda", "garment", ""), ("prenda dañada", "damaged garment", ""),  # Encounter 47
                ("defecto de fábrica", "factory defect", ""), ("marca", "brand", ""), ("misma marca", "same brand", ""),  # Encounter 48
                ("línea premium", "premium line", ""), ("tejido", "fabric", ""), ("fibra natural", "natural fiber", ""),  # Encounter 49
                ("tela", "cloth", ""), ("se encoge", "shrinks", ""), ("destiñe", "fades", ""),  # Encounter 50
            ],
        },
    ],
    "contractor": [
        {
            "title": "Hiring a Contractor",
            "goal": "Manage a construction project, discuss plans, costs, and quality with your contractor",
            "word_prefix": "contr",
            "words": [
                ("contratista", "contractor", ""), ("trabajador", "worker", ""), ("equipo", "equipment", ""),  # Encounter 1
                ("plan de construcción", "construction plan", ""), ("sitio de obra", "construction site", ""), ("obra en curso", "work in progress", ""),  # Encounter 2
                ("plano", "map", ""), ("diseño", "design", ""), ("cotización", "quote", ""),  # Encounter 3
                ("estimado", "dear", ""), ("costo", "cost", ""), ("tarifa", "rate", ""),  # Encounter 4
                ("saldo final", "final balance", ""), ("pago", "payment", ""), ("anticipo", "advance", ""),  # Encounter 5
                ("pago final", "final payment", ""), ("equipo de obra", "work equipment", ""), ("materiales", "materials", ""),  # Encounter 6
                ("proveedor", "provider", ""), ("disponibilidad", "availability", ""), ("no está disponible", "not available", ""),  # Encounter 7
                ("retraso", "delay", ""), ("atraso", "delay", ""), ("va atrasado", "running late", ""),  # Encounter 8
                ("a tiempo", "on time", ""), ("horario", "schedule", ""), ("cumplen el horario", "they meet the schedule", ""),  # Encounter 9
                ("tiempo estimado", "estimated time", ""), ("terminan hoy", "end today", ""), ("empiezan hoy", "start today", ""),  # Encounter 10
                ("siguen trabajando", "still working", ""), ("trabajo detenido", "work stopped", ""), ("revisan esto", "check this", ""),  # Encounter 11
                ("inspección", "inspection", ""), ("ajuste", "adjustment", ""), ("alternativa", "alternative", ""),  # Encounter 12
                ("calidad", "quality", ""), ("misma calidad", "same quality", ""), ("es diferente", "it’s different", ""),  # Encounter 13
                ("mejor opción", "best option", ""), ("es más caro", "it’s more expensive", ""), ("es más barato", "it’s cheaper", ""),  # Encounter 14
                ("costo adicional", "additional cost", ""), ("no estaba incluido", "not included", ""), ("fuera del presupuesto", "over budget", ""),  # Encounter 15
                ("¿cuánto cuesta?", "how much does it cost?", ""), ("¿cuánto tarda?", "how long does it take?", ""), ("¿cuándo terminan?", "when do they finish?", ""),  # Encounter 16
                ("¿cuándo empiezan?", "when do they start?", ""), ("¿por qué hay retraso?", "Why delay?", ""), ("¿qué pasó?", "What happened?", ""),  # Encounter 17
                ("¿puede explicar?", "Can explain?", ""), ("no entiendo", "do not understand", ""), ("necesito más detalle", "need more detail", ""),  # Encounter 18
                ("quiero ver el plano", "want to see plan", ""), ("me envía el plano", "sends me the plan", ""), ("está en proceso", "in process", ""),  # Encounter 19
                ("ya empezaron", "already started", ""), ("ya terminaron", "they already finished", ""), ("falta trabajo", "lack work", ""),  # Encounter 20
                ("está incompleto", "incomplete", ""), ("está mal hecho", "poorly done", ""), ("está bien hecho", "well done", ""),  # Encounter 21
                ("corrigen esto", "they correct this", ""), ("reparan esto", "they repair this", ""), ("rehacen esto", "redo this", ""),  # Encounter 22
                ("ajustan el nivel", "adjust the level", ""), ("superficie", "surface", ""), ("tabique", "partition", ""),  # Encounter 23
                ("piso", "floor", ""), ("techo", "roof", ""), ("pintura", "paint", ""),  # Encounter 24
                ("hay manchas", "there are stains", ""), ("acabado", "finished", ""), ("está nivelado", "leveled", ""),  # Encounter 25
                ("está desnivelado", "uneven", ""), ("hay una grieta", "there is crack", ""), ("humedad", "humidity", ""),  # Encounter 26
                ("hay una fuga", "there is leak", ""), ("cañería", "piping", ""), ("instalación", "installation", ""),  # Encounter 27
                ("sistema eléctrico", "electrical system", ""), ("cable", "cable", ""), ("enchufe", "plug", ""),  # Encounter 28
                ("válvula", "valve", ""), ("agua", "water", ""), ("llave de agua", "water valve", ""),  # Encounter 29
                ("abren la pared", "open the wall", ""), ("cierran la pared", "close wall", ""), ("hay daño", "there is damage", ""),  # Encounter 30
                ("evitan el daño", "prevent damage", ""), ("es urgente", "it’s urgent", ""), ("puede empeorar", "can worsen", ""),  # Encounter 31
                ("apruebo el cambio", "I approve change", ""), ("no autorizo ese cambio", "do not authorize change", ""), ("sin autorización", "unauthorized", ""),  # Encounter 32
                ("avisan antes", "notify before", ""), ("falta comunicación", "lack communication", ""), ("nadie vino", "no one came", ""),  # Encounter 33
                ("no llegaron", "didn't arrive", ""), ("vienen mañana", "come tomorrow", ""), ("vienen hoy", "come today", ""),  # Encounter 34
                ("en la mañana", "in the morning", ""), ("en la tarde", "in the afternoon", ""), ("llegan tarde", "arrive late", ""),  # Encounter 35
                ("cumplen el plazo", "they meet the deadline", ""), ("plazo", "term", ""), ("entrega", "delivery", ""),  # Encounter 36
                ("entrega final", "final delivery", ""), ("inspección final", "final inspection", ""), ("garantía", "warranty", ""),  # Encounter 37
                ("incluye garantía", "includes warranty", ""), ("sin garantía", "no warranty", ""), ("equipo eléctrico", "electrical equipment", ""),  # Encounter 38
                ("maquinaria", "machinery", ""), ("cortan el material", "they cut the material", ""), ("instalan esto", "install this", ""),  # Encounter 39
                ("miden esto", "they measure this", ""), ("nivelan esto", "level this", ""), ("fijan esto", "fix this", ""),  # Encounter 40
                ("desmontan esto", "disassemble this", ""), ("montan esto", "they assemble this", ""), ("limpian el área", "they clean area", ""),  # Encounter 41
                ("retiran los escombros", "remove debris", ""), ("escombros", "debris", ""), ("limpieza final", "final cleaning", ""),  # Encounter 42
                ("área", "Area", ""), ("superficie", "surface", ""), ("acceso", "access", ""),  # Encounter 43
                ("entrada", "entrance", ""), ("salida", "exit", ""), ("permiso de obra", "building permit", ""),  # Encounter 44
                ("vibración", "vibration", ""), ("escombros", "debris", ""), ("seguridad", "security", ""),  # Encounter 45
                ("seguridad", "security", ""), ("protección", "protection", ""), ("equipo de seguridad", "safety equipment", ""),  # Encounter 46
                ("casco", "helmet", ""), ("guantes", "gloves", ""), ("gafas de seguridad", "safety glasses", ""),  # Encounter 47
                ("azulejo", "tile", ""), ("baldosa", "tile", ""), ("madera", "wood", ""),  # Encounter 48
                ("mortero", "mortar", ""), ("yeso", "plaster", ""), ("sellador", "sealer", ""),  # Encounter 49
                ("impermeabilización", "waterproofing", ""), ("permiso", "permission", ""), ("inspector", "inspector", ""),  # Encounter 50
            ],
        },
    ],
    "groceries": [
        {
            "title": "At the Supermarket",
            "goal": "Check out at the supermarket, handle pricing issues, and bag your groceries",
            "word_prefix": "groc",
            "words": [
                ("cajero", "cashier", ""), ("cliente", "customer", ""), ("caja", "box", ""),  # Encounter 1
                ("fila", "line", ""), ("turno", "shift", ""), ("siguiente", "next", ""),  # Encounter 2
                ("productos", "products", ""), ("artículo", "item", ""), ("código de barras", "barcode", ""),  # Encounter 3
                ("escanean el producto", "they scan the product", ""), ("pasan los productos", "scan products", ""), ("total de la compra", "total purchase", ""),  # Encounter 4
                ("precio correcto", "correct price", ""), ("precio incorrecto", "incorrect price", ""), ("oferta", "offer", ""),  # Encounter 5
                ("descuento", "discount", ""), ("promoción", "promotion", ""), ("el descuento aplica", "discount applies", ""),  # Encounter 6
                ("no aplica", "not applicable", ""), ("inventario", "inventory", ""), ("no aparece", "does not appear", ""),  # Encounter 7
                ("revisan el precio", "check the price", ""), ("verifican el precio", "check the price", ""), ("letrero", "sign", ""),  # Encounter 8
                ("carrito de compra", "shopping cart", ""), ("pasarela de cajas", "checkout lane", ""), ("supervisor", "supervisor", ""),  # Encounter 9
                ("llaman al supervisor", "call supervisor", ""), ("corrigen el precio", "they correct the price", ""), ("factura final", "final invoice", ""),  # Encounter 10
                ("monto total", "total amount", ""), ("subtotal", "subtotal", ""), ("cargo adicional", "additional charge", ""),  # Encounter 11
                ("incluye impuesto", "includes tax", ""), ("no incluye impuesto", "no tax included", ""), ("pago", "payment", ""),  # Encounter 12
                ("pago aprobado", "payment approved", ""), ("pago rechazado", "payment rejected", ""), ("tarjeta", "card", ""),  # Encounter 13
                ("tarjeta rechazada", "rejected card", ""), ("inserta la tarjeta", "insert card", ""), ("pasa la tarjeta", "swipe card", ""),  # Encounter 14
                ("acerca la tarjeta", "bring the card closer", ""), ("ingresa el PIN", "enter PIN", ""), ("firma aquí", "sign here", ""),  # Encounter 15
                ("efectivo", "cash", ""), ("pago en efectivo", "cash payment", ""), ("dividir el pago", "split payment", ""),  # Encounter 16
                ("pago dividido", "split payment", ""), ("pago parcial", "partial payment", ""), ("pago completo", "full payment", ""),  # Encounter 17
                ("vuelto", "change (money)", ""), ("le dan cambio", "give change", ""), ("ticket de compra", "purchase ticket", ""),  # Encounter 18
                ("imprimen el recibo", "print receipt", ""), ("bolsa", "bag", ""), ("bolsa grande", "large bag", ""),  # Encounter 19
                ("bolsa pequeña", "small bag", ""), ("sin bolsa", "no bag", ""), ("separan los productos", "separate products", ""),  # Encounter 20
                ("producto frío", "cold product", ""), ("producto congelado", "frozen product", ""), ("producto seco", "dry product", ""),  # Encounter 21
                ("huevos", "eggs", ""), ("frágil", "fragile", ""), ("pesado", "heavy", ""),  # Encounter 22
                ("liviano", "light (weight)", ""), ("porción", "portion", ""), ("una unidad", "one unit", ""),  # Encounter 23
                ("dos unidades", "two units", ""), ("marcan la cantidad", "mark the quantity", ""), ("corrigen la cantidad", "they correct the quantity", ""),  # Encounter 24
                ("quitan el producto", "remove product", ""), ("agregan el producto", "add the product", ""), ("no es mío", "not mine", ""),  # Encounter 25
                ("es incorrecto", "it’s incorrect", ""), ("revisan el producto", "check the product", ""), ("escaneo doble", "double scan", ""),  # Encounter 26
                ("error del sistema", "system error", ""), ("ya quedó", "it's done", ""), ("sigue igual", "stays same", ""),  # Encounter 27
                ("cliente siguiente", "next customer", ""), ("fila larga", "long line", ""), ("mucha gente", "many people", ""),  # Encounter 28
                ("tarda mucho", "takes long", ""), ("fila", "line", ""), ("horario", "schedule", ""),  # Encounter 29
                ("está abierto", "is open", ""), ("está cerrado", "is closed", ""), ("identificación", "identification", ""),  # Encounter 30
                ("muestra su identificación", "shows ID", ""), ("requiere edad mínima", "requires minimum age", ""), ("verifican la edad", "check age", ""),  # Encounter 31
                ("producto restringido", "restricted product", ""), ("aprobado", "approved", ""), ("denegado", "denied", ""),  # Encounter 32
                ("alcohol", "alcohol", ""), ("tabaco", "tobacco", ""), ("bebida", "drink", ""),  # Encounter 33
                ("frutas", "fruits", ""), ("huevos", "eggs", ""), ("pan integral", "whole wheat bread", ""),  # Encounter 34
                ("carne", "meat", ""), ("verduras", "vegetables", ""), ("fruta", "fruit", ""),  # Encounter 35
                ("caja rápida", "express checkout", ""), ("pocos productos", "few products", ""), ("muchos productos", "many products", ""),  # Encounter 36
                ("carrito", "cart", ""), ("canasta", "basket", ""), ("empacan los productos", "pack products", ""),  # Encounter 37
                ("cliente espera", "customer waiting", ""), ("número de caja", "box number", ""), ("caja abierta", "open box", ""),  # Encounter 38
                ("caja cerrada", "closed box", ""), ("cambio exacto", "exact change", ""), ("sin cambio", "no change", ""),  # Encounter 39
                ("pago exacto", "exact payment", ""), ("tarjeta válida", "valid card", ""), ("tarjeta inválida", "invalid card", ""),  # Encounter 40
                ("saldo insuficiente", "insufficient balance", ""), ("hay fondos", "there are funds", ""), ("no hay fondos", "no funds", ""),  # Encounter 41
                ("listo para pagar", "ready to pay", ""), ("ingresa el código", "enter code", ""), ("código manual", "manual code", ""),  # Encounter 42
                ("ingreso manual", "manual entry", ""), ("producto sin código", "product without code", ""), ("pesa el producto", "weighs product", ""),  # Encounter 43
                ("balanza", "scale", ""), ("etiqueta de precio", "price tag", ""), ("no coincide", "does not match", ""),  # Encounter 44
                ("revise la etiqueta", "check the label", ""), ("actualizan el precio", "update the price", ""), ("precio actualizado", "updated price", ""),  # Encounter 45
                ("inténtalo otra vez", "try again", ""), ("caja central", "central box", ""), ("lector", "reader", ""),  # Encounter 46
                ("el lector da error", "reader error", ""), ("promoción vencida", "expired promotion", ""), ("vence hoy", "expires today", ""),  # Encounter 47
                ("unidad equivocada", "wrong unit", ""), ("precio por kilo", "price per kilo", ""), ("precio por unidad", "price per unit", ""),  # Encounter 48
                ("pesa menos", "weighs less", ""), ("pesa más", "weighs more", ""), ("producto abierto", "opened product", ""),  # Encounter 49
                ("producto dañado", "damaged product", ""), ("reemplazo", "replacement", ""), ("devolución al método de pago", "refund to payment", ""),  # Encounter 50
            ],
        },
    ],
    "mechanic": [
        {
            "title": "At the Mechanic",
            "goal": "Describe car problems, get a diagnosis, and handle repairs and payment",
            "word_prefix": "mech",
            "words": [
                ("automóvil", "car", ""), ("vehículo", "vehicle", ""), ("motorista", "motorcyclist", ""),  # Encounter 1
                ("batería", "battery", ""), ("frenos", "brakes", ""), ("cambio de aceite", "oil change", ""),  # Encounter 2
                ("filtro", "filter", ""), ("transmisión", "transmission", ""), ("suspensión", "suspension", ""),  # Encounter 3
                ("faro", "headlight", ""), ("amortiguador", "shock absorber", ""), ("radiador", "radiator", ""),  # Encounter 4
                ("bujía", "spark plug", ""), ("correa", "strap", ""), ("alternador", "alternator", ""),  # Encounter 5
                ("falla", "failure", ""), ("golpeteo", "knocking", ""), ("vibración", "vibration", ""),  # Encounter 6
                ("fuga", "leak", ""), ("no arranca", "does not start", ""), ("no enciende", "does not turn on", ""),  # Encounter 7
                ("se apaga", "turns off", ""), ("huele raro", "smells strange", ""), ("se sobrecalienta", "overheats", ""),  # Encounter 8
                ("tiene poca potencia", "low power", ""), ("consume aceite", "consumes oil", ""), ("pierde líquido", "leaks liquid", ""),  # Encounter 9
                ("frenos débiles", "weak brakes", ""), ("pedal suave", "soft pedal", ""), ("revisan el carro", "check the car", ""),  # Encounter 10
                ("inspección", "inspection", ""), ("evaluación", "evaluation", ""), ("reparan", "repair", ""),  # Encounter 11
                ("lo arreglan", "fix it", ""), ("cambian la pieza", "change part", ""), ("ajustan", "adjust", ""),  # Encounter 12
                ("instalan", "they install", ""), ("limpian", "they clean", ""), ("lo prueban", "test it", ""),  # Encounter 13
                ("revisan el motor", "check the engine", ""), ("cambio de aceite", "oil change", ""), ("cambian el filtro", "change filter", ""),  # Encounter 14
                ("revisan los frenos", "check the brakes", ""), ("alinean las llantas", "align the tires", ""), ("¿qué problema tiene?", "What problem?", ""),  # Encounter 15
                ("¿qué pasa?", "What’s wrong?", ""), ("¿desde cuándo?", "Since when?", ""), ("¿cuándo empezó?", "when did it start?", ""),  # Encounter 16
                ("¿hace ruido?", "Makes noise?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""), ("¿cuánto tarda?", "how long does it take?", ""),  # Encounter 17
                ("¿es grave?", "Is serious?", ""), ("¿puede empeorar?", "Can worsen?", ""), ("¿puede revisarlo?", "Can check it?", ""),  # Encounter 18
                ("tarifa", "rate", ""), ("costo", "cost", ""), ("importe", "amount", ""),  # Encounter 19
                ("estimado", "dear", ""), ("mano de obra", "labor", ""), ("piezas", "parts", ""),  # Encounter 20
                ("adicional", "additional", ""), ("incluye", "includes", ""), ("no incluye", "does not include", ""),  # Encounter 21
                ("presupuesto", "budget", ""), ("pago", "payment", ""), ("en efectivo", "in cash", ""),  # Encounter 22
                ("con tarjeta", "by card", ""), ("garantía", "warranty", ""), ("recibo", "receipt", ""),  # Encounter 23
                ("desgastado", "worn out", ""), ("dañado", "damaged", ""), ("roto", "broken", ""),  # Encounter 24
                ("sucio", "dirty", ""), ("flojo", "loose", ""), ("apretado", "tight", ""),  # Encounter 25
                ("en buen estado", "in good condition", ""), ("en mal estado", "in bad condition", ""), ("urgente", "urgent", ""),  # Encounter 26
                ("peligroso", "dangerous", ""), ("sistema de frenos", "brake system", ""), ("sistema eléctrico", "electrical system", ""),  # Encounter 27
                ("presión", "pressure", ""), ("medidor", "meter", ""), ("nivel de aceite", "oil level", ""),  # Encounter 28
                ("nivel bajo", "low level", ""), ("nivel alto", "high level", ""), ("luz de motor", "engine light", ""),  # Encounter 29
                ("código de error", "error code", ""), ("dejo el carro", "I leave the car", ""), ("recojo el carro", "get the cart", ""),  # Encounter 30
                ("listo", "ready", ""), ("todavía no", "not yet", ""), ("en proceso", "in process", ""),  # Encounter 31
                ("espero", "I hope", ""), ("más tarde", "later", ""), ("hoy", "today", ""),  # Encounter 32
                ("pieza de repuesto", "spare part", ""), ("tiempo estimado", "estimated time", ""), ("muy caro", "very expensive", ""),  # Encounter 33
                ("más barato", "cheaper", ""), ("solo eso", "only that", ""), ("no lo necesito", "don't need it", ""),  # Encounter 34
                ("prefiero eso primero", "I prefer that first", ""), ("después vemos", "see later", ""), ("no autorizo ese trabajo", "do not authorize work", ""),  # Encounter 35
                ("sin autorización", "unauthorized", ""), ("quiero más detalle", "want more detail", ""), ("líquido de frenos", "brake fluid", ""),  # Encounter 36
                ("aceite de motor", "motor oil", ""), ("refrigerante", "coolant", ""), ("líquido", "liquid", ""),  # Encounter 37
                ("combustible", "fuel", ""), ("etanol", "ethanol", ""), ("diésel", "diesel", ""),  # Encounter 38
                ("tanque", "tank", ""), ("bomba de aire", "air pump", ""), ("válvula", "valve", ""),  # Encounter 39
                ("al frenar", "when braking", ""), ("al arrancar", "when starting", ""), ("en movimiento", "in motion", ""),  # Encounter 40
                ("en frío", "cold", ""), ("en caliente", "hot", ""), ("a alta velocidad", "high speed", ""),  # Encounter 41
                ("a baja velocidad", "low speed", ""), ("en curva", "on a curve", ""), ("en subida", "going up", ""),  # Encounter 42
                ("en bajada", "downhill", ""), ("mecánica", "mechanics", ""), ("garaje", "garage", ""),  # Encounter 43
                ("herramienta manual", "hand tool", ""), ("elevador", "elevator", ""), ("garantía", "warranty", ""),  # Encounter 44
                ("servicio técnico", "technical service", ""), ("revisión general", "general inspection", ""), ("mantenimiento", "maintenance", ""),  # Encounter 45
                ("historial", "history", ""), ("diagnóstico completo", "full diagnosis", ""), ("no entiendo", "do not understand", ""),  # Encounter 46
                ("¿puede repetir?", "Can repeat?", ""), ("más despacio", "slower", ""), ("¿qué significa?", "What means?", ""),  # Encounter 47
                ("pastillas de freno", "brake pads", ""), ("disco de freno", "brake disc", ""), ("amortiguador", "shock absorber", ""),  # Encounter 48
                ("dirección", "address", ""), ("alineación", "alignment", ""), ("balanceo", "swaying", ""),  # Encounter 49
                ("embrague", "clutch", ""), ("escape", "escape", ""), ("filtro de aire", "air filter", ""),  # Encounter 50
            ],
        },
    ],
    "police": [
        {
            "title": "Traffic Stop",
            "goal": "Handle a traffic stop calmly by providing documents and following instructions",
            "word_prefix": "pol",
            "words": [
                ("policía", "police", ""), ("agente", "agent", ""), ("patrulla", "patrol", ""),  # Encounter 1
                ("control policial", "police control", ""), ("licencia de conducir", "driver's license", ""), ("registro del vehículo", "vehicle registration", ""),  # Encounter 2
                ("prueba de seguro", "insurance proof", ""), ("documentos", "documents", ""), ("identificación", "identification", ""),  # Encounter 3
                ("¿licencia, por favor?", "License, please?", ""), ("¿tiene el registro?", "Do you have the registration?", ""), ("¿tiene seguro?", "Do you have insurance?", ""),  # Encounter 4
                ("¿puede mostrarlo?", "Can show it?", ""), ("aquí tiene", "here you go", ""), ("está en el vehículo", "in the vehicle", ""),  # Encounter 5
                ("está en la guantera", "in glovebox", ""), ("lo detuve", "I stopped", ""), ("parada", "stop", ""),  # Encounter 6
                ("¿sabe por qué lo detuve?", "Do you know why I stopped him?", ""), ("exceso de velocidad", "speeding", ""), ("velocidad máxima", "maximum speed", ""),  # Encounter 7
                ("límite de velocidad", "speed limit", ""), ("zona", "zone", ""), ("en esta zona", "in this area", ""),  # Encounter 8
                ("iba a", "was going to", ""), ("por encima de", "above", ""), ("infracción", "infraction", ""),  # Encounter 9
                ("motivo", "reason", ""), ("vehículo", "vehicle", ""), ("automóvil", "car", ""),  # Encounter 10
                ("luces", "lights", ""), ("luz trasera", "rear light", ""), ("luz delantera", "front light", ""),  # Encounter 11
                ("no funciona", "does not work", ""), ("placa", "plate", ""), ("luz trasera", "rear light", ""),  # Encounter 12
                ("cinturón", "belt", ""), ("sin cinturón", "no seatbelt", ""), ("en regla", "in order", ""),  # Encounter 13
                ("apague el motor", "turn off engine", ""), ("baje la ventana", "roll down window", ""), ("salga del vehículo", "get out", ""),  # Encounter 14
                ("quédese en el vehículo", "stay in vehicle", ""), ("espere aquí", "wait here", ""), ("despacio", "slowly", ""),  # Encounter 15
                ("con calma", "calmly", ""), ("siga mis instrucciones", "follow instructions", ""), ("no se mueva", "don't move", ""),  # Encounter 16
                ("frenó fuerte", "braked hard", ""), ("cambió de carril", "lane change", ""), ("sin señalizar", "unmarked", ""),  # Encounter 17
                ("conducción peligrosa", "dangerous driving", ""), ("carril", "lane", ""), ("carril restringido", "restricted lane", ""),  # Encounter 18
                ("giro", "turn", ""), ("no señalizó", "didn't signal", ""), ("tráfico", "traffic", ""),  # Encounter 19
                ("intersección", "intersection", ""), ("señal de tránsito", "traffic sign", ""), ("luz roja", "red light", ""),  # Encounter 20
                ("luz verde", "green light", ""), ("¿de dónde viene?", "Where from?", ""), ("¿a dónde va?", "where are you going?", ""),  # Encounter 21
                ("¿cuánto tiempo lleva manejando?", "How long driving?", ""), ("¿es su vehículo?", "Is your vehicle?", ""), ("¿es un vehículo de alquiler?", "Is rental vehicle?", ""),  # Encounter 22
                ("¿tiene el contrato?", "Do you have the contract?", ""), ("¿ha consumido alcohol?", "Consumed alcohol?", ""), ("¿ha tomado algo?", "Had anything?", ""),  # Encounter 23
                ("¿entiende?", "Understand?", ""), ("¿puede explicar?", "Can explain?", ""), ("alcohol", "alcohol", ""),  # Encounter 24
                ("análisis", "analysis", ""), ("prueba de alcohol", "alcohol test", ""), ("sople aquí", "blow here", ""),  # Encounter 25
                ("resultado", "result", ""), ("negativo", "negative", ""), ("positivo", "positive", ""),  # Encounter 26
                ("bajo la influencia", "under influence", ""), ("sobrio", "sober", ""), ("verifican el sistema", "check the system", ""),  # Encounter 27
                ("registro activo", "active registration", ""), ("seguro activo", "active insurance", ""), ("no aparece", "does not appear", ""),  # Encounter 28
                ("pendiente", "pending", ""), ("infracción", "infraction", ""), ("advertencia", "warning", ""),  # Encounter 29
                ("sanción", "penalty", ""), ("emiten la multa", "issue fine", ""), ("dan una advertencia", "they give a warning", ""),  # Encounter 30
                ("paga la multa", "pays fine", ""), ("en línea", "online", ""), ("plazo", "term", ""),  # Encounter 31
                ("monto", "amount", ""), ("carretera", "highway", ""), ("intersección", "intersection", ""),  # Encounter 32
                ("zona urbana", "urban area", ""), ("zona escolar", "school zone", ""), ("zona residencial", "residential area", ""),  # Encounter 33
                ("cartel", "sign", ""), ("señal de tránsito", "traffic sign", ""), ("dirección", "address", ""),  # Encounter 34
                ("carril derecho", "right lane", ""), ("alquiler", "rent", ""), ("licencia de conducir", "driver's license", ""),  # Encounter 35
                ("propietario", "owner", ""), ("está a su nombre", "in your name", ""), ("no es mío", "not mine", ""),  # Encounter 36
                ("vehículo prestado", "borrowed vehicle", ""), ("permiso del dueño", "owner's permission", ""), ("no lo encuentro", "can't find it", ""),  # Encounter 37
                ("no lo tengo", "don't have it", ""), ("no carga", "does not load", ""), ("sin señal", "no signal", ""),  # Encounter 38
                ("en el celular", "on the phone", ""), ("copia digital", "digital copy", ""), ("sin documento", "no document", ""),  # Encounter 39
                ("vencido", "expired", ""), ("por vencer", "about to expire", ""), ("no es válido", "not valid", ""),  # Encounter 40
                ("no entiendo", "do not understand", ""), ("¿puede repetir?", "Can repeat?", ""), ("más despacio", "slower", ""),  # Encounter 41
                ("¿qué significa?", "What means?", ""), ("¿es una multa?", "Is fine?", ""), ("¿es una advertencia?", "Is warning?", ""),  # Encounter 42
                ("¿puedo irme?", "Can I leave?", ""), ("¿puedo seguir?", "Can I continue?", ""), ("inspección", "inspection", ""),  # Encounter 43
                ("oríllese", "pull over", ""), ("arcén", "shoulder (road)", ""), ("luces de emergencia", "emergency lights", ""),  # Encounter 44
                ("documento físico", "physical document", ""), ("permiso de conducir", "driver's license", ""), ("matrícula", "registration", ""),  # Encounter 45
                ("agente de tránsito", "traffic agent", ""), ("triángulo", "triangle", ""), ("chaleco reflectante", "reflective vest", ""),  # Encounter 46
                ("accidente", "accident", ""), ("colisión", "collision", ""), ("reporte", "report", ""),  # Encounter 47
                ("reporte policial", "police report", ""), ("testimonio", "testimony", ""), ("declaración", "statement", ""),  # Encounter 48
                ("firme aquí", "sign here", ""), ("corte", "cut", ""), ("fecha de corte", "cutoff date", ""),  # Encounter 49
                ("comparecencia", "appearance", ""), ("multas", "fines", ""), ("remolque", "trailer", ""),  # Encounter 50
            ],
        },
    ],
    "restaurant": [
        {
            "title": "Eating Out",
            "goal": "Order food, interact with the server, and pay for your meal",
            "word_prefix": "rest",
            "words": [
                ("menú", "menu", ""), ("plato del día", "daily special", ""), ("mesero", "waiter", ""),  # Encounter 1
                ("menú", "menu", ""), ("reserva", "reservation", ""), ("¿tienen reserva?", "Do you have a reservation?", ""),  # Encounter 2
                ("mesa para dos", "table for two", ""), ("pido", "I order", ""), ("¿qué desea?", "What want?", ""),  # Encounter 3
                ("¿qué van a pedir?", "What will you order?", ""), ("tomo la orden", "takes order", ""), ("aquí está el menú", "here is menu", ""),  # Encounter 4
                ("recomendación", "recommendation", ""), ("¿qué recomienda?", "What recommend?", ""), ("especialidad", "specialty", ""),  # Encounter 5
                ("entrada", "entrance", ""), ("plato principal", "main course", ""), ("bebida", "drink", ""),  # Encounter 6
                ("acompañamiento", "accompaniment", ""), ("guarnición", "garnish", ""), ("porción", "portion", ""),  # Encounter 7
                ("ingrediente", "ingredient", ""), ("salsa", "sauce", ""), ("plato principal", "main course", ""),  # Encounter 8
                ("mariscos", "seafood", ""), ("carne", "meat", ""), ("pescado", "fish", ""),  # Encounter 9
                ("verduras", "vegetables", ""), ("plato vegetariano", "vegetarian dish", ""), ("vegetariano", "vegetarian", ""),  # Encounter 10
                ("vegano", "vegan", ""), ("alergia", "allergy", ""), ("alérgico", "allergic", ""),  # Encounter 11
                ("frutos secos", "nuts", ""), ("sin gluten", "gluten-free", ""), ("con azúcar", "with sugar", ""),  # Encounter 12
                ("¿tiene…?", "Do you have...?", ""), ("¿lleva…?", "Carry...?", ""), ("sin picante", "no spice", ""),  # Encounter 13
                ("picante", "spicy", ""), ("poco picante", "mildly spicy", ""), ("sin carne", "no meat", ""),  # Encounter 14
                ("sin gluten", "gluten-free", ""), ("¿se puede cambiar?", "Can it be changed?", ""), ("bebida", "drink", ""),  # Encounter 15
                ("refresco", "soda", ""), ("con gas", "sparkling", ""), ("sin gas", "no gas", ""),  # Encounter 16
                ("refresco", "soda", ""), ("jugo", "juice", ""), ("cerveza", "beer", ""),  # Encounter 17
                ("vino", "wine", ""), ("copa", "glass", ""), ("menú", "menu", ""),  # Encounter 18
                ("¿algo de tomar?", "something to drink?", ""), ("tiempo de espera", "wait time", ""), ("¿cuánto tiempo tarda?", "How long takes?", ""),  # Encounter 19
                ("regreso enseguida", "back soon", ""), ("aquí está", "here it is", ""), ("quedan platos", "dishes left", ""),  # Encounter 20
                ("no llegó", "didn't arrive", ""), ("pedimos la comida", "we order food", ""), ("trae", "brings", ""),  # Encounter 21
                ("lleva", "carries", ""), ("sirve", "serves", ""), ("mesa lista", "table ready", ""),  # Encounter 22
                ("síganme", "follow me", ""), ("error", "error", ""), ("equivocado", "wrong", ""),  # Encounter 23
                ("no es esto", "not this", ""), ("no pedimos eso", "we didn't order that", ""), ("falta esto", "missing this", ""),  # Encounter 24
                ("propina", "tip", ""), ("cambian el plato", "change plate", ""), ("menú del día", "daily menu", ""),  # Encounter 25
                ("preparan otro plato", "they prepare another dish", ""), ("tardó mucho", "took long", ""), ("frío", "cold", ""),  # Encounter 26
                ("caliente", "hot", ""), ("recalentado", "overheated", ""), ("¿qué es esto?", "What is this?", ""),  # Encounter 27
                ("¿qué lleva?", "What carry?", ""), ("¿cómo es?", "What is it like?", ""), ("¿está listo?", "Is ready?", ""),  # Encounter 28
                ("¿falta mucho?", "Much left?", ""), ("¿puede explicar?", "Can explain?", ""), ("no entiendo", "do not understand", ""),  # Encounter 29
                ("repítalo", "repeat it", ""), ("más despacio", "slower", ""), ("aclárelo", "clarify it", ""),  # Encounter 30
                ("cuenta", "bill", ""), ("la cuenta", "the bill", ""), ("propina", "tip", ""),  # Encounter 31
                ("menú", "menu", ""), ("incluye", "includes", ""), ("no incluye", "does not include", ""),  # Encounter 32
                ("propina", "tip", ""), ("menú del día", "daily menu", ""), ("dividimos la cuenta", "split the bill", ""),  # Encounter 33
                ("pago", "payment", ""), ("con tarjeta", "by card", ""), ("en efectivo", "in cash", ""),  # Encounter 34
                ("terminal", "terminal", ""), ("no funciona", "does not work", ""), ("menú", "menu", ""),  # Encounter 35
                ("mesa libre", "free table", ""), ("ocupado", "busy", ""), ("reservado", "reserved", ""),  # Encounter 36
                ("afuera", "outside", ""), ("adentro", "inside", ""), ("terraza", "terrace", ""),  # Encounter 37
                ("aire acondicionado", "air conditioning", ""), ("ambiente agradable", "pleasant environment", ""), ("tranquilo", "calm", ""),  # Encounter 38
                ("ambiente", "environment", ""), ("para dos", "for two", ""), ("reserva", "reservation", ""),  # Encounter 39
                ("menos cantidad", "less quantity", ""), ("suficiente", "enough", ""), ("extra", "extra", ""),  # Encounter 40
                ("otra porción", "another portion", ""), ("lo mismo", "the same", ""), ("para llevar", "to go", ""),  # Encounter 41
                ("pedido", "order", ""), ("factura", "invoice", ""), ("reserva confirmada", "confirmed reservation", ""),  # Encounter 42
                ("mesa asignada", "assigned table", ""), ("lista de espera", "waiting list", ""), ("disponibilidad", "availability", ""),  # Encounter 43
                ("horario", "schedule", ""), ("cubiertos", "cutlery", ""), ("servilleta", "napkin", ""),  # Encounter 44
                ("tenedor", "fork", ""), ("cuchillo", "knife", ""), ("servilleta", "napkin", ""),  # Encounter 45
                ("copa", "glass", ""), ("taza", "cup", ""), ("servilleta", "napkin", ""),  # Encounter 46
                ("sin hielo", "no ice", ""), ("otra ronda", "another round", ""), ("traen la cuenta", "bring bill", ""),  # Encounter 47
                ("cobro adicional", "additional charge", ""), ("cargo por servicio", "service charge", ""), ("plato hondo", "soup plate", ""),  # Encounter 48
                ("plato llano", "flat plate", ""), ("cubierto extra", "extra cover", ""), ("para compartir", "to share", ""),  # Encounter 49
                ("recogen los platos", "clear dishes", ""), ("mesa sucia", "dirty table", ""), ("mesa limpia", "clean table", ""),  # Encounter 50
            ],
        },
    ],
    "small_talk": [
        {
            "title": "Meeting a Neighbor",
            "goal": "Have a friendly conversation with your neighbor about building life",
            "word_prefix": "talk",
            "words": [
                ("residente", "resident", ""), ("vecina", "neighbor (female)", ""), ("portal", "doorway", ""),  # Encounter 1
                ("departamento", "department", ""), ("vivienda", "housing", ""), ("zona", "zone", ""),  # Encounter 2
                ("barrio", "neighborhood", ""), ("vecindario", "neighborhood", ""), ("parque cercano", "nearby park", ""),  # Encounter 3
                ("volumen", "volume", ""), ("baja el volumen", "lower volume", ""), ("reunión", "meeting", ""),  # Encounter 4
                ("fiesta", "party", ""), ("anoche", "last night", ""), ("tarde", "late", ""),  # Encounter 5
                ("temprano", "early", ""), ("trabajo temprano", "early work", ""), ("no pude dormir", "couldn't sleep", ""),  # Encounter 6
                ("quería comentarte algo", "wanted to tell you", ""), ("solo quería avisarte", "just wanted to tell you", ""), ("la próxima vez", "next time", ""),  # Encounter 7
                ("tenga cuidado", "be careful", ""), ("estacionamiento", "parking", ""), ("plaza de aparcamiento", "parking space", ""),  # Encounter 8
                ("plaza", "square", ""), ("mi lugar", "my place", ""), ("asignado", "assigned", ""),  # Encounter 9
                ("visitante", "visitor", ""), ("mueve el carro", "moves car", ""), ("lo muevo ahora mismo", "move now", ""),  # Encounter 10
                ("ya pasó dos veces", "it already happened twice", ""), ("no sabía", "didn't know", ""), ("no fue intencional", "not intentional", ""),  # Encounter 11
                ("paquete postal", "postal package", ""), ("entrega", "delivery", ""), ("repartidor", "delivery person", ""),  # Encounter 12
                ("puerta", "door", ""), ("lo dejó aquí por error", "left here", ""), ("nombre", "name", ""),  # Encounter 13
                ("mi nombre", "my name", ""), ("aquí está su paquete", "here is package", ""), ("lo tengo", "I have it", ""),  # Encounter 14
                ("se perdió", "lost", ""), ("pasa seguido", "comes often", ""), ("hace tiempo", "long ago", ""),  # Encounter 15
                ("hace meses", "months ago", ""), ("hace un año", "one year ago", ""), ("vivo aquí", "I live here", ""),  # Encounter 16
                ("me mudé", "I moved", ""), ("¿te gusta vivir aquí?", "Do you like living here?", ""), ("me gusta", "I like", ""),  # Encounter 17
                ("es tranquilo", "it’s quiet", ""), ("es ruidoso", "it’s noisy", ""), ("es seguro", "it’s safe", ""),  # Encounter 18
                ("fuga", "leak", ""), ("humedad", "humidity", ""), ("pared del baño", "bathroom wall", ""),  # Encounter 19
                ("fuga de agua", "water leak", ""), ("problema de agua", "water problem", ""), ("administración", "administration", ""),  # Encounter 20
                ("ya llamé", "I already called", ""), ("no han venido", "have not come", ""), ("mejor así", "better this way", ""),  # Encounter 21
                ("más urgente", "more urgent", ""), ("cierra la llave de agua", "turn off water", ""), ("llave de agua", "water valve", ""),  # Encounter 22
                ("puede empeorar", "can worsen", ""), ("avísame", "notify me", ""), ("me dices", "you tell me", ""),  # Encounter 23
                ("entiendo", "I understand", ""), ("tiene sentido", "makes sense", ""), ("vecino cercano", "close neighbor", ""),  # Encounter 24
                ("lejos", "far", ""), ("planta", "plant", ""), ("mismo piso", "same floor", ""),  # Encounter 25
                ("arriba", "up", ""), ("abajo", "down", ""), ("toca la puerta", "knocks door", ""),  # Encounter 26
                ("abre", "opens", ""), ("cierra", "saw", ""), ("puerta principal", "main door", ""),  # Encounter 27
                ("horario", "schedule", ""), ("ocupado", "busy", ""), ("disponible", "available", ""),  # Encounter 28
                ("fin de semana", "weekend", ""), ("tarde", "late", ""), ("mañana por la mañana", "tomorrow morning", ""),  # Encounter 29
                ("ayer", "yesterday", ""), ("en un rato", "in a while", ""), ("prestas una herramienta", "you lend a tool", ""),  # Encounter 30
                ("destornillador", "screwdriver", ""), ("llave inglesa", "wrench", ""), ("taladro", "drill", ""),  # Encounter 31
                ("recoger la basura", "pick up trash", ""), ("basura", "trash", ""), ("saco la basura", "take out trash", ""),  # Encounter 32
                ("reciclaje", "recycling", ""), ("portal", "doorway", ""), ("timbre", "doorbell", ""),  # Encounter 33
                ("puerta del garaje", "garage door", ""), ("entrada principal", "main entrance", ""), ("intercomunicador", "intercom", ""),  # Encounter 34
                ("copia de llave", "key copy", ""), ("administración del edificio", "building management", ""), ("portero", "doorman", ""),  # Encounter 35
                ("conserje", "concierge", ""), ("paquete equivocado", "wrong package", ""), ("se confundieron de puerta", "wrong door", ""),  # Encounter 36
                ("visita", "visit", ""), ("visitas", "visits", ""), ("¿espera visitas?", "Expecting visitors?", ""),  # Encounter 37
                ("mudanza", "move", ""), ("camión de mudanza", "moving truck", ""), ("se mudan hoy", "moving today", ""),  # Encounter 38
                ("mascota", "pet", ""), ("conejo", "rabbit", ""), ("gato", "cat", ""),  # Encounter 39
                ("correa", "strap", ""), ("ladra mucho", "barks a lot", ""), ("¿cómo se llama?", "What is name?", ""),  # Encounter 40
                ("terraza", "terrace", ""), ("plantas", "plants", ""), ("riego", "watering", ""),  # Encounter 41
                ("riega las plantas", "water the plants", ""), ("balcón", "balcony", ""), ("puerta del apartamento", "apartment door", ""),  # Encounter 42
                ("corriente de aire", "draft", ""), ("hace frío aquí", "it’s cold here", ""), ("hace calor aquí", "it’s hot here", ""),  # Encounter 43
                ("humedad en el techo", "ceiling humidity", ""), ("corte de agua", "water cut", ""), ("corte de luz", "power outage", ""),  # Encounter 44
                ("luz apagada", "light off", ""), ("se fue la luz", "power outage", ""), ("vuelve pronto", "come back soon", ""),  # Encounter 45
                ("vecino nuevo", "new neighbor", ""), ("recién llegado", "newly arrived", ""), ("¿desde cuándo vive aquí?", "Since when lives here?", ""),  # Encounter 46
                ("alquiler", "rent", ""), ("subió el alquiler", "rent increased", ""), ("administración no responde", "management does not respond", ""),  # Encounter 47
                ("queja", "complaint", ""), ("pongo una queja", "I complain", ""), ("ruido arriba", "noise upstairs", ""),  # Encounter 48
                ("ruido abajo", "noise downstairs", ""), ("paso lateral", "side step", ""), ("entrada trasera", "back entrance", ""),  # Encounter 49
                ("puerta principal", "main door", ""), ("interfono", "intercom", ""), ("correo", "mail", ""),  # Encounter 50
            ],
        },
    ],
    "internet": [
        {
            "title": "Setting Up WiFi",
            "goal": "Set up your internet service by speaking with the technician",
            "word_prefix": "inet",
            "words": [
                ("internet", "internet", "internet"), ("wifi", "WiFi", "wifi"), ("red inalámbrica", "wireless network", "xarxa sense fils"),  # Encounter 1
                ("wifi doméstico", "home WiFi", "wifi domèstic"), ("clave de acceso", "access code", "clau d'accés"), ("red local", "local network", "xarxa local"),  # Encounter 2
                ("router", "router", "router"), ("cable", "cable", "cable"), ("intensidad", "signal strength", "intensitat"),  # Encounter 3
                ("enrutador", "router", "enrutador"), ("cable de red", "network cable", "cable de xarxa"), ("tomacorriente", "outlet", "endoll"),  # Encounter 4
                ("plan", "plan", "pla"), ("pausado", "slow", "pausat"), ("rapidez", "speed", "rapidesa"),  # Encounter 5
                ("paquete de datos", "data plan", "paquet de dades"), ("cuota mensual", "monthly fee", "quota mensual"), ("visita", "visit", "visita"),  # Encounter 6
                ("nombre de red", "network name", "nom de xarxa"), ("colocar", "to install", "col·locar"), ("configurar", "to configure", "configurar"),  # Encounter 7
                ("conectar", "to connect", "connectar"), ("desconectar", "to disconnect", "desconnectar"), ("reiniciar", "to restart", "reiniciar"),  # Encounter 8
                ("especialista", "specialist", "especialista"), ("cita de servicio", "service appointment", "cita de servei"), ("SSID", "SSID", "SSID"),  # Encounter 9
                ("funcionar", "to work/function", "funcionar"), ("renombrar", "to rename", "renombrar"), ("solución", "solution", "solució"),  # Encounter 10
                ("banda ancha", "broadband", "banda ampla"), ("fibra óptica", "fiber optic", "fibra òptica"), ("megabits", "megabits", "megabits"),  # Encounter 11
                ("descargar", "to download", "descarregar"), ("ajustar", "to adjust", "ajustar"), ("enlazar", "to connect", "enllaçar"),  # Encounter 12
                ("cortar enlace", "to disconnect", "tallar enllaç"), ("rearrancar", "to restart", "rearrencar"), ("aparato", "device", "aparell"),  # Encounter 13
                ("portátil", "laptop", "portàtil"), ("teléfono móvil", "mobile phone", "telèfon mòbil"), ("operar", "to work/operate", "operar"),  # Encounter 14
                ("modem", "modem", "mòdem"), ("antena", "antenna", "antena"), ("inconveniente", "issue", "inconvenient"),  # Encounter 15
                ("conexión de alta velocidad", "high-speed connection", "connexió d'alta velocitat"), ("cable óptico", "fiber optic cable", "cable òptic"), ("alcance", "range", "abast"),  # Encounter 16
                ("corte", "outage", "cort"), ("interrupción", "interruption", "interrupció"), ("megabytes", "megabytes", "megabytes"),  # Encounter 17
                ("bajar archivos", "to download files", "baixar arxius"), ("permanencia", "commitment period", "permanència"), ("cargar archivos", "to upload files", "carregar arxius"),  # Encounter 18
                ("fecha de pago", "payment date", "data de pagament"), ("mejorar", "to improve", "millorar"), ("soporte al cliente", "customer support", "suport al client"),  # Encounter 19
                ("televisión", "television", "televisió"), ("comunicarse", "to communicate", "comunicar-se"), ("combo", "bundle", "combo"),  # Encounter 20
                ("streaming", "streaming", "streaming"), ("videollamada", "video call", "videotrucada"), ("juego en línea", "online gaming", "joc en línia"),  # Encounter 21
                ("módem", "modem", "mòdem"), ("ilimitado", "unlimited", "il·limitat"), ("antena receptora", "receiving antenna", "antena receptora"),  # Encounter 22
                ("decodificador", "decoder", "decodificador"), ("firewall", "firewall", "firewall"), ("área de cobertura", "coverage area", "àrea de cobertura"),  # Encounter 23
                ("virus", "virus", "virus"), ("malware", "malware", "malware"), ("antivirus", "antivirus", "antivirus"),  # Encounter 24
                ("extensión", "extension/extender", "extensió"), ("repetidor", "repeater", "repetidor"), ("amplificar", "to amplify", "amplificar"),  # Encounter 25
                ("dirección IP", "IP address", "adreça IP"), ("DNS", "DNS", "DNS"), ("puerto", "port", "port"),  # Encounter 26
                ("ethernet", "ethernet", "ethernet"), ("inalámbrico", "wireless", "inalàmbric"), ("bluetooth", "bluetooth", "bluetooth"),  # Encounter 27
                ("latencia", "latency", "latència"), ("ping", "ping", "ping"), ("estabilidad", "stability", "estabilitat"),  # Encounter 28
                ("asistencia técnica", "technical support", "assistència tècnica"), ("soporte", "support", "suport"), ("extensión de señal", "signal range", "extensió de senyal"),  # Encounter 29
                ("apagón", "outage", "apagada"), ("navegador", "browser", "navegador"), ("página web", "webpage", "pàgina web"),  # Encounter 30
                ("usuario", "username", "usuari"), ("falla", "failure", "fallada"), ("registrar", "to register", "registrar"),  # Encounter 31
                ("restablecer", "to restore", "restablir"), ("acuerdo de servicio", "service agreement", "acord de servei"), ("periodo de permanencia", "commitment period", "període de permanència"),  # Encounter 32
                ("control parental", "parental controls", "control parental"), ("dar de baja", "to cancel", "donar de baixa"), ("renovar plan", "to upgrade plan", "renovar pla"),  # Encounter 33
                ("cámara", "camera", "càmera"), ("monitor", "monitor", "monitor"), ("vigilancia", "surveillance", "vigilància"),  # Encounter 34
                ("domótica", "home automation", "domòtica"), ("inteligente", "smart", "intel·ligent"), ("automatizar", "to automate", "automatitzar"),  # Encounter 35
                ("optimizar", "to improve", "optimitzar"), ("almacenar", "to store", "emmagatzemar"), ("combo de servicios", "service bundle", "combo de serveis"),  # Encounter 36
                ("impresora", "printer", "impressora"), ("compartir", "to share", "compartir"), ("acceso remoto", "remote access", "accés remot"),  # Encounter 37
                ("VPN", "VPN", "VPN"), ("privacidad", "privacy", "privacitat"), ("encriptar", "to encrypt", "encriptar"),  # Encounter 38
                ("ancho de banda", "bandwidth", "ample de banda"), ("saturado", "saturated", "saturat"), ("TV por cable", "cable TV", "TV per cable"),  # Encounter 39
                ("línea fija", "landline", "línia fixa"), ("competencia", "competition", "competència"), ("paquete triple", "triple bundle", "paquet triple"),  # Encounter 40
                ("instalación", "installation", "instal·lació"), ("cableado", "wiring", "cablejat"), ("infraestructura", "infrastructure", "infraestructura"),  # Encounter 41
                ("contratación", "hiring/contracting", "contractació"), ("video en vivo", "live streaming", "vídeo en viu"), ("llamada de video", "video call", "trucada de vídeo"),  # Encounter 42
                ("migración", "migration", "migració"), ("portabilidad", "portability", "portabilitat"), ("juego en red", "online gaming", "joc en xarxa"),  # Encounter 43
                ("tope de datos", "data cap", "topall de dades"), ("sin tope", "unlimited", "sense topall"), ("uso de datos", "data usage", "ús de dades"),  # Encounter 44
                ("queja", "complaint", "queixa"), ("protección de red", "network security", "protecció de xarxa"), ("cortafuegos", "firewall", "cortafocs"),  # Encounter 45
                ("resguardar", "to protect", "resguardar"), ("consumo real", "actual usage", "consum real"), ("programa malicioso", "malicious software", "programa maliciós"),  # Encounter 46
                ("satelital", "satellite", "satel·lit"), ("rural", "rural", "rural"), ("urbano", "urban", "urbà"),  # Encounter 47
                ("mantenimiento", "maintenance", "manteniment"), ("actualización", "update", "actualització"), ("software dañino", "harmful software", "programari maliciós"),  # Encounter 48
                ("programa de protección", "protection software", "programa de protecció"), ("amplificador", "amplifier", "amplificador"), ("encuesta", "survey", "enquesta"),  # Encounter 49
                ("listo", "ready", "llest"), ("funcionando", "working", "funcionant"), ("repetidor de señal", "signal repeater", "repetidor de senyal"),  # Encounter 50
            ],
        },
    ],
}

# --- Generate ENCOUNTER_WORDS, SITUATIONS, SITUATION_WORDS from compact data ---

ENCOUNTER_WORDS: dict[str, list[dict]] = {}
SITUATIONS: list[dict] = []
SITUATION_WORDS: list[dict] = []

# Order index base per animation_type (ensures globally unique order_index)
_ANIM_ORDER = list(_SUB_SITUATIONS.keys())

for category, sub_list in _SUB_SITUATIONS.items():
    category_words = []
    anim_base = _ANIM_ORDER.index(category) * 200  # 200 slots per animation type

    for sub_idx, sub in enumerate(sub_list):
        prefix = sub["word_prefix"]
        words = sub["words"]

        for enc_num in range(1, 51):
            # Word indices: 3 words per encounter
            base = (enc_num - 1) * 3
            w1 = words[base]
            w2 = words[base + 1]
            w3 = words[base + 2]

            # Each situation gets encounter_number 1-50 independently
            # Situation ID uses word_prefix for uniqueness (e.g., bank_open_1, bank_wire_1)
            situation_id = f"{prefix}_{enc_num}"

            # Encounter words
            for pos, (spanish, english, catalan) in enumerate([(w1[0], w1[1], w1[2]), (w2[0], w2[1], w2[2]), (w3[0], w3[1], w3[2])], 1):
                word_id = f"enc_{prefix}_{(enc_num - 1) * 3 + pos:03d}"
                category_words.append({
                    "id": word_id,
                    "spanish": spanish,
                    "english": english,
                    "catalan": catalan,
                })
                SITUATION_WORDS.append({
                    "situation_id": situation_id,
                    "word_id": word_id,
                    "position": pos,
                })

            # Situation
            SITUATIONS.append({
                "id": situation_id,
                "title": sub["title"],
                "animation_type": category,
                "encounter_number": enc_num,
                "order_index": anim_base + sub_idx * 50 + enc_num,
                "is_free": enc_num <= 5,  # First 5 encounters per sub-situation are free
                "goal": sub["goal"],
            })

    ENCOUNTER_WORDS[category] = category_words
