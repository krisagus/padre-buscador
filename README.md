# Padre Buscador: Radar de la Esperanza (Recuperación y Rescate de Vida)

**Autor original e investigador principal:** Agustín Christian Aragón López  
**Institución:** Universidad Autónoma de Baja California (UABC) - Ciencia de Datos  
**Fecha de registro inicial:** 25 de septiembre de 2026  

## Propósito Humanitario y Social
Este proyecto nace bajo el nombre **Padre Buscador (Radar de la Esperanza)** con el objetivo de desarrollar tecnología de detección y rescate de ultra bajo costo. Está pensado como una herramienta accesible y solidaria que pueda servir de apoyo técnico a los colectivos de **Madres Buscadoras** y brigadas de rescate, democratizando el acceso a sistemas de detección mediante hardware cotidiano y ciencia de datos.

## Descripción Técnica y Aportación Propia
A diferencia de sistemas comerciales costosos o implementaciones dependientes de hardware especializado, **Padre Buscador** implementa un sistema de radar pasivo de apertura sintética (SAR) utilizando periféricos estándar de bajo costo para la localización de sobrevivientes, detección de signos vitales y anomalías a través de obstáculos, muros o terreno.

El sistema utiliza una antena **Signal King RT3070** para medir variaciones en el RSSI de ondas de radiofrecuencia ambientales, integrando:
1. **Adquisición pasiva de RF (`src/capture_rssi.py`):** Captura en modo monitor de fluctuaciones de potencia RSSI.
2. **Procesamiento de Ciencia de Datos (`src/processor.py`):** Filtrado de Kalman y análisis espectral para limpiar el ruido y aislar patrones de interferencia.
3. **Rastreo Espacial y Odometría (`src/spatial_tracker.py`):** Fusión de coordenadas precisas mediante sensor óptico (ratón) y datos inerciales (IMU móvil) para reconstruir el barrido espacial.

## Referencias, Créditos y Proyectos Base
Este proyecto sigue la filosofía del software libre y toma inspiración conceptual en el mapeo y análisis espectral Wi-Fi de los siguientes repositorios de la comunidad:

* **[ruvnet/RuView](https://github.com/ruvnet/RuView):** Referencia conceptual en visualización y mapeo espacial mediante señales inalámbricas.
* **[francescopace/espectre](https://github.com/francescopace/espectre):** Inspiración en el análisis espectral de radiofrecuencia, adaptado en este proyecto hacia una arquitectura pasiva con antena RT3070 y odometría óptica.

## Espíritu Open Source y Colaboraciones
Este proyecto se distribuye bajo la **Licencia MIT**. ¡Toda contribución de la comunidad para mejorar los filtros matemáticos, optimizar la captura con la RT3070 o potenciar su uso en labores de rescate es bienvenida mediante *Fork* y *Pull Request*!
