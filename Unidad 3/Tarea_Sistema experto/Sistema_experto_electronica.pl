:- dynamic componente/1.
:- dynamic continuidad/1.
:- dynamic voltaje_salida/1.
:- dynamic sobrecalentamiento/1.
:- dynamic hinchado/1.
:- dynamic fuga_corriente/1.
:- dynamic ruido/1.
:- dynamic falla/1.

preguntar_componente :-
    \+ componente(_),
    writeln("Bienvenido al Sistema Experto de Diagnóstico de Fallas Electrónicas."),
    writeln("Por favor, responde todas las preguntas escribiendo 'si', 'no' o lo que se indique."),
    writeln("¿Qué tipo de componente deseas diagnosticar?"),
    writeln("Opciones: fusible, transistor, capacitor, diodo, microcontrolador, resistor, rele, bobina."),
    read(Respuesta),
    assertz(componente(Respuesta)).

preguntar_sintomas :-
    ( \+ continuidad(_) ->
        write("¿Hay continuidad en el componente? (si / no): "), read(R), assertz(continuidad(R))
    ; true ),
    ( \+ voltaje_salida(_) ->
        write("¿Tiene salida de voltaje? (si / no / muy_bajo): "), read(R), assertz(voltaje_salida(R))
    ; true ),
    ( \+ sobrecalentamiento(_) ->
        write("¿El componente se sobrecalienta? (si / no): "), read(R), assertz(sobrecalentamiento(R))
    ; true ),
    ( \+ hinchado(_) ->
        write("¿El componente está hinchado? (si / no): "), read(R), assertz(hinchado(R))
    ; true ),
    ( \+ fuga_corriente(_) ->
        write("¿Se detecta fuga de corriente en el componente? (si / no): "), read(R), assertz(fuga_corriente(R))
    ; true ),
    ( \+ ruido(_) ->
        write("¿El componente emite algún sonido extraño (zumbido, clic)? (si / no / continuo): "), read(R), assertz(ruido(R))
    ; true ).

% Reglas de diagnóstico basadas en los síntomas y tipo de componente
diagnosticar :-
    componente(fusible),
    continuidad(no),
    assertz(falla(fusible_quemado)).

diagnosticar :-
    componente(transistor),
    continuidad(si),
    voltaje_salida(no),
    sobrecalentamiento(si),
    assertz(falla(transistor_cortocircuito)).

diagnosticar :-
    componente(capacitor),
    hinchado(si),
    assertz(falla(capacitor_danado)).

diagnosticar :-
    componente(diodo),
    continuidad(no),
    voltaje_salida(no),
    assertz(falla(diodo_abierto)).

diagnosticar :-
    componente(diodo),
    continuidad(si),
    voltaje_salida(muy_bajo),
    assertz(falla(diodo_cortocircuito)).

diagnosticar :-
    componente(microcontrolador),
    voltaje_salida(si),
    ruido(no),
    continuidad(si),
    assertz(falla(microcontrolador_sin_respuesta)).

diagnosticar :-
    componente(resistor),
    continuidad(no),
    assertz(falla(resistencia_abierta)).

diagnosticar :-
    componente(rele),
    ruido(continuo),
    voltaje_salida(si),
    assertz(falla(rele_pegado)).

diagnosticar :-
    componente(bobina),
    fuga_corriente(si),
    sobrecalentamiento(si),
    assertz(falla(bobina_cortocircuito)).

mostrar_diagnostico :-
    falla(fusible_quemado),
    writeln(">> Diagnóstico: El fusible está quemado. Debe ser reemplazado.").

mostrar_diagnostico :-
    falla(transistor_cortocircuito),
    writeln(">> Diagnóstico: El transistor presenta un cortocircuito. Revisar conexiones y reemplazar.").

mostrar_diagnostico :-
    falla(capacitor_danado),
    writeln(">> Diagnóstico: El capacitor está dañado. Posible hinchazón o fuga de electrolito.").

mostrar_diagnostico :-
    falla(diodo_abierto),
    writeln(">> Diagnóstico: El diodo está abierto. No conduce corriente.").

mostrar_diagnostico :-
    falla(diodo_cortocircuito),
    writeln(">> Diagnóstico: El diodo está en cortocircuito. El voltaje de salida es muy bajo.").

mostrar_diagnostico :-
    falla(microcontrolador_sin_respuesta),
    writeln(">> Diagnóstico: El microcontrolador no responde. Puede estar dañado o mal programado.").

mostrar_diagnostico :-
    falla(resistencia_abierta),
    writeln(">> Diagnóstico: La resistencia está abierta. No hay continuidad.").

mostrar_diagnostico :-
    falla(rele_pegado),
    writeln(">> Diagnóstico: El relé está pegado. Hay zumbido o ruido continuo. Verificar contactos.").

mostrar_diagnostico :-
    falla(bobina_cortocircuito),
    writeln(">> Diagnóstico: La bobina tiene un cortocircuito interno. Posible sobrecalentamiento.").

mostrar_diagnostico :-
    \+ falla(_),
    writeln(">> No se ha detectado ninguna falla específica con los datos proporcionados.").

iniciar :-
    preguntar_componente,
    preguntar_sintomas,
    diagnosticar,
    mostrar_diagnostico.
