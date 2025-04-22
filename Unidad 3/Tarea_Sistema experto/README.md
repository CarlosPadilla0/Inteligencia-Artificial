# Sistema Experto de Diagnóstico Electrónico

## Descripción

Este sistema experto está diseñado para diagnosticar fallas comunes en componentes electrónicos. Utiliza un conjunto de reglas basadas en hechos y síntomas proporcionados por el usuario para identificar posibles problemas en componentes como fusibles, transistores, capacitores, diodos, microcontroladores, resistencias, relés y bobinas.

El sistema interactúa con el usuario mediante preguntas específicas sobre los síntomas observados en el componente, y con base en las respuestas, determina el diagnóstico más probable.

## Características

- **Interfaz interactiva:** El sistema realiza preguntas al usuario para recopilar información sobre el estado del componente.
- **Diagnósticos específicos:** Proporciona diagnósticos detallados para diferentes tipos de componentes electrónicos.
- **Reglas basadas en hechos:** Utiliza reglas CLIPS para inferir fallas a partir de los síntomas observados.
- **Componentes soportados:** Fusibles, transistores, capacitores, diodos, microcontroladores, resistencias, relés y bobinas.

## Funcionamiento

1. **Inicio del sistema:** El sistema da la bienvenida al usuario y solicita el tipo de componente que desea diagnosticar.
2. **Recopilación de síntomas:** Se realizan preguntas específicas sobre los síntomas observados, como continuidad, voltaje, sobrecalentamiento, hinchazón, fugas de corriente, y ruidos extraños.
3. **Inferencia de fallas:** Con base en las respuestas del usuario, el sistema aplica reglas predefinidas para identificar la falla más probable.
4. **Diagnóstico final:** El sistema imprime un diagnóstico detallado con recomendaciones para resolver el problema.

## Ejemplo de Diagnósticos

- **Fusible quemado:** "Fusible quemado. Reemplazar."
- **Transistor en cortocircuito:** "Transistor en cortocircuito. Verificar conexiones."
- **Capacitor dañado:** "El capacitor está dañado (posible hinchazón o fuga)."
- **Diodo abierto:** "El diodo está abierto, no conduce corriente."
- **Microcontrolador sin respuesta:** "El microcontrolador no responde, revisar programación o daños internos."

## Reglas Principales

El sistema utiliza reglas CLIPS para diagnosticar fallas. Algunas de las reglas principales incluyen:

- **Fusible quemado:** Si no hay continuidad en el fusible.
- **Transistor en cortocircuito:** Si hay continuidad, no hay salida de voltaje y el componente se sobrecalienta.
- **Capacitor dañado:** Si el capacitor está hinchado.
- **Diodo en cortocircuito:** Si hay continuidad y la salida de voltaje es muy baja.
- **Bobina en cortocircuito:** Si hay fuga de corriente y sobrecalentamiento.

## Requisitos

- **CLIPS:** Este sistema está implementado en el lenguaje CLIPS, por lo que es necesario tener instalado el entorno de ejecución de CLIPS para ejecutarlo.

## Uso

1. Ejecuta el archivo `sistema_experto_electronica.clp` en el entorno de CLIPS.
2. Responde las preguntas que el sistema te hará sobre el componente que deseas diagnosticar.
3. Revisa el diagnóstico final proporcionado por el sistema.

## Autores

- Diana Leticia Alvarez Moreno
- Carlos Eduardo Padilla Pimentel