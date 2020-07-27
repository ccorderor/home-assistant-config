## Hogar Digital con Home Assistant... y más

Hace ya unos cuantos años me picó la mosca de la **domótica** y desde ese momento no he parado de cacharrear. Siempre he tenido algo claro, la domótica hecha por uno mismo es la que mejor cumple las necesidades de cada hogar. Este repositorio debe servir como inspiración, y espero que permita que partes del mismo aterricen en otras cosas. Úsalo como inspiración, como fuente de datos, como lo que quieras... pero aprovecha todo lo que quieras.

Mi _smart home_ está basada en Home Assistant y Node Red... con un poquito de allí y otro poquito de allá. ¡Disfruta!

## ¿Qué encontrarás aquí?

Debo decirte, para empezar, que aquí encontrarás mucha información. No es ni mucho menos necesario integrar todo lo que puedes ver aquí para tener un **hogar digital**, pero sirva como aviso a navegantes que la domótica es algo que suele enganchar... y por lo tanto, es posible que una vez que empieces, esto se convierta en un hobbie que nunca termine.

## Infraestructura



## Diagramas

![Image](https://github.com/ccorderor/home-assistant-config/raw/master/docs/images/hardware.png)

![Image](https://github.com/ccorderor/home-assistant-config/raw/master/docs/images/zwave.png)

![Image](https://github.com/ccorderor/home-assistant-config/raw/master/docs/images/zigbee.png)

![Image](https://github.com/ccorderor/home-assistant-config/raw/master/docs/images/philipshue.png)

## Climatización / Climate

### Calefacción / Heating

La calefacción está controlada por componentes de la marca Tadoº compuesto por un termostato con compatibilidad OpenTherm conectado a una caldera de gas Viessmann Vitodens y una serie de TRV que regulan la temperatura de las estancias principales de la vivienda (salón y habitaciones). También hay dos TRVs con tecnología Z-Wave en los radiadores del despacho, dado que los instalé antes de instalar Tadoº (que a su vez, reemplaza un termostato Google Nest).

El termostato y todos los TRVs están integrados en Home Assistant, ya sea con el componente de Tadoº o a través de la red Z-Wave.

### Aire Acondicionado / AC

En casa hay a día de hoy 4 equipos (tipo split) de aire acondicionado. El más reciente es un Daikin con módulo IP, por lo que tiene integración directa con Home Assistant. Los otros 3 (2 Mitsubishi Electric y 1 Daikin) son de tipo "dumb", es decir, sólo se pueden controlar con mando a distancia IR.

Por lo tanto, ¿no podemos controlarlos? En una casa en la que se busca la eficiencia energética eso no tiene ningún sentido, así que si, si son controlables. Para ello utilizo:
- Un broadlink RM mini en cada estancia donde quiero controlar un split AC
- Un sensor magnético para saber si el equipo está encendido o apagado (si, yo tampoco me lo creí cuando lo leí)
- Un sensor de temperatura (y opcionalmente uno de humedad)
- Un componente custom en HA llamado **SmartIR** ([Link](https://github.com/smartHomeHub/SmartIR)) que permite agrupar todos los componentes y crear un componente de tipo **climate** que a todos los efectos permite simular un equipo de AC inteligente.

_Inicialmente tenía previsto controlar si los equipos AC estaban conectados con un sensor de consumo eléctrico, pero hace un tiempo leí en un foro una idea brillante: utilizar un sensor magnético de puerta/ventana de Xiaomi Aqara, dado que cuando un equipo AC está encendido, la trampilla de aire se mueve y abre, y cuando esté apagado, se cierra. Haré una foto próximamente_


## Seguridad / Security

La seguridad fue una de las bases principales sobre las que empecé, hace años, a montar un sistema de domótica. Estaba muy cansado de pagar una cuota mensual a una central de alarmas que, cuando hacía falta, no servía para nada.

Por supuesto, **la seguridad no es absoluta**, pero a lo largo de los años he conseguido integrar un sistema que cumple ampliamente con mis condiciones:
- Utiliza dispositivos cableados e inalámbricos
- Utiliza dispositivos de distintas tecnologías
- Une sensores de diversos tipos, video y audio
- Tiene un sistema de simulación de presencia
- Está redundado: el sistema está comunicado con un servidor externo, y en caso de cortarse la comunicación, inmediatamente lo comunica

El código del sistema de alarma no lo publico por motivos obvios.

El sistema se nutre de un gran número de sensores:
- Dos alarmas de Visonic, en formato híbrido
- Sensores en ventanas, puertas y movimiento
- Cámaras con reconocimiento de objetos (tensorflow y otros componentes)

La gestión de la alarma se realiza con Home Assistant y varios nodos de Node-Red. También existe un panel en la puerta dedicado a la alarma y un sensor RFID oculto con tags que permiten desactivar la alarma.

La alarma, en remoto, está conectada con varios sistemas de aviso: notificaciones al móvil, SMS y Twilio para notificaciones por voz.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ccorderor/home-assistant-config/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
