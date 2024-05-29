# Análisis de accidentes fatales de transito en la ciudad de Buenos Aires

El presente repositorio contiene un análisis estadístico y descriptivo sobre los accidentes fatales de tránsito en la ciudad de Buenos Aires.
Los datos se obtuvieron del [dataset](https://docs.google.com/spreadsheets/d/1nq00jGIZHQ1RLSET43zKnUsMsoFb-pBg/edit#gid=1625530738) brindado por el Gobierno de la Ciudad de Buenos Aires.

Se realizó un [análisis exploratorio y limpieza de los datos](/ETL-EDA.ipynb), subiendose los datos a un repositorio de MySQL, y luego analizando los mismos en un [tablero con datos dinámicos](/Analisis%20Power%20BI.pbix), para que los responsables de tránsito puedan buscar ubicaciones en dónde gestionar.

Por otro lado, dado que la transparencia de un gobierno es fundamental, se generó una [app online](https://transito-bsas.onrender.com) para que los ciudadanos puedan obtener información acerca de los accidentes fatales en su comuna.

## Calidad y limpieza de los datos

Los datos obtenidos eran de buena calidad. En muy pocos casos se obtenían datos nulos, y no había casos repetidos.
Sobre las ubicaciones nulas, se obtuvo la ubicación de la dirección más similar.
También se bajó la precisión de la geolocalización. Se tenía una precisión al mm, y se bajó su exactitud a 12 m, de manera tal de que los accidentes que hayan ocurrido a pocos metros de la misma esquina, sean considerados como del mismo lugar, ayudando a encontrar las ubicaciones que son más propensas a los accidentes fatales.

## Análisis exploratorio de datos

Del análisis de los datos podemos concluir que la tendencia de las muertes por accidentes viales viene bajando. Existe una excepción en el año 2020, que tiene un valor muy bajo, pero esto es debido a la baja circulación de vehículos que hubo en la pandemia.

![Muertesporanio](/Datos_procesados/Muertesxanio.png)

La mayoría de los accidentes fatales se dan en las avenidas.

![Tipo_de_calle](/Datos_procesados/Tipo_de_calle.png)

La mayor cantidad de víctimas eran peatones o viajaban en moto.

![VICTIMA](/Datos_procesados/VICTIMA.png)

La mayor cantidad de accidentes fueron generados por autos, vehículos de carga y de transporte de pasajeros

![ACUSADO](/Datos_procesados/ACUSADO.png)

Se analizó la edad y vehículo de las víctimas, y se conculuyó que los motociclistas de entre 20 y 40 años, y los peatones mayores de 60 son los grupos que más muertes tuvieron. Debería trabajarse sobre capacitación y prevención, e infraestructura para proteger a esos grupos.

## KPIs

Se definieron tres KPIs para gestionar la Dirección de tránsito. La gestión de los mismos reflejará el impacto de las políticas de prevención realizadas.

### Tasa de homicidios en siniestros viales

*Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior.*

![KPI1](/Datos_procesados/KPI1.png)

Puede observarse que en el último semestre se cumple con dicho objetivo.

### Accidentes mortales de motociclistas

*Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior.*

![KPI2](/Datos_procesados/KPI2.png)

El último año no pudo cumplirse el objetivo. Sin embargo, se mide contra un año que tiene un valor anormal, debido a la baja circulación ed tránsito durante la pandemia.

### Accidentes mortales causados por el transporte público

*Reducir en un 15% la cantidad de accidentes mortales causados por colectivos.*

![KPI3](/Datos_procesados/KPI3.png)

La alta capacidad de gestión que tiene el gobierno de la ciudad sobre el transporte público genera la responsabilidad de gestionar y accionar para bajar esta causa de mortalidad. El último año pudo alcanzarse el objetivo.