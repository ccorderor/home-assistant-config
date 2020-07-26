## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/ccorderor/home-assistant-config/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

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
