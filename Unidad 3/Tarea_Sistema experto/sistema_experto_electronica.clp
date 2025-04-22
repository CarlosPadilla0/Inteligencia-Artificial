
;; Preguntar tipo de componente


(defrule preguntar-componente
   (declare (salience 100))
   (not (componente ?))
   =>
   (printout t "Bienvenido al Sistema Experto de Diagnostico Electronico" crlf)
   (printout t "Por favor, responde las preguntas con 'si' o 'no'" crlf)
   (printout t crlf "¿Que tipo de componente desea diagnosticar?" crlf)
   (printout t "- fusible, transistor, capacitor, diodo, microcontrolador, resistor, rele, bobina" crlf)
   (bind ?resp (read))
   (assert (componente ?resp)))


;; Preguntas comunes de sintomas

(defrule preguntar-continuidad
   (declare (salience 90))
   (not (verificado continuidad))
   =>
   (printout t "¿Hay continuidad en el componente? (si/no): ")
   (bind ?resp (read))
   (assert (verificado continuidad))
   (assert (continuidad ?resp)))

(defrule preguntar-voltaje
   (declare (salience 80))
   (not (verificado voltaje-salida))
   =>
   (printout t "¿Tiene salida de voltaje? (si/no/muy-bajo): ")
   (bind ?resp (read))
   (assert (verificado voltaje-salida))
   (assert (voltaje-salida ?resp)))

(defrule preguntar-sobrecalentamiento
   (declare (salience 70))
   (not (verificado sobrecalentamiento))
   =>
   (printout t "¿El componente se sobrecalienta? (si/no): ")
   (bind ?resp (read))
   (assert (verificado sobrecalentamiento))
   (assert (sobrecalentamiento ?resp)))

(defrule preguntar-hinchado
   (declare (salience 60))
   (not (verificado hinchado))
   =>
   (printout t "¿El componente esta hinchado? (si/no): ")
   (bind ?resp (read))
   (assert (verificado hinchado))
   (assert (hinchado ?resp)))

(defrule preguntar-fuga-corriente
   (declare (salience 50))
   (not (verificado fuga-corriente))
   =>
   (printout t "¿Se detecta fuga de corriente? (si/no): ")
   (bind ?resp (read))
   (assert (verificado fuga-corriente))
   (assert (fuga-corriente ?resp)))

(defrule preguntar-ruido
   (declare (salience 40))
   (not (verificado ruido))
   =>
   (printout t "¿El componente emite un sonido extrano (zumbido, clic)? (si/no/continuo): ")
   (bind ?resp (read))
   (assert (verificado ruido))
   (assert (ruido ?resp)))

;; Reglas de diagnostico

(defrule detectar-fusible
   (componente fusible)
   (continuidad no)
   =>
   (assert (falla fusible-quemado)))

(defrule detectar-transistor
   (componente transistor)
   (continuidad si)
   (voltaje-salida no)
   (sobrecalentamiento si)
   =>
   (assert (falla transistor-en-corto)))

(defrule detectar-capacitor-hinchado
   (componente capacitor)
   (hinchado si)
   =>
   (assert (falla capacitor-danado)))

(defrule detectar-diodo-abierto
   (componente diodo)
   (continuidad no)
   (voltaje-salida no)
   =>
   (assert (falla diodo-abierto)))

(defrule detectar-diodo-en-corto
   (componente diodo)
   (continuidad si)
   (voltaje-salida muy-bajo)
   =>
   (assert (falla diodo-en-corto)))

(defrule detectar-microcontrolador-sin-respuesta
   (componente microcontrolador)
   (voltaje-salida si)
   (ruido no)
   (continuidad si)
   =>
   (assert (falla microcontrolador-sin-respuesta)))

(defrule detectar-resistencia-abierta
   (componente resistor)
   (continuidad no)
   =>
   (assert (falla resistencia-abierta)))

(defrule detectar-rele-pegado
   (componente rele)
   (ruido continuo)
   (voltaje-salida si)
   =>
   (assert (falla rele-pegado)))

(defrule detectar-bobina-en-corto
   (componente bobina)
   (fuga-corriente si)
   (sobrecalentamiento si)
   =>
   (assert (falla bobina-corto)))

;; Diagnosticos

(defrule diagnostico-fusible
   (falla fusible-quemado)
   =>
   (printout t crlf ">> Diagnostico Final: Fusible quemado. Reemplazar." crlf))

(defrule diagnostico-transistor
   (falla transistor-en-corto)
   =>
   (printout t crlf ">> Diagnostico Final: Transistor en cortocircuito. Verificar conexiones." crlf))

(defrule diagnostico-capacitor
   (falla capacitor-danado)
   =>
   (printout t crlf ">> Diagnostico Final: El capacitor esta danado (posible hinchazon o fuga)." crlf))

(defrule diagnostico-diodo-abierto
   (falla diodo-abierto)
   =>
   (printout t crlf ">> Diagnostico Final: El diodo esta abierto, no conduce corriente." crlf))

(defrule diagnostico-diodo-corto
   (falla diodo-en-corto)
   =>
   (printout t crlf ">> Diagnostico Final: El diodo esta en cortocircuito, baja caida de voltaje." crlf))

(defrule diagnostico-micro
   (falla microcontrolador-sin-respuesta)
   =>
   (printout t crlf ">> Diagnostico Final: El microcontrolador no responde, revisar programacion o danos internos." crlf))

(defrule diagnostico-resistencia
   (falla resistencia-abierta)
   =>
   (printout t crlf ">> Diagnostico Final: Resistencia abierta, circuito interrumpido." crlf))

(defrule diagnostico-rele
   (falla rele-pegado)
   =>
   (printout t crlf ">> Diagnostico Final: Rele pegado, revisar contactos." crlf))

(defrule diagnostico-bobina
   (falla bobina-corto)
   =>
   (printout t crlf ">> Diagnostico Final: Bobina en cortocircuito, posible sobrecalentamiento." crlf))
