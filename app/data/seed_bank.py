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
                ("pasaporte", "passport", ""), ("reserva", "reservation", ""), ("confirmación", "confirmation", ""),  # Encounter 1
                ("número de reserva", "reservation number", ""), ("nombre", "first name", ""), ("apellido", "last name", ""),  # Encounter 2
                ("documento", "document", ""), ("identificación", "ID", ""), ("visa", "visa", ""),  # Encounter 3
                ("permiso", "permit", ""), ("documentos de viaje", "travel documents", ""), ("fecha de vencimiento", "expiration date", ""),  # Encounter 4
                ("a nombre de", "under the name of", ""), ("¿tiene reserva?", "do you have a reservation?", ""), ("¿me muestra el pasaporte?", "do you show me your passport?", ""),  # Encounter 5
                ("¿a qué nombre?", "under what name?", ""), ("vuelo", "flight", ""), ("número de vuelo", "flight number", ""),  # Encounter 6
                ("destino", "destination", ""), ("destino final", "final destination", ""), ("origen", "origin", ""),  # Encounter 7
                ("conexión", "connection", ""), ("vuelo de conexión", "connecting flight", ""), ("vuelo directo", "direct flight", ""),  # Encounter 8
                ("vuelo lleno", "full flight", ""), ("vuelo anterior", "previous flight", ""), ("vuelo siguiente", "next flight", ""),  # Encounter 9
                ("¿va directo a…?", "does it go direct to…?", ""), ("¿hasta dónde va?", "how far does it go?", ""), ("¿sale hoy?", "does it leave today?", ""),  # Encounter 10
                ("¿sale mañana?", "does it leave tomorrow?", ""), ("salida", "departure", ""), ("llegada", "arrival", ""),  # Encounter 11
                ("embarque", "boarding", ""), ("hora de embarque", "boarding time", ""), ("hora de salida", "departure time", ""),  # Encounter 12
                ("puerta", "gate", ""), ("número de puerta", "gate number", ""), ("puerta de embarque", "boarding gate", ""),  # Encounter 13
                ("zona de embarque", "boarding area", ""), ("preembarque", "preboarding", ""), ("prioridad", "priority", ""),  # Encounter 14
                ("a tiempo", "on time", ""), ("retraso", "delay", ""), ("demora", "delay", ""),  # Encounter 15
                ("cambio de puerta", "gate change", ""), ("¿cuál es la puerta?", "what is the gate?", ""), ("aparece en las pantallas", "it appears on the screens", ""),  # Encounter 16
                ("aparece en la app", "it appears in the app", ""), ("no está asignada", "it is not assigned", ""), ("asiento", "seat", ""),  # Encounter 17
                ("número de asiento", "seat number", ""), ("fila", "row", ""), ("ventana", "window", ""),  # Encounter 18
                ("pasillo", "aisle", ""), ("asiento del medio", "middle seat", ""), ("asiento de ventana", "window seat", ""),  # Encounter 19
                ("asiento de pasillo", "aisle seat", ""), ("salida de emergencia", "exit row", ""), ("juntos", "together", ""),  # Encounter 20
                ("separados", "separate", ""), ("¿prefiere ventana o pasillo?", "do you prefer a window or an aisle?", ""), ("¿hay asientos juntos?", "are there seats together?", ""),  # Encounter 21
                ("¿hay otro asiento?", "is there another seat?", ""), ("cambio de asiento", "seat change", ""), ("asignado", "assigned", ""),  # Encounter 22
                ("equipaje", "luggage", ""), ("maleta", "suitcase", ""), ("equipaje de mano", "carry-on", ""),  # Encounter 23
                ("equipaje facturado", "checked baggage", ""), ("maleta de cabina", "cabin bag", ""), ("artículo personal", "personal item", ""),  # Encounter 24
                ("primera maleta", "first bag", ""), ("segunda maleta", "second bag", ""), ("etiqueta", "tag", ""),  # Encounter 25
                ("recibo de equipaje", "baggage receipt", ""), ("cinta", "carousel", ""), ("recogida de equipaje", "baggage claim", ""),  # Encounter 26
                ("¿va a facturar equipaje?", "are you checking baggage?", ""), ("¿lleva equipaje?", "are you carrying luggage?", ""), ("balanza", "scale", ""),  # Encounter 27
                ("peso", "weight", ""), ("límite", "limit", ""), ("exceso", "excess", ""),  # Encounter 28
                ("sobrepeso", "overweight", ""), ("medidas", "dimensions", ""), ("medidas permitidas", "allowed dimensions", ""),  # Encounter 29
                ("está demasiado pesado", "it is too heavy", ""), ("está demasiado grande", "it is too big", ""), ("póngalo en la balanza", "put it on the scale (Ud.)", ""),  # Encounter 30
                ("¿cuál es el límite?", "what is the limit?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""), ("facturo el equipaje", "I check the baggage", ""),  # Encounter 31
                ("etiquetan el equipaje", "they tag the baggage", ""), ("abre la maleta", "open the suitcase (Ud.)", ""), ("saca los objetos", "take the items out (Ud.)", ""),  # Encounter 32
                ("pasa algunas cosas a la mochila", "move some things to the backpack (Ud.)", ""), ("lo lleva con usted", "carry it with you", ""), ("no puede ir en la maleta", "it cannot go in the suitcase", ""),  # Encounter 33
                ("¿puede facturarlo?", "can you check it?", ""), ("¿puede llevarlo con usted?", "can you carry it with you?", ""), ("líquidos", "liquids", ""),  # Encounter 34
                ("batería portátil", "power bank", ""), ("cargador", "charger", ""), ("computadora", "laptop", ""),  # Encounter 35
                ("objetos de valor", "valuables", ""), ("medicinas", "medication", ""), ("¿lleva líquidos?", "are you carrying liquids?", ""),  # Encounter 36
                ("¿lleva baterías?", "are you carrying batteries?", ""), ("no está permitido", "it is not allowed", ""), ("está permitido", "it is allowed", ""),  # Encounter 37
                ("control de seguridad", "security check", ""), ("revisión", "inspection", ""), ("revisión adicional", "additional screening", ""),  # Encounter 38
                ("selección aleatoria", "random selection", ""), ("control", "checkpoint", ""), ("seguridad", "security", ""),  # Encounter 39
                ("terminal", "terminal", ""), ("aeropuerto", "airport", ""), ("aerolínea", "airline", ""),  # Encounter 40
                ("mostrador", "counter", ""), ("sistema", "system", ""), ("no funciona", "it does not work", ""),  # Encounter 41
                ("exceso de equipaje", "excess baggage", ""), ("paga el exceso", "pay the excess fee (Ud.)", ""), ("con tarjeta", "with a card", ""),  # Encounter 42
                ("en efectivo", "in cash", ""), ("sin costo", "with no charge", ""), ("tarifa", "fee", ""),  # Encounter 43
                ("total", "total", ""), ("recibo", "receipt", ""), ("pasajero", "passenger", ""),  # Encounter 44
                ("familia", "family", ""), ("niño", "child", ""), ("niña", "girl", ""),  # Encounter 45
                ("coche de bebé", "stroller", ""), ("hasta la puerta", "up to the gate", ""), ("tarjeta de embarque", "boarding pass", ""),  # Encounter 46
                ("imprimen la tarjeta de embarque", "they print the boarding pass", ""), ("celular", "cellphone", ""), ("correo", "email", ""),  # Encounter 47
                ("confirmación por correo", "email confirmation", ""), ("hay espacio", "there is space", ""), ("no hay espacio", "there is no space", ""),  # Encounter 48
                ("conexión corta", "short connection", ""), ("conexión larga", "long connection", ""), ("aduana", "customs", ""),  # Encounter 49
                ("migración", "immigration", ""), ("control migratorio", "immigration control", ""), ("formulario de aduana", "customs form", ""),  # Encounter 50
            ],
        },
    ],
    "banking": [
        {
            "title": "Banking",
            "goal": "Handle banking tasks including accounts, transfers, cards, and loans",
            "word_prefix": "bank",
            "words": [
                ("banco", "bank", ""), ("cajero", "teller", ""), ("cliente", "customer", ""),  # Encounter 1
                ("cuenta", "account", ""), ("cuenta bancaria", "bank account", ""), ("saldo", "balance", ""),  # Encounter 2
                ("saldo disponible", "available balance", ""), ("saldo actual", "current balance", ""), ("tarjeta", "card", ""),  # Encounter 3
                ("tarjeta de débito", "debit card", ""), ("tarjeta de crédito", "credit card", ""), ("tarjeta bloqueada", "blocked card", ""),  # Encounter 4
                ("tarjeta nueva", "new card", ""), ("PIN", "PIN", ""), ("clave", "PIN", ""),  # Encounter 5
                ("contraseña", "password", ""), ("número de cuenta", "account number", ""), ("número incorrecto", "wrong number", ""),  # Encounter 6
                ("transferencia", "transfer", ""), ("transferencia enviada", "sent transfer", ""), ("transferencia recibida", "received transfer", ""),  # Encounter 7
                ("no llegó", "it did not arrive", ""), ("llegó tarde", "it arrived late", ""), ("comprobante", "receipt", ""),  # Encounter 8
                ("muestro el comprobante", "I show the receipt", ""), ("reviso la cuenta", "I check the account", ""), ("revisan los movimientos", "they check the transactions", ""),  # Encounter 9
                ("movimientos", "transactions", ""), ("cargo", "charge", ""), ("cargos extra", "extra charges", ""),  # Encounter 10
                ("no lo reconozco", "I do not recognize it", ""), ("cargo sospechoso", "suspicious charge", ""), ("intento sospechoso", "suspicious attempt", ""),  # Encounter 11
                ("bloqueo", "block", ""), ("se bloqueó", "it got blocked", ""), ("desbloquean la tarjeta", "they unblock the card", ""),  # Encounter 12
                ("activan la tarjeta", "they activate the card", ""), ("emiten la tarjeta", "they issue the card", ""), ("funciona ahora", "it works now", ""),  # Encounter 13
                ("no funciona", "it does not work", ""), ("rechazada", "declined", ""), ("pago rechazado", "declined payment", ""),  # Encounter 14
                ("hago el pago", "I make the payment", ""), ("pago aprobado", "approved payment", ""), ("pago pendiente", "pending payment", ""),  # Encounter 15
                ("monto", "amount", ""), ("monto total", "total amount", ""), ("cantidad", "amount", ""),  # Encounter 16
                ("deposito dinero", "I deposit money", ""), ("retiro", "withdrawal", ""), ("retiro dinero", "I withdraw money", ""),  # Encounter 17
                ("efectivo", "cash", ""), ("con tarjeta", "with a card", ""), ("cajero automático", "ATM", ""),  # Encounter 18
                ("retiro en el cajero", "I withdraw at the ATM", ""), ("saldo insuficiente", "insufficient funds", ""), ("no hay fondos", "there are no funds", ""),  # Encounter 19
                ("hay fondos", "there are funds", ""), ("abro una cuenta", "I open an account", ""), ("abro una cuenta nueva", "I open a new account", ""),  # Encounter 20
                ("cierro la cuenta", "I close the account", ""), ("cambio de cuenta", "account change", ""), ("tipo de cuenta", "account type", ""),  # Encounter 21
                ("cuenta principal", "main account", ""), ("cuenta de ahorros", "savings account", ""), ("cuenta corriente", "checking account", ""),  # Encounter 22
                ("comisión", "fee", ""), ("cobran comisión", "they charge a fee", ""), ("sin comisión", "without a fee", ""),  # Encounter 23
                ("comisión mensual", "monthly fee", ""), ("eliminan la comisión", "they remove the fee", ""), ("contrato", "contract", ""),  # Encounter 24
                ("condiciones", "terms", ""), ("saldo mínimo", "minimum balance", ""), ("requiere saldo mínimo", "it requires a minimum balance", ""),  # Encounter 25
                ("requiere depósitos", "it requires deposits", ""), ("historial", "history", ""), ("historial crediticio", "credit history", ""),  # Encounter 26
                ("crédito", "credit", ""), ("buen crédito", "good credit", ""), ("mal crédito", "bad credit", ""),  # Encounter 27
                ("préstamo", "loan", ""), ("solicito un préstamo", "I apply for a loan", ""), ("monto del préstamo", "loan amount", ""),  # Encounter 28
                ("aprueban el préstamo", "they approve the loan", ""), ("rechazan el préstamo", "they reject the loan", ""), ("aprobación", "approval", ""),  # Encounter 29
                ("está en proceso", "it is in process", ""), ("solicitud", "application", ""), ("envío la solicitud", "I send the application", ""),  # Encounter 30
                ("documentos", "documents", ""), ("falta un documento", "one document is missing", ""), ("envío los documentos", "I send the documents", ""),  # Encounter 31
                ("comprobante de ingresos", "proof of income", ""), ("revisan el sistema", "they check the system", ""), ("el sistema falla", "the system fails", ""),  # Encounter 32
                ("el sistema está lento", "the system is slow", ""), ("error del sistema", "system error", ""), ("abren un caso", "they open a case", ""),  # Encounter 33
                ("número de caso", "case number", ""), ("seguimiento del caso", "case follow-up", ""), ("tarda unos días", "it takes a few days", ""),  # Encounter 34
                ("tiempo estimado", "estimated time", ""), ("depende del sistema", "it depends on the system", ""), ("espero la respuesta", "I wait for the response", ""),  # Encounter 35
                ("hoy no", "not today", ""), ("mañana sí", "tomorrow yes", ""), ("llamo al banco", "I call the bank", ""),  # Encounter 36
                ("atención al cliente", "customer service", ""), ("hablo con un agente", "I speak with an agent", ""), ("verifican mi identidad", "they verify my identity", ""),  # Encounter 37
                ("confirman mis datos", "they confirm my information", ""), ("fecha de nacimiento", "birth date", ""), ("dirección", "address", ""),  # Encounter 38
                ("número de teléfono", "phone number", ""), ("correo electrónico", "email", ""), ("actualizan mis datos", "they update my information", ""),  # Encounter 39
                ("datos incorrectos", "incorrect information", ""), ("cambio mis datos", "I change my information", ""), ("código de seguridad", "security code", ""),  # Encounter 40
                ("envían el código", "they send the code", ""), ("ingreso el código", "I enter the code", ""), ("código válido", "valid code", ""),  # Encounter 41
                ("código inválido", "invalid code", ""), ("acceso a la cuenta", "account access", ""), ("no tengo acceso", "I do not have access", ""),  # Encounter 42
                ("recupero el acceso", "I recover access", ""), ("restablecen la clave", "they reset the password", ""), ("cambio la clave", "I change the PIN", ""),  # Encounter 43
                ("bloquean el acceso", "they block the access", ""), ("acceso activo", "active access", ""), ("sigue igual", "it is still the same", ""),  # Encounter 44
                ("mejora un poco", "it improves a little", ""), ("no mejora", "it does not improve", ""), ("¿qué pasó?", "what happened?", ""),  # Encounter 45
                ("¿qué hago?", "what do I do?", ""), ("¿cuánto tarda?", "how long does it take?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""),  # Encounter 46
                ("no entiendo", "I do not understand", ""), ("¿puede repetir?", "can you repeat that?", ""), ("más despacio", "more slowly", ""),  # Encounter 47
                ("sucursal", "branch", ""), ("ejecutivo", "bank advisor", ""), ("ventanilla", "teller window", ""),  # Encounter 48
                ("firma registrada", "signature on file", ""), ("la firma no coincide", "the signature does not match", ""), ("transferencia internacional", "international transfer", ""),  # Encounter 49
                ("tipo de cambio", "exchange rate", ""), ("comisión por transferencia", "transfer fee", ""), ("fondos retenidos", "held funds", ""),  # Encounter 50
            ],
        },
    ],
    "clothing": [
        {
            "title": "Clothing Shopping",
            "goal": "Navigate a clothing store, find your size, make a purchase, and handle returns",
            "word_prefix": "cloth",
            "words": [
                ("vendedor", "salesperson", ""), ("cliente", "customer", ""), ("tienda", "store", ""),  # Encounter 1
                ("ropa", "clothing", ""), ("camisa", "shirt", ""), ("pantalón", "pants", ""),  # Encounter 2
                ("chaqueta", "jacket", ""), ("vestido", "dress", ""), ("falda", "skirt", ""),  # Encounter 3
                ("talla", "size", ""), ("¿qué talla usa?", "what size do you wear?", ""), ("le queda bien", "it fits you well", ""),  # Encounter 4
                ("le queda grande", "it is too big on you", ""), ("le queda pequeño", "it is too small on you", ""), ("no le queda", "it does not fit you", ""),  # Encounter 5
                ("otra talla", "another size", ""), ("más grande", "bigger", ""), ("más pequeño", "smaller", ""),  # Encounter 6
                ("probador", "fitting room", ""), ("usa el probador", "use the fitting room", ""), ("espere su turno", "wait your turn (Ud.)", ""),  # Encounter 7
                ("hay fila", "there is a line", ""), ("modelo", "style", ""), ("mismo modelo", "same style", ""),  # Encounter 8
                ("modelo diferente", "different style", ""), ("color", "color", ""), ("otro color", "another color", ""),  # Encounter 9
                ("no hay talla", "there is no size available", ""), ("no hay stock", "there is no stock", ""), ("está agotado", "it is sold out", ""),  # Encounter 10
                ("reviso el stock", "I check the stock", ""), ("reviso el sistema", "I check the system", ""), ("hay en otra sucursal", "it is available at another branch", ""),  # Encounter 11
                ("otra sucursal", "another branch", ""), ("lo pueden pedir", "they can order it", ""), ("llega en unos días", "it arrives in a few days", ""),  # Encounter 12
                ("tarda unos días", "it takes a few days", ""), ("lo aparto", "I put it on hold", ""), ("apartado", "item on hold", ""),  # Encounter 13
                ("precio", "price", ""), ("precio normal", "regular price", ""), ("precio de oferta", "sale price", ""),  # Encounter 14
                ("descuento", "discount", ""), ("el descuento aplica", "the discount applies", ""), ("no aplica", "it does not apply", ""),  # Encounter 15
                ("promoción", "promotion", ""), ("condición", "condition", ""), ("con membresía", "with membership", ""),  # Encounter 16
                ("sin membresía", "without membership", ""), ("registro", "sign-up", ""), ("no quiero registrarme", "I do not want to sign up", ""),  # Encounter 17
                ("el sistema marca otro precio", "the system shows another price", ""), ("no coincide", "it does not match", ""), ("reviso el precio", "I check the price", ""),  # Encounter 18
                ("corrigen el precio", "they correct the price", ""), ("ajuste manual", "manual adjustment", ""), ("etiqueta", "tag", ""),  # Encounter 19
                ("mal etiquetado", "mislabeled", ""), ("letrero", "sign", ""), ("política de la tienda", "store policy", ""),  # Encounter 20
                ("no aceptamos devoluciones", "we do not accept returns", ""), ("solo damos crédito de tienda", "we only give store credit", ""), ("crédito de tienda", "store credit", ""),  # Encounter 21
                ("devolución", "refund", ""), ("procesan la devolución", "they process the refund", ""), ("cambio de producto", "exchange", ""),  # Encounter 22
                ("producto defectuoso", "defective item", ""), ("está roto", "it is broken", ""), ("costura rota", "torn seam", ""),  # Encounter 23
                ("recibo", "receipt", ""), ("tiene recibo", "do you have a receipt?", ""), ("sin recibo", "without a receipt", ""),  # Encounter 24
                ("dentro del plazo", "within the return window", ""), ("fuera del plazo", "outside the return window", ""), ("quiero hablar con la gerente", "I want to speak with the manager", ""),  # Encounter 25
                ("gerente", "manager", ""), ("excepción", "exception", ""), ("aprueban la excepción", "they approve the exception", ""),  # Encounter 26
                ("caja", "checkout", ""), ("total", "total", ""), ("monto total", "total amount", ""),  # Encounter 27
                ("pago", "payment", ""), ("inserta la tarjeta", "insert the card", ""), ("acerca la tarjeta", "tap the card", ""),  # Encounter 28
                ("pasa la tarjeta", "swipe the card", ""), ("no pasa", "it does not go through", ""), ("inténtalo otra vez", "try again", ""),  # Encounter 29
                ("pago aprobado", "approved payment", ""), ("pago rechazado", "declined payment", ""), ("otra tarjeta", "another card", ""),  # Encounter 30
                ("efectivo", "cash", ""), ("pago en efectivo", "cash payment", ""), ("firma aquí", "sign here (Ud.)", ""),  # Encounter 31
                ("bolsa", "bag", ""), ("¿quiere bolsa?", "do you want a bag?", ""), ("bolsa grande", "big bag", ""),  # Encounter 32
                ("bolsa pequeña", "small bag", ""), ("sin bolsa", "no bag", ""), ("lo empacan", "they pack it", ""),  # Encounter 33
                ("fila larga", "long line", ""), ("mucha gente", "many people", ""), ("espera larga", "long wait", ""),  # Encounter 34
                ("tarda mucho", "it takes a long time", ""), ("servicio lento", "slow service", ""), ("está abierto", "it is open", ""),  # Encounter 35
                ("está cerrado", "it is closed", ""), ("horario", "store hours", ""), ("identificación", "ID", ""),  # Encounter 36
                ("muestra su identificación", "show your ID (Ud.)", ""), ("alarma", "alarm", ""), ("sensor", "security tag", ""),  # Encounter 37
                ("quitan el sensor", "they remove the security tag", ""), ("sensor activo", "active security tag", ""), ("la alarma suena", "the alarm goes off", ""),  # Encounter 38
                ("revisan la compra", "they check the purchase", ""), ("el código escanea", "the barcode scans", ""), ("el código no escanea", "the barcode does not scan", ""),  # Encounter 39
                ("ingreso manual", "manual entry", ""), ("código manual", "manual code", ""), ("problema del sistema", "system issue", ""),  # Encounter 40
                ("ya quedó", "it is fixed now", ""), ("sigue igual", "it is still the same", ""), ("talla correcta", "correct size", ""),  # Encounter 41
                ("talla incorrecta", "wrong size", ""), ("se lo traigo", "I bring it to you", ""), ("no le queda bien", "it does not fit you well", ""),  # Encounter 42
                ("le queda mejor", "it fits you better", ""), ("me lo llevo", "I am taking it", ""), ("devolución parcial", "partial refund", ""),  # Encounter 43
                ("monto reembolsado", "refunded amount", ""), ("te lo cambio", "I exchange it for you", ""), ("te hago un descuento", "I give you a discount", ""),  # Encounter 44
                ("caja abierta", "open register", ""), ("caja cerrada", "closed register", ""), ("precio final", "final price", ""),  # Encounter 45
                ("cupón", "coupon", ""), ("el cupón vence hoy", "the coupon expires today", ""), ("temporada", "season", ""),  # Encounter 46
                ("colección nueva", "new collection", ""), ("prenda", "garment", ""), ("prenda dañada", "damaged garment", ""),  # Encounter 47
                ("defecto de fábrica", "manufacturing defect", ""), ("marca", "brand", ""), ("misma marca", "same brand", ""),  # Encounter 48
                ("línea premium", "premium line", ""), ("material", "material", ""), ("algodón", "cotton", ""),  # Encounter 49
                ("tela", "fabric", ""), ("se encoge", "it shrinks", ""), ("destiñe", "it bleeds color", ""),  # Encounter 50
            ],
        },
    ],
    "contractor": [
        {
            "title": "Hiring a Contractor",
            "goal": "Manage a construction project, discuss plans, costs, and quality with your contractor",
            "word_prefix": "contr",
            "words": [
                ("contratista", "contractor", ""), ("trabajador", "worker", ""), ("equipo", "crew", ""),  # Encounter 1
                ("proyecto", "project", ""), ("obra", "construction work", ""), ("trabajo", "work", ""),  # Encounter 2
                ("plano", "plan", ""), ("diseño", "design", ""), ("presupuesto", "budget", ""),  # Encounter 3
                ("estimado", "estimate", ""), ("costo", "cost", ""), ("precio", "price", ""),  # Encounter 4
                ("total", "total", ""), ("pago", "payment", ""), ("anticipo", "deposit", ""),  # Encounter 5
                ("pago final", "final payment", ""), ("material", "material", ""), ("materiales", "materials", ""),  # Encounter 6
                ("proveedor", "supplier", ""), ("disponibilidad", "availability", ""), ("no está disponible", "it is not available", ""),  # Encounter 7
                ("retraso", "delay", ""), ("atraso", "delay", ""), ("va atrasado", "it is running late", ""),  # Encounter 8
                ("a tiempo", "on time", ""), ("horario", "schedule", ""), ("cumplen el horario", "they keep the schedule", ""),  # Encounter 9
                ("tiempo estimado", "estimated time", ""), ("terminan hoy", "they finish today", ""), ("empiezan hoy", "they start today", ""),  # Encounter 10
                ("siguen trabajando", "they keep working", ""), ("trabajo detenido", "stopped work", ""), ("revisan esto", "they check this", ""),  # Encounter 11
                ("inspección", "inspection", ""), ("ajuste", "adjustment", ""), ("alternativa", "alternative", ""),  # Encounter 12
                ("calidad", "quality", ""), ("misma calidad", "same quality", ""), ("es diferente", "it is different", ""),  # Encounter 13
                ("mejor opción", "better option", ""), ("es más caro", "it is more expensive", ""), ("es más barato", "it is cheaper", ""),  # Encounter 14
                ("costo adicional", "additional cost", ""), ("no estaba incluido", "it was not included", ""), ("fuera del presupuesto", "over budget", ""),  # Encounter 15
                ("¿cuánto cuesta?", "how much does it cost?", ""), ("¿cuánto tarda?", "how long does it take?", ""), ("¿cuándo terminan?", "when do they finish?", ""),  # Encounter 16
                ("¿cuándo empiezan?", "when do they start?", ""), ("¿por qué hay retraso?", "why is there a delay?", ""), ("¿qué pasó?", "what happened?", ""),  # Encounter 17
                ("¿puede explicar?", "can you explain it?", ""), ("no entiendo", "I do not understand", ""), ("necesito más detalle", "I need more detail", ""),  # Encounter 18
                ("quiero ver el plano", "I want to see the plan", ""), ("me envía el plano", "send me the plan (Ud.)", ""), ("está en proceso", "it is in progress", ""),  # Encounter 19
                ("ya empezaron", "they already started", ""), ("ya terminaron", "they already finished", ""), ("falta trabajo", "work is still missing", ""),  # Encounter 20
                ("está incompleto", "it is incomplete", ""), ("está mal hecho", "it is poorly done", ""), ("está bien hecho", "it is well done", ""),  # Encounter 21
                ("corrigen esto", "they fix this", ""), ("reparan esto", "they repair this", ""), ("rehacen esto", "they redo this", ""),  # Encounter 22
                ("ajustan el nivel", "they level this", ""), ("superficie", "surface", ""), ("pared", "wall", ""),  # Encounter 23
                ("piso", "floor", ""), ("techo", "ceiling", ""), ("pintura", "paint", ""),  # Encounter 24
                ("hay manchas", "there are stains", ""), ("acabado", "finish", ""), ("está nivelado", "it is level", ""),  # Encounter 25
                ("está desnivelado", "it is uneven", ""), ("hay una grieta", "there is a crack", ""), ("humedad", "moisture", ""),  # Encounter 26
                ("hay una fuga", "there is a leak", ""), ("tubería", "pipe", ""), ("instalación", "installation", ""),  # Encounter 27
                ("sistema eléctrico", "electrical system", ""), ("cable", "wire", ""), ("enchufe", "outlet", ""),  # Encounter 28
                ("interruptor", "switch", ""), ("agua", "water", ""), ("llave de agua", "water valve", ""),  # Encounter 29
                ("abren la pared", "they open the wall", ""), ("cierran la pared", "they close the wall", ""), ("hay daño", "there is damage", ""),  # Encounter 30
                ("evitan el daño", "they avoid the damage", ""), ("es urgente", "it is urgent", ""), ("puede empeorar", "it can get worse", ""),  # Encounter 31
                ("apruebo el cambio", "I approve the change", ""), ("no autorizo ese cambio", "I do not authorize that change", ""), ("sin autorización", "without authorization", ""),  # Encounter 32
                ("avisan antes", "they notify me beforehand", ""), ("falta comunicación", "there is poor communication", ""), ("nadie vino", "nobody came", ""),  # Encounter 33
                ("no llegaron", "they did not arrive", ""), ("vienen mañana", "they come tomorrow", ""), ("vienen hoy", "they come today", ""),  # Encounter 34
                ("en la mañana", "in the morning", ""), ("en la tarde", "in the afternoon", ""), ("llegan tarde", "they arrive late", ""),  # Encounter 35
                ("cumplen el plazo", "they meet the deadline", ""), ("plazo", "deadline", ""), ("entrega", "delivery", ""),  # Encounter 36
                ("entrega final", "final delivery", ""), ("inspección final", "final inspection", ""), ("garantía", "warranty", ""),  # Encounter 37
                ("incluye garantía", "it includes a warranty", ""), ("sin garantía", "without a warranty", ""), ("herramienta", "tool", ""),  # Encounter 38
                ("maquinaria", "machinery", ""), ("cortan el material", "they cut the material", ""), ("instalan esto", "they install this", ""),  # Encounter 39
                ("miden esto", "they measure this", ""), ("nivelan esto", "they level this", ""), ("fijan esto", "they secure this", ""),  # Encounter 40
                ("desmontan esto", "they remove this", ""), ("montan esto", "they assemble this", ""), ("limpian el área", "they clean the area", ""),  # Encounter 41
                ("retiran los escombros", "they remove the debris", ""), ("escombros", "debris", ""), ("limpieza final", "final cleanup", ""),  # Encounter 42
                ("área", "area", ""), ("espacio", "space", ""), ("acceso", "access", ""),  # Encounter 43
                ("entrada", "entrance", ""), ("salida", "exit", ""), ("vecino", "neighbor", ""),  # Encounter 44
                ("ruido", "noise", ""), ("polvo", "dust", ""), ("seguridad", "safety", ""),  # Encounter 45
                ("riesgo", "risk", ""), ("protección", "protection", ""), ("equipo de seguridad", "safety gear", ""),  # Encounter 46
                ("casco", "helmet", ""), ("guantes", "gloves", ""), ("gafas de seguridad", "safety glasses", ""),  # Encounter 47
                ("azulejo", "tile", ""), ("baldosa", "floor tile", ""), ("madera", "wood", ""),  # Encounter 48
                ("cemento", "cement", ""), ("yeso", "plaster", ""), ("sellador", "sealant", ""),  # Encounter 49
                ("impermeabilización", "waterproofing", ""), ("permiso", "permit", ""), ("inspector", "inspector", ""),  # Encounter 50
            ],
        },
    ],
    "groceries": [
        {
            "title": "At the Supermarket",
            "goal": "Check out at the supermarket, handle pricing issues, and bag your groceries",
            "word_prefix": "groc",
            "words": [
                ("cajero", "cashier", ""), ("cliente", "customer", ""), ("caja", "checkout", ""),  # Encounter 1
                ("fila", "line", ""), ("turno", "turn", ""), ("siguiente", "next", ""),  # Encounter 2
                ("productos", "products", ""), ("artículo", "item", ""), ("código de barras", "barcode", ""),  # Encounter 3
                ("escanean el producto", "they scan the item", ""), ("pasan los productos", "they pass the items through", ""), ("precio", "price", ""),  # Encounter 4
                ("precio correcto", "correct price", ""), ("precio incorrecto", "wrong price", ""), ("oferta", "sale", ""),  # Encounter 5
                ("descuento", "discount", ""), ("promoción", "promotion", ""), ("el descuento aplica", "the discount applies", ""),  # Encounter 6
                ("no aplica", "it does not apply", ""), ("sistema", "system", ""), ("no aparece", "it does not show up", ""),  # Encounter 7
                ("revisan el precio", "they check the price", ""), ("verifican el precio", "they verify the price", ""), ("letrero", "sign", ""),  # Encounter 8
                ("estante", "shelf", ""), ("pasillo", "aisle", ""), ("supervisor", "supervisor", ""),  # Encounter 9
                ("llaman al supervisor", "they call the supervisor", ""), ("corrigen el precio", "they correct the price", ""), ("total", "total", ""),  # Encounter 10
                ("monto total", "total amount", ""), ("subtotal", "subtotal", ""), ("impuesto", "tax", ""),  # Encounter 11
                ("incluye impuesto", "it includes tax", ""), ("no incluye impuesto", "it does not include tax", ""), ("pago", "payment", ""),  # Encounter 12
                ("pago aprobado", "approved payment", ""), ("pago rechazado", "declined payment", ""), ("tarjeta", "card", ""),  # Encounter 13
                ("tarjeta rechazada", "declined card", ""), ("inserta la tarjeta", "insert the card", ""), ("pasa la tarjeta", "swipe the card", ""),  # Encounter 14
                ("acerca la tarjeta", "tap the card", ""), ("ingresa el PIN", "enter the PIN", ""), ("firma aquí", "sign here (Ud.)", ""),  # Encounter 15
                ("efectivo", "cash", ""), ("pago en efectivo", "cash payment", ""), ("dividir el pago", "split the payment", ""),  # Encounter 16
                ("pago dividido", "split payment", ""), ("pago parcial", "partial payment", ""), ("pago completo", "full payment", ""),  # Encounter 17
                ("cambio", "change", ""), ("le dan cambio", "they give you change", ""), ("recibo", "receipt", ""),  # Encounter 18
                ("imprimen el recibo", "they print the receipt", ""), ("bolsa", "bag", ""), ("bolsa grande", "big bag", ""),  # Encounter 19
                ("bolsa pequeña", "small bag", ""), ("sin bolsa", "no bag", ""), ("separan los productos", "they separate the items", ""),  # Encounter 20
                ("producto frío", "cold item", ""), ("producto congelado", "frozen item", ""), ("producto seco", "dry item", ""),  # Encounter 21
                ("huevos", "eggs", ""), ("frágil", "fragile", ""), ("pesado", "heavy", ""),  # Encounter 22
                ("liviano", "light", ""), ("cantidad", "quantity", ""), ("una unidad", "one unit", ""),  # Encounter 23
                ("dos unidades", "two units", ""), ("marcan la cantidad", "they enter the quantity", ""), ("corrigen la cantidad", "they correct the quantity", ""),  # Encounter 24
                ("quitan el producto", "they remove the item", ""), ("agregan el producto", "they add the item", ""), ("no es mío", "it is not mine", ""),  # Encounter 25
                ("es incorrecto", "it is incorrect", ""), ("revisan el producto", "they check the item", ""), ("escaneo doble", "double scan", ""),  # Encounter 26
                ("error del sistema", "system error", ""), ("ya quedó", "it is fixed now", ""), ("sigue igual", "it is still the same", ""),  # Encounter 27
                ("cliente siguiente", "next customer", ""), ("fila larga", "long line", ""), ("mucha gente", "many people", ""),  # Encounter 28
                ("tarda mucho", "it takes a long time", ""), ("servicio", "service", ""), ("horario", "store hours", ""),  # Encounter 29
                ("está abierto", "it is open", ""), ("está cerrado", "it is closed", ""), ("identificación", "ID", ""),  # Encounter 30
                ("muestra su identificación", "show your ID (Ud.)", ""), ("requiere edad mínima", "it requires a minimum age", ""), ("verifican la edad", "they verify your age", ""),  # Encounter 31
                ("producto restringido", "restricted item", ""), ("aprobado", "approved", ""), ("denegado", "denied", ""),  # Encounter 32
                ("alcohol", "alcohol", ""), ("tabaco", "tobacco", ""), ("bebida", "drink", ""),  # Encounter 33
                ("comida", "food", ""), ("pan", "bread", ""), ("leche", "milk", ""),  # Encounter 34
                ("carne", "meat", ""), ("verduras", "vegetables", ""), ("fruta", "fruit", ""),  # Encounter 35
                ("caja rápida", "express checkout", ""), ("pocos productos", "few items", ""), ("muchos productos", "many items", ""),  # Encounter 36
                ("carrito", "cart", ""), ("canasta", "basket", ""), ("empacan los productos", "they pack the items", ""),  # Encounter 37
                ("cliente espera", "the customer waits", ""), ("número de caja", "register number", ""), ("caja abierta", "open register", ""),  # Encounter 38
                ("caja cerrada", "closed register", ""), ("cambio exacto", "exact change", ""), ("sin cambio", "without change", ""),  # Encounter 39
                ("pago exacto", "exact payment", ""), ("tarjeta válida", "valid card", ""), ("tarjeta inválida", "invalid card", ""),  # Encounter 40
                ("saldo insuficiente", "insufficient funds", ""), ("hay fondos", "there are funds", ""), ("no hay fondos", "there are no funds", ""),  # Encounter 41
                ("listo para pagar", "ready to pay", ""), ("ingresa el código", "enter the code", ""), ("código manual", "manual code", ""),  # Encounter 42
                ("ingreso manual", "manual entry", ""), ("producto sin código", "item without a barcode", ""), ("pesa el producto", "weigh the item", ""),  # Encounter 43
                ("balanza", "scale", ""), ("etiqueta de precio", "price label", ""), ("no coincide", "it does not match", ""),  # Encounter 44
                ("revise la etiqueta", "check the label (Ud.)", ""), ("actualizan el precio", "they update the price", ""), ("precio actualizado", "updated price", ""),  # Encounter 45
                ("inténtalo otra vez", "try again", ""), ("caja central", "main checkout", ""), ("lector", "scanner", ""),  # Encounter 46
                ("el lector da error", "the scanner gives an error", ""), ("promoción vencida", "expired promotion", ""), ("vence hoy", "it expires today", ""),  # Encounter 47
                ("unidad equivocada", "wrong unit", ""), ("precio por kilo", "price per kilo", ""), ("precio por unidad", "price per unit", ""),  # Encounter 48
                ("pesa menos", "it weighs less", ""), ("pesa más", "it weighs more", ""), ("producto abierto", "opened item", ""),  # Encounter 49
                ("producto dañado", "damaged item", ""), ("reemplazo", "replacement", ""), ("devolución al método de pago", "refund to the payment method", ""),  # Encounter 50
            ],
        },
    ],
    "mechanic": [
        {
            "title": "At the Mechanic",
            "goal": "Describe car problems, get a diagnosis, and handle repairs and payment",
            "word_prefix": "mech",
            "words": [
                ("carro", "car", ""), ("vehículo", "vehicle", ""), ("motor", "engine", ""),  # Encounter 1
                ("batería", "battery", ""), ("frenos", "brakes", ""), ("aceite", "oil", ""),  # Encounter 2
                ("filtro", "filter", ""), ("transmisión", "transmission", ""), ("suspensión", "suspension", ""),  # Encounter 3
                ("llanta", "tire", ""), ("rueda", "wheel", ""), ("radiador", "radiator", ""),  # Encounter 4
                ("bujía", "spark plug", ""), ("correa", "belt", ""), ("alternador", "alternator", ""),  # Encounter 5
                ("falla", "issue", ""), ("ruido", "noise", ""), ("vibración", "vibration", ""),  # Encounter 6
                ("fuga", "leak", ""), ("no arranca", "it does not start", ""), ("no enciende", "it does not turn on", ""),  # Encounter 7
                ("se apaga", "it shuts off", ""), ("huele raro", "it smells strange", ""), ("se sobrecalienta", "it overheats", ""),  # Encounter 8
                ("tiene poca potencia", "it has low power", ""), ("consume aceite", "it burns oil", ""), ("pierde líquido", "it is leaking fluid", ""),  # Encounter 9
                ("frenos débiles", "weak brakes", ""), ("pedal suave", "soft pedal", ""), ("revisan el carro", "they check the car", ""),  # Encounter 10
                ("inspección", "inspection", ""), ("diagnóstico", "diagnosis", ""), ("reparan", "they repair it", ""),  # Encounter 11
                ("lo arreglan", "they fix it", ""), ("cambian la pieza", "they replace the part", ""), ("ajustan", "they adjust it", ""),  # Encounter 12
                ("instalan", "they install it", ""), ("limpian", "they clean it", ""), ("lo prueban", "they test it", ""),  # Encounter 13
                ("revisan el motor", "they check the engine", ""), ("cambio de aceite", "oil change", ""), ("cambian el filtro", "they change the filter", ""),  # Encounter 14
                ("revisan los frenos", "they check the brakes", ""), ("alinean las llantas", "they align the tires", ""), ("¿qué problema tiene?", "what problem does it have?", ""),  # Encounter 15
                ("¿qué pasa?", "what is happening?", ""), ("¿desde cuándo?", "since when?", ""), ("¿cuándo empezó?", "when did it start?", ""),  # Encounter 16
                ("¿hace ruido?", "does it make noise?", ""), ("¿cuánto cuesta?", "how much does it cost?", ""), ("¿cuánto tarda?", "how long does it take?", ""),  # Encounter 17
                ("¿es grave?", "is it serious?", ""), ("¿puede empeorar?", "can it get worse?", ""), ("¿puede revisarlo?", "can you check it?", ""),  # Encounter 18
                ("precio", "price", ""), ("costo", "cost", ""), ("total", "total", ""),  # Encounter 19
                ("estimado", "estimate", ""), ("mano de obra", "labor", ""), ("piezas", "parts", ""),  # Encounter 20
                ("adicional", "additional", ""), ("incluye", "it includes", ""), ("no incluye", "it does not include", ""),  # Encounter 21
                ("presupuesto", "quote", ""), ("pago", "payment", ""), ("en efectivo", "in cash", ""),  # Encounter 22
                ("con tarjeta", "with a card", ""), ("factura", "invoice", ""), ("recibo", "receipt", ""),  # Encounter 23
                ("desgastado", "worn out", ""), ("dañado", "damaged", ""), ("roto", "broken", ""),  # Encounter 24
                ("sucio", "dirty", ""), ("flojo", "loose", ""), ("apretado", "tight", ""),  # Encounter 25
                ("en buen estado", "in good condition", ""), ("en mal estado", "in bad condition", ""), ("urgente", "urgent", ""),  # Encounter 26
                ("peligroso", "dangerous", ""), ("sistema de frenos", "brake system", ""), ("sistema eléctrico", "electrical system", ""),  # Encounter 27
                ("presión", "pressure", ""), ("nivel", "level", ""), ("nivel de aceite", "oil level", ""),  # Encounter 28
                ("nivel bajo", "low level", ""), ("nivel alto", "high level", ""), ("luz de motor", "check-engine light", ""),  # Encounter 29
                ("código de error", "error code", ""), ("dejo el carro", "I leave the car", ""), ("recojo el carro", "I pick up the car", ""),  # Encounter 30
                ("listo", "ready", ""), ("todavía no", "not yet", ""), ("en proceso", "in progress", ""),  # Encounter 31
                ("espero", "I wait", ""), ("más tarde", "later", ""), ("hoy", "today", ""),  # Encounter 32
                ("mañana", "tomorrow", ""), ("tiempo estimado", "estimated time", ""), ("muy caro", "too expensive", ""),  # Encounter 33
                ("más barato", "cheaper", ""), ("solo eso", "just that", ""), ("no lo necesito", "I do not need it", ""),  # Encounter 34
                ("prefiero eso primero", "I prefer that first", ""), ("después vemos", "we look at the rest later", ""), ("no autorizo ese trabajo", "I do not authorize that work", ""),  # Encounter 35
                ("sin autorización", "without authorization", ""), ("quiero más detalle", "I want more detail", ""), ("líquido de frenos", "brake fluid", ""),  # Encounter 36
                ("aceite de motor", "engine oil", ""), ("refrigerante", "coolant", ""), ("líquido", "fluid", ""),  # Encounter 37
                ("combustible", "fuel", ""), ("gasolina", "gasoline", ""), ("diésel", "diesel", ""),  # Encounter 38
                ("tanque", "tank", ""), ("manguera", "hose", ""), ("válvula", "valve", ""),  # Encounter 39
                ("al frenar", "when I brake", ""), ("al arrancar", "when I start it", ""), ("en movimiento", "while it is moving", ""),  # Encounter 40
                ("en frío", "when it is cold", ""), ("en caliente", "when it is hot", ""), ("a alta velocidad", "at high speed", ""),  # Encounter 41
                ("a baja velocidad", "at low speed", ""), ("en curva", "in a turn", ""), ("en subida", "uphill", ""),  # Encounter 42
                ("en bajada", "downhill", ""), ("mecánico", "mechanic", ""), ("taller", "shop", ""),  # Encounter 43
                ("herramienta", "tool", ""), ("elevador", "lift", ""), ("garantía", "warranty", ""),  # Encounter 44
                ("servicio", "service", ""), ("revisión general", "general inspection", ""), ("mantenimiento", "maintenance", ""),  # Encounter 45
                ("historial", "service history", ""), ("diagnóstico completo", "full diagnosis", ""), ("no entiendo", "I do not understand", ""),  # Encounter 46
                ("¿puede repetir?", "can you repeat that?", ""), ("más despacio", "more slowly", ""), ("¿qué significa?", "what does that mean?", ""),  # Encounter 47
                ("pastillas de freno", "brake pads", ""), ("disco de freno", "brake rotor", ""), ("amortiguador", "shock absorber", ""),  # Encounter 48
                ("dirección", "steering", ""), ("alineación", "alignment", ""), ("balanceo", "wheel balancing", ""),  # Encounter 49
                ("embrague", "clutch", ""), ("escape", "exhaust", ""), ("filtro de aire", "air filter", ""),  # Encounter 50
            ],
        },
    ],
    "police": [
        {
            "title": "Traffic Stop",
            "goal": "Handle a traffic stop calmly by providing documents and following instructions",
            "word_prefix": "pol",
            "words": [
                ("policía", "police officer", ""), ("agente", "officer", ""), ("patrulla", "patrol car", ""),  # Encounter 1
                ("control policial", "traffic stop", ""), ("licencia de conducir", "driver's license", ""), ("registro del vehículo", "vehicle registration", ""),  # Encounter 2
                ("prueba de seguro", "proof of insurance", ""), ("documentos", "documents", ""), ("identificación", "ID", ""),  # Encounter 3
                ("¿licencia, por favor?", "your license, please?", ""), ("¿tiene el registro?", "do you have the registration?", ""), ("¿tiene seguro?", "do you have insurance?", ""),  # Encounter 4
                ("¿puede mostrarlo?", "can you show it?", ""), ("aquí tiene", "here you are", ""), ("está en el vehículo", "it is in the vehicle", ""),  # Encounter 5
                ("está en la guantera", "it is in the glove compartment", ""), ("lo detuve", "I stopped you", ""), ("parada", "stop", ""),  # Encounter 6
                ("¿sabe por qué lo detuve?", "do you know why I stopped you?", ""), ("exceso de velocidad", "speeding", ""), ("velocidad", "speed", ""),  # Encounter 7
                ("límite de velocidad", "speed limit", ""), ("zona", "zone", ""), ("en esta zona", "in this zone", ""),  # Encounter 8
                ("iba a", "were going at (speed)", ""), ("por encima de", "above", ""), ("infracción", "violation", ""),  # Encounter 9
                ("motivo", "reason", ""), ("vehículo", "vehicle", ""), ("carro", "car", ""),  # Encounter 10
                ("luces", "lights", ""), ("luz trasera", "tail light", ""), ("luz delantera", "headlight", ""),  # Encounter 11
                ("no funciona", "it does not work", ""), ("placa", "plate", ""), ("parabrisas", "windshield", ""),  # Encounter 12
                ("cinturón", "seatbelt", ""), ("sin cinturón", "without a seatbelt", ""), ("en regla", "in order", ""),  # Encounter 13
                ("apague el motor", "turn off the engine (Ud.)", ""), ("baje la ventana", "roll down the window (Ud.)", ""), ("salga del vehículo", "get out of the vehicle (Ud.)", ""),  # Encounter 14
                ("quédese en el vehículo", "stay in the vehicle (Ud.)", ""), ("espere aquí", "wait here (Ud.)", ""), ("despacio", "slowly", ""),  # Encounter 15
                ("con calma", "calmly", ""), ("siga mis instrucciones", "follow my instructions (Ud.)", ""), ("no se mueva", "do not move (Ud.)", ""),  # Encounter 16
                ("frenó fuerte", "braked hard (past)", ""), ("cambió de carril", "changed lanes (past)", ""), ("sin señalizar", "without signaling", ""),  # Encounter 17
                ("conducción peligrosa", "dangerous driving", ""), ("carril", "lane", ""), ("carril restringido", "restricted lane", ""),  # Encounter 18
                ("giro", "turn", ""), ("no señalizó", "did not signal (past)", ""), ("tráfico", "traffic", ""),  # Encounter 19
                ("intersección", "intersection", ""), ("semáforo", "traffic light", ""), ("luz roja", "red light", ""),  # Encounter 20
                ("luz verde", "green light", ""), ("¿de dónde viene?", "where are you coming from?", ""), ("¿a dónde va?", "where are you going?", ""),  # Encounter 21
                ("¿cuánto tiempo lleva manejando?", "how long have you been driving?", ""), ("¿es su vehículo?", "is this your vehicle?", ""), ("¿es un vehículo de alquiler?", "is it a rental vehicle?", ""),  # Encounter 22
                ("¿tiene el contrato?", "do you have the contract?", ""), ("¿ha consumido alcohol?", "have you consumed alcohol?", ""), ("¿ha tomado algo?", "have you had anything to drink?", ""),  # Encounter 23
                ("¿entiende?", "do you understand?", ""), ("¿puede explicar?", "can you explain it?", ""), ("alcohol", "alcohol", ""),  # Encounter 24
                ("prueba", "test", ""), ("prueba de alcohol", "breath test", ""), ("sople aquí", "blow here (Ud.)", ""),  # Encounter 25
                ("resultado", "result", ""), ("negativo", "negative", ""), ("positivo", "positive", ""),  # Encounter 26
                ("bajo la influencia", "under the influence", ""), ("sobrio", "sober", ""), ("verifican el sistema", "they check the system", ""),  # Encounter 27
                ("registro activo", "active registration", ""), ("seguro activo", "active insurance", ""), ("no aparece", "it does not show up", ""),  # Encounter 28
                ("pendiente", "pending", ""), ("multa", "ticket", ""), ("advertencia", "warning", ""),  # Encounter 29
                ("sanción", "penalty", ""), ("emiten la multa", "they issue the ticket", ""), ("dan una advertencia", "they give a warning", ""),  # Encounter 30
                ("paga la multa", "pay the ticket", ""), ("en línea", "online", ""), ("plazo", "deadline", ""),  # Encounter 31
                ("monto", "amount", ""), ("carretera", "road", ""), ("calle", "street", ""),  # Encounter 32
                ("zona urbana", "urban area", ""), ("zona escolar", "school zone", ""), ("autopista", "highway", ""),  # Encounter 33
                ("señal", "sign", ""), ("señalización", "road signage", ""), ("dirección", "direction", ""),  # Encounter 34
                ("carril derecho", "right lane", ""), ("alquiler", "rental", ""), ("contrato", "contract", ""),  # Encounter 35
                ("propietario", "owner", ""), ("está a su nombre", "it is in your name", ""), ("no es mío", "it is not mine", ""),  # Encounter 36
                ("vehículo prestado", "borrowed vehicle", ""), ("permiso del dueño", "owner's permission", ""), ("no lo encuentro", "I cannot find it", ""),  # Encounter 37
                ("no lo tengo", "I do not have it", ""), ("no carga", "it does not load", ""), ("sin señal", "without signal", ""),  # Encounter 38
                ("en el celular", "on the cellphone", ""), ("copia digital", "digital copy", ""), ("sin documento", "without the document", ""),  # Encounter 39
                ("vencido", "expired", ""), ("por vencer", "about to expire", ""), ("no es válido", "it is not valid", ""),  # Encounter 40
                ("no entiendo", "I do not understand", ""), ("¿puede repetir?", "can you repeat that?", ""), ("más despacio", "more slowly", ""),  # Encounter 41
                ("¿qué significa?", "what does that mean?", ""), ("¿es una multa?", "is it a ticket?", ""), ("¿es una advertencia?", "is it a warning?", ""),  # Encounter 42
                ("¿puedo irme?", "can I leave?", ""), ("¿puedo seguir?", "can I continue?", ""), ("control", "checkpoint", ""),  # Encounter 43
                ("oríllese", "pull over (Ud.)", ""), ("orilla", "roadside", ""), ("luces de emergencia", "hazard lights", ""),  # Encounter 44
                ("documento físico", "physical document", ""), ("permiso de conducir", "driver's license", ""), ("matrícula", "license plate", ""),  # Encounter 45
                ("agente de tránsito", "traffic officer", ""), ("triángulo", "warning triangle", ""), ("chaleco reflectante", "reflective vest", ""),  # Encounter 46
                ("accidente", "accident", ""), ("choque", "crash", ""), ("reporte", "report", ""),  # Encounter 47
                ("reporte policial", "police report", ""), ("testigo", "witness", ""), ("declaración", "statement", ""),  # Encounter 48
                ("firme aquí", "sign here (Ud.)", ""), ("corte", "court", ""), ("fecha de corte", "court date", ""),  # Encounter 49
                ("comparecencia", "court appearance", ""), ("grúa", "tow truck", ""), ("remolque", "towing", ""),  # Encounter 50
            ],
        },
    ],
    "restaurant": [
        {
            "title": "Eating Out",
            "goal": "Order food, interact with the server, and pay for your meal",
            "word_prefix": "rest",
            "words": [
                ("menú", "menu", ""), ("carta", "menu", ""), ("mesero", "waiter", ""),  # Encounter 1
                ("mesa", "table", ""), ("reserva", "reservation", ""), ("¿tienen reserva?", "do you have a reservation?", ""),  # Encounter 2
                ("mesa para dos", "table for two", ""), ("pido", "I order", ""), ("¿qué desea?", "what would you like?", ""),  # Encounter 3
                ("¿qué van a pedir?", "what are you going to order?", ""), ("tomo la orden", "I take the order", ""), ("aquí está el menú", "here is the menu", ""),  # Encounter 4
                ("recomendación", "recommendation", ""), ("¿qué recomienda?", "what do you recommend?", ""), ("plato", "dish", ""),  # Encounter 5
                ("entrada", "appetizer", ""), ("plato principal", "main dish", ""), ("postre", "dessert", ""),  # Encounter 6
                ("acompañamiento", "side dish", ""), ("guarnición", "side dish", ""), ("porción", "portion", ""),  # Encounter 7
                ("ingrediente", "ingredient", ""), ("salsa", "sauce", ""), ("arroz", "rice", ""),  # Encounter 8
                ("pollo", "chicken", ""), ("carne", "meat", ""), ("pescado", "fish", ""),  # Encounter 9
                ("verduras", "vegetables", ""), ("ensalada", "salad", ""), ("vegetariano", "vegetarian", ""),  # Encounter 10
                ("vegano", "vegan", ""), ("alergia", "allergy", ""), ("alérgico", "allergic", ""),  # Encounter 11
                ("frutos secos", "nuts", ""), ("sin", "without", ""), ("con", "with", ""),  # Encounter 12
                ("¿tiene…?", "does it have…?", ""), ("¿lleva…?", "does it come with…?", ""), ("sin picante", "not spicy", ""),  # Encounter 13
                ("picante", "spicy", ""), ("poco picante", "mildly spicy", ""), ("sin carne", "without meat", ""),  # Encounter 14
                ("sin gluten", "gluten-free", ""), ("¿se puede cambiar?", "can it be changed?", ""), ("bebida", "drink", ""),  # Encounter 15
                ("agua", "water", ""), ("con gas", "sparkling", ""), ("sin gas", "still", ""),  # Encounter 16
                ("refresco", "soda", ""), ("jugo", "juice", ""), ("cerveza", "beer", ""),  # Encounter 17
                ("vino", "wine", ""), ("copa", "glass", ""), ("botella", "bottle", ""),  # Encounter 18
                ("¿algo de tomar?", "would you like something to drink?", ""), ("tiempo de espera", "wait time", ""), ("¿cuánto tiempo tarda?", "how long does it take?", ""),  # Encounter 19
                ("regreso enseguida", "I come right back", ""), ("aquí está", "here it is", ""), ("falta", "it is missing", ""),  # Encounter 20
                ("no llegó", "it did not arrive", ""), ("pedimos la comida", "we order the food", ""), ("trae", "bring (command)", ""),  # Encounter 21
                ("lleva", "it comes with", ""), ("sirve", "it serves", ""), ("mesa lista", "ready table", ""),  # Encounter 22
                ("síganme", "follow me (Uds.)", ""), ("error", "mistake", ""), ("equivocado", "wrong", ""),  # Encounter 23
                ("no es esto", "this is not it", ""), ("no pedimos eso", "we did not order that", ""), ("falta esto", "this is missing", ""),  # Encounter 24
                ("cambio", "change", ""), ("cambian el plato", "they change the dish", ""), ("cocina", "kitchen", ""),  # Encounter 25
                ("preparan otro plato", "they prepare another dish", ""), ("tardó mucho", "it took too long", ""), ("frío", "cold", ""),  # Encounter 26
                ("caliente", "hot", ""), ("recalentado", "reheated", ""), ("¿qué es esto?", "what is this?", ""),  # Encounter 27
                ("¿qué lleva?", "what does it have?", ""), ("¿cómo es?", "what is it like?", ""), ("¿está listo?", "is it ready?", ""),  # Encounter 28
                ("¿falta mucho?", "is there much longer to wait?", ""), ("¿puede explicar?", "can you explain it?", ""), ("no entiendo", "I do not understand", ""),  # Encounter 29
                ("repítalo", "repeat it (Ud.)", ""), ("más despacio", "more slowly", ""), ("aclárelo", "clarify it (Ud.)", ""),  # Encounter 30
                ("cuenta", "bill", ""), ("la cuenta", "the bill", ""), ("total", "total", ""),  # Encounter 31
                ("precio", "price", ""), ("incluye", "it includes", ""), ("no incluye", "it does not include", ""),  # Encounter 32
                ("propina", "tip", ""), ("servicio", "service", ""), ("dividimos la cuenta", "we split the bill", ""),  # Encounter 33
                ("pago", "payment", ""), ("con tarjeta", "with a card", ""), ("en efectivo", "in cash", ""),  # Encounter 34
                ("terminal", "card terminal", ""), ("no funciona", "it does not work", ""), ("recibo", "receipt", ""),  # Encounter 35
                ("mesa libre", "free table", ""), ("ocupado", "occupied", ""), ("lleno", "full", ""),  # Encounter 36
                ("afuera", "outside", ""), ("adentro", "inside", ""), ("terraza", "patio", ""),  # Encounter 37
                ("aire acondicionado", "air conditioning", ""), ("ruido", "noise", ""), ("tranquilo", "quiet", ""),  # Encounter 38
                ("ambiente", "atmosphere", ""), ("para dos", "for two", ""), ("más", "more", ""),  # Encounter 39
                ("menos", "less", ""), ("suficiente", "enough", ""), ("extra", "extra", ""),  # Encounter 40
                ("otra", "another one", ""), ("lo mismo", "the same", ""), ("para llevar", "to go", ""),  # Encounter 41
                ("pedido", "order", ""), ("factura", "invoice", ""), ("reserva confirmada", "confirmed reservation", ""),  # Encounter 42
                ("mesa asignada", "assigned table", ""), ("lista de espera", "waitlist", ""), ("disponibilidad", "availability", ""),  # Encounter 43
                ("horario", "opening hours", ""), ("cubiertos", "utensils", ""), ("cuchara", "spoon", ""),  # Encounter 44
                ("tenedor", "fork", ""), ("cuchillo", "knife", ""), ("servilleta", "napkin", ""),  # Encounter 45
                ("vaso", "glass", ""), ("taza", "cup", ""), ("hielo", "ice", ""),  # Encounter 46
                ("sin hielo", "without ice", ""), ("otra ronda", "another round", ""), ("traen la cuenta", "they bring the bill", ""),  # Encounter 47
                ("cobro adicional", "extra charge", ""), ("cargo por servicio", "service charge", ""), ("plato hondo", "bowl", ""),  # Encounter 48
                ("plato llano", "dinner plate", ""), ("cubierto extra", "extra utensil", ""), ("para compartir", "to share", ""),  # Encounter 49
                ("recogen los platos", "they clear the plates", ""), ("mesa sucia", "dirty table", ""), ("mesa limpia", "clean table", ""),  # Encounter 50
            ],
        },
    ],
    "small_talk": [
        {
            "title": "Meeting a Neighbor",
            "goal": "Have a friendly conversation with your neighbor about building life",
            "word_prefix": "talk",
            "words": [
                ("vecino", "neighbor", ""), ("vecina", "female neighbor", ""), ("edificio", "building", ""),  # Encounter 1
                ("departamento", "apartment", ""), ("casa", "house", ""), ("zona", "area", ""),  # Encounter 2
                ("barrio", "neighborhood", ""), ("ruido", "noise", ""), ("música", "music", ""),  # Encounter 3
                ("volumen", "volume", ""), ("baja el volumen", "lower the volume", ""), ("reunión", "gathering", ""),  # Encounter 4
                ("fiesta", "party", ""), ("anoche", "last night", ""), ("tarde", "late", ""),  # Encounter 5
                ("temprano", "early", ""), ("trabajo temprano", "I work early", ""), ("no pude dormir", "I could not sleep", ""),  # Encounter 6
                ("quería comentarte algo", "I wanted to mention something to you", ""), ("solo quería avisarte", "I just wanted to let you know", ""), ("la próxima vez", "next time", ""),  # Encounter 7
                ("tenga cuidado", "be careful (Ud.)", ""), ("estacionamiento", "parking", ""), ("lugar", "spot", ""),  # Encounter 8
                ("espacio", "space", ""), ("mi lugar", "my spot", ""), ("asignado", "assigned", ""),  # Encounter 9
                ("visitante", "visitor", ""), ("mueve el carro", "move the car", ""), ("lo muevo ahora mismo", "I move it right now", ""),  # Encounter 10
                ("ya pasó dos veces", "it has already happened twice", ""), ("no sabía", "I did not know", ""), ("no fue intencional", "it was not intentional", ""),  # Encounter 11
                ("paquete", "package", ""), ("entrega", "delivery", ""), ("repartidor", "delivery person", ""),  # Encounter 12
                ("puerta", "door", ""), ("lo dejó aquí por error", "he left it here by mistake", ""), ("nombre", "name", ""),  # Encounter 13
                ("mi nombre", "my name", ""), ("aquí está su paquete", "here is your package", ""), ("lo tengo", "I have it", ""),  # Encounter 14
                ("se perdió", "it got lost", ""), ("pasa seguido", "it happens often", ""), ("hace tiempo", "a long time ago", ""),  # Encounter 15
                ("hace meses", "months ago", ""), ("hace un año", "a year ago", ""), ("vivo aquí", "I live here", ""),  # Encounter 16
                ("me mudé", "I moved", ""), ("¿te gusta vivir aquí?", "do you like living here?", ""), ("me gusta", "I like it", ""),  # Encounter 17
                ("es tranquilo", "it is quiet", ""), ("es ruidoso", "it is noisy", ""), ("agua", "water", ""),  # Encounter 18
                ("fuga", "leak", ""), ("humedad", "dampness", ""), ("pared", "wall", ""),  # Encounter 19
                ("tubería", "pipe", ""), ("problema de agua", "water issue", ""), ("administración", "building management", ""),  # Encounter 20
                ("ya llamé", "I already called", ""), ("no han venido", "they have not come", ""), ("mejor así", "it is better this way", ""),  # Encounter 21
                ("más urgente", "more urgent", ""), ("cierra la llave de agua", "shut off the water valve", ""), ("llave de agua", "water valve", ""),  # Encounter 22
                ("puede empeorar", "it can get worse", ""), ("avísame", "let me know", ""), ("me dices", "tell me", ""),  # Encounter 23
                ("entiendo", "I understand", ""), ("tiene sentido", "it makes sense", ""), ("cerca", "nearby", ""),  # Encounter 24
                ("lejos", "far", ""), ("piso", "floor", ""), ("mismo piso", "same floor", ""),  # Encounter 25
                ("arriba", "upstairs", ""), ("abajo", "downstairs", ""), ("toca la puerta", "knock on the door", ""),  # Encounter 26
                ("abre", "it opens", ""), ("cierra", "it closes", ""), ("trabajo", "work", ""),  # Encounter 27
                ("horario", "schedule", ""), ("ocupado", "busy", ""), ("libre", "free", ""),  # Encounter 28
                ("fin de semana", "weekend", ""), ("hoy", "today", ""), ("mañana", "tomorrow", ""),  # Encounter 29
                ("ayer", "yesterday", ""), ("en un rato", "in a little while", ""), ("prestas una herramienta", "lend a tool", ""),  # Encounter 30
                ("herramienta", "tool", ""), ("llave inglesa", "wrench", ""), ("taladro", "drill", ""),  # Encounter 31
                ("escalera", "ladder", ""), ("basura", "trash", ""), ("saco la basura", "I take out the trash", ""),  # Encounter 32
                ("reciclaje", "recycling", ""), ("ascensor", "elevator", ""), ("timbre", "doorbell", ""),  # Encounter 33
                ("portón", "gate", ""), ("entrada principal", "main entrance", ""), ("llave", "key", ""),  # Encounter 34
                ("copia de llave", "spare key", ""), ("administración del edificio", "building management", ""), ("portero", "doorman", ""),  # Encounter 35
                ("conserje", "caretaker", ""), ("paquete equivocado", "wrong package", ""), ("se confundieron de puerta", "they got the door wrong", ""),  # Encounter 36
                ("visita", "visitor", ""), ("visitas", "guests", ""), ("¿espera visitas?", "are you expecting guests?", ""),  # Encounter 37
                ("mudanza", "move", ""), ("camión de mudanza", "moving truck", ""), ("se mudan hoy", "they move today", ""),  # Encounter 38
                ("mascota", "pet", ""), ("perro", "dog", ""), ("gato", "cat", ""),  # Encounter 39
                ("correa", "leash", ""), ("ladra mucho", "it barks a lot", ""), ("¿cómo se llama?", "what is it called?", ""),  # Encounter 40
                ("jardín", "garden", ""), ("plantas", "plants", ""), ("riego", "watering", ""),  # Encounter 41
                ("riega las plantas", "water the plants", ""), ("balcón", "balcony", ""), ("ventana", "window", ""),  # Encounter 42
                ("corriente de aire", "draft", ""), ("hace frío aquí", "it is cold here", ""), ("hace calor aquí", "it is hot here", ""),  # Encounter 43
                ("humedad en el techo", "moisture on the ceiling", ""), ("corte de agua", "water outage", ""), ("corte de luz", "power outage", ""),  # Encounter 44
                ("luz", "electricity", ""), ("se fue la luz", "the power went out", ""), ("vuelve pronto", "it comes back soon", ""),  # Encounter 45
                ("vecino nuevo", "new neighbor", ""), ("recién llegado", "newly arrived", ""), ("¿desde cuándo vive aquí?", "since when do you live here?", ""),  # Encounter 46
                ("alquiler", "rent", ""), ("subió el alquiler", "the rent went up", ""), ("administración no responde", "management does not respond", ""),  # Encounter 47
                ("queja", "complaint", ""), ("pongo una queja", "I file a complaint", ""), ("ruido arriba", "upstairs noise", ""),  # Encounter 48
                ("ruido abajo", "downstairs noise", ""), ("pasillo", "hallway", ""), ("entrada trasera", "back entrance", ""),  # Encounter 49
                ("puerta principal", "front door", ""), ("buzón", "mailbox", ""), ("correo", "mail", ""),  # Encounter 50
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
