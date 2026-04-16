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
    "core": "Core",
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
                ("pasaporte", "passport", "passaport", "pass"), ("reserva", "reservation", "reserva", "bokning"), ("confirmación", "confirmation", "confirmació", "bekräftelse"),  # Encounter 1
                ("número de reserva", "reservation number", "número de reserva", "bokningsnummer"), ("nombre", "first name", "nom", "namn"), ("apellido", "last name", "cognom", "efternamn"),  # Encounter 2
                ("documento", "document", "document", "dokument"), ("identificación", "ID", "identificació", "legitimation"), ("visa", "visa", "visa", "visum"),  # Encounter 3
                ("permiso", "permit", "permís", "tillstånd"), ("documentos de viaje", "travel documents", "documents de viatge", "resehandlingar"), ("fecha de vencimiento", "expiration date", "data de caducitat", "utgångsdatum"),  # Encounter 4
                ("a nombre de", "under the name of", "a nom de", "i namnet på"), ("¿tiene reserva?", "do you have a reservation?", "té reserva?", "har du en bokning?"), ("¿me muestra el pasaporte?", "do you show me your passport?", "em pot mostrar el passaport?", "kan jag få se ditt pass?"),  # Encounter 5
                ("¿a qué nombre?", "under what name?", "a quin nom?", "på vilket namn?"), ("vuelo", "flight", "vol", "flyg"), ("número de vuelo", "flight number", "número de vol", "flygnummer"),  # Encounter 6
                ("destino", "destination", "destí", "destination"), ("destino final", "final destination", "destí final", "slutdestination"), ("origen", "origin", "origen", "ursprung"),  # Encounter 7
                ("conexión", "connection", "connexió", "anslutning"), ("vuelo de conexión", "connecting flight", "vol de connexió", "anslutningsflyg"), ("vuelo directo", "direct flight", "vol directe", "direktflyg"),  # Encounter 8
                ("vuelo lleno", "full flight", "vol ple", "fullbokat flyg"), ("vuelo anterior", "previous flight", "vol anterior", "tidigare flyg"), ("vuelo siguiente", "next flight", "vol següent", "nästa flyg"),  # Encounter 9
                ("¿va directo a…?", "does it go direct to…?", "va directe a…?", "går den direkt till…?"), ("¿hasta dónde va?", "how far does it go?", "fins a on va?", "hur långt går det?"), ("¿sale hoy?", "does it leave today?", "surt avui?", "går den idag?"),  # Encounter 10
                ("¿sale mañana?", "does it leave tomorrow?", "surt demà?", "går den imorgon?"), ("salida", "departure", "sortida", "utgång"), ("llegada", "arrival", "arribada", "ankomst"),  # Encounter 11
                ("embarque", "boarding", "embarcament", "ombordstigning"), ("hora de embarque", "boarding time", "hora d'embarcament", "ombordstigningstid"), ("hora de salida", "departure time", "hora de sortida", "avgångstid"),  # Encounter 12
                ("puerta", "gate", "porta", "dörr"), ("número de puerta", "gate number", "número de porta", "gate-nummer"), ("puerta de embarque", "boarding gate", "porta d’embarcament", "gate"),  # Encounter 13
                ("zona de embarque", "boarding area", "zona d'embarcament", "incheckningsområde"), ("preembarque", "preboarding", "preembarqui", "förboarding"), ("prioridad", "priority", "prioritat", "prioritet"),  # Encounter 14
                ("a tiempo", "on time", "a temps", "i tid"), ("retraso", "delay", "retard", "försening"), ("demora", "delay", "retard", "försening"),  # Encounter 15
                ("cambio de puerta", "gate change", "canvi de porta", "gatebyte"), ("¿cuál es la puerta?", "what is the gate?", "quina és la porta?", "vilken är gaten?"), ("aparece en las pantallas", "it appears on the screens", "apareix a les pantalles", "det visas på skärmarna"),  # Encounter 16
                ("aparece en la app", "it appears in the app", "apareix a l'app", "det visas i appen"), ("no está asignada", "it is not assigned", "no està assignada", "den är inte tilldelad"), ("asiento", "seat", "seient", "säte"),  # Encounter 17
                ("número de asiento", "seat number", "número de seient", "platsnummer"), ("fila", "row", "cua", "rad"), ("ventana", "window", "finestra", "fönster"),  # Encounter 18
                ("pasillo", "aisle", "passadís", "gång"), ("asiento del medio", "middle seat", "seient del mig", "mellansäte"), ("asiento de ventana", "window seat", "seient de finestra", "fönstersäte"),  # Encounter 19
                ("asiento de pasillo", "aisle seat", "seient del passadís", "gångsäte"), ("salida de emergencia", "exit row", "sortida d'emergència", "nödflykt"), ("juntos", "together", "junts", "tillsammans"),  # Encounter 20
                ("separados", "separate", "separats", "separerade"), ("¿prefiere ventana o pasillo?", "do you prefer a window or an aisle?", "prefereix finestra o passadís?", "föredrar du fönster eller gång?"), ("¿hay asientos juntos?", "are there seats together?", "hi ha seients junts?", "finns det sittplatser tillsammans?"),  # Encounter 21
                ("¿hay otro asiento?", "is there another seat?", "hi ha un altre seient?", "finns det en annan plats?"), ("cambio de asiento", "seat change", "canvi de seient", "sätebyte"), ("asignado", "assigned", "assignat", "tilldelad"),  # Encounter 22
                ("equipaje", "luggage", "equipatge", "bagage"), ("maleta", "suitcase", "maleta", "resväska"), ("equipaje de mano", "carry-on", "equipatge de mà", "handbagage"),  # Encounter 23
                ("equipaje facturado", "checked baggage", "equipatge facturat", "incheckat bagage"), ("maleta de cabina", "cabin bag", "maleta de cabina", "handbagage"), ("artículo personal", "personal item", "article personal", "personligt föremål"),  # Encounter 24
                ("primera maleta", "first bag", "primera maleta", "första väskan"), ("segunda maleta", "second bag", "segona maleta", "andra väskan"), ("etiqueta", "tag", "etiqueta", "etikett"),  # Encounter 25
                ("recibo de equipaje", "baggage receipt", "justificant d'equipatge", "bagagekvitto"), ("cinta", "carousel", "cinta transportadora", ""), ("recogida de equipaje", "baggage claim", "recollida d'equipatge", "bagageutlämning"),  # Encounter 26
                ("¿va a facturar equipaje?", "are you checking baggage?", "portarà equipatge per facturar?", "ska du checka in bagage?"), ("¿lleva equipaje?", "are you carrying luggage?", "porta equipatge?", "har du bagage med dig?"), ("balanza", "scale", "balança", "våg"),  # Encounter 27
                ("peso", "weight", "pes", "vikt"), ("límite", "limit", "límit", "gräns"), ("exceso", "excess", "excés", "överskott"),  # Encounter 28
                ("sobrepeso", "overweight", "sobrepès", "övervikt"), ("medidas", "dimensions", "mides", "mått"), ("medidas permitidas", "allowed dimensions", "mides permeses", "tillåtna mått"),  # Encounter 29
                ("está demasiado pesado", "it is too heavy", "és massa pesat", "det är för tungt"), ("está demasiado grande", "it is too big", "és massa gran", "det är för stort"), ("póngalo en la balanza", "put it on the scale (Ud.)", "posi-ho a la bàscula", "lägg det på vågen"),  # Encounter 30
                ("¿cuál es el límite?", "what is the limit?", "quin és el límit?", "vad är gränsen?"), ("¿cuánto cuesta?", "how much does it cost?", "quant costa?", "hur mycket kostar det?"), ("facturo el equipaje", "I check the baggage", "facturo l'equipatge", "jag checkar in bagaget"),  # Encounter 31
                ("etiquetan el equipaje", "they tag the baggage", "etiqueten l'equipatge", "de märker bagaget"), ("abre la maleta", "open the suitcase (Ud.)", "obri la maleta", "öppna resväskan"), ("saca los objetos", "take the items out (Ud.)", "treu els objectes", "ta ut föremålen"),  # Encounter 32
                ("pasa algunas cosas a la mochila", "move some things to the backpack (Ud.)", "passi algunes coses a la motxilla", "lägg några saker i ryggsäcken"), ("lo lleva con usted", "carry it with you", "el porti amb vostè", "ta med det med dig"), ("no puede ir en la maleta", "it cannot go in the suitcase", "no pot anar a la maleta", "det får inte plats i resväskan"),  # Encounter 33
                ("¿puede facturarlo?", "can you check it?", "pot facturar-ho?", "kan du checka in det?"), ("¿puede llevarlo con usted?", "can you carry it with you?", "pot portar-ho amb vostè?", "kan du ta med det?"), ("líquidos", "liquids", "líquids", "vätskor"),  # Encounter 34
                ("batería portátil", "power bank", "bateria externa", "powerbank"), ("cargador", "charger", "carregador", "laddare"), ("computadora", "laptop", "ordinador portàtil", "laptop"),  # Encounter 35
                ("objetos de valor", "valuables", "objectes de valor", "värdesaker"), ("medicinas", "medication", "medicaments", "mediciner"), ("¿lleva líquidos?", "are you carrying liquids?", "porta líquids?", "har du vätskor med dig?"),  # Encounter 36
                ("¿lleva baterías?", "are you carrying batteries?", "porta bateries?", "har du batterier med dig?"), ("no está permitido", "it is not allowed", "no està permès", "det är inte tillåtet"), ("está permitido", "it is allowed", "està permès", "det är tillåtet"),  # Encounter 37
                ("control de seguridad", "security check", "control de seguretat", "säkerhetskontroll"), ("revisión", "inspection", "revisió", "inspektion"), ("revisión adicional", "additional screening", "revisió addicional", "ytterligare kontroll"),  # Encounter 38
                ("selección aleatoria", "random selection", "selecció aleatòria", "slumpmässigt urval"), ("control", "checkpoint", "control", "kontrollpunkt"), ("seguridad", "security", "seguretat", "trygghet"),  # Encounter 39
                ("terminal", "terminal", "terminal", "terminal"), ("aeropuerto", "airport", "aeroport", "flygplats"), ("aerolínea", "airline", "aerolínia", "flygbolag"),  # Encounter 40
                ("mostrador", "counter", "taulell", "disk"), ("sistema", "system", "sistema", "system"), ("no funciona", "it does not work", "no funciona", "det fungerar inte"),  # Encounter 41
                ("exceso de equipaje", "excess baggage", "excés d'equipatge", "övervikt på bagage"), ("paga el exceso", "pay the excess fee (Ud.)", "pagi l’excés", "betala övervikten"), ("con tarjeta", "with a card", "amb targeta", "med kort"),  # Encounter 42
                ("en efectivo", "in cash", "en efectiu", "kontant"), ("sin costo", "with no charge", "sense cost", "kostnadsfritt"), ("tarifa", "fee", "tarifa", "avgift"),  # Encounter 43
                ("total", "total", "total", "totalt"), ("recibo", "receipt", "rebut", "kvitto"), ("pasajero", "passenger", "passatger", "passagerare"),  # Encounter 44
                ("familia", "family", "família", "familj"), ("niño", "child", "nen", "barn"), ("niña", "girl", "nena", "flicka"),  # Encounter 45
                ("coche de bebé", "stroller", "cotxet", ""), ("hasta la puerta", "up to the gate", "fins a la porta", "fram till gaten"), ("tarjeta de embarque", "boarding pass", "targeta d'embarcament", "boardingkort"),  # Encounter 46
                ("imprimen la tarjeta de embarque", "they print the boarding pass", "imprimeixen la targeta d'embarcament", "de skriver ut boardingkortet"), ("celular", "cellphone", "telèfon mòbil", ""), ("correo", "email", "correu", "e-post"),  # Encounter 47
                ("confirmación por correo", "email confirmation", "confirmació per correu", "bekräftelse via e-post"), ("hay espacio", "there is space", "hi ha espai", "det finns plats"), ("no hay espacio", "there is no space", "no hi ha espai", "det finns inget utrymme"),  # Encounter 48
                ("conexión corta", "short connection", "connexió curta", "kort anslutning"), ("conexión larga", "long connection", "connexió llarga", "lång anslutning"), ("aduana", "customs", "duana", "tull"),  # Encounter 49
                ("migración", "immigration", "migració", "migration"), ("control migratorio", "immigration control", "control migratori", "gränskontroll"), ("formulario de aduana", "customs form", "formulari de duana", "tullformulär"),  # Encounter 50
            ],
        },
    ],
    "banking": [
        {
            "title": "Banking",
            "goal": "Handle banking tasks including accounts, transfers, cards, and loans",
            "word_prefix": "bank",
            "words": [
                ("banco", "bank", "banc", "bank"), ("cajero", "teller", "caixer", "kassör"), ("cliente", "customer", "client", ""),  # Encounter 1
                ("cuenta", "account", "compte", "konto"), ("cuenta bancaria", "bank account", "compte bancari", "bankkonto"), ("saldo", "balance", "saldo", "saldo"),  # Encounter 2
                ("saldo disponible", "available balance", "saldo disponible", "tillgängligt saldo"), ("saldo actual", "current balance", "saldo actual", "aktuellt saldo"), ("tarjeta", "card", "targeta", "kort"),  # Encounter 3
                ("tarjeta de débito", "debit card", "targeta de dèbit", "betalkort"), ("tarjeta de crédito", "credit card", "targeta de crèdit", "kreditkort"), ("tarjeta bloqueada", "blocked card", "targeta bloquejada", "blockerat kort"),  # Encounter 4
                ("tarjeta nueva", "new card", "targeta nova", "nytt kort"), ("PIN", "PIN", "PIN", "PIN"), ("clave", "PIN", "clau", ""),  # Encounter 5
                ("contraseña", "password", "contrasenya", "lösenord"), ("número de cuenta", "account number", "número de compte", "kontonummer"), ("número incorrecto", "wrong number", "número incorrecte", "fel nummer"),  # Encounter 6
                ("transferencia", "transfer", "transferència", "överföring"), ("transferencia enviada", "sent transfer", "transferència enviada", "skickad överföring"), ("transferencia recibida", "received transfer", "transferència rebuda", "mottagen överföring"),  # Encounter 7
                ("no llegó", "it did not arrive", "no va arribar", "det kom inte"), ("llegó tarde", "it arrived late", "va arribar tard", "den kom för sent"), ("comprobante", "receipt", "justificant", "kvitto"),  # Encounter 8
                ("muestro el comprobante", "I show the receipt", "mostro el comprovant", "jag visar kvittot"), ("reviso la cuenta", "I check the account", "reviso el compte", "jag kontrollerar kontot"), ("revisan los movimientos", "they check the transactions", "revisen els moviments", "de kontrollerar transaktionerna"),  # Encounter 9
                ("movimientos", "transactions", "moviments", "transaktioner"), ("cargo", "charge", "càrrec", "avgift"), ("cargos extra", "extra charges", "càrrecs extra", "extra avgifter"),  # Encounter 10
                ("no lo reconozco", "I do not recognize it", "no el reconec", "jag känner inte igen det"), ("cargo sospechoso", "suspicious charge", "càrrec sospitós", "misstänkt avgift"), ("intento sospechoso", "suspicious attempt", "intent sospitós", "misstänkt försök"),  # Encounter 11
                ("bloqueo", "block", "bloqueig", "blockering"), ("se bloqueó", "it got blocked", "es va bloquejar", "den låste sig"), ("desbloquean la tarjeta", "they unblock the card", "desbloquegen la targeta", "de låser upp kortet"),  # Encounter 12
                ("activan la tarjeta", "they activate the card", "activen la targeta", "de aktiverar kortet"), ("emiten la tarjeta", "they issue the card", "emeten la targeta", "de utfärdar kortet"), ("funciona ahora", "it works now", "funciona ara", "det fungerar nu"),  # Encounter 13
                ("no funciona", "it does not work", "no funciona", "det fungerar inte"), ("rechazada", "declined", "rebutjada", "avvisad"), ("pago rechazado", "declined payment", "pagament rebutjat", "avvisad betalning"),  # Encounter 14
                ("hago el pago", "I make the payment", "faig el pagament", "jag gör betalningen"), ("pago aprobado", "approved payment", "pagament aprovat", "godkänd betalning"), ("pago pendiente", "pending payment", "pagament pendent", "obetalad betalning"),  # Encounter 15
                ("monto", "amount", "import", "belopp"), ("monto total", "total amount", "import total", "totalt belopp"), ("cantidad", "amount", "quantitat", "mängd"),  # Encounter 16
                ("deposito dinero", "I deposit money", "diposito diners", "jag sätter in pengar"), ("retiro", "withdrawal", "retirada", "uttag"), ("retiro dinero", "I withdraw money", "retiro diners", "jag tar ut pengar"),  # Encounter 17
                ("efectivo", "cash", "efectiu", "kontanter"), ("con tarjeta", "with a card", "amb targeta", "med kort"), ("cajero automático", "ATM", "caixer automàtic", "bankomat"),  # Encounter 18
                ("retiro en el cajero", "I withdraw at the ATM", "retiro a l'caixer", "jag tar ut pengar i bankomaten"), ("saldo insuficiente", "insufficient funds", "saldo insuficient", "otillräckligt saldo"), ("no hay fondos", "there are no funds", "no hi ha fons", "det finns inga medel"),  # Encounter 19
                ("hay fondos", "there are funds", "hi ha fons", "det finns medel"), ("abro una cuenta", "I open an account", "obro un compte", "jag öppnar ett konto"), ("abro una cuenta nueva", "I open a new account", "obro un compte nou", "jag öppnar ett nytt konto"),  # Encounter 20
                ("cierro la cuenta", "I close the account", "tanco el compte", ""), ("cambio de cuenta", "account change", "canvi de compte", "kontobyte"), ("tipo de cuenta", "account type", "tipus de compte", "kontotyp"),  # Encounter 21
                ("cuenta principal", "main account", "compte principal", "huvudkonto"), ("cuenta de ahorros", "savings account", "compte d’estalvi", "sparkonto"), ("cuenta corriente", "checking account", "compte corrent", "checkkonto"),  # Encounter 22
                ("comisión", "fee", "comissió", "avgift"), ("cobran comisión", "they charge a fee", "cobren comissió", ""), ("sin comisión", "without a fee", "sense comissió", "utan avgift"),  # Encounter 23
                ("comisión mensual", "monthly fee", "comissió mensual", "månatlig avgift"), ("eliminan la comisión", "they remove the fee", "eliminar la comissió", "de tar bort avgiften"), ("contrato", "contract", "contracte", "kontrakt"),  # Encounter 24
                ("condiciones", "terms", "condicions", "villkor"), ("saldo mínimo", "minimum balance", "saldo mínim", "minimalt saldo"), ("requiere saldo mínimo", "it requires a minimum balance", "requereix saldo mínim", "det kräver minsta saldo"),  # Encounter 25
                ("requiere depósitos", "it requires deposits", "requereix dipòsits", "det kräver insättningar"), ("historial", "history", "historial", "historik"), ("historial crediticio", "credit history", "historial creditici", "kredithistorik"),  # Encounter 26
                ("crédito", "credit", "crèdit", "kredit"), ("buen crédito", "good credit", "bon crèdit", "bra kredit"), ("mal crédito", "bad credit", "mal crèdit", "dålig kredit"),  # Encounter 27
                ("préstamo", "loan", "préstec", "lån"), ("solicito un préstamo", "I apply for a loan", "sol·licito un préstec", "jag ansöker om ett lån"), ("monto del préstamo", "loan amount", "import del préstec", "lånebelopp"),  # Encounter 28
                ("aprueban el préstamo", "they approve the loan", "aproven el préstec", "de godkänner lånet"), ("rechazan el préstamo", "they reject the loan", "rebutgen el préstec", "de avslår lånet"), ("aprobación", "approval", "aprovació", "godkännande"),  # Encounter 29
                ("está en proceso", "it is in process", "està en procés", "det är på gång"), ("solicitud", "application", "sol·licitud", "ansökan"), ("envío la solicitud", "I send the application", "envio la sol·licitud", "jag skickar ansökan"),  # Encounter 30
                ("documentos", "documents", "documents", "dokument"), ("falta un documento", "one document is missing", "falta un document", "ett dokument saknas"), ("envío los documentos", "I send the documents", "envio els documents", "jag skickar dokumenten"),  # Encounter 31
                ("comprobante de ingresos", "proof of income", "justificant d'ingressos", "inkomstbevis"), ("revisan el sistema", "they check the system", "revisen el sistema", "de kontrollerar systemet"), ("el sistema falla", "the system fails", "el sistema falla", "systemet kraschar"),  # Encounter 32
                ("el sistema está lento", "the system is slow", "el sistema està lent", "systemet är långsamt"), ("error del sistema", "system error", "error del sistema", "systemfel"), ("abren un caso", "they open a case", "obren un cas", "de öppnar ett ärende"),  # Encounter 33
                ("número de caso", "case number", "número de cas", "ärendenummer"), ("seguimiento del caso", "case follow-up", "seguiment del cas", "ärendeuppföljning"), ("tarda unos días", "it takes a few days", "triga uns dies", "det tar några dagar"),  # Encounter 34
                ("tiempo estimado", "estimated time", "temps estimat", "beräknad tid"), ("depende del sistema", "it depends on the system", "depèn del sistema", "det beror på systemet"), ("espero la respuesta", "I wait for the response", "espero la resposta", "jag väntar på svaret"),  # Encounter 35
                ("hoy no", "not today", "avui no", "inte idag"), ("mañana sí", "tomorrow yes", "demà sí", "imorgon ja"), ("llamo al banco", "I call the bank", "truco al banc", "jag ringer banken"),  # Encounter 36
                ("atención al cliente", "customer service", "atenció al client", "kundservice"), ("hablo con un agente", "I speak with an agent", "parlo amb un agent", "jag pratar med en agent"), ("verifican mi identidad", "they verify my identity", "verifiquen la meva identitat", "de verifierar min identitet"),  # Encounter 37
                ("confirman mis datos", "they confirm my information", "confirmen les meves dades", "de bekräftar mina uppgifter"), ("fecha de nacimiento", "birth date", "data de naixement", "födelsedatum"), ("dirección", "address", "adreça", "adress"),  # Encounter 38
                ("número de teléfono", "phone number", "número de telèfon", "telefonnummer"), ("correo electrónico", "email", "correu electrònic", "e-post"), ("actualizan mis datos", "they update my information", "actualitzen les meves dades", "de uppdaterar mina uppgifter"),  # Encounter 39
                ("datos incorrectos", "incorrect information", "dades incorrectes", "felaktiga uppgifter"), ("cambio mis datos", "I change my information", "canvio les meves dades", "jag ändrar mina uppgifter"), ("código de seguridad", "security code", "codi de seguretat", "säkerhetskod"),  # Encounter 40
                ("envían el código", "they send the code", "envien el codi", "de skickar koden"), ("ingreso el código", "I enter the code", "introdueixo el codi", "jag anger koden"), ("código válido", "valid code", "codi vàlid", "giltig kod"),  # Encounter 41
                ("código inválido", "invalid code", "codi invàlid", "ogiltig kod"), ("acceso a la cuenta", "account access", "accés al compte", "åtkomst till kontot"), ("no tengo acceso", "I do not have access", "no tinc accés", "jag har inte tillgång"),  # Encounter 42
                ("recupero el acceso", "I recover access", "recupero l'accés", "jag återfår tillgången"), ("restablecen la clave", "they reset the password", "restableixen la clau", "de återställer lösenordet"), ("cambio la clave", "I change the PIN", "canvio el codi PIN", "jag byter koden"),  # Encounter 43
                ("bloquean el acceso", "they block the access", "bloquegen l'accés", "de blockerar tillgången"), ("acceso activo", "active access", "accés actiu", "aktiv åtkomst"), ("sigue igual", "it is still the same", "segueix igual", "det är fortfarande samma"),  # Encounter 44
                ("mejora un poco", "it improves a little", "millora una mica", "det förbättras lite"), ("no mejora", "it does not improve", "no millora", "det blir inte bättre"), ("¿qué pasó?", "what happened?", "què va passar?", "vad hände?"),  # Encounter 45
                ("¿qué hago?", "what do I do?", "què faig?", "vad ska jag göra?"), ("¿cuánto tarda?", "how long does it take?", "quant triga?", "hur lång tid tar det?"), ("¿cuánto cuesta?", "how much does it cost?", "quant costa?", "hur mycket kostar det?"),  # Encounter 46
                ("no entiendo", "I do not understand", "no entenc", "jag förstår inte"), ("¿puede repetir?", "can you repeat that?", "pot repetir-ho?", "kan du upprepa?"), ("más despacio", "more slowly", "més a poc a poc", "långsammare"),  # Encounter 47
                ("sucursal", "branch", "sucursal", "filial"), ("ejecutivo", "bank advisor", "assessor bancari", "bankrådgivare"), ("ventanilla", "teller window", "mostrador", "lucka"),  # Encounter 48
                ("firma registrada", "signature on file", "signatura registrada", "registrerad signatur"), ("la firma no coincide", "the signature does not match", "la signatura no coincideix", "signaturen stämmer inte"), ("transferencia internacional", "international transfer", "transferència internacional", "internationell överföring"),  # Encounter 49
                ("tipo de cambio", "exchange rate", "tipus de canvi", "växelkurs"), ("comisión por transferencia", "transfer fee", "comissió per transferència", "överföringsavgift"), ("fondos retenidos", "held funds", "fons retinguts", "hållna medel"),  # Encounter 50
            ],
        },
    ],
    "clothing": [
        {
            "title": "Clothing Shopping",
            "goal": "Navigate a clothing store, find your size, make a purchase, and handle returns",
            "word_prefix": "cloth",
            "words": [
                ("vendedor", "salesperson", "venedor", "säljare"), ("cliente", "customer", "client", ""), ("tienda", "store", "botiga", "butik"),  # Encounter 1
                ("ropa", "clothing", "roba", "kläder"), ("camisa", "shirt", "camisa", "skjorta"), ("pantalón", "pants", "pantalons", "byxor"),  # Encounter 2
                ("chaqueta", "jacket", "jaqueta", ""), ("vestido", "dress", "vestit", "klänning"), ("falda", "skirt", "falda", "kjol"),  # Encounter 3
                ("talla", "size", "mida", "storlek"), ("¿qué talla usa?", "what size do you wear?", "quina talla fa servir?", "vilken storlek har du?"), ("le queda bien", "it fits you well", "li queda bé", "den passar dig bra"),  # Encounter 4
                ("le queda grande", "it is too big on you", "li queda gran", "den är för stor för dig"), ("le queda pequeño", "it is too small on you", "li queda petit", "den är för liten för dig"), ("no le queda", "it does not fit you", "no li queda", "det passar dig inte"),  # Encounter 5
                ("otra talla", "another size", "una altra talla", "en annan storlek"), ("más grande", "bigger", "més gran", "större"), ("más pequeño", "smaller", "més petit", "mindre"),  # Encounter 6
                ("probador", "fitting room", "probador", "provrum"), ("usa el probador", "use the fitting room", "fes servir el vestidor", "använd provrummet"), ("espere su turno", "wait your turn (Ud.)", "esperi el seu torn", "vänta på din tur"),  # Encounter 7
                ("hay fila", "there is a line", "hi ha cua", "det är kö"), ("modelo", "style", "model", "modell"), ("mismo modelo", "same style", "mateix model", "samma modell"),  # Encounter 8
                ("modelo diferente", "different style", "model diferent", "annan modell"), ("color", "color", "color", "färg"), ("otro color", "another color", "un altre color", "en annan färg"),  # Encounter 9
                ("no hay talla", "there is no size available", "no hi ha talla", "det finns ingen storlek"), ("no hay stock", "there is no stock", "no hi ha estoc", "det finns ingen lager"), ("está agotado", "it is sold out", "està esgotat", "det är slut"),  # Encounter 10
                ("reviso el stock", "I check the stock", "reviso l'estoc", "jag kontrollerar lagret"), ("reviso el sistema", "I check the system", "reviso el sistema", "jag kontrollerar systemet"), ("hay en otra sucursal", "it is available at another branch", "hi ha en una altra sucursal", "det finns på en annan filial"),  # Encounter 11
                ("otra sucursal", "another branch", "una altra sucursal", "en annan filial"), ("lo pueden pedir", "they can order it", "ho poden demanar", "de kan beställa det"), ("llega en unos días", "it arrives in a few days", "arriba en uns dies", "den kommer om några dagar"),  # Encounter 12
                ("tarda unos días", "it takes a few days", "triga uns dies", "det tar några dagar"), ("lo aparto", "I put it on hold", "el reservo", "jag reserverar den"), ("apartado", "item on hold", "apartat", "avsnitt"),  # Encounter 13
                ("precio", "price", "preu", "pris"), ("precio normal", "regular price", "preu normal", "ordinarie pris"), ("precio de oferta", "sale price", "preu d'oferta", "erbjudandepris"),  # Encounter 14
                ("descuento", "discount", "descompte", "rabatt"), ("el descuento aplica", "the discount applies", "el descompte s'aplica", "rabatten gäller"), ("no aplica", "it does not apply", "no s'aplica", "det gäller inte"),  # Encounter 15
                ("promoción", "promotion", "promoció", "kampanj"), ("condición", "condition", "condició", "villkor"), ("con membresía", "with membership", "amb membresia", "med medlemskap"),  # Encounter 16
                ("sin membresía", "without membership", "sense membresia", "utan medlemskap"), ("registro", "sign-up", "registre", "registrering"), ("no quiero registrarme", "I do not want to sign up", "no vull registrar-me", "jag vill inte registrera mig"),  # Encounter 17
                ("el sistema marca otro precio", "the system shows another price", "el sistema marca un altre preu", "systemet visar ett annat pris"), ("no coincide", "it does not match", "no coincideix", "det stämmer inte"), ("reviso el precio", "I check the price", "reviso el preu", "jag kontrollerar priset"),  # Encounter 18
                ("corrigen el precio", "they correct the price", "corregixen el preu", "de rättar priset"), ("ajuste manual", "manual adjustment", "ajust manual", "manuell justering"), ("etiqueta", "tag", "etiqueta", "etikett"),  # Encounter 19
                ("mal etiquetado", "mislabeled", "mal etiquetat", "felmärkt"), ("letrero", "sign", "rètol", "skylt"), ("política de la tienda", "store policy", "política de la botiga", "butikens policy"),  # Encounter 20
                ("no aceptamos devoluciones", "we do not accept returns", "no acceptem devolucions", "vi accepterar inte returer"), ("solo damos crédito de tienda", "we only give store credit", "només donem crèdit de botiga", "vi ger bara butikskredit"), ("crédito de tienda", "store credit", "crèdit de botiga", "butikskredit"),  # Encounter 21
                ("devolución", "refund", "devolució", "återbetalning"), ("procesan la devolución", "they process the refund", "procesen la devolució", "de behandlar återbetalningen"), ("cambio de producto", "exchange", "canvi de producte", "produktbyte"),  # Encounter 22
                ("producto defectuoso", "defective item", "producte defectuós", "defekt vara"), ("está roto", "it is broken", "està trencat", "det är trasigt"), ("costura rota", "torn seam", "costura trencada", "trasig söm"),  # Encounter 23
                ("recibo", "receipt", "rebut", "kvitto"), ("tiene recibo", "do you have a receipt?", "té rebut?", "har du kvitto?"), ("sin recibo", "without a receipt", "sense rebut", "utan kvitto"),  # Encounter 24
                ("dentro del plazo", "within the return window", "dins del termini", "inom returperioden"), ("fuera del plazo", "outside the return window", "fora del termini", "utanför returperioden"), ("quiero hablar con la gerente", "I want to speak with the manager", "vull parlar amb la gerent", "jag vill prata med chefen"),  # Encounter 25
                ("gerente", "manager", "gerent", "chef"), ("excepción", "exception", "excepció", "undantag"), ("aprueban la excepción", "they approve the exception", "aproven l'excepció", "de godkänner undantaget"),  # Encounter 26
                ("caja", "checkout", "caixa", "kassa"), ("total", "total", "total", "totalt"), ("monto total", "total amount", "import total", "totalt belopp"),  # Encounter 27
                ("pago", "payment", "pagament", "betalning"), ("inserta la tarjeta", "insert the card", "insereix la targeta", "sätt i kortet"), ("acerca la tarjeta", "tap the card", "acosta la targeta", "håll kortet nära"),  # Encounter 28
                ("pasa la tarjeta", "swipe the card", "passi la targeta", "dra kortet"), ("no pasa", "it does not go through", "no passa", "det går inte igenom"), ("inténtalo otra vez", "try again", "torna-ho a provar", "försök igen"),  # Encounter 29
                ("pago aprobado", "approved payment", "pagament aprovat", "godkänd betalning"), ("pago rechazado", "declined payment", "pagament rebutjat", "avvisad betalning"), ("otra tarjeta", "another card", "una altra targeta", "ett annat kort"),  # Encounter 30
                ("efectivo", "cash", "efectiu", "kontanter"), ("pago en efectivo", "cash payment", "pagament en efectiu", "kontant betalning"), ("firma aquí", "sign here (Ud.)", "signi aquí", "skriv under här"),  # Encounter 31
                ("bolsa", "bag", "bossa", "väska"), ("¿quiere bolsa?", "do you want a bag?", "vol bossa?", "vill du ha en påse?"), ("bolsa grande", "big bag", "bossa gran", "stor väska"),  # Encounter 32
                ("bolsa pequeña", "small bag", "bossa petita", "liten väska"), ("sin bolsa", "no bag", "sense bossa", "utan påse"), ("lo empacan", "they pack it", "el empaqueten", "de packar den"),  # Encounter 33
                ("fila larga", "long line", "cua llarga", "lång kö"), ("mucha gente", "many people", "molta gent", "många människor"), ("espera larga", "long wait", "espera llarga", "lång väntan"),  # Encounter 34
                ("tarda mucho", "it takes a long time", "triga molt", "det tar lång tid"), ("servicio lento", "slow service", "servei lent", "långsam service"), ("está abierto", "it is open", "està obert", "det är öppet"),  # Encounter 35
                ("está cerrado", "it is closed", "està tancat", "det är stängt"), ("horario", "store hours", "horari", "öppettider"), ("identificación", "ID", "identificació", "legitimation"),  # Encounter 36
                ("muestra su identificación", "show your ID (Ud.)", "mostri la seva identificació", "visa din legitimation"), ("alarma", "alarm", "alarma", "larm"), ("sensor", "security tag", "sensor", "säkerhetsetikett"),  # Encounter 37
                ("quitan el sensor", "they remove the security tag", "treuen l'etiqueta de seguretat", "de tar bort larmet"), ("sensor activo", "active security tag", "sensor actiu", "aktiv säkerhetsetikett"), ("la alarma suena", "the alarm goes off", "la alarma sona", "larmet går"),  # Encounter 38
                ("revisan la compra", "they check the purchase", "revisen la compra", "de kontrollerar köpet"), ("el código escanea", "the barcode scans", "el codi escaneja", "koden skannas"), ("el código no escanea", "the barcode does not scan", "el codi no escaneja", "koden skannas inte"),  # Encounter 39
                ("ingreso manual", "manual entry", "introducció manual", "manuell inmatning"), ("código manual", "manual code", "codi manual", "manuell kod"), ("problema del sistema", "system issue", "problema del sistema", "systemproblem"),  # Encounter 40
                ("ya quedó", "it is fixed now", "ja està arreglat", "det är fixat nu"), ("sigue igual", "it is still the same", "segueix igual", "det är fortfarande samma"), ("talla correcta", "correct size", "mida correcta", "rätt storlek"),  # Encounter 41
                ("talla incorrecta", "wrong size", "mida incorrecta", "fel storlek"), ("se lo traigo", "I bring it to you", "li ho porto", "jag hämtar den åt dig"), ("no le queda bien", "it does not fit you well", "no li queda bé", "den passar dig inte bra"),  # Encounter 42
                ("le queda mejor", "it fits you better", "li queda millor", "den passar dig bättre"), ("me lo llevo", "I am taking it", "me'l porto", "jag tar det"), ("devolución parcial", "partial refund", "devolució parcial", "delåterbetalning"),  # Encounter 43
                ("monto reembolsado", "refunded amount", "import reemborsat", "återbetalat belopp"), ("te lo cambio", "I exchange it for you", "te'l canvio", "jag byter det åt dig"), ("te hago un descuento", "I give you a discount", "et faig un descompte", "jag ger dig rabatt"),  # Encounter 44
                ("caja abierta", "open register", "caixa oberta", "öppen kassa"), ("caja cerrada", "closed register", "caixa tancada", "stängd kassa"), ("precio final", "final price", "preu final", "slutpris"),  # Encounter 45
                ("cupón", "coupon", "cupó", "kupong"), ("el cupón vence hoy", "the coupon expires today", "el cupó venç avui", "kupongen går ut idag"), ("temporada", "season", "temporada", "säsong"),  # Encounter 46
                ("colección nueva", "new collection", "col·lecció nova", "ny kollektion"), ("prenda", "garment", "prenda", "plagg"), ("prenda dañada", "damaged garment", "prenda danyada", "skadat plagg"),  # Encounter 47
                ("defecto de fábrica", "manufacturing defect", "defecte de fàbrica", "fabrikationsfel"), ("marca", "brand", "marca", "märke"), ("misma marca", "same brand", "mateixa marca", "samma märke"),  # Encounter 48
                ("línea premium", "premium line", "línia premium", "premiumlinje"), ("material", "material", "material", "material"), ("algodón", "cotton", "cotó", "bomull"),  # Encounter 49
                ("tela", "fabric", "tela", "tyg"), ("se encoge", "it shrinks", "es contrau", "den krymper"), ("destiñe", "it bleeds color", "destenyeix", "det färgar av sig"),  # Encounter 50
            ],
        },
    ],
    "contractor": [
        {
            "title": "Hiring a Contractor",
            "goal": "Manage a construction project, discuss plans, costs, and quality with your contractor",
            "word_prefix": "contr",
            "words": [
                ("contratista", "contractor", "contractista", "entreprenör"), ("trabajador", "worker", "treballador", "arbetare"), ("equipo", "crew", "equip", "team"),  # Encounter 1
                ("proyecto", "project", "projecte", "projekt"), ("obra", "construction work", "obra", "byggarbete"), ("trabajo", "work", "feina", "arbete"),  # Encounter 2
                ("plano", "plan", "plànol", "plan"), ("diseño", "design", "disseny", "design"), ("presupuesto", "budget", "pressupost", "offert"),  # Encounter 3
                ("estimado", "estimate", "estimació", "uppskattning"), ("costo", "cost", "cost", "kostnad"), ("precio", "price", "preu", "pris"),  # Encounter 4
                ("total", "total", "total", "totalt"), ("pago", "payment", "pagament", "betalning"), ("anticipo", "deposit", "avançament", "förskottsbetalning"),  # Encounter 5
                ("pago final", "final payment", "pagament final", "slutbetalning"), ("material", "material", "material", "material"), ("materiales", "materials", "materials", "material"),  # Encounter 6
                ("proveedor", "supplier", "proveïdor", "leverantör"), ("disponibilidad", "availability", "disponibilitat", "tillgänglighet"), ("no está disponible", "it is not available", "no està disponible", "det är inte tillgängligt"),  # Encounter 7
                ("retraso", "delay", "retard", "försening"), ("atraso", "delay", "retard", "försening"), ("va atrasado", "it is running late", "va amb retard", "den är försenad"),  # Encounter 8
                ("a tiempo", "on time", "a temps", "i tid"), ("horario", "schedule", "horari", "öppettider"), ("cumplen el horario", "they keep the schedule", "compleixen l’horari", "de håller schemat"),  # Encounter 9
                ("tiempo estimado", "estimated time", "temps estimat", "beräknad tid"), ("terminan hoy", "they finish today", "acaben avui", "de slutar idag"), ("empiezan hoy", "they start today", "comencen avui", "de börjar idag"),  # Encounter 10
                ("siguen trabajando", "they keep working", "segueixen treballant", "de fortsätter arbeta"), ("trabajo detenido", "stopped work", "feina aturada", "stoppat arbete"), ("revisan esto", "they check this", "revisen això", "de kontrollerar detta"),  # Encounter 11
                ("inspección", "inspection", "inspecció", "inspektion"), ("ajuste", "adjustment", "ajust", "justering"), ("alternativa", "alternative", "alternativa", "alternativ"),  # Encounter 12
                ("calidad", "quality", "qualitat", "kvalitet"), ("misma calidad", "same quality", "mateixa qualitat", "samma kvalitet"), ("es diferente", "it is different", "és diferent", "det är annorlunda"),  # Encounter 13
                ("mejor opción", "better option", "millor opció", "bättre alternativ"), ("es más caro", "it is more expensive", "és més car", "det är dyrare"), ("es más barato", "it is cheaper", "és més barat", "det är billigare"),  # Encounter 14
                ("costo adicional", "additional cost", "cost addicional", "extra kostnad"), ("no estaba incluido", "it was not included", "no estava inclòs", "det var inte inkluderat"), ("fuera del presupuesto", "over budget", "fora del pressupost", "över budget"),  # Encounter 15
                ("¿cuánto cuesta?", "how much does it cost?", "quant costa?", "hur mycket kostar det?"), ("¿cuánto tarda?", "how long does it take?", "quant triga?", "hur lång tid tar det?"), ("¿cuándo terminan?", "when do they finish?", "quan acaben?", "när slutar de?"),  # Encounter 16
                ("¿cuándo empiezan?", "when do they start?", "quan comencen?", "när börjar de?"), ("¿por qué hay retraso?", "why is there a delay?", "per què hi ha retard?", "varför är det försening?"), ("¿qué pasó?", "what happened?", "què va passar?", "vad hände?"),  # Encounter 17
                ("¿puede explicar?", "can you explain it?", "pot explicar-ho?", "kan du förklara?"), ("no entiendo", "I do not understand", "no entenc", "jag förstår inte"), ("necesito más detalle", "I need more detail", "necessito més detall", "jag behöver mer detaljer"),  # Encounter 18
                ("quiero ver el plano", "I want to see the plan", "vull veure el plànol", "jag vill se planen"), ("me envía el plano", "send me the plan (Ud.)", "em envia el plànol", "skicka mig planen"), ("está en proceso", "it is in progress", "està en procés", "det är på gång"),  # Encounter 19
                ("ya empezaron", "they already started", "ja han començat", "de har redan börjat"), ("ya terminaron", "they already finished", "ja han acabat", "de har redan slutat"), ("falta trabajo", "work is still missing", "encara falta feina", "det saknas arbete"),  # Encounter 20
                ("está incompleto", "it is incomplete", "està incomplet", "det är ofullständigt"), ("está mal hecho", "it is poorly done", "està mal fet", "det är dåligt gjort"), ("está bien hecho", "it is well done", "està ben fet", "det är väl gjort"),  # Encounter 21
                ("corrigen esto", "they fix this", "corregixen això", "de rättar detta"), ("reparan esto", "they repair this", "reparen això", "de reparerar detta"), ("rehacen esto", "they redo this", "refan això", "de gör om detta"),  # Encounter 22
                ("ajustan el nivel", "they level this", "ajusten el nivell", "de justerar nivån"), ("superficie", "surface", "superfície", "yta"), ("pared", "wall", "paret", "vägg"),  # Encounter 23
                ("piso", "floor", "pis", "våning"), ("techo", "ceiling", "sostre", "tak"), ("pintura", "paint", "pintura", "färg"),  # Encounter 24
                ("hay manchas", "there are stains", "hi ha taques", "det finns fläckar"), ("acabado", "finish", "acabat", "slut"), ("está nivelado", "it is level", "està nivellat", "det är i nivå"),  # Encounter 25
                ("está desnivelado", "it is uneven", "està desnivellat", "det är ojämnt"), ("hay una grieta", "there is a crack", "hi ha una esquerda", "det finns en spricka"), ("humedad", "moisture", "humitat", "fukt"),  # Encounter 26
                ("hay una fuga", "there is a leak", "hi ha una fuita", "det finns en läcka"), ("tubería", "pipe", "canonada", "rör"), ("instalación", "installation", "instal·lació", "installation"),  # Encounter 27
                ("sistema eléctrico", "electrical system", "sistema elèctric", "elsystem"), ("cable", "wire", "cable", "kabel"), ("enchufe", "outlet", "endoll", "uttag"),  # Encounter 28
                ("interruptor", "switch", "interruptor", "strömbrytare"), ("agua", "water", "aigua", "vatten"), ("llave de agua", "water valve", "clau d'aigua", "vattenkran"),  # Encounter 29
                ("abren la pared", "they open the wall", "obren la paret", "de öppnar väggen"), ("cierran la pared", "they close the wall", "tanquen la paret", ""), ("hay daño", "there is damage", "hi ha dany", "det finns skada"),  # Encounter 30
                ("evitan el daño", "they avoid the damage", "eviten el dany", "de undviker skadan"), ("es urgente", "it is urgent", "és urgent", "det är brådskande"), ("puede empeorar", "it can get worse", "pot empitjorar", "det kan bli värre"),  # Encounter 31
                ("apruebo el cambio", "I approve the change", "aprovo el canvi", "jag godkänner ändringen"), ("no autorizo ese cambio", "I do not authorize that change", "no autoritzo aquest canvi", "jag godkänner inte den ändringen"), ("sin autorización", "without authorization", "sense autorització", "utan tillstånd"),  # Encounter 32
                ("avisan antes", "they notify me beforehand", "avisen abans", "de meddelar i förväg"), ("falta comunicación", "there is poor communication", "hi ha poca comunicació", "det saknas kommunikation"), ("nadie vino", "nobody came", "ningú va venir", "ingen kom"),  # Encounter 33
                ("no llegaron", "they did not arrive", "no van arribar", "de kom inte"), ("vienen mañana", "they come tomorrow", "venen demà", "de kommer imorgon"), ("vienen hoy", "they come today", "venen avui", "de kommer idag"),  # Encounter 34
                ("en la mañana", "in the morning", "al matí", "på morgonen"), ("en la tarde", "in the afternoon", "a la tarda", "på eftermiddagen"), ("llegan tarde", "they arrive late", "arriben tard", "de kommer för sent"),  # Encounter 35
                ("cumplen el plazo", "they meet the deadline", "compleixen el termini", "de håller tidsfristen"), ("plazo", "deadline", "termini", "deadline"), ("entrega", "delivery", "entrega", "leverans"),  # Encounter 36
                ("entrega final", "final delivery", "entrega final", "slutleverans"), ("inspección final", "final inspection", "inspecció final", "slutbesiktning"), ("garantía", "warranty", "garantia", "garanti"),  # Encounter 37
                ("incluye garantía", "it includes a warranty", "inclou garantia", "det inkluderar garanti"), ("sin garantía", "without a warranty", "sense garantia", "utan garanti"), ("herramienta", "tool", "eina", "verktyg"),  # Encounter 38
                ("maquinaria", "machinery", "maquinària", "maskiner"), ("cortan el material", "they cut the material", "tallen el material", "de klipper materialet"), ("instalan esto", "they install this", "instal·len això", "de installerar detta"),  # Encounter 39
                ("miden esto", "they measure this", "mesuren això", "de mäter detta"), ("nivelan esto", "they level this", "nivel·len això", "de jämnar ut detta"), ("fijan esto", "they secure this", "fixen això", "de fäster detta"),  # Encounter 40
                ("desmontan esto", "they remove this", "desmunten això", "de tar bort detta"), ("montan esto", "they assemble this", "munten això", "de monterar detta"), ("limpian el área", "they clean the area", "netegen l'àrea", "de städar området"),  # Encounter 41
                ("retiran los escombros", "they remove the debris", "retiren les runes", "de tar bort skräpet"), ("escombros", "debris", "enderrocs", "röjning"), ("limpieza final", "final cleanup", "neteja final", "slutstädning"),  # Encounter 42
                ("área", "area", "àrea", "område"), ("espacio", "space", "espai", "utrymme"), ("acceso", "access", "accés", "åtkomst"),  # Encounter 43
                ("entrada", "entrance", "entrada", "ingång"), ("salida", "exit", "sortida", "utgång"), ("vecino", "neighbor", "veí", "granne"),  # Encounter 44
                ("ruido", "noise", "soroll", "buller"), ("polvo", "dust", "pols", "damm"), ("seguridad", "safety", "seguretat", "trygghet"),  # Encounter 45
                ("riesgo", "risk", "risc", "risk"), ("protección", "protection", "protecció", "skydd"), ("equipo de seguridad", "safety gear", "equip de seguretat", "säkerhetsutrustning"),  # Encounter 46
                ("casco", "helmet", "casca", ""), ("guantes", "gloves", "guants", "handskar"), ("gafas de seguridad", "safety glasses", "ulleres de seguretat", "skyddsglasögon"),  # Encounter 47
                ("azulejo", "tile", "rajola", "kakel"), ("baldosa", "floor tile", "rajola", "golvkakel"), ("madera", "wood", "fusta", "trä"),  # Encounter 48
                ("cemento", "cement", "ciment", ""), ("yeso", "plaster", "guix", "gips"), ("sellador", "sealant", "segellant", "tätningsmedel"),  # Encounter 49
                ("impermeabilización", "waterproofing", "impermeabilització", "vattentätning"), ("permiso", "permit", "permís", "tillstånd"), ("inspector", "inspector", "inspector", "inspektör"),  # Encounter 50
            ],
        },
    ],
    "groceries": [
        {
            "title": "At the Supermarket",
            "goal": "Check out at the supermarket, handle pricing issues, and bag your groceries",
            "word_prefix": "groc",
            "words": [
                ("cajero", "cashier", "caixer", "kassör"), ("cliente", "customer", "client", ""), ("caja", "checkout", "caixa", "kassa"),  # Encounter 1
                ("fila", "line", "cua", "rad"), ("turno", "turn", "torn", "tur"), ("siguiente", "next", "següent", "nästa"),  # Encounter 2
                ("productos", "products", "productes", "produkter"), ("artículo", "item", "article", "artikel"), ("código de barras", "barcode", "codi de barres", "streckkod"),  # Encounter 3
                ("escanean el producto", "they scan the item", "escanejen el producte", "de skannar produkten"), ("pasan los productos", "they pass the items through", "passen els productes", "de scannar varorna"), ("precio", "price", "preu", "pris"),  # Encounter 4
                ("precio correcto", "correct price", "preu correcte", "rätt pris"), ("precio incorrecto", "wrong price", "preu incorrecte", "fel pris"), ("oferta", "sale", "oferta", "erbjudande"),  # Encounter 5
                ("descuento", "discount", "descompte", "rabatt"), ("promoción", "promotion", "promoció", "kampanj"), ("el descuento aplica", "the discount applies", "el descompte s'aplica", "rabatten gäller"),  # Encounter 6
                ("no aplica", "it does not apply", "no s'aplica", "det gäller inte"), ("sistema", "system", "sistema", "system"), ("no aparece", "it does not show up", "no apareix", "det visas inte"),  # Encounter 7
                ("revisan el precio", "they check the price", "revisen el preu", "de kontrollerar priset"), ("verifican el precio", "they verify the price", "verifiquen el preu", "de kontrollerar priset"), ("letrero", "sign", "rètol", "skylt"),  # Encounter 8
                ("estante", "shelf", "estalvi", "hylla"), ("pasillo", "aisle", "passadís", "gång"), ("supervisor", "supervisor", "supervisor", "handledare"),  # Encounter 9
                ("llaman al supervisor", "they call the supervisor", "trucen al supervisor", "de ringer till handledaren"), ("corrigen el precio", "they correct the price", "corregixen el preu", "de rättar priset"), ("total", "total", "total", "totalt"),  # Encounter 10
                ("monto total", "total amount", "import total", "totalt belopp"), ("subtotal", "subtotal", "subtotal", "delsumma"), ("impuesto", "tax", "impost", "skatt"),  # Encounter 11
                ("incluye impuesto", "it includes tax", "inclou impost", "det inkluderar skatt"), ("no incluye impuesto", "it does not include tax", "no inclou impostos", "det inkluderar inte skatt"), ("pago", "payment", "pagament", "betalning"),  # Encounter 12
                ("pago aprobado", "approved payment", "pagament aprovat", "godkänd betalning"), ("pago rechazado", "declined payment", "pagament rebutjat", "avvisad betalning"), ("tarjeta", "card", "targeta", "kort"),  # Encounter 13
                ("tarjeta rechazada", "declined card", "targeta rebutjada", "avvisat kort"), ("inserta la tarjeta", "insert the card", "insereix la targeta", "sätt i kortet"), ("pasa la tarjeta", "swipe the card", "passi la targeta", "dra kortet"),  # Encounter 14
                ("acerca la tarjeta", "tap the card", "acosta la targeta", "håll kortet nära"), ("ingresa el PIN", "enter the PIN", "introdueix el PIN", "ange PIN-koden"), ("firma aquí", "sign here (Ud.)", "signi aquí", "skriv under här"),  # Encounter 15
                ("efectivo", "cash", "efectiu", "kontanter"), ("pago en efectivo", "cash payment", "pagament en efectiu", "kontant betalning"), ("dividir el pago", "split the payment", "dividir el pagament", "dela upp betalningen"),  # Encounter 16
                ("pago dividido", "split payment", "pagament fraccionat", "delbetalning"), ("pago parcial", "partial payment", "pagament parcial", "delvis betalning"), ("pago completo", "full payment", "pagament complet", "full betalning"),  # Encounter 17
                ("cambio", "change", "canvi", "byte"), ("le dan cambio", "they give you change", "li donen canvi", "de ger dig växel"), ("recibo", "receipt", "rebut", "kvitto"),  # Encounter 18
                ("imprimen el recibo", "they print the receipt", "imprimeixen el rebut", "de skriver ut kvittot"), ("bolsa", "bag", "bossa", "väska"), ("bolsa grande", "big bag", "bossa gran", "stor väska"),  # Encounter 19
                ("bolsa pequeña", "small bag", "bossa petita", "liten väska"), ("sin bolsa", "no bag", "sense bossa", "utan påse"), ("separan los productos", "they separate the items", "separen els productes", "de separerar produkterna"),  # Encounter 20
                ("producto frío", "cold item", "producte fred", "kall vara"), ("producto congelado", "frozen item", "producte congelat", "fryst vara"), ("producto seco", "dry item", "producte sec", "torr vara"),  # Encounter 21
                ("huevos", "eggs", "ous", "ägg"), ("frágil", "fragile", "fràgil", "skör"), ("pesado", "heavy", "pesat", "tung"),  # Encounter 22
                ("liviano", "light", "lleuger", "lätt"), ("cantidad", "quantity", "quantitat", "mängd"), ("una unidad", "one unit", "una unitat", "en enhet"),  # Encounter 23
                ("dos unidades", "two units", "dues unitats", "två enheter"), ("marcan la cantidad", "they enter the quantity", "marquen la quantitat", "de anger mängden"), ("corrigen la cantidad", "they correct the quantity", "corregixen la quantitat", "de rättar mängden"),  # Encounter 24
                ("quitan el producto", "they remove the item", "treuen el producte", "de tar bort produkten"), ("agregan el producto", "they add the item", "afegeixen el producte", "de lägger till produkten"), ("no es mío", "it is not mine", "no és meu", "det är inte mitt"),  # Encounter 25
                ("es incorrecto", "it is incorrect", "és incorrecte", "det är fel"), ("revisan el producto", "they check the item", "revisen el producte", "de kontrollerar produkten"), ("escaneo doble", "double scan", "escaneig doble", "dubbel skanning"),  # Encounter 26
                ("error del sistema", "system error", "error del sistema", "systemfel"), ("ya quedó", "it is fixed now", "ja està arreglat", "det är fixat nu"), ("sigue igual", "it is still the same", "segueix igual", "det är fortfarande samma"),  # Encounter 27
                ("cliente siguiente", "next customer", "següent client", ""), ("fila larga", "long line", "cua llarga", "lång kö"), ("mucha gente", "many people", "molta gent", "många människor"),  # Encounter 28
                ("tarda mucho", "it takes a long time", "triga molt", "det tar lång tid"), ("servicio", "service", "servei", "service"), ("horario", "store hours", "horari", "öppettider"),  # Encounter 29
                ("está abierto", "it is open", "està obert", "det är öppet"), ("está cerrado", "it is closed", "està tancat", "det är stängt"), ("identificación", "ID", "identificació", "legitimation"),  # Encounter 30
                ("muestra su identificación", "show your ID (Ud.)", "mostri la seva identificació", "visa din legitimation"), ("requiere edad mínima", "it requires a minimum age", "requereix edat mínima", "det kräver minimiålder"), ("verifican la edad", "they verify your age", "verifiquen l'edat", "de kontrollerar åldern"),  # Encounter 31
                ("producto restringido", "restricted item", "producte restringit", "begränsad vara"), ("aprobado", "approved", "aprobat", "godkänd"), ("denegado", "denied", "denegat", "avvisad"),  # Encounter 32
                ("alcohol", "alcohol", "alcohol", "alkohol"), ("tabaco", "tobacco", "tabac", "tobak"), ("bebida", "drink", "beguda", "dryck"),  # Encounter 33
                ("comida", "food", "menjar", "mat"), ("pan", "bread", "pa", "bröd"), ("leche", "milk", "llet", "mjölk"),  # Encounter 34
                ("carne", "meat", "carn", "kött"), ("verduras", "vegetables", "verdures", "grönsaker"), ("fruta", "fruit", "fruita", "frukt"),  # Encounter 35
                ("caja rápida", "express checkout", "caixa ràpida", "expresskassa"), ("pocos productos", "few items", "pocs productes", "få produkter"), ("muchos productos", "many items", "molts productes", "många produkter"),  # Encounter 36
                ("carrito", "cart", "carret", "kundvagn"), ("canasta", "basket", "cistella", "korg"), ("empacan los productos", "they pack the items", "empacuen els productes", "de packar produkterna"),  # Encounter 37
                ("cliente espera", "the customer waits", "el client espera", ""), ("número de caja", "register number", "número de caixa", "kassanummer"), ("caja abierta", "open register", "caixa oberta", "öppen kassa"),  # Encounter 38
                ("caja cerrada", "closed register", "caixa tancada", "stängd kassa"), ("cambio exacto", "exact change", "canvi exacte", "exakt växel"), ("sin cambio", "without change", "sense canvi", "utan växel"),  # Encounter 39
                ("pago exacto", "exact payment", "pagament exacte", "exakt betalning"), ("tarjeta válida", "valid card", "targeta vàlida", "giltigt kort"), ("tarjeta inválida", "invalid card", "targeta invàlida", "ogiltigt kort"),  # Encounter 40
                ("saldo insuficiente", "insufficient funds", "saldo insuficient", "otillräckligt saldo"), ("hay fondos", "there are funds", "hi ha fons", "det finns medel"), ("no hay fondos", "there are no funds", "no hi ha fons", "det finns inga medel"),  # Encounter 41
                ("listo para pagar", "ready to pay", "llest per pagar", "redo att betala"), ("ingresa el código", "enter the code", "introdueix el codi", "ange koden"), ("código manual", "manual code", "codi manual", "manuell kod"),  # Encounter 42
                ("ingreso manual", "manual entry", "introducció manual", "manuell inmatning"), ("producto sin código", "item without a barcode", "producte sense codi", "vara utan streckkod"), ("pesa el producto", "weigh the item", "pesa el producte", "väg produkten"),  # Encounter 43
                ("balanza", "scale", "balança", "våg"), ("etiqueta de precio", "price label", "etiqueta de preu", "prisetikett"), ("no coincide", "it does not match", "no coincideix", "det stämmer inte"),  # Encounter 44
                ("revise la etiqueta", "check the label (Ud.)", "revisi l'etiqueta", "kontrollera etiketten"), ("actualizan el precio", "they update the price", "actualitzen el preu", "de uppdaterar priset"), ("precio actualizado", "updated price", "preu actualitzat", "uppdaterat pris"),  # Encounter 45
                ("inténtalo otra vez", "try again", "torna-ho a provar", "försök igen"), ("caja central", "main checkout", "caixa central", "huvudkassa"), ("lector", "scanner", "lector", "läsare"),  # Encounter 46
                ("el lector da error", "the scanner gives an error", "el lector dona error", "läsaren ger fel"), ("promoción vencida", "expired promotion", "promoció vençuda", "utgången kampanj"), ("vence hoy", "it expires today", "vence avui", "går ut idag"),  # Encounter 47
                ("unidad equivocada", "wrong unit", "unitat equivocada", "fel enhet"), ("precio por kilo", "price per kilo", "preu per quilo", "pris per kilo"), ("precio por unidad", "price per unit", "preu per unitat", "pris per styck"),  # Encounter 48
                ("pesa menos", "it weighs less", "pesa menys", "det väger mindre"), ("pesa más", "it weighs more", "pesa més", "det väger mer"), ("producto abierto", "opened item", "producte obert", "öppnad vara"),  # Encounter 49
                ("producto dañado", "damaged item", "producte danyat", "skadad vara"), ("reemplazo", "replacement", "substitució", "ersättning"), ("devolución al método de pago", "refund to the payment method", "devolució al mètode de pagament", "återbetalning till betalningsmetoden"),  # Encounter 50
            ],
        },
    ],
    "mechanic": [
        {
            "title": "At the Mechanic",
            "goal": "Describe car problems, get a diagnosis, and handle repairs and payment",
            "word_prefix": "mech",
            "words": [
                ("carro", "car", "cotxe", "bil"), ("vehículo", "vehicle", "vehicle", "fordon"), ("motor", "engine", "motor", "motor"),  # Encounter 1
                ("batería", "battery", "bateria", "batteri"), ("frenos", "brakes", "frens", "bromsar"), ("aceite", "oil", "oli", "olja"),  # Encounter 2
                ("filtro", "filter", "filtre", "filter"), ("transmisión", "transmission", "transmissió", "överföring"), ("suspensión", "suspension", "suspensió", "avstängning"),  # Encounter 3
                ("llanta", "tire", "pneumàtic", "däck"), ("rueda", "wheel", "roda", "hjul"), ("radiador", "radiator", "radiador", "radiator"),  # Encounter 4
                ("bujía", "spark plug", "bugia", "tändstift"), ("correa", "belt", "cinturó", "koppel"), ("alternador", "alternator", "alternador", "generator"),  # Encounter 5
                ("falla", "issue", "fallada", "problem"), ("ruido", "noise", "soroll", "buller"), ("vibración", "vibration", "vibració", "vibration"),  # Encounter 6
                ("fuga", "leak", "fuita", "läcka"), ("no arranca", "it does not start", "no arrenca", "den startar inte"), ("no enciende", "it does not turn on", "no s'encén", "den tänds inte"),  # Encounter 7
                ("se apaga", "it shuts off", "s'apaga", "den stängs av"), ("huele raro", "it smells strange", "fa una olor estranya", "det luktar konstigt"), ("se sobrecalienta", "it overheats", "s'escalfa massa", "den överhettas"),  # Encounter 8
                ("tiene poca potencia", "it has low power", "té poca potència", "den har låg effekt"), ("consume aceite", "it burns oil", "consumeix oli", "den förbrukar olja"), ("pierde líquido", "it is leaking fluid", "perd líquid", "det läcker vätska"),  # Encounter 9
                ("frenos débiles", "weak brakes", "frens dèbils", "svaga bromsar"), ("pedal suave", "soft pedal", "pedal suau", "mjuk pedal"), ("revisan el carro", "they check the car", "revisen el cotxe", "de kontrollerar bilen"),  # Encounter 10
                ("inspección", "inspection", "inspecció", "inspektion"), ("diagnóstico", "diagnosis", "diagnòstic", "diagnos"), ("reparan", "they repair it", "reparen", "de reparerar det"),  # Encounter 11
                ("lo arreglan", "they fix it", "el reparen", "de lagar den"), ("cambian la pieza", "they replace the part", "canvien la peça", "de byter delen"), ("ajustan", "they adjust it", "ajusten", "de justerar det"),  # Encounter 12
                ("instalan", "they install it", "instal·len", "de installerar"), ("limpian", "they clean it", "netegen", "de städar"), ("lo prueban", "they test it", "ho proven", "de testar det"),  # Encounter 13
                ("revisan el motor", "they check the engine", "revisen el motor", "de kontrollerar motorn"), ("cambio de aceite", "oil change", "canvi d'oli", "oljebyte"), ("cambian el filtro", "they change the filter", "canvien el filtre", "de byter filtret"),  # Encounter 14
                ("revisan los frenos", "they check the brakes", "revisen els frens", "de kontrollerar bromsarna"), ("alinean las llantas", "they align the tires", "alineen els pneumàtics", "de ställer in hjulen"), ("¿qué problema tiene?", "what problem does it have?", "quin problema té?", "vilket problem har du?"),  # Encounter 15
                ("¿qué pasa?", "what is happening?", "què passa?", "vad händer?"), ("¿desde cuándo?", "since when?", "des de quan?", "sedan när?"), ("¿cuándo empezó?", "when did it start?", "quan va començar?", "när började det?"),  # Encounter 16
                ("¿hace ruido?", "does it make noise?", "fa soroll?", "låter det?"), ("¿cuánto cuesta?", "how much does it cost?", "quant costa?", "hur mycket kostar det?"), ("¿cuánto tarda?", "how long does it take?", "quant triga?", "hur lång tid tar det?"),  # Encounter 17
                ("¿es grave?", "is it serious?", "és greu?", "är det allvarligt?"), ("¿puede empeorar?", "can it get worse?", "pot empitjorar?", "kan det bli värre?"), ("¿puede revisarlo?", "can you check it?", "pot revisar-ho?", "kan du kontrollera det?"),  # Encounter 18
                ("precio", "price", "preu", "pris"), ("costo", "cost", "cost", "kostnad"), ("total", "total", "total", "totalt"),  # Encounter 19
                ("estimado", "estimate", "estimació", "uppskattning"), ("mano de obra", "labor", "mà d'obra", "arbetskraft"), ("piezas", "parts", "peces", "delar"),  # Encounter 20
                ("adicional", "additional", "addicional", "ytterligare"), ("incluye", "it includes", "inclou", "det inkluderar"), ("no incluye", "it does not include", "no inclou", "det inkluderar inte"),  # Encounter 21
                ("presupuesto", "quote", "pressupost", "offert"), ("pago", "payment", "pagament", "betalning"), ("en efectivo", "in cash", "en efectiu", "kontant"),  # Encounter 22
                ("con tarjeta", "with a card", "amb targeta", "med kort"), ("factura", "invoice", "factura", "faktura"), ("recibo", "receipt", "rebut", "kvitto"),  # Encounter 23
                ("desgastado", "worn out", "gastat", "sliten"), ("dañado", "damaged", "danyat", "skadad"), ("roto", "broken", "trencat", "trasig"),  # Encounter 24
                ("sucio", "dirty", "brut", "smutsig"), ("flojo", "loose", "fluix", "lös"), ("apretado", "tight", "estrenyit", "tajt"),  # Encounter 25
                ("en buen estado", "in good condition", "en bon estat", "i gott skick"), ("en mal estado", "in bad condition", "en mal estat", "i dåligt skick"), ("urgente", "urgent", "urgent", "brådskande"),  # Encounter 26
                ("peligroso", "dangerous", "perillós", "farlig"), ("sistema de frenos", "brake system", "sistema de frens", "bromssystem"), ("sistema eléctrico", "electrical system", "sistema elèctric", "elsystem"),  # Encounter 27
                ("presión", "pressure", "pressió", "tryck"), ("nivel", "level", "nivell", "nivå"), ("nivel de aceite", "oil level", "nivell d'oli", "oljenivå"),  # Encounter 28
                ("nivel bajo", "low level", "nivell baix", "låg nivå"), ("nivel alto", "high level", "nivell alt", "hög nivå"), ("luz de motor", "check-engine light", "testimoni del motor", "motorlampa"),  # Encounter 29
                ("código de error", "error code", "codi d'error", "felkod"), ("dejo el carro", "I leave the car", "deixo el cotxe", "jag lämnar bilen"), ("recojo el carro", "I pick up the car", "recullo el cotxe", "jag hämtar bilen"),  # Encounter 30
                ("listo", "ready", "llest", "klar"), ("todavía no", "not yet", "encara no", "inte än"), ("en proceso", "in progress", "en procés", "pågående"),  # Encounter 31
                ("espero", "I wait", "espero", "jag väntar"), ("más tarde", "later", "més tard", "senare"), ("hoy", "today", "avui", "idag"),  # Encounter 32
                ("mañana", "tomorrow", "demà", "imorgon"), ("tiempo estimado", "estimated time", "temps estimat", "beräknad tid"), ("muy caro", "too expensive", "massa car", "för dyrt"),  # Encounter 33
                ("más barato", "cheaper", "més barat", "billigare"), ("solo eso", "just that", "només això", "bara det"), ("no lo necesito", "I do not need it", "no el necessito", "jag behöver det inte"),  # Encounter 34
                ("prefiero eso primero", "I prefer that first", "prefereixo això primer", "jag föredrar det först"), ("después vemos", "we look at the rest later", "després ho veiem", "vi tittar på resten senare"), ("no autorizo ese trabajo", "I do not authorize that work", "no autoritzo aquesta feina", "jag godkänner inte det arbetet"),  # Encounter 35
                ("sin autorización", "without authorization", "sense autorització", "utan tillstånd"), ("quiero más detalle", "I want more detail", "vull més detall", "jag vill ha mer detaljer"), ("líquido de frenos", "brake fluid", "líquid de frens", "bromsvätska"),  # Encounter 36
                ("aceite de motor", "engine oil", "oli de motor", "motorolja"), ("refrigerante", "coolant", "refrigerant", "kylvätska"), ("líquido", "fluid", "líquid", "vätska"),  # Encounter 37
                ("combustible", "fuel", "combustible", "bränsle"), ("gasolina", "gasoline", "benzina", "bensin"), ("diésel", "diesel", "dièsel", "diesel"),  # Encounter 38
                ("tanque", "tank", "dipòsit", "tank"), ("manguera", "hose", "mànega", "slang"), ("válvula", "valve", " vàlvula", "ventil"),  # Encounter 39
                ("al frenar", "when I brake", "en frenar", "när jag bromsar"), ("al arrancar", "when I start it", "en arrencar", "när jag startar den"), ("en movimiento", "while it is moving", "en moviment", "i rörelse"),  # Encounter 40
                ("en frío", "when it is cold", "en fred", "när det är kallt"), ("en caliente", "when it is hot", "en calent", "när det är varmt"), ("a alta velocidad", "at high speed", "a alta velocitat", "i hög hastighet"),  # Encounter 41
                ("a baja velocidad", "at low speed", "a baixa velocitat", "i låg hastighet"), ("en curva", "in a turn", "en corba", "i en kurva"), ("en subida", "uphill", "de pujada", "uppförsbacke"),  # Encounter 42
                ("en bajada", "downhill", "de baixada", "utförsbacke"), ("mecánico", "mechanic", "mecànic", "mekaniker"), ("taller", "shop", "taller", "verkstad"),  # Encounter 43
                ("herramienta", "tool", "eina", "verktyg"), ("elevador", "lift", "ascensor", "hiss"), ("garantía", "warranty", "garantia", "garanti"),  # Encounter 44
                ("servicio", "service", "servei", "service"), ("revisión general", "general inspection", "revisió general", "allmän inspektion"), ("mantenimiento", "maintenance", "manteniment", "underhåll"),  # Encounter 45
                ("historial", "service history", "historial", "historik"), ("diagnóstico completo", "full diagnosis", "diagnòstic complet", "fullständig diagnos"), ("no entiendo", "I do not understand", "no entenc", "jag förstår inte"),  # Encounter 46
                ("¿puede repetir?", "can you repeat that?", "pot repetir-ho?", "kan du upprepa?"), ("más despacio", "more slowly", "més a poc a poc", "långsammare"), ("¿qué significa?", "what does that mean?", "què significa?", "vad betyder det?"),  # Encounter 47
                ("pastillas de freno", "brake pads", "pastilles de fre", "bromsbelägg"), ("disco de freno", "brake rotor", "disc de fre", "bromsskiva"), ("amortiguador", "shock absorber", "amortidor", "stötdämpare"),  # Encounter 48
                ("dirección", "steering", "adreça", "adress"), ("alineación", "alignment", "alineació", "justering"), ("balanceo", "wheel balancing", "balanceig", "hjulbalansering"),  # Encounter 49
                ("embrague", "clutch", "embragatge", "koppling"), ("escape", "exhaust", "escape", "avgaser"), ("filtro de aire", "air filter", "filtre d’aire", "luftfilter"),  # Encounter 50
            ],
        },
    ],
    "police": [
        {
            "title": "Traffic Stop",
            "goal": "Handle a traffic stop calmly by providing documents and following instructions",
            "word_prefix": "pol",
            "words": [
                ("policía", "police officer", "policia", "polis"), ("agente", "officer", "agent", "tjänsteman"), ("patrulla", "patrol car", "patrulla", "patrullbil"),  # Encounter 1
                ("control policial", "traffic stop", "control policial", "polisens kontroll"), ("licencia de conducir", "driver's license", "carnet de conduir", "körkort"), ("registro del vehículo", "vehicle registration", "matrícula del vehicle", "fordonsregistrering"),  # Encounter 2
                ("prueba de seguro", "proof of insurance", "justificant d’assegurança", "försäkringsbevis"), ("documentos", "documents", "documents", "dokument"), ("identificación", "ID", "identificació", "legitimation"),  # Encounter 3
                ("¿licencia, por favor?", "your license, please?", "la llicència, si us plau?", "körkort, tack?"), ("¿tiene el registro?", "do you have the registration?", "té el registre?", "har du registreringen?"), ("¿tiene seguro?", "do you have insurance?", "té assegurança?", "har du försäkring?"),  # Encounter 4
                ("¿puede mostrarlo?", "can you show it?", "pot mostrar-ho?", "kan du visa det?"), ("aquí tiene", "here you are", "aquí té", "varsågod"), ("está en el vehículo", "it is in the vehicle", "és al vehicle", "det är i fordonet"),  # Encounter 5
                ("está en la guantera", "it is in the glove compartment", "és a la guantera", "det är i handskfacket"), ("lo detuve", "I stopped you", "t'he aturat", "jag stoppade dig"), ("parada", "stop", "parada", "hållplats"),  # Encounter 6
                ("¿sabe por qué lo detuve?", "do you know why I stopped you?", "sap per què l'he aturat?", "vet du varför jag stoppade dig?"), ("exceso de velocidad", "speeding", "excés de velocitat", "fortkörning"), ("velocidad", "speed", "velocitat", "hastighet"),  # Encounter 7
                ("límite de velocidad", "speed limit", "límit de velocitat", "hastighetsgräns"), ("zona", "zone", "zona", "zon"), ("en esta zona", "in this zone", "en aquesta zona", "i det här området"),  # Encounter 8
                ("iba a", "were going at (speed)", "anava a", "höll på att"), ("por encima de", "above", "per sobre de", "över"), ("infracción", "violation", "infracció", "överträdelser"),  # Encounter 9
                ("motivo", "reason", "motiu", "orsak"), ("vehículo", "vehicle", "vehicle", "fordon"), ("carro", "car", "cotxe", "bil"),  # Encounter 10
                ("luces", "lights", "llums", "lampor"), ("luz trasera", "tail light", "llum posterior", "bakljus"), ("luz delantera", "headlight", "llum davantera", "strålkastare"),  # Encounter 11
                ("no funciona", "it does not work", "no funciona", "det fungerar inte"), ("placa", "plate", "placa", "skylt"), ("parabrisas", "windshield", "parabrisa", "vindruta"),  # Encounter 12
                ("cinturón", "seatbelt", "cinturó", ""), ("sin cinturón", "without a seatbelt", "sense cinturó", "utan säkerhetsbälte"), ("en regla", "in order", "en regla", "i ordning"),  # Encounter 13
                ("apague el motor", "turn off the engine (Ud.)", "apagueu el motor", "stäng av motorn"), ("baje la ventana", "roll down the window (Ud.)", "baixi la finestra", "sänk ner rutan"), ("salga del vehículo", "get out of the vehicle (Ud.)", "surti del vehicle", "stig ur fordonet"),  # Encounter 14
                ("quédese en el vehículo", "stay in the vehicle (Ud.)", "resti al vehicle", "stanna i fordonet"), ("espere aquí", "wait here (Ud.)", "esperi aquí", "vänta här"), ("despacio", "slowly", "a poc a poc", "långsamt"),  # Encounter 15
                ("con calma", "calmly", "amb calma", "lugnt"), ("siga mis instrucciones", "follow my instructions (Ud.)", "segueixi les meves instruccions", "följ mina instruktioner"), ("no se mueva", "do not move (Ud.)", "no es mogui", "rör dig inte"),  # Encounter 16
                ("frenó fuerte", "braked hard (past)", "va frenar fort", "bromsade hårt"), ("cambió de carril", "changed lanes (past)", "va canviar de carril", "han/hon bytte fil"), ("sin señalizar", "without signaling", "sense senyalitzar", "utan att blinka"),  # Encounter 17
                ("conducción peligrosa", "dangerous driving", "conducció perillosa", "farlig körning"), ("carril", "lane", "carril", "fil"), ("carril restringido", "restricted lane", "carril restringit", "begränsad fil"),  # Encounter 18
                ("giro", "turn", "gir", "sväng"), ("no señalizó", "did not signal (past)", "no va senyalitzar", "han/hon/den/det blinkade inte"), ("tráfico", "traffic", "trànsit", "trafik"),  # Encounter 19
                ("intersección", "intersection", "creuament", "korsning"), ("semáforo", "traffic light", "semàfor", "trafikljus"), ("luz roja", "red light", "llum vermella", "rött ljus"),  # Encounter 20
                ("luz verde", "green light", "llum verda", "grönt ljus"), ("¿de dónde viene?", "where are you coming from?", "d'on ve?", "varifrån kommer du?"), ("¿a dónde va?", "where are you going?", "on va?", "vart ska du?"),  # Encounter 21
                ("¿cuánto tiempo lleva manejando?", "how long have you been driving?", "quant de temps fa que condueix?", "hur länge har du kört?"), ("¿es su vehículo?", "is this your vehicle?", "és el seu vehicle?", "är det ditt fordon?"), ("¿es un vehículo de alquiler?", "is it a rental vehicle?", "és un vehicle de lloguer?", "är det en hyrbil?"),  # Encounter 22
                ("¿tiene el contrato?", "do you have the contract?", "té el contracte?", "har du kontraktet?"), ("¿ha consumido alcohol?", "have you consumed alcohol?", "ha consumit alcohol?", "har du druckit alkohol?"), ("¿ha tomado algo?", "have you had anything to drink?", "ha pres alguna cosa?", "har du druckit något?"),  # Encounter 23
                ("¿entiende?", "do you understand?", "entén?", "förstår du?"), ("¿puede explicar?", "can you explain it?", "pot explicar-ho?", "kan du förklara?"), ("alcohol", "alcohol", "alcohol", "alkohol"),  # Encounter 24
                ("prueba", "test", "prova", "test"), ("prueba de alcohol", "breath test", "prova d’alcohol", "alkoholtest"), ("sople aquí", "blow here (Ud.)", "bufi aquí", "blås här"),  # Encounter 25
                ("resultado", "result", "resultat", "resultat"), ("negativo", "negative", "negatiu", "negativ"), ("positivo", "positive", "positiu", "positiv"),  # Encounter 26
                ("bajo la influencia", "under the influence", "sota la influència", "påverkad"), ("sobrio", "sober", "savi", "nykter"), ("verifican el sistema", "they check the system", "comproven el sistema", "de kontrollerar systemet"),  # Encounter 27
                ("registro activo", "active registration", "registre actiu", "aktiv registrering"), ("seguro activo", "active insurance", "assegurança activa", "aktiv försäkring"), ("no aparece", "it does not show up", "no apareix", "det visas inte"),  # Encounter 28
                ("pendiente", "pending", "pendent", "obestämd"), ("multa", "ticket", "multa", "böter"), ("advertencia", "warning", "advertència", "varning"),  # Encounter 29
                ("sanción", "penalty", "sanció", "påföljd"), ("emiten la multa", "they issue the ticket", "emeten la multa", "de utfärdar bötern"), ("dan una advertencia", "they give a warning", "donen un avís", "de ger en varning"),  # Encounter 30
                ("paga la multa", "pay the ticket", "pagi la multa", "betala bötern"), ("en línea", "online", "en línia", "online"), ("plazo", "deadline", "termini", "deadline"),  # Encounter 31
                ("monto", "amount", "import", "belopp"), ("carretera", "road", "carretera", "väg"), ("calle", "street", "carrer", "gata"),  # Encounter 32
                ("zona urbana", "urban area", "zona urbana", "stadsområde"), ("zona escolar", "school zone", "zona escolar", "skolzon"), ("autopista", "highway", "autopista", "motorväg"),  # Encounter 33
                ("señal", "sign", "senyal", "skylt"), ("señalización", "road signage", "senyalització", "vägmärkning"), ("dirección", "direction", "adreça", "adress"),  # Encounter 34
                ("carril derecho", "right lane", "carril dret", "höger fil"), ("alquiler", "rental", "lloguer", "hyra"), ("contrato", "contract", "contracte", "kontrakt"),  # Encounter 35
                ("propietario", "owner", "propietari", "ägare"), ("está a su nombre", "it is in your name", "és al seu nom", "det står i ditt namn"), ("no es mío", "it is not mine", "no és meu", "det är inte mitt"),  # Encounter 36
                ("vehículo prestado", "borrowed vehicle", "vehicle prestat", "lånat fordon"), ("permiso del dueño", "owner's permission", "permís del propietari", "ägartillstånd"), ("no lo encuentro", "I cannot find it", "no el trobo", "jag hittar det inte"),  # Encounter 37
                ("no lo tengo", "I do not have it", "no el tinc", "jag har det inte"), ("no carga", "it does not load", "no carrega", "det laddar inte"), ("sin señal", "without signal", "sense senyal", "utan signal"),  # Encounter 38
                ("en el celular", "on the cellphone", "al mòbil", "på mobilen"), ("copia digital", "digital copy", "còpia digital", "digital kopia"), ("sin documento", "without the document", "sense document", "utan dokument"),  # Encounter 39
                ("vencido", "expired", "vençut", "utgånget"), ("por vencer", "about to expire", "a punt de vèncer", "på väg att gå ut"), ("no es válido", "it is not valid", "no és vàlid", "det är inte giltigt"),  # Encounter 40
                ("no entiendo", "I do not understand", "no entenc", "jag förstår inte"), ("¿puede repetir?", "can you repeat that?", "pot repetir-ho?", "kan du upprepa?"), ("más despacio", "more slowly", "més a poc a poc", "långsammare"),  # Encounter 41
                ("¿qué significa?", "what does that mean?", "què significa?", "vad betyder det?"), ("¿es una multa?", "is it a ticket?", "és una multa?", "är det en böter?"), ("¿es una advertencia?", "is it a warning?", "és un avís?", "är det en varning?"),  # Encounter 42
                ("¿puedo irme?", "can I leave?", "em puc anar?", "kan jag gå?"), ("¿puedo seguir?", "can I continue?", "puc continuar?", "kan jag fortsätta?"), ("control", "checkpoint", "control", "kontrollpunkt"),  # Encounter 43
                ("oríllese", "pull over (Ud.)", "aturi's al voral", "kör åt sidan"), ("orilla", "roadside", "vorera", "vägkant"), ("luces de emergencia", "hazard lights", "intermitents d'emergència", "varningsblinkers"),  # Encounter 44
                ("documento físico", "physical document", "document físic", "fysiskt dokument"), ("permiso de conducir", "driver's license", "permís de conduir", "körkort"), ("matrícula", "license plate", "matrícula", "registreringsskylt"),  # Encounter 45
                ("agente de tránsito", "traffic officer", "agent de trànsit", "trafikpolis"), ("triángulo", "warning triangle", "triangle de senyalització", "varningstriangel"), ("chaleco reflectante", "reflective vest", "armilla reflectant", ""),  # Encounter 46
                ("accidente", "accident", "accident", "olycka"), ("choque", "crash", "xoc", ""), ("reporte", "report", "informe", "rapport"),  # Encounter 47
                ("reporte policial", "police report", "informe policial", "polisrapport"), ("testigo", "witness", "testimoni", "vittne"), ("declaración", "statement", "declaració", "utdrag"),  # Encounter 48
                ("firme aquí", "sign here (Ud.)", "signi aquí", "skriv under här"), ("corte", "court", "jutjat", "avbrott"), ("fecha de corte", "court date", "data de judici", "rättsdatum"),  # Encounter 49
                ("comparecencia", "court appearance", "compareixença", "rättsförhandling"), ("grúa", "tow truck", "grua", "bärgningsbil"), ("remolque", "towing", "remolc", "släp"),  # Encounter 50
            ],
        },
    ],
    "restaurant": [
        {
            "title": "Eating Out",
            "goal": "Order food, interact with the server, and pay for your meal",
            "word_prefix": "rest",
            "words": [
                ("menú", "menu", "menú", "meny"), ("carta", "menu", "carta", ""), ("mesero", "waiter", "cambrer", "servitör"),  # Encounter 1
                ("mesa", "table", "taula", "bord"), ("reserva", "reservation", "reserva", "bokning"), ("¿tienen reserva?", "do you have a reservation?", "tenen reserva?", "har ni en bokning?"),  # Encounter 2
                ("mesa para dos", "table for two", "taula per a dos", "bord för två"), ("pido", "I order", "demano", "jag beställer"), ("¿qué desea?", "what would you like?", "què desitja?", "vad önskar du?"),  # Encounter 3
                ("¿qué van a pedir?", "what are you going to order?", "què demanareu?", "vad ska ni beställa?"), ("tomo la orden", "I take the order", "prenc la comanda", "jag tar beställningen"), ("aquí está el menú", "here is the menu", "aquí teniu el menú", "här är menyn"),  # Encounter 4
                ("recomendación", "recommendation", "recomanació", "rekommendation"), ("¿qué recomienda?", "what do you recommend?", "què recomana?", "vad rekommenderar du?"), ("plato", "dish", "plat", "rätt"),  # Encounter 5
                ("entrada", "appetizer", "entrada", "ingång"), ("plato principal", "main dish", "plat principal", "huvudrätt"), ("postre", "dessert", "postres", "efterrätt"),  # Encounter 6
                ("acompañamiento", "side dish", "acompanyament", "tillbehör"), ("guarnición", "side dish", "guarnició", "sidorätt"), ("porción", "portion", "porció", "portion"),  # Encounter 7
                ("ingrediente", "ingredient", "ingredient", "ingrediens"), ("salsa", "sauce", "salsa", "sås"), ("arroz", "rice", "arròs", "ris"),  # Encounter 8
                ("pollo", "chicken", "pollastre", "kyckling"), ("carne", "meat", "carn", "kött"), ("pescado", "fish", "peix", "fisk"),  # Encounter 9
                ("verduras", "vegetables", "verdures", "grönsaker"), ("ensalada", "salad", "amanida", "sallad"), ("vegetariano", "vegetarian", "vegetarià", "vegetarian"),  # Encounter 10
                ("vegano", "vegan", "vegà", "vegan"), ("alergia", "allergy", "al·lèrgia", "allergi"), ("alérgico", "allergic", "al·lèrgic", "allergisk"),  # Encounter 11
                ("frutos secos", "nuts", "fruits secs", "nötter"), ("sin", "without", "sense", "utan"), ("con", "with", "amb", "med"),  # Encounter 12
                ("¿tiene…?", "does it have…?", "té…?", "har det…?"), ("¿lleva…?", "does it come with…?", "porta…?", "har du…?"), ("sin picante", "not spicy", "sense picant", "inte stark"),  # Encounter 13
                ("picante", "spicy", "picant", "stark"), ("poco picante", "mildly spicy", "poc picant", "mildt kryddad"), ("sin carne", "without meat", "sense carn", "utan kött"),  # Encounter 14
                ("sin gluten", "gluten-free", "sense gluten", "glutenfri"), ("¿se puede cambiar?", "can it be changed?", "es pot canviar?", "kan det ändras?"), ("bebida", "drink", "beguda", "dryck"),  # Encounter 15
                ("agua", "water", "aigua", "vatten"), ("con gas", "sparkling", "amb gas", "med bubblor"), ("sin gas", "still", "sense gas", "utan gas"),  # Encounter 16
                ("refresco", "soda", "refresc", "läsk"), ("jugo", "juice", "suc", "juice"), ("cerveza", "beer", "cervesa", ""),  # Encounter 17
                ("vino", "wine", "vi", "vin"), ("copa", "glass", "copa", "glas"), ("botella", "bottle", "ampolla", "flaska"),  # Encounter 18
                ("¿algo de tomar?", "would you like something to drink?", "vols alguna cosa per beure?", "vill du ha något att dricka?"), ("tiempo de espera", "wait time", "temps d'espera", "väntetid"), ("¿cuánto tiempo tarda?", "how long does it take?", "quant de temps triga?", "hur lång tid tar det?"),  # Encounter 19
                ("regreso enseguida", "I come right back", "torno de seguida", "jag kommer strax tillbaka"), ("aquí está", "here it is", "aquí està", "här är det"), ("falta", "it is missing", "falta", "det saknas"),  # Encounter 20
                ("no llegó", "it did not arrive", "no va arribar", "det kom inte"), ("pedimos la comida", "we order the food", "demanem el menjar", "vi beställer maten"), ("trae", "bring (command)", "porta", "ta med"),  # Encounter 21
                ("lleva", "it comes with", "porta", "den har med sig"), ("sirve", "it serves", "serveix", "det fungerar"), ("mesa lista", "ready table", "taula preparada", "klart bord"),  # Encounter 22
                ("síganme", "follow me (Uds.)", "segueixin-me", "följ mig"), ("error", "mistake", "error", "misstag"), ("equivocado", "wrong", "equivocat", "fel"),  # Encounter 23
                ("no es esto", "this is not it", "no és això", "det här är det inte"), ("no pedimos eso", "we did not order that", "no vam demanar això", "vi beställde inte det"), ("falta esto", "this is missing", "falta això", "det här saknas"),  # Encounter 24
                ("cambio", "change", "canvi", "byte"), ("cambian el plato", "they change the dish", "canvien el plat", "de byter tallriken"), ("cocina", "kitchen", "cuina", "kök"),  # Encounter 25
                ("preparan otro plato", "they prepare another dish", "preparen un altre plat", "de förbereder en annan rätt"), ("tardó mucho", "it took too long", "va trigar molt", "det tog lång tid"), ("frío", "cold", "fred", "kallt"),  # Encounter 26
                ("caliente", "hot", "calent", "varm"), ("recalentado", "reheated", "recalentat", "uppvärmd"), ("¿qué es esto?", "what is this?", "què és això?", "vad är det här?"),  # Encounter 27
                ("¿qué lleva?", "what does it have?", "què porta?", "vad innehåller det?"), ("¿cómo es?", "what is it like?", "com és?", "hur är det?"), ("¿está listo?", "is it ready?", "està llest?", "är det klart?"),  # Encounter 28
                ("¿falta mucho?", "is there much longer to wait?", "queda molt?", "är det långt kvar?"), ("¿puede explicar?", "can you explain it?", "pot explicar-ho?", "kan du förklara?"), ("no entiendo", "I do not understand", "no entenc", "jag förstår inte"),  # Encounter 29
                ("repítalo", "repeat it (Ud.)", "repeteixi-ho", "upprepa det"), ("más despacio", "more slowly", "més a poc a poc", "långsammare"), ("aclárelo", "clarify it (Ud.)", "aclari-ho", "förtydliga det"),  # Encounter 30
                ("cuenta", "bill", "compte", "konto"), ("la cuenta", "the bill", "el compte", "notan"), ("total", "total", "total", "totalt"),  # Encounter 31
                ("precio", "price", "preu", "pris"), ("incluye", "it includes", "inclou", "det inkluderar"), ("no incluye", "it does not include", "no inclou", "det inkluderar inte"),  # Encounter 32
                ("propina", "tip", "propina", "dricks"), ("servicio", "service", "servei", "service"), ("dividimos la cuenta", "we split the bill", "dividim el compte", "vi delar notan"),  # Encounter 33
                ("pago", "payment", "pagament", "betalning"), ("con tarjeta", "with a card", "amb targeta", "med kort"), ("en efectivo", "in cash", "en efectiu", "kontant"),  # Encounter 34
                ("terminal", "card terminal", "terminal", "terminal"), ("no funciona", "it does not work", "no funciona", "det fungerar inte"), ("recibo", "receipt", "rebut", "kvitto"),  # Encounter 35
                ("mesa libre", "free table", "taula lliure", "ledigt bord"), ("ocupado", "occupied", "ocupat", "ockuperad"), ("lleno", "full", "ple", "full"),  # Encounter 36
                ("afuera", "outside", "a fora", "utanför"), ("adentro", "inside", "a dins", "inne"), ("terraza", "patio", "terrassa", "terrass"),  # Encounter 37
                ("aire acondicionado", "air conditioning", "aire condicionat", "luftkonditionering"), ("ruido", "noise", "soroll", "buller"), ("tranquilo", "quiet", "tranquil", "lugnt"),  # Encounter 38
                ("ambiente", "atmosphere", "ambient", "miljö"), ("para dos", "for two", "per a dos", "för två"), ("más", "more", "més", "mer"),  # Encounter 39
                ("menos", "less", "menys", "mindre"), ("suficiente", "enough", "suficient", "tillräckligt"), ("extra", "extra", "extra", "extra"),  # Encounter 40
                ("otra", "another one", "una altra", "en till"), ("lo mismo", "the same", "el mateix", "samma sak"), ("para llevar", "to go", "per emportar", "att ta med"),  # Encounter 41
                ("pedido", "order", "comanda", "beställning"), ("factura", "invoice", "factura", "faktura"), ("reserva confirmada", "confirmed reservation", "reserva confirmada", "bekräftad bokning"),  # Encounter 42
                ("mesa asignada", "assigned table", "taula assignada", "tilldelat bord"), ("lista de espera", "waitlist", "llista d'espera", "väntelista"), ("disponibilidad", "availability", "disponibilitat", "tillgänglighet"),  # Encounter 43
                ("horario", "opening hours", "horari", "öppettider"), ("cubiertos", "utensils", "estris", "bestick"), ("cuchara", "spoon", "cullera", "sked"),  # Encounter 44
                ("tenedor", "fork", "forquilla", "gaffel"), ("cuchillo", "knife", "ganivet", "kniv"), ("servilleta", "napkin", "tovalló", "servett"),  # Encounter 45
                ("vaso", "glass", "got", "glas"), ("taza", "cup", "tassa", "kopp"), ("hielo", "ice", "gel", "is"),  # Encounter 46
                ("sin hielo", "without ice", "sense gel", "utan is"), ("otra ronda", "another round", "una altra ronda", "en runda till"), ("traen la cuenta", "they bring the bill", "porten el compte", "de kommer med notan"),  # Encounter 47
                ("cobro adicional", "extra charge", "càrrec addicional", ""), ("cargo por servicio", "service charge", "càrrec per servei", "serviceavgift"), ("plato hondo", "bowl", "bol", "djup tallrik"),  # Encounter 48
                ("plato llano", "dinner plate", "plat pla", "flat tallrik"), ("cubierto extra", "extra utensil", "estri extra", "extra bestick"), ("para compartir", "to share", "per compartir", "att dela"),  # Encounter 49
                ("recogen los platos", "they clear the plates", "recullen els plats", "de plockar bort tallrikarna"), ("mesa sucia", "dirty table", "taula bruta", "smutsigt bord"), ("mesa limpia", "clean table", "taula neta", "rent bord"),  # Encounter 50
            ],
        },
    ],
    "small_talk": [
        {
            "title": "Meeting a Neighbor",
            "goal": "Have a friendly conversation with your neighbor about building life",
            "word_prefix": "talk",
            "words": [
                ("vecino", "neighbor", "veí", "granne"), ("vecina", "female neighbor", "veïna", "granne (kvinna)"), ("edificio", "building", "edifici", "byggnad"),  # Encounter 1
                ("departamento", "apartment", "pis", "lägenhet"), ("casa", "house", "casa", ""), ("zona", "area", "zona", "zon"),  # Encounter 2
                ("barrio", "neighborhood", "barri", "kvarter"), ("ruido", "noise", "soroll", "buller"), ("música", "music", "música", "musik"),  # Encounter 3
                ("volumen", "volume", "volum", "volym"), ("baja el volumen", "lower the volume", "baixa el volum", "sänk volymen"), ("reunión", "gathering", "reunió", "möte"),  # Encounter 4
                ("fiesta", "party", "festa", "fest"), ("anoche", "last night", "ahir a la nit", "i går kväll"), ("tarde", "late", "tard", "sen"),  # Encounter 5
                ("temprano", "early", "d'hora", "tidigt"), ("trabajo temprano", "I work early", "treballo d'hora", "jag jobbar tidigt"), ("no pude dormir", "I could not sleep", "no vaig poder dormir", "jag kunde inte sova"),  # Encounter 6
                ("quería comentarte algo", "I wanted to mention something to you", "volia comentar-te una cosa", "jag ville nämna något för dig"), ("solo quería avisarte", "I just wanted to let you know", "només volia avisar-te", "jag ville bara meddela dig"), ("la próxima vez", "next time", "la propera vegada", "nästa gång"),  # Encounter 7
                ("tenga cuidado", "be careful (Ud.)", "tingui cura", "var försiktig"), ("estacionamiento", "parking", "aparcament", "parkering"), ("lugar", "spot", "lloc", "plats"),  # Encounter 8
                ("espacio", "space", "espai", "utrymme"), ("mi lugar", "my spot", "el meu lloc", "min plats"), ("asignado", "assigned", "assignat", "tilldelad"),  # Encounter 9
                ("visitante", "visitor", "visitant", "besökare"), ("mueve el carro", "move the car", "mou el cotxe", "flytta bilen"), ("lo muevo ahora mismo", "I move it right now", "el moc ara mateix", "jag flyttar det nu"),  # Encounter 10
                ("ya pasó dos veces", "it has already happened twice", "ja ha passat dues vegades", "det har redan hänt två gånger"), ("no sabía", "I did not know", "no sabia", "jag visste inte"), ("no fue intencional", "it was not intentional", "no va ser intencionat", "det var inte avsiktligt"),  # Encounter 11
                ("paquete", "package", "paquet", "paket"), ("entrega", "delivery", "entrega", "leverans"), ("repartidor", "delivery person", "repartidor", "bud"),  # Encounter 12
                ("puerta", "door", "porta", "dörr"), ("lo dejó aquí por error", "he left it here by mistake", "el va deixar aquí per error", "han lämnade det här av misstag"), ("nombre", "name", "nom", "namn"),  # Encounter 13
                ("mi nombre", "my name", "el meu nom", "mitt namn"), ("aquí está su paquete", "here is your package", "aquí té el seu paquet", "här är ditt paket"), ("lo tengo", "I have it", "ho tinc", "jag har det"),  # Encounter 14
                ("se perdió", "it got lost", "es va perdre", "den försvann"), ("pasa seguido", "it happens often", "passa sovint", "det händer ofta"), ("hace tiempo", "a long time ago", "fa temps", "för länge sedan"),  # Encounter 15
                ("hace meses", "months ago", "fa mesos", "för flera månader sedan"), ("hace un año", "a year ago", "fa un any", "för ett år sedan"), ("vivo aquí", "I live here", "visc aquí", "jag bor här"),  # Encounter 16
                ("me mudé", "I moved", "em vaig mudar", "jag flyttade"), ("¿te gusta vivir aquí?", "do you like living here?", "t'agrada viure aquí?", "gillar du att bo här?"), ("me gusta", "I like it", "m'agrada", "jag gillar det"),  # Encounter 17
                ("es tranquilo", "it is quiet", "és tranquil", "det är lugnt"), ("es ruidoso", "it is noisy", "és sorollós", "det är högljutt"), ("agua", "water", "aigua", "vatten"),  # Encounter 18
                ("fuga", "leak", "fuita", "läcka"), ("humedad", "dampness", "humitat", "fukt"), ("pared", "wall", "paret", "vägg"),  # Encounter 19
                ("tubería", "pipe", "canonada", "rör"), ("problema de agua", "water issue", "problema d’aigua", "vattenproblem"), ("administración", "building management", "administració", "fastighetsförvaltning"),  # Encounter 20
                ("ya llamé", "I already called", "ja he trucat", "jag har redan ringt"), ("no han venido", "they have not come", "no han vingut", "de har inte kommit"), ("mejor así", "it is better this way", "millor així", "bättre så"),  # Encounter 21
                ("más urgente", "more urgent", "més urgent", "mer brådskande"), ("cierra la llave de agua", "shut off the water valve", "tanca la clau de l'aigua", ""), ("llave de agua", "water valve", "clau d'aigua", "vattenkran"),  # Encounter 22
                ("puede empeorar", "it can get worse", "pot empitjorar", "det kan bli värre"), ("avísame", "let me know", "avisa'm", "hör av dig"), ("me dices", "tell me", "em dius", "säg mig"),  # Encounter 23
                ("entiendo", "I understand", "entenc", "jag förstår"), ("tiene sentido", "it makes sense", "té sentit", "det är vettigt"), ("cerca", "nearby", "a prop", ""),  # Encounter 24
                ("lejos", "far", "lluny", "långt"), ("piso", "floor", "pis", "våning"), ("mismo piso", "same floor", "mateix pis", "samma våning"),  # Encounter 25
                ("arriba", "upstairs", "a dalt", "uppe"), ("abajo", "downstairs", "a baix", "nere"), ("toca la puerta", "knock on the door", "toca la porta", "knacka på dörren"),  # Encounter 26
                ("abre", "it opens", "obre", "den öppnar"), ("cierra", "it closes", "tanca", ""), ("trabajo", "work", "feina", "arbete"),  # Encounter 27
                ("horario", "schedule", "horari", "öppettider"), ("ocupado", "busy", "ocupat", "ockuperad"), ("libre", "free", "lliure", "ledig"),  # Encounter 28
                ("fin de semana", "weekend", "cap de setmana", "helg"), ("hoy", "today", "avui", "idag"), ("mañana", "tomorrow", "demà", "imorgon"),  # Encounter 29
                ("ayer", "yesterday", "ahir", "igår"), ("en un rato", "in a little while", "d'aquí a una estona", "om en liten stund"), ("prestas una herramienta", "lend a tool", "prestes una eina", "lånar ut ett verktyg"),  # Encounter 30
                ("herramienta", "tool", "eina", "verktyg"), ("llave inglesa", "wrench", "clau anglesa", "skiftnyckel"), ("taladro", "drill", "trepant", "borrmaskin"),  # Encounter 31
                ("escalera", "ladder", "escala", "stege"), ("basura", "trash", "escombraries", "skräp"), ("saco la basura", "I take out the trash", "trec la brossa", "jag tar ut soporna"),  # Encounter 32
                ("reciclaje", "recycling", "reciclatge", "återvinning"), ("ascensor", "elevator", "ascensor", "hiss"), ("timbre", "doorbell", "timbre", "dörrklocka"),  # Encounter 33
                ("portón", "gate", "porta gran", "grind"), ("entrada principal", "main entrance", "entrada principal", "huvudingång"), ("llave", "key", "clau", "nyckel"),  # Encounter 34
                ("copia de llave", "spare key", "còpia de clau", "extranyckel"), ("administración del edificio", "building management", "administració de l’edifici", "fastighetsförvaltning"), ("portero", "doorman", "porter", "portvakt"),  # Encounter 35
                ("conserje", "caretaker", "conserge", "vaktmästare"), ("paquete equivocado", "wrong package", "paquet equivocat", "fel paket"), ("se confundieron de puerta", "they got the door wrong", "es van confondre de porta", "de tog fel dörr"),  # Encounter 36
                ("visita", "visitor", "visita", "besök"), ("visitas", "guests", "visites", "gäster"), ("¿espera visitas?", "are you expecting guests?", "espera visites?", "väntar du besök?"),  # Encounter 37
                ("mudanza", "move", "mudança", "flytt"), ("camión de mudanza", "moving truck", "camió de mudances", "flyttbil"), ("se mudan hoy", "they move today", "es muden avui", "de flyttar idag"),  # Encounter 38
                ("mascota", "pet", "mascota", "husdjur"), ("perro", "dog", "gos", "hund"), ("gato", "cat", "gat", "katt"),  # Encounter 39
                ("correa", "leash", "cinturó", "koppel"), ("ladra mucho", "it barks a lot", "lladra molt", "den skäller mycket"), ("¿cómo se llama?", "what is it called?", "com es diu?", "vad heter det?"),  # Encounter 40
                ("jardín", "garden", "jardí", "trädgård"), ("plantas", "plants", "plantes", "växter"), ("riego", "watering", "reg", "bevattning"),  # Encounter 41
                ("riega las plantas", "water the plants", "rega les plantes", "vattna växterna"), ("balcón", "balcony", "balcó", "balkong"), ("ventana", "window", "finestra", "fönster"),  # Encounter 42
                ("corriente de aire", "draft", "corrent d’aire", "drag"), ("hace frío aquí", "it is cold here", "fa fred aquí", "det är kallt här"), ("hace calor aquí", "it is hot here", "fa calor aquí", "det är varmt här"),  # Encounter 43
                ("humedad en el techo", "moisture on the ceiling", "humitat al sostre", "fukt i taket"), ("corte de agua", "water outage", "tall d’aigua", "vattenavbrott"), ("corte de luz", "power outage", "tall de llum", "strömavbrott"),  # Encounter 44
                ("luz", "electricity", "llum", "ljus"), ("se fue la luz", "the power went out", "va faltar la llum", "strömmen gick"), ("vuelve pronto", "it comes back soon", "torna aviat", "den kommer tillbaka snart"),  # Encounter 45
                ("vecino nuevo", "new neighbor", "veí nou", "ny granne"), ("recién llegado", "newly arrived", "recent arribat", "nyanländ"), ("¿desde cuándo vive aquí?", "since when do you live here?", "des de quan viu aquí?", "sedan när bor du här?"),  # Encounter 46
                ("alquiler", "rent", "lloguer", "hyra"), ("subió el alquiler", "the rent went up", "va pujar el lloguer", "hyran höjdes"), ("administración no responde", "management does not respond", "l’administració no respon", "förvaltningen svarar inte"),  # Encounter 47
                ("queja", "complaint", "queixa", "klagomål"), ("pongo una queja", "I file a complaint", "poso una queixa", "jag lämnar in ett klagomål"), ("ruido arriba", "upstairs noise", "soroll a dalt", "buller uppe"),  # Encounter 48
                ("ruido abajo", "downstairs noise", "soroll a baix", "buller nere"), ("pasillo", "hallway", "passadís", "gång"), ("entrada trasera", "back entrance", "entrada posterior", "bakdörr"),  # Encounter 49
                ("puerta principal", "front door", "porta principal", "ytterdörr"), ("buzón", "mailbox", "bústia", "brevlåda"), ("correo", "mail", "correu", "e-post"),  # Encounter 50
            ],
        },
    ],
    "internet": [
        {
            "title": "Setting Up WiFi",
            "goal": "Set up your internet service by speaking with the technician",
            "word_prefix": "inet",
            "words": [
                ("internet", "internet", "internet", "internet"), ("wifi", "WiFi", "wifi", "wifi"), ("red inalámbrica", "wireless network", "xarxa sense fils", "trådlöst nätverk"),  # Encounter 1
                ("wifi doméstico", "home WiFi", "wifi domèstic", "hemwifi"), ("clave de acceso", "access code", "clau d'accés", ""), ("red local", "local network", "xarxa local", "lokalt nätverk"),  # Encounter 2
                ("router", "router", "router", "router"), ("cable", "cable", "cable", "kabel"), ("intensidad", "signal strength", "intensitat", "signalstyrka"),  # Encounter 3
                ("enrutador", "router", "enrutador", "router"), ("cable de red", "network cable", "cable de xarxa", "nätverkskabel"), ("tomacorriente", "outlet", "endoll", "eluttag"),  # Encounter 4
                ("plan", "plan", "pla", "plan"), ("pausado", "slow", "pausat", "långsam"), ("rapidez", "speed", "rapidesa", "snabbhet"),  # Encounter 5
                ("paquete de datos", "data plan", "paquet de dades", "datapaket"), ("cuota mensual", "monthly fee", "quota mensual", "månadskostnad"), ("visita", "visit", "visita", "besök"),  # Encounter 6
                ("nombre de red", "network name", "nom de xarxa", "nätverksnamn"), ("colocar", "to install", "col·locar", "installera"), ("configurar", "to configure", "configurar", "konfigurera"),  # Encounter 7
                ("conectar", "to connect", "connectar", "ansluta"), ("desconectar", "to disconnect", "desconnectar", "koppla bort"), ("reiniciar", "to restart", "reiniciar", "starta om"),  # Encounter 8
                ("especialista", "specialist", "especialista", "specialist"), ("cita de servicio", "service appointment", "cita de servei", ""), ("SSID", "SSID", "SSID", "SSID"),  # Encounter 9
                ("funcionar", "to work/function", "funcionar", "fungera"), ("renombrar", "to rename", "renombrar", "byta namn på"), ("solución", "solution", "solució", "lösning"),  # Encounter 10
                ("banda ancha", "broadband", "banda ampla", "bredband"), ("fibra óptica", "fiber optic", "fibra òptica", "fiberoptik"), ("megabits", "megabits", "megabits", "megabit"),  # Encounter 11
                ("descargar", "to download", "descarregar", "ladda ner"), ("ajustar", "to adjust", "ajustar", "justera"), ("enlazar", "to connect", "enllaçar", "koppla ihop"),  # Encounter 12
                ("cortar enlace", "to disconnect", "tallar enllaç", "koppla från"), ("rearrancar", "to restart", "rearrencar", "starta om"), ("aparato", "device", "aparell", "apparat"),  # Encounter 13
                ("portátil", "laptop", "portàtil", "bärbar dator"), ("teléfono móvil", "mobile phone", "telèfon mòbil", "mobiltelefon"), ("operar", "to work/operate", "operar", "fungera"),  # Encounter 14
                ("modem", "modem", "mòdem", "modem"), ("antena", "antenna", "antena", "antenn"), ("inconveniente", "issue", "inconvenient", "problem"),  # Encounter 15
                ("conexión de alta velocidad", "high-speed connection", "connexió d'alta velocitat", "hög hastighetsanslutning"), ("cable óptico", "fiber optic cable", "cable òptic", "fiberkabel"), ("alcance", "range", "abast", "räckvidd"),  # Encounter 16
                ("corte", "outage", "cort", "avbrott"), ("interrupción", "interruption", "interrupció", "avbrott"), ("megabytes", "megabytes", "megabytes", "megabyte"),  # Encounter 17
                ("bajar archivos", "to download files", "baixar arxius", "ladda ner filer"), ("permanencia", "commitment period", "permanència", "bindningstid"), ("cargar archivos", "to upload files", "carregar arxius", "ladda upp filer"),  # Encounter 18
                ("fecha de pago", "payment date", "data de pagament", "betalningsdatum"), ("mejorar", "to improve", "millorar", "förbättra"), ("soporte al cliente", "customer support", "suport al client", "kundsupport"),  # Encounter 19
                ("televisión", "television", "televisió", "tv"), ("comunicarse", "to communicate", "comunicar-se", "kommunicera"), ("combo", "bundle", "combo", "paket"),  # Encounter 20
                ("streaming", "streaming", "streaming", "streaming"), ("videollamada", "video call", "videotrucada", "videosamtal"), ("juego en línea", "online gaming", "joc en línia", "onlinespel"),  # Encounter 21
                ("módem", "modem", "mòdem", "modem"), ("ilimitado", "unlimited", "il·limitat", "obegränsad"), ("antena receptora", "receiving antenna", "antena receptora", "mottagarantenn"),  # Encounter 22
                ("decodificador", "decoder", "decodificador", "avkodare"), ("firewall", "firewall", "firewall", "brandvägg"), ("área de cobertura", "coverage area", "àrea de cobertura", "täckt område"),  # Encounter 23
                ("virus", "virus", "virus", "virus"), ("malware", "malware", "malware", "skadlig programvara"), ("antivirus", "antivirus", "antivirus", "antivirus"),  # Encounter 24
                ("extensión", "extension/extender", "extensió", "förlängning"), ("repetidor", "repeater", "repetidor", "repeater"), ("amplificar", "to amplify", "amplificar", "förstärka"),  # Encounter 25
                ("dirección IP", "IP address", "adreça IP", "IP-adress"), ("DNS", "DNS", "DNS", "DNS"), ("puerto", "port", "port", "hamn"),  # Encounter 26
                ("ethernet", "ethernet", "ethernet", "ethernet"), ("inalámbrico", "wireless", "inalàmbric", "trådlös"), ("bluetooth", "bluetooth", "bluetooth", "bluetooth"),  # Encounter 27
                ("latencia", "latency", "latència", "latens"), ("ping", "ping", "ping", "ping"), ("estabilidad", "stability", "estabilitat", "stabilitet"),  # Encounter 28
                ("asistencia técnica", "technical support", "assistència tècnica", "teknisk support"), ("soporte", "support", "suport", "stöd"), ("extensión de señal", "signal range", "extensió de senyal", "signalräckvidd"),  # Encounter 29
                ("apagón", "outage", "apagada", "strömavbrott"), ("navegador", "browser", "navegador", "webbläsare"), ("página web", "webpage", "pàgina web", "webbsida"),  # Encounter 30
                ("usuario", "username", "usuari", "användarnamn"), ("falla", "failure", "fallada", "problem"), ("registrar", "to register", "registrar", "registrera"),  # Encounter 31
                ("restablecer", "to restore", "restablir", "återställa"), ("acuerdo de servicio", "service agreement", "acord de servei", "serviceavtal"), ("periodo de permanencia", "commitment period", "període de permanència", "bindningstid"),  # Encounter 32
                ("control parental", "parental controls", "control parental", "föräldrakontroll"), ("dar de baja", "to cancel", "donar de baixa", "avsluta"), ("renovar plan", "to upgrade plan", "renovar pla", "uppgradera plan"),  # Encounter 33
                ("cámara", "camera", "càmera", "kamera"), ("monitor", "monitor", "monitor", "monitor"), ("vigilancia", "surveillance", "vigilància", "övervakning"),  # Encounter 34
                ("domótica", "home automation", "domòtica", "hemautomation"), ("inteligente", "smart", "intel·ligent", "smart"), ("automatizar", "to automate", "automatitzar", "automatisera"),  # Encounter 35
                ("optimizar", "to improve", "optimitzar", "förbättra"), ("almacenar", "to store", "emmagatzemar", "lagra"), ("combo de servicios", "service bundle", "combo de serveis", "tjänstepaket"),  # Encounter 36
                ("impresora", "printer", "impressora", "skrivare"), ("compartir", "to share", "compartir", "dela"), ("acceso remoto", "remote access", "accés remot", "fjärråtkomst"),  # Encounter 37
                ("VPN", "VPN", "VPN", "VPN"), ("privacidad", "privacy", "privacitat", "integritet"), ("encriptar", "to encrypt", "encriptar", "kryptera"),  # Encounter 38
                ("ancho de banda", "bandwidth", "ample de banda", "bandbredd"), ("saturado", "saturated", "saturat", "mättad"), ("TV por cable", "cable TV", "TV per cable", "kabel-TV"),  # Encounter 39
                ("línea fija", "landline", "línia fixa", "fast telefon"), ("competencia", "competition", "competència", "tävling"), ("paquete triple", "triple bundle", "paquet triple", "trippelpaket"),  # Encounter 40
                ("instalación", "installation", "instal·lació", "installation"), ("cableado", "wiring", "cablejat", "elsystem"), ("infraestructura", "infrastructure", "infraestructura", "infrastruktur"),  # Encounter 41
                ("contratación", "hiring/contracting", "contractació", "anställning"), ("video en vivo", "live streaming", "vídeo en viu", "livevideo"), ("llamada de video", "video call", "trucada de vídeo", "videosamtal"),  # Encounter 42
                ("migración", "migration", "migració", "migration"), ("portabilidad", "portability", "portabilitat", "portabilitet"), ("juego en red", "online gaming", "joc en xarxa", "onlinespel"),  # Encounter 43
                ("tope de datos", "data cap", "topall de dades", "datagräns"), ("sin tope", "unlimited", "sense topall", "obegränsad"), ("uso de datos", "data usage", "ús de dades", "dataanvändning"),  # Encounter 44
                ("queja", "complaint", "queixa", "klagomål"), ("protección de red", "network security", "protecció de xarxa", "nätverkssäkerhet"), ("cortafuegos", "firewall", "cortafocs", "brandvägg"),  # Encounter 45
                ("resguardar", "to protect", "resguardar", "skydda"), ("consumo real", "actual usage", "consum real", "faktisk förbrukning"), ("programa malicioso", "malicious software", "programa maliciós", "skadligt program"),  # Encounter 46
                ("satelital", "satellite", "satel·lit", "satellit-"), ("rural", "rural", "rural", "landsbygd"), ("urbano", "urban", "urbà", "urban"),  # Encounter 47
                ("mantenimiento", "maintenance", "manteniment", "underhåll"), ("actualización", "update", "actualització", "uppdatering"), ("software dañino", "harmful software", "programari maliciós", "skadlig programvara"),  # Encounter 48
                ("programa de protección", "protection software", "programa de protecció", "skyddsprogram"), ("amplificador", "amplifier", "amplificador", "förstärkare"), ("encuesta", "survey", "enquesta", "undersökning"),  # Encounter 49
                ("listo", "ready", "llest", "klar"), ("funcionando", "working", "funcionant", "fungerar"), ("repetidor de señal", "signal repeater", "repetidor de senyal", "signalförstärkare"),  # Encounter 50
            ],
        },
    ],
    "core": [
        {
            "title": "Core",
            "goal": "Practice essential everyday Spanish phrases and expressions",
            "word_prefix": "core",
            "words": [
                ("quiero dormir", "I want to sleep", "", "jag vill sova"), ("quiero comer", "I want to eat", "", "jag vill äta"), ("quiero irme", "I want to leave", "", "jag vill gå"),  # Encounter 1
                ("necesito comer", "I need to eat", "", "jag behöver äta"), ("necesito dormir", "I need to sleep", "", "jag behöver sova"), ("necesito salir", "I need to leave", "", "jag behöver gå iväg"),  # Encounter 2
                ("puedo entrar", "I can enter", "", "jag kan gå in"), ("puedo pasar", "I can come in", "", "jag kan komma in"), ("puedo sentarme", "I can sit down", "", "jag kan sätta mig"),  # Encounter 3
                ("no puedo encontrarlo", "I can't find it", "", "jag kan inte hitta det"), ("no puedo hacerlo", "I can't do it", "", "jag kan inte göra det"), ("no puedo verlo", "I can't see it", "", "jag kan inte se det"),  # Encounter 4
                ("voy a salir", "I'm going to leave", "", "jag ska gå ut"), ("voy a entrar", "I'm going to enter", "", "jag ska gå in"), ("voy a volver", "I'm going to return", "", "jag ska komma tillbaka"),  # Encounter 5
                ("estoy buscando", "I am looking", "", "jag letar efter"), ("estoy esperando", "I am waiting", "", "jag väntar"), ("estoy trabajando", "I am working", "", "jag arbetar"),  # Encounter 6
                ("tengo que trabajar", "I have to work", "", "jag måste jobba"), ("tengo que salir", "I have to leave", "", "jag måste gå"), ("tengo que pagar", "I have to pay", "", "jag måste betala"),  # Encounter 7
                ("no tengo que pagar", "I don't have to pay", "", "jag behöver inte betala"), ("no tengo que ir", "I don't have to go", "", "jag behöver inte gå"), ("no tengo que hacerlo", "I don't have to do it", "", "jag behöver inte göra det"),  # Encounter 8
                ("debo llamar", "I should call", "", "jag bör ringa"), ("debo ir", "I should go", "", "jag bör gå"), ("debo pagar", "I should pay", "", "jag bör betala"),  # Encounter 9
                ("trato de entender", "I try to understand", "", "jag försöker förstå"), ("trato de encontrarlo", "I try to find it", "", "jag försöker hitta det"), ("trato de hacerlo", "I try to do it", "", "jag försöker göra det"),  # Encounter 10
                ("puedes ayudarme", "can you help me", "", "kan du hjälpa mig"), ("puedes llamarme", "can you call me", "", "kan du ringa mig"), ("puedes esperarme", "can you wait for me", "", "kan du vänta på mig"),  # Encounter 11
                ("puedes darme agua", "can you give me water", "", "kan du ge mig vatten"), ("puedes darme eso", "can you give me that", "", "kan du ge mig det"), ("puedes darme tiempo", "can you give me time", "", "kan du ge mig tid"),  # Encounter 12
                ("me puedes ayudar con esto", "can you help me with this", "", "kan du hjälpa mig med det här"), ("me puedes ayudar con eso", "can you help me with that", "", "kan du hjälpa mig med det"), ("me puedes ayudar con el problema", "can you help me with the problem", "", "kan du hjälpa mig med problemet"),  # Encounter 13
                ("necesito que vengas", "I need you to come", "", "jag behöver att du kommer"), ("necesito que me ayudes", "I need you to help me", "", "jag behöver att du hjälper mig"), ("necesito que esperes", "I need you to wait", "", "jag behöver att du väntar"),  # Encounter 14
                ("dime la verdad", "tell me the truth", "", "säg mig sanningen"), ("dime qué pasa", "tell me what's happening", "", "säg mig vad som händer"), ("dime dónde está", "tell me where it is", "", "säg mig var det är"),  # Encounter 15
                ("explícame cómo funciona", "explain how it works to me", "", "förklara för mig hur det fungerar"), ("explícame qué pasó", "explain what happened to me", "", "förklara för mig vad som hände"), ("explícame por qué", "explain why to me", "", "förklara för mig varför"),  # Encounter 16
                ("muéstrame dónde está", "show me where it is", "", "visa mig var det är"), ("muéstrame cómo funciona", "show me how it works", "", "visa mig hur det fungerar"), ("muéstrame el camino", "show me the way", "", "visa mig vägen"),  # Encounter 17
                ("déjame ver", "let me see", "", "låt mig se"), ("déjame hacerlo", "let me do it", "", "låt mig göra det"), ("déjame entrar", "let me enter", "", "låt mig komma in"),  # Encounter 18
                ("ayúdame a encontrarlo", "help me find it", "", "hjälp mig att hitta det"), ("ayúdame a hacerlo", "help me do it", "", "hjälp mig att göra det"), ("ayúdame a entender", "help me understand", "", "hjälp mig att förstå"),  # Encounter 19
                ("no me digas eso", "don't tell me that", "", "säg inte det till mig"), ("no me digas nada", "don't tell me anything", "", "säg ingenting till mig"), ("no me digas mentiras", "don't tell me lies", "", "säg inte lögner till mig"),  # Encounter 20
                ("estoy en el hotel", "I am at the hotel", "", "jag är på hotellet"), ("estoy en casa", "I am at home", "", "jag är hemma"), ("estoy en la calle", "I am on the street", "", "jag är på gatan"),  # Encounter 21
                ("voy al baño", "I'm going to the bathroom", "", "jag ska på toaletten"), ("voy al hotel", "I'm going to the hotel", "", "jag ska till hotellet"), ("voy al trabajo", "I'm going to work", "", "jag ska till jobbet"),  # Encounter 22
                ("vengo de la tienda", "I come from the store", "", "jag kommer från affären"), ("vengo del trabajo", "I come from work", "", "jag kommer från jobbet"), ("vengo de casa", "I come from home", "", "jag kommer hemifrån"),  # Encounter 23
                ("estoy cerca del centro", "I'm near downtown", "", "jag är nära centrum"), ("estoy cerca de aquí", "I'm near here", "", "jag är nära här"), ("estoy cerca del lugar", "I'm near the place", "", "jag är nära platsen"),  # Encounter 24
                ("estoy lejos de aquí", "I'm far from here", "", "jag är långt härifrån"), ("estoy lejos del centro", "I'm far from downtown", "", "jag är långt från centrum"), ("estoy lejos de casa", "I'm far from home", "", "jag är långt hemifrån"),  # Encounter 25
                ("voy hacia la salida", "I'm heading toward the exit", "", "jag är på väg mot utgången"), ("voy hacia el centro", "I'm heading toward downtown", "", "jag är på väg mot centrum"), ("voy hacia la puerta", "I'm heading toward the door", "", "jag är på väg mot dörren"),  # Encounter 26
                ("paso por tu casa", "I pass by your house", "", "jag går förbi ditt hus"), ("paso por aquí", "I pass by here", "", "jag går förbi här"), ("paso por el centro", "I pass through downtown", "", "jag passerar centrum"),  # Encounter 27
                ("entro al edificio", "I enter the building", "", "jag går in i byggnaden"), ("entro a la casa", "I enter the house", "", "jag går in i huset"), ("entro al lugar", "I enter the place", "", "jag går in på platsen"),  # Encounter 28
                ("salgo del trabajo", "I leave work", "", "jag slutar jobbet"), ("salgo de casa", "I leave home", "", "jag går hemifrån"), ("salgo del edificio", "I leave the building", "", "jag lämnar byggnaden"),  # Encounter 29
                ("me quedo en casa", "I stay at home", "", "jag stannar hemma"), ("me quedo aquí", "I stay here", "", "jag stannar här"), ("me quedo en el hotel", "I stay at the hotel", "", "jag bor på hotellet"),  # Encounter 30
                ("ya comí", "I already ate", "", "jag har redan ätit"), ("ya llegué", "I already arrived", "", "jag har redan kommit fram"), ("ya terminé", "I already finished", "", "jag är klar"),  # Encounter 31
                ("todavía estoy aquí", "I'm still here", "", "jag är fortfarande här"), ("todavía estoy esperando", "I'm still waiting", "", "jag väntar fortfarande"), ("todavía estoy trabajando", "I'm still working", "", "jag jobbar fortfarande"),  # Encounter 32
                ("aún no llega", "it hasn't arrived yet", "", "det har inte kommit än"), ("aún no empieza", "it hasn't started yet", "", "det har inte börjat än"), ("aún no termina", "it hasn't finished yet", "", "det är inte klart än"),  # Encounter 33
                ("ahora mismo voy", "I'm going right now", "", "jag går precis nu"), ("ahora mismo llego", "I'm arriving right now", "", "jag kommer precis nu"), ("ahora mismo salgo", "I'm leaving right now", "", "jag går precis nu"),  # Encounter 34
                ("después de comer", "after eating", "", "efter att ha ätit"), ("después de trabajar", "after working", "", "efter att ha jobbat"), ("después de salir", "after leaving", "", "efter att ha gått"),  # Encounter 35
                ("antes de salir", "before leaving", "", "innan du går ut"), ("antes de comer", "before eating", "", "innan du äter"), ("antes de entrar", "before entering", "", "innan du går in"),  # Encounter 36
                ("desde ayer", "since yesterday", "", "sedan igår"), ("desde hoy", "since today", "", "från och med idag"), ("desde la mañana", "since the morning", "", "sedan i morse"),  # Encounter 37
                ("por dos horas", "for two hours", "", "i två timmar"), ("por un rato", "for a while", "", "en stund"), ("por unos días", "for a few days", "", "några dagar"),  # Encounter 38
                ("en diez minutos", "in ten minutes", "", "om tio minuter"), ("en un momento", "in a moment", "", "om en stund"), ("en un rato", "in a bit", "", "om en liten stund"),  # Encounter 39
                ("cuando llegues", "when you arrive", "", "när du kommer"), ("cuando salgas", "when you leave", "", "när du går"), ("cuando puedas", "when you can", "", "när du kan"),  # Encounter 40
                ("tengo hambre", "I'm hungry", "", "jag är hungrig"), ("tengo sueño", "I'm sleepy", "", "jag är sömnig"), ("tengo frío", "I'm cold", "", "jag fryser"),  # Encounter 41
                ("tengo calor", "I'm hot", "", "jag är varm"), ("me siento cansado", "I feel tired", "", "jag känner mig trött"), ("me siento bien", "I feel good", "", "jag mår bra"),  # Encounter 42
                ("me siento mal", "I feel bad", "", "jag mår dåligt"), ("me gusta este lugar", "I like this place", "", "jag gillar den här platsen"), ("me gusta esto", "I like this", "", "jag gillar det här"),  # Encounter 43
                ("me gusta eso", "I like that", "", "jag gillar det där"), ("no me gusta eso", "I don't like that", "", "jag gillar inte det"), ("no me gusta esto", "I don't like this", "", "jag gillar inte det här"),  # Encounter 44
                ("no me gusta aquí", "I don't like it here", "", "jag gillar inte det här"), ("necesito dinero", "I need money", "", "jag behöver pengar"), ("necesito ayuda", "I need help", "", "jag behöver hjälp"),  # Encounter 45
                ("necesito tiempo", "I need time", "", "jag behöver tid"), ("busco un baño", "I'm looking for a bathroom", "", "jag letar efter en toalett"), ("busco ayuda", "I'm looking for help", "", "jag söker hjälp"),  # Encounter 46
                ("busco el lugar", "I'm looking for the place", "", "jag letar efter platsen"), ("encuentro la salida", "I find the exit", "", "jag hittar utgången"), ("encuentro el lugar", "I find the place", "", "jag hittar platsen"),  # Encounter 47
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

        num_encounters = len(words) // 3
        for enc_num in range(1, num_encounters + 1):
            # Word indices: 3 words per encounter
            base = (enc_num - 1) * 3
            w1 = words[base]
            w2 = words[base + 1]
            w3 = words[base + 2]

            # Situation ID uses word_prefix for uniqueness (e.g., bank_open_1, bank_wire_1)
            situation_id = f"{prefix}_{enc_num}"

            # Encounter words — tuples are (spanish, english, catalan) or (spanish, english, catalan, swedish)
            for pos, w in enumerate([w1, w2, w3], 1):
                spanish, english, catalan = w[0], w[1], w[2]
                swedish = w[3] if len(w) > 3 else ""
                word_id = f"enc_{prefix}_{(enc_num - 1) * 3 + pos:03d}"
                category_words.append({
                    "id": word_id,
                    "spanish": spanish,
                    "english": english,
                    "catalan": catalan,
                    "swedish": swedish,
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
