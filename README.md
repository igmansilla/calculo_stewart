# Cálculo de Varias Variables - James Stewart (Ejercicios Modularizados)

Este repositorio contiene la estructura modularizada para resolver la colección de ejercicios del libro **Cálculo de Varias Variables** de **James Stewart** (Capítulo 12: Derivadas Parciales y secciones sucesivas). 

La estructura está diseñada para permitir la compilación tanto de un compendio general del libro como de cuadernillos específicos de cada sección, con espacios pre-configurados para la resolución de los problemas a mano.

---

## 📂 Estructura del Proyecto

La estructura del proyecto es completamente modular, siguiendo el patrón de diseño implementado para Serway:

```text
calculo_stewart/
├── .gitignore
├── README.md
├── build.py                             # Script de compilación automatizada
├── main.tex                             # Archivo maestro del libro completo
├── pdfs/                                # Carpeta de salida para los PDFs compilados
│   ├── Stewart_Calculo_Completo.pdf
│   ├── capitulo_12/                         # PDFs de Derivadas Parciales (Capítulo 12)
│   │   ├── Stewart_Seccion_12_1_Funciones_de_Varias_Variables.pdf
│   │   └── ... (secciones 12.2 a 12.8, repaso y problemas adicionales)
│   ├── capitulo_13/                         # PDFs de Integrales Múltiples (Capítulo 13)
│   │   ├── Stewart_Seccion_13_1_Integrales_Dobles_sobre_Rectangulos.pdf
│   │   └── ... (secciones 13.2 a 13.9, repaso y problemas adicionales)
│   ├── capitulo_14/                         # PDFs de Cálculo Vectorial (Capítulo 14)
    │   ├── Stewart_Seccion_14_1_Campos_Vectoriales.pdf
    │   ├── Stewart_Seccion_14_2_Integrales_de_Linea.pdf
    │   ├── Stewart_Seccion_14_3_Teorema_Fundamental_para_Integrales_de_Linea.pdf
    │   ├── Stewart_Seccion_14_4_Teorema_de_Green.pdf
    │   ├── Stewart_Seccion_14_5_Rotacional_y_Divergencia.pdf
    │   ├── Stewart_Seccion_14_6_Superficies_Parametricas_y_sus_Areas.pdf
    │   ├── Stewart_Seccion_14_7_Integrales_de_Superficie.pdf
    │   ├── Stewart_Seccion_14_8_Teorema_de_Stokes.pdf
    │   ├── Stewart_Seccion_14_9_Teorema_de_la_Divergencia.pdf
    │   ├── Stewart_Capitulo_14_Repaso.pdf
    │   └── Stewart_Capitulo_14_Problemas_Adicionales.pdf
    └── capitulo_15/                         # PDFs de Ecuaciones Diferenciales (Capítulo 15)
        ├── Stewart_Seccion_15_1_Ecuaciones_Diferenciales_Separables_y_Homogeneas.pdf
        ├── Stewart_Seccion_15_2_Ecuaciones_Diferenciales_Lineales_y_de_Bernoulli.pdf
        ├── Stewart_Seccion_15_3_Ecuaciones_Diferenciales_Exactas_y_Factores_Integrantes.pdf
        ├── Stewart_Seccion_15_4_Estrategia_para_Resolver_Ecuaciones_de_Primer_Orden.pdf
        ├── Stewart_Seccion_15_5_Ecuaciones_Lineales_de_Segundo_Orden.pdf
        ├── Stewart_Seccion_15_6_Coeficientes_Indeterminados_y_Variacion_de_Parametros.pdf
        ├── Stewart_Seccion_15_7_Aplicaciones_de_las_Ecuaciones_Diferenciales_de_Segundo_Orden.pdf
        ├── Stewart_Seccion_15_8_Soluciones_en_Series_de_Potencias.pdf
        ├── Stewart_Capitulo_15_Repaso.pdf
        └── Stewart_Capitulo_15_Aplicaciones_Adicionales.pdf
├── derivadas_parciales/                 # Bloque de Derivadas Parciales
│   ├── capitulo_12.tex                  # Índice de secciones del Capítulo 12
│   ├── seccion_12_1/                    # Sección 12.1: Funciones de Varias Variables
│   │   ├── seccion_12_1.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_1_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_64/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_2/                    # Sección 12.2: Límites y Continuidad
│   │   ├── seccion_12_2.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_2_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_42/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_3/                    # Sección 12.3: Derivadas Parciales
│   │   ├── seccion_12_3.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_3_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_001/ a ejercicio_100/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_4/                    # Sección 12.4: Tangentes y Diferenciales
│   │   ├── seccion_12_4.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_4_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_42/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_5/                    # Sección 12.5: Regla de la Cadena
│   │   ├── seccion_12_5.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_5_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_53/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_6/                    # Sección 12.6: Derivadas Direccionales y el Vector Gradiente
│   │   ├── seccion_12_6.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_6_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_58/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_7/                    # Sección 12.7: Valores Máximos y Mínimos
│   │   ├── seccion_12_7.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_7_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_48/ # Enunciados individuales de los ejercicios
│   ├── seccion_12_8/                    # Sección 12.8: Multiplicadores de Lagrange
│   │   ├── seccion_12_8.tex             # Lista modularizada de ejercicios
│   │   ├── seccion_12_8_standalone.tex  # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_38/ # Enunciados individuales de los ejercicios
│   ├── repaso/                          # Capítulo 12: Ejercicios de Repaso
│   │   ├── repaso.tex                   # Lista modularizada de ejercicios
│   │   ├── repaso_standalone.tex        # Documento independiente para compilar solo esta sección
│   │   └── ejercicio_01/ a ejercicio_69/ # Enunciados individuales de los ejercicios
│   └── problemas_adicionales/           # Capítulo 12: Problemas Adicionales
│       ├── problemas_adicionales.tex    # Lista modularizada de ejercicios
│       ├── problemas_adicionales_standalone.tex # Documento independiente para compilar solo esta sección
│       └── ejercicio_01/ a ejercicio_14/ # Enunciados individuales de los ejercicios
└── integrales_multiples/                # Bloque de Integrales Múltiples
    ├── capitulo_13.tex                  # Índice de secciones del Capítulo 13
    ├── seccion_13_1/                    # Sección 13.1: Integrales Dobles sobre Rectángulos
    │   ├── seccion_13_1.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_1_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_12/ # Enunciados individuales de los ejercicios
    ├── seccion_13_2/                    # Sección 13.2: Integrales Iteradas
    │   ├── seccion_13_2.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_2_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_34/ # Enunciados individuales de los ejercicios
    ├── seccion_13_3/                    # Sección 13.3: Integrales Dobles sobre Regiones Generales
    │   ├── seccion_13_3.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_3_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_53/ # Enunciados individuales de los ejercicios
    ├── seccion_13_4/                    # Sección 13.4: Integrales Dobles en Coordenadas Polares
    │   ├── seccion_13_4.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_4_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_32/ # Enunciados individuales de los ejercicios
    ├── seccion_13_5/                    # Sección 13.5: Aplicaciones de las Integrales Dobles
    │   ├── seccion_13_5.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_5_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_24/ # Enunciados individuales de los ejercicios
    ├── seccion_13_6/                    # Sección 13.6: Área de una Superficie
    │   ├── seccion_13_6.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_6_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_14/ # Enunciados individuales de los ejercicios
    ├── seccion_13_7/                    # Sección 13.7: Integrales Triples
    │   ├── seccion_13_7.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_7_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_44/ # Enunciados individuales de los ejercicios
    ├── seccion_13_8/                    # Sección 13.8: Integrales Triples en Coordenadas Cilindricas y Esfericas
    │   ├── seccion_13_8.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_8_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_38/ # Enunciados individuales de los ejercicios
    ├── seccion_13_9/                    # Sección 13.9: Cambio de Variables en Integrales Múltiples
    │   ├── seccion_13_9.tex             # Lista modularizada de ejercicios
    │   ├── seccion_13_9_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_24/ # Enunciados individuales de los ejercicios
    ├── repaso/                          # Capítulo 13: Ejercicios de Repaso
    │   ├── repaso.tex                   # Lista modularizada de ejercicios
    │   ├── repaso_standalone.tex        # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_54/ # Enunciados individuales de los ejercicios
    └── problemas_adicionales/           # Capítulo 13: Aplicaciones Adicionales
        ├── problemas_adicionales.tex    # Lista modularizada de ejercicios
        ├── problemas_adicionales_standalone.tex # Documento independiente para compilar solo esta sección
        └── ejercicio_01/ a ejercicio_08/ # Enunciados individuales de los ejercicios
└── calculo_vectorial/                   # Bloque de Cálculo Vectorial
    ├── capitulo_14.tex                  # Índice de secciones del Capítulo 14
    ├── seccion_14_1/                    # Sección 14.1: Campos Vectoriales
    │   ├── seccion_14_1.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_1_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_19/ # Enunciados individuales de los ejercicios
    ├── seccion_14_2/                    # Sección 14.2: Integrales de Línea
    │   ├── seccion_14_2.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_2_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_35/ # Enunciados individuales de los ejercicios
    ├── seccion_14_3/                    # Sección 14.3: Teorema Fundamental para Integrales de Línea
    │   ├── seccion_14_3.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_3_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_30/ # Enunciados individuales de los ejercicios
    ├── seccion_14_4/                    # Sección 14.4: Teorema de Green
    │   ├── seccion_14_4.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_4_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_29/ # Enunciados individuales de los ejercicios
    ├── seccion_14_5/                    # Sección 14.5: Rotacional y Divergencia
    │   ├── seccion_14_5.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_5_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_41/ # Enunciados individuales de los ejercicios
    ├── seccion_14_6/                    # Sección 14.6: Superficies Paramétricas y sus Áreas
    │   ├── seccion_14_6.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_6_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_26/ # Enunciados individuales de los ejercicios
    ├── seccion_14_7/                    # Sección 14.7: Integrales de Superficie
    │   ├── seccion_14_7.tex             # Lista modularizada de ejercicios
    │   ├── seccion_14_7_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_34/ # Enunciados individuales de los ejercicios
    └── seccion_14_8/                    # Sección 14.8: Teorema de Stokes
        ├── seccion_14_8.tex             # Introducción y Teorema de Stokes (Ejercicios 1 a 20)
        ├── seccion_14_8_standalone.tex  # Documento independiente para compilar solo esta sección
        └── ejercicio_01/ a ejercicio_20/ # Enunciados individuales de los ejercicios
    ├── seccion_14_9/                    # Sección 14.9: Teorema de la Divergencia
    │   ├── seccion_14_9.tex             # Introducción y Teorema de la Divergencia (Ejercicios 1 a 24)
    │   ├── seccion_14_9_standalone.tex  # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_24/ # Enunciados individuales de los ejercicios
    ├── repaso/                          # Capítulo 14: Repaso
    │   ├── repaso.tex                   # Temas Básicos, Ejercicios 1-21 y Continuación 46-49
    │   ├── repaso_standalone.tex        # Documento independiente para compilar solo el repaso
    │   └── ejercicio_01/ a ejercicio_49/ # Enunciados individuales de los ejercicios
    ├── problemas_adicionales/           # Capítulo 14: Problemas Adicionales
    │   ├── problemas_adicionales.tex    # Lista modularizada de problemas
    │   ├── problemas_adicionales_standalone.tex # Documento independiente para compilar solo esta sección
    │   └── ejercicio_01/ a ejercicio_12/ # Enunciados individuales de los problemas
    └── ecuaciones_diferenciales/        # Bloque de Ecuaciones Diferenciales
        ├── capitulo_15.tex              # Índice de secciones del Capítulo 15
        ├── seccion_15_1/                # Sección 15.1: Ecuaciones Separables y Homogéneas
        │   ├── seccion_15_1.tex         # Lista modularizada de ejercicios
        │   ├── seccion_15_1_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_36/ # Enunciados individuales de los ejercicios
        ├── seccion_15_2/                # Sección 15.2: Ecuaciones Lineales y de Bernoulli
        │   ├── seccion_15_2.tex         # Lista modularizada de ejercicios
        │   ├── seccion_15_2_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_33/ # Enunciados individuales de los ejercicios
        ├── seccion_15_3/                # Sección 15.3: Ecuaciones Exactas y Factores Integrantes
        │   ├── seccion_15_3.tex         # Lista modularizada de ejercicios
        │   ├── seccion_15_3_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_27/ # Enunciados individuales de los ejercicios
        ├── seccion_15_4/                # Sección 15.4: Estrategia de Primer Orden
        │   ├── seccion_15_4.tex         # Contenido conceptual y guías de clasificación
        │   ├── seccion_15_4_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_25/ # Enunciados individuales de los ejercicios
        ├── seccion_15_5/                # Sección 15.5: Ecuaciones Lineales de Segundo Orden
        │   ├── seccion_15_5.tex         # Contenido conceptual e introducción (Ecuación 15.23)
        │   └── seccion_15_5_standalone.tex # Documento independiente para compilar solo esta sección
        ├── seccion_15_6/                # Sección 15.6: Coeficientes Indeterminados y Variación de Parámetros
        │   ├── seccion_15_6.tex         # Lista modularizada de ejercicios
        │   ├── seccion_15_6_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_26/ # Enunciados individuales de los ejercicios
        ├── seccion_15_7/                # Sección 15.7: Aplicaciones de Ecuaciones de Segundo Orden
        │   ├── seccion_15_7.tex         # Contenido conceptual, resorte en TikZ y analogías RLC
        │   ├── seccion_15_7_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_13/ # Enunciados individuales de los ejercicios
        ├── seccion_15_8/                # Sección 15.8: Soluciones en Series de Potencias
        │   ├── seccion_15_8.tex         # Contenido conceptual, series e integral de Bessel de orden 0
        │   ├── seccion_15_8_standalone.tex # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_12/ # Enunciados individuales de los ejercicios
        ├── repaso/                      # Capítulo 15: Repaso
        │   ├── repaso.tex               # Preguntas conceptuales, de clasificación y 44 ejercicios
        │   ├── repaso_standalone.tex    # Documento independiente para compilar solo esta sección
        │   └── ejercicio_01/ a ejercicio_44/ # Enunciados individuales de los ejercicios del repaso
        └── aplicaciones_adicionales/    # Capítulo 15: Aplicaciones Adicionales
            ├── aplicaciones_adicionales.tex # Problemas avanzados de modelado físico
            ├── aplicaciones_adicionales_standalone.tex # Documento independiente para compilar solo esta sección
            └── ejercicio_01/ a ejercicio_05/ # Enunciados individuales de los ejercicios avanzados
```

---

## 🛠️ Cómo Compilar los Ejercicios

El script `build.py` automatiza completamente la compilación llamando a `pdflatex` y realizando las pasadas requeridas para los índices y referencias cruzadas, limpiando automáticamente todos los archivos temporales auxiliares `.aux`, `.log`, `.toc`, etc.

### 1. Compilar todo (Libro general y Secciones Standalone)
Para compilar todos los objetivos configurados:
```bash
./build.py
```

### 2. Compilar un objetivo específico
Puedes ver los objetivos disponibles dentro de `build.py` y compilar solo uno:
- **Libro completo (`main.tex`)**:
  ```bash
  ./build.py --target main
  ```
- **Sección 12.1 independiente (`seccion_12_1_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_1
  ```
- **Sección 12.2 independiente (`seccion_12_2_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_2
  ```
- **Sección 12.3 independiente (`seccion_12_3_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_3
  ```
- **Sección 12.4 independiente (`seccion_12_4_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_4
  ```
- **Sección 12.5 independiente (`seccion_12_5_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_5
  ```
- **Sección 12.6 independiente (`seccion_12_6_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_6
  ```
- **Sección 12.7 independiente (`seccion_12_7_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_7
  ```
- **Sección 12.8 independiente (`seccion_12_8_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_12_8
  ```
- **Capítulo 12 Repaso independiente (`repaso_standalone.tex`)**:
  ```bash
  ./build.py --target repaso
  ```
- **Capítulo 12 Problemas Adicionales independiente (`problemas_adicionales_standalone.tex`)**:
  ```bash
  ./build.py --target problemas_adicionales
  ```
- **Sección 13.1 independiente (`seccion_13_1_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_1
  ```
- **Sección 13.2 independiente (`seccion_13_2_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_2
  ```
- **Sección 13.3 independiente (`seccion_13_3_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_3
  ```
- **Sección 13.4 independiente (`seccion_13_4_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_4
  ```
- **Sección 13.5 independiente (`seccion_13_5_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_5
  ```
- **Sección 13.6 independiente (`seccion_13_6_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_6
  ```
- **Sección 13.7 independiente (`seccion_13_7_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_7
  ```
- **Sección 13.8 independiente (`seccion_13_8_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_8
  ```
- **Sección 13.9 independiente (`seccion_13_9_standalone.tex`)**:
  ```bash
  ./build.py --target seccion_13_9
  ```
- **Capítulo 13 Repaso independiente (`repaso_standalone.tex` en `integrales_multiples/repaso/`)**:
  ```bash
  ./build.py --target repaso_13
  ```
- **Capítulo 13 Problemas Adicionales independiente (`problemas_adicionales_standalone.tex` en `integrales_multiples/problemas_adicionales/`)**:
  ```bash
  ./build.py --target problemas_adicionales_13
  ```
- **Sección 14.1 independiente (`seccion_14_1_standalone.tex` en `calculo_vectorial/seccion_14_1/`)**:
  ```bash
  ./build.py --target seccion_14_1
  ```
- **Sección 14.2 independiente (`seccion_14_2_standalone.tex` en `calculo_vectorial/seccion_14_2/`)**:
  ```bash
  ./build.py --target seccion_14_2
  ```
- **Sección 14.3 independiente (`seccion_14_3_standalone.tex` en `calculo_vectorial/seccion_14_3/`)**:
  ```bash
  ./build.py --target seccion_14_3
  ```
- **Sección 14.4 independiente (`seccion_14_4_standalone.tex` en `calculo_vectorial/seccion_14_4/`)**:
  ```bash
  ./build.py --target seccion_14_4
  ```
- **Sección 14.5 independiente (`seccion_14_5_standalone.tex` en `calculo_vectorial/seccion_14_5/`)**:
  ```bash
  ./build.py --target seccion_14_5
  ```
- **Sección 14.6 independiente (`seccion_14_6_standalone.tex` en `calculo_vectorial/seccion_14_6/`)**:
  ```bash
  ./build.py --target seccion_14_6
  ```
- **Sección 14.7 independiente (`seccion_14_7_standalone.tex` en `calculo_vectorial/seccion_14_7/`)**:
  ```bash
  ./build.py --target seccion_14_7
  ```
- **Sección 14.8 independiente (`seccion_14_8_standalone.tex` en `calculo_vectorial/seccion_14_8/`)**:
  ```bash
  ./build.py --target seccion_14_8
  ```
- **Sección 14.9 independiente (`seccion_14_9_standalone.tex` en `calculo_vectorial/seccion_14_9/`)**:
  ```bash
  ./build.py --target seccion_14_9
  ```
- **Repaso del Capítulo 14 independiente (`repaso_standalone.tex` en `calculo_vectorial/repaso/`)**:
  ```bash
  ./build.py --target repaso_14
  ```
- **Problemas Adicionales del Capítulo 14 independientes (`problemas_adicionales_standalone.tex` en `calculo_vectorial/problemas_adicionales/`)**:
  ```bash
  ./build.py --target problemas_adicionales_14
  ```
- **Sección 15.1 independiente (`seccion_15_1_standalone.tex` en `ecuaciones_diferenciales/seccion_15_1/`)**:
  ```bash
  ./build.py --target seccion_15_1
  ```
- **Sección 15.2 independiente (`seccion_15_2_standalone.tex` en `ecuaciones_diferenciales/seccion_15_2/`)**:
  ```bash
  ./build.py --target seccion_15_2
  ```
- **Sección 15.3 independiente (`seccion_15_3_standalone.tex` en `ecuaciones_diferenciales/seccion_15_3/`)**:
  ```bash
  ./build.py --target seccion_15_3
  ```
- **Sección 15.4 independiente (`seccion_15_4_standalone.tex` en `ecuaciones_diferenciales/seccion_15_4/`)**:
  ```bash
  ./build.py --target seccion_15_4
  ```
- **Sección 15.5 independiente (`seccion_15_5_standalone.tex` en `ecuaciones_diferenciales/seccion_15_5/`)**:
  ```bash
  ./build.py --target seccion_15_5
  ```
- **Sección 15.6 independiente (`seccion_15_6_standalone.tex` en `ecuaciones_diferenciales/seccion_15_6/`)**:
  ```bash
  ./build.py --target seccion_15_6
  ```
- **Sección 15.7 independiente (`seccion_15_7_standalone.tex` en `ecuaciones_diferenciales/seccion_15_7/`)**:
  ```bash
  ./build.py --target seccion_15_7
  ```
- **Sección 15.8 independiente (`seccion_15_8_standalone.tex` en `ecuaciones_diferenciales/seccion_15_8/`)**:
  ```bash
  ./build.py --target seccion_15_8
  ```
- **Repaso del Capítulo 15 independiente (`repaso_standalone.tex` en `ecuaciones_diferenciales/repaso/`)**:
  ```bash
  ./build.py --target repaso_15
  ```
- **Aplicaciones Adicionales del Capítulo 15 independientes (`aplicaciones_adicionales_standalone.tex` en `ecuaciones_diferenciales/aplicaciones_adicionales/`)**:
  ```bash
  ./build.py --target aplicaciones_adicionales_15
  ```

### 3. Limpiar archivos basura de LaTeX
Si deseas hacer una limpieza manual de los archivos auxiliares sin compilar:
```bash
./build.py --clean
```

---

## ✏️ Personalización del Espacio de Resolución

Cada documento (`main.tex`, `seccion_12_1_standalone.tex`, `seccion_12_2_standalone.tex`, `seccion_12_3_standalone.tex`, `seccion_12_4_standalone.tex`, `seccion_12_5_standalone.tex`, `seccion_12_6_standalone.tex`, `seccion_12_7_standalone.tex`, `seccion_12_8_standalone.tex`, `repaso_standalone.tex`, `problemas_adicionales_standalone.tex`, `seccion_13_1_standalone.tex`, `seccion_13_2_standalone.tex`, `seccion_13_3_standalone.tex`, `seccion_13_4_standalone.tex`, `seccion_13_5_standalone.tex`, `seccion_13_6_standalone.tex`, `seccion_13_7_standalone.tex`, `seccion_13_8_standalone.tex`, `seccion_13_9_standalone.tex`, `repaso_standalone.tex`, `problemas_adicionales_standalone.tex`, `seccion_14_1_standalone.tex`, `seccion_14_2_standalone.tex`, `seccion_14_3_standalone.tex`, `seccion_14_4_standalone.tex`, `seccion_14_5_standalone.tex`, `seccion_14_6_standalone.tex`, `seccion_14_7_standalone.tex`, `seccion_14_8_standalone.tex`, `seccion_14_9_standalone.tex`, `repaso_standalone.tex`, `problemas_adicionales_standalone.tex`, `seccion_15_1_standalone.tex`, `seccion_15_2_standalone.tex`, `seccion_15_3_standalone.tex`, `seccion_15_4_standalone.tex`, `seccion_15_5_standalone.tex`, `seccion_15_6_standalone.tex`, `seccion_15_7_standalone.tex`, `seccion_15_8_standalone.tex`, `repaso_standalone.tex` y `aplicaciones_adicionales_standalone.tex` en sus respectivas carpetas) incluye una variable para ajustar el espacio vertical asignado a la resolución manual de cada ejercicio. 

Puedes buscar la siguiente línea en los encabezados TeX:
```latex
\setlength{\espacioresolucion}{5cm}
```
* **Aumentar espacio**: Modifícala por `6cm`, `8cm`, etc.
* **Reducir espacio (para guardar hojas)**: Cambia a `3cm`, `2cm`, etc.
