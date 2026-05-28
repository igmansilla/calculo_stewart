#!/usr/bin/env python3
import os
import subprocess
import shutil
import argparse

base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "pdfs")

targets = {
    "main": {
        "tex_path": os.path.join(base_dir, "main.tex"),
        "working_dir": base_dir,
        "dest_name": "Stewart_Calculo_Completo.pdf",
        "description": "Libro completo (Capítulo 12 y secciones futuras)"
    },
    "seccion_12_1": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_1/seccion_12_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_1"),
        "dest_name": "Stewart_Seccion_12_1_Funciones_de_Varias_Variables.pdf",
        "description": "Sección 12.1 Standalone (Funciones de varias variables)"
    },
    "seccion_12_2": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_2/seccion_12_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_2"),
        "dest_name": "Stewart_Seccion_12_2_Limites_y_Continuidad.pdf",
        "description": "Sección 12.2 Standalone (Límites y continuidad)"
    },
    "seccion_12_3": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_3/seccion_12_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_3"),
        "dest_name": "Stewart_Seccion_12_3_Derivadas_Parciales.pdf",
        "description": "Sección 12.3 Standalone (Derivadas parciales)"
    },
    "seccion_12_4": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_4/seccion_12_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_4"),
        "dest_name": "Stewart_Seccion_12_4_Tangentes_y_Diferenciales.pdf",
        "description": "Sección 12.4 Standalone (Tangentes y diferenciales)"
    },
    "seccion_12_5": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_5/seccion_12_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_5"),
        "dest_name": "Stewart_Seccion_12_5_Regla_de_la_Cadena.pdf",
        "description": "Sección 12.5 Standalone (Regla de la cadena)"
    },
    "seccion_12_6": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_6/seccion_12_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_6"),
        "dest_name": "Stewart_Seccion_12_6_Derivadas_Direccionales_y_Vector_Gradiente.pdf",
        "description": "Sección 12.6 Standalone (Derivadas direccionales y vector gradiente)"
    },
    "seccion_12_7": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_7/seccion_12_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_7"),
        "dest_name": "Stewart_Seccion_12_7_Valores_Maximos_y_Minimos.pdf",
        "description": "Sección 12.7 Standalone (Valores máximos y mínimos)"
    },
    "seccion_12_8": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/seccion_12_8/seccion_12_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/seccion_12_8"),
        "dest_name": "Stewart_Seccion_12_8_Multiplicadores_de_Lagrange.pdf",
        "description": "Sección 12.8 Standalone (Multiplicadores de Lagrange)"
    },
    "repaso": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/repaso"),
        "dest_name": "Stewart_Capitulo_12_Repaso.pdf",
        "description": "Capítulo 12 Repaso Standalone (Ejercicios de repaso)"
    },
    "problemas_adicionales": {
        "tex_path": os.path.join(base_dir, "derivadas_parciales/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas_parciales/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_12_Problemas_Adicionales.pdf",
        "description": "Capítulo 12 Problemas Adicionales Standalone"
    },
    "seccion_13_1": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_1/seccion_13_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_1"),
        "dest_name": "Stewart_Seccion_13_1_Integrales_Dobles_sobre_Rectangulos.pdf",
        "description": "Sección 13.1 Standalone (Integrales dobles sobre rectángulos)"
    },
    "seccion_13_2": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_2/seccion_13_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_2"),
        "dest_name": "Stewart_Seccion_13_2_Integrales_Iteradas.pdf",
        "description": "Sección 13.2 Standalone (Integrales iteradas)"
    },
    "seccion_13_3": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_3/seccion_13_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_3"),
        "dest_name": "Stewart_Seccion_13_3_Integrales_Dobles_sobre_Regiones_Generales.pdf",
        "description": "Sección 13.3 Standalone (Integrales dobles sobre regiones generales)"
    },
    "seccion_13_4": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_4/seccion_13_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_4"),
        "dest_name": "Stewart_Seccion_13_4_Integrales_Dobles_en_Coordenadas_Polares.pdf",
        "description": "Sección 13.4 Standalone (Integrales dobles en coordenadas polares)"
    },
    "seccion_13_5": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_5/seccion_13_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_5"),
        "dest_name": "Stewart_Seccion_13_5_Aplicaciones_de_las_Integrales_Dobles.pdf",
        "description": "Sección 13.5 Standalone (Aplicaciones de las integrales dobles)"
    },
    "seccion_13_6": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_6/seccion_13_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_6"),
        "dest_name": "Stewart_Seccion_13_6_Area_de_una_Superficie.pdf",
        "description": "Sección 13.6 Standalone (Área de una superficie)"
    },
    "seccion_13_7": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_7/seccion_13_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_7"),
        "dest_name": "Stewart_Seccion_13_7_Integrales_Triples.pdf",
        "description": "Sección 13.7 Standalone (Integrales triples)"
    },
    "seccion_13_8": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_8/seccion_13_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_8"),
        "dest_name": "Stewart_Seccion_13_8_Integrales_Triples_en_Coordenadas_Cilindricas_y_Esfericas.pdf",
        "description": "Sección 13.8 Standalone (Integrales triples en coordenadas cilíndricas y esféricas)"
    },
    "seccion_13_9": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/seccion_13_9/seccion_13_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/seccion_13_9"),
        "dest_name": "Stewart_Seccion_13_9_Cambio_de_Variables_en_Integrales_Multiples.pdf",
        "description": "Sección 13.9 Standalone (Cambio de variables en integrales múltiples)"
    },
    "repaso_13": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/repaso"),
        "dest_name": "Stewart_Capitulo_13_Repaso.pdf",
        "description": "Capítulo 13 Repaso Standalone (Ejercicios de repaso)"
    },
    "problemas_adicionales_13": {
        "tex_path": os.path.join(base_dir, "integrales_multiples/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integrales_multiples/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_13_Problemas_Adicionales.pdf",
        "description": "Capítulo 13 Problemas Adicionales Standalone"
    },
    "seccion_14_1": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_1/seccion_14_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_1"),
        "dest_name": "Stewart_Seccion_14_1_Campos_Vectoriales.pdf",
        "description": "Sección 14.1 Standalone (Campos vectoriales)"
    },
    "seccion_14_2": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_2/seccion_14_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_2"),
        "dest_name": "Stewart_Seccion_14_2_Integrales_de_Linea.pdf",
        "description": "Sección 14.2 Standalone (Integrales de línea)"
    },
    "seccion_14_3": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_3/seccion_14_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_3"),
        "dest_name": "Stewart_Seccion_14_3_Teorema_Fundamental_para_Integrales_de_Linea.pdf",
        "description": "Sección 14.3 Standalone (Teorema fundamental para integrales de línea)"
    },
    "seccion_14_4": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_4/seccion_14_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_4"),
        "dest_name": "Stewart_Seccion_14_4_Teorema_de_Green.pdf",
        "description": "Sección 14.4 Standalone (Teorema de Green)"
    },
    "seccion_14_5": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_5/seccion_14_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_5"),
        "dest_name": "Stewart_Seccion_14_5_Rotacional_y_Divergencia.pdf",
        "description": "Sección 14.5 Standalone (Rotacional y Divergencia)"
    },
    "seccion_14_6": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_6/seccion_14_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_6"),
        "dest_name": "Stewart_Seccion_14_6_Superficies_Parametricas_y_sus_Areas.pdf",
        "description": "Sección 14.6 Standalone (Superficies Paramétricas y sus Áreas)"
    },
    "seccion_14_7": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_7/seccion_14_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_7"),
        "dest_name": "Stewart_Seccion_14_7_Integrales_de_Superficie.pdf",
        "description": "Sección 14.7 Standalone (Integrales de Superficie)"
    },
    "seccion_14_8": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_8/seccion_14_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_8"),
        "dest_name": "Stewart_Seccion_14_8_Teorema_de_Stokes.pdf",
        "description": "Sección 14.8 Standalone (Teorema de Stokes)"
    },
    "seccion_14_9": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/seccion_14_9/seccion_14_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/seccion_14_9"),
        "dest_name": "Stewart_Seccion_14_9_Teorema_de_la_Divergencia.pdf",
        "description": "Sección 14.9 Standalone (Teorema de la Divergencia)"
    },
    "repaso_14": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/repaso"),
        "dest_name": "Stewart_Capitulo_14_Repaso.pdf",
        "description": "Capítulo 14 Repaso Standalone (Ejercicios de Repaso)"
    },
    "problemas_adicionales_14": {
        "tex_path": os.path.join(base_dir, "calculo_vectorial/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "calculo_vectorial/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_14_Problemas_Adicionales.pdf",
        "description": "Capítulo 14 Problemas Adicionales Standalone (Problemas Adicionales)"
    },
    "seccion_15_1": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_1/seccion_15_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_1"),
        "dest_name": "Stewart_Seccion_15_1_Ecuaciones_Diferenciales_Separables_y_Homogeneas.pdf",
        "description": "Sección 15.1 Standalone (Ecuaciones Diferenciales Separables y Homogéneas)"
    },
    "seccion_15_2": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_2/seccion_15_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_2"),
        "dest_name": "Stewart_Seccion_15_2_Ecuaciones_Diferenciales_Lineales_y_de_Bernoulli.pdf",
        "description": "Sección 15.2 Standalone (Ecuaciones Diferenciales Lineales y de Bernoulli)"
    },
    "seccion_15_3": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_3/seccion_15_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_3"),
        "dest_name": "Stewart_Seccion_15_3_Ecuaciones_Diferenciales_Exactas_y_Factores_Integrantes.pdf",
        "description": "Sección 15.3 Standalone (Ecuaciones Diferenciales Exactas y Factores Integrantes)"
    },
    "seccion_15_4": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_4/seccion_15_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_4"),
        "dest_name": "Stewart_Seccion_15_4_Estrategia_para_Resolver_Ecuaciones_de_Primer_Orden.pdf",
        "description": "Sección 15.4 Standalone (Estrategia para Resolver Ecuaciones de Primer Orden)"
    },
    "seccion_15_5": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_5/seccion_15_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_5"),
        "dest_name": "Stewart_Seccion_15_5_Ecuaciones_Lineales_de_Segundo_Orden.pdf",
        "description": "Sección 15.5 Standalone (Ecuaciones Lineales de Segundo Orden)"
    },
    "seccion_15_6": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_6/seccion_15_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_6"),
        "dest_name": "Stewart_Seccion_15_6_Coeficientes_Indeterminados_y_Variacion_de_Parametros.pdf",
        "description": "Sección 15.6 Standalone (Coeficientes Indeterminados y Variación de Parámetros)"
    },
    "seccion_15_7": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_7/seccion_15_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_7"),
        "dest_name": "Stewart_Seccion_15_7_Aplicaciones_de_las_Ecuaciones_Diferenciales_de_Segundo_Orden.pdf",
        "description": "Sección 15.7 Standalone (Aplicaciones de las Ecuaciones Diferenciales de Segundo Orden)"
    },
    "seccion_15_8": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_8/seccion_15_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/seccion_15_8"),
        "dest_name": "Stewart_Seccion_15_8_Soluciones_en_Series_de_Potencias.pdf",
        "description": "Sección 15.8 Standalone (Soluciones en Series de Potencias)"
    },
    "repaso_15": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/repaso"),
        "dest_name": "Stewart_Capitulo_15_Repaso.pdf",
        "description": "Capítulo 15 Repaso Standalone"
    },
    "aplicaciones_adicionales_15": {
        "tex_path": os.path.join(base_dir, "ecuaciones_diferenciales/aplicaciones_adicionales/aplicaciones_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_diferenciales/aplicaciones_adicionales"),
        "dest_name": "Stewart_Capitulo_15_Aplicaciones_Adicionales.pdf",
        "description": "Capítulo 15 Aplicaciones Adicionales Standalone"
    },
    "seccion_0_1": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_1/seccion_0_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_1"),
        "dest_name": "Stewart_Seccion_0_1_Conceptos_Preliminares.pdf",
        "description": "Capítulo 0 Sección 1 Standalone"
    },
    "seccion_0_2": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_2/seccion_0_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_2"),
        "dest_name": "Stewart_Seccion_0_2_Geometria_Analitica_y_Secciones_Conicas.pdf",
        "description": "Capítulo 0 Sección 2 Standalone"
    },
    "seccion_0_3": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_3/seccion_0_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_3"),
        "dest_name": "Stewart_Seccion_0_3_Funciones_Dominios_y_Modelado.pdf",
        "description": "Capítulo 0 Sección 3 Standalone"
    },
    "seccion_0_4": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_4/seccion_0_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_4"),
        "dest_name": "Stewart_Seccion_0_4_Algebra_y_Composicion_de_Funciones.pdf",
        "description": "Capítulo 0 Sección 4 Standalone"
    },
    "seccion_0_5": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_5/seccion_0_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_5"),
        "dest_name": "Stewart_Seccion_0_5_Graficas_y_Transformaciones_de_Funciones.pdf",
        "description": "Capítulo 0 Sección 5 Standalone"
    },
    "seccion_0_6": {
        "tex_path": os.path.join(base_dir, "capitulo_0/seccion_0_6/seccion_0_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "capitulo_0/seccion_0_6"),
        "dest_name": "Stewart_Seccion_0_6_Repaso_General_de_Conceptos.pdf",
        "description": "Capítulo 0 Sección 6 Standalone"
    },
    "seccion_1_1": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_1/seccion_01_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_1"),
        "dest_name": "Stewart_Seccion_1_1_El_Problema_de_la_Tangente_y_de_la_Velocidad.pdf",
        "description": "Capítulo 1 Sección 1.1 Standalone"
    },
    "seccion_1_2": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_2/seccion_01_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_2"),
        "dest_name": "Stewart_Seccion_1_2_Limite_de_una_Funcion.pdf",
        "description": "Capítulo 1 Sección 1.2 Standalone"
    },
    "seccion_1_3": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_3/seccion_01_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_3"),
        "dest_name": "Stewart_Seccion_1_3_Calculo_de_Limites_Aplicando_sus_Leyes_Fundamentales.pdf",
        "description": "Capítulo 1 Sección 1.3 Standalone"
    },
    "seccion_1_4": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_4/seccion_01_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_4"),
        "dest_name": "Stewart_Seccion_1_4_La_Definicion_Precisa_de_Limite.pdf",
        "description": "Capítulo 1 Sección 1.4 Standalone"
    },
    "seccion_1_5": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_5/seccion_01_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_5"),
        "dest_name": "Stewart_Seccion_1_5_Continuidad.pdf",
        "description": "Capítulo 1 Sección 1.5 Standalone"
    },
    "seccion_1_6": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/seccion_01_6/seccion_01_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/seccion_01_6"),
        "dest_name": "Stewart_Seccion_1_6_Tangentes_Velocidades_y_Otras_Razones_de_Cambio.pdf",
        "description": "Capítulo 1 Sección 1.6 Standalone"
    },
    "repaso_1": {
        "tex_path": os.path.join(base_dir, "limites_y_continuidad/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "limites_y_continuidad/repaso"),
        "dest_name": "Stewart_Capitulo_1_Repaso.pdf",
        "description": "Capítulo 1 Repaso de Conceptos Standalone"
    },
    "seccion_2_1": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_1/seccion_02_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_1"),
        "dest_name": "Stewart_Seccion_2_1_La_Derivada_y_la_Razon_de_Cambio.pdf",
        "description": "Capítulo 2 Sección 2.1 Standalone"
    },
    "seccion_2_2": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_2/seccion_02_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_2"),
        "dest_name": "Stewart_Seccion_2_2_Reglas_de_Derivacion.pdf",
        "description": "Capítulo 2 Sección 2.2 Standalone"
    },
    "seccion_2_3": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_3/seccion_02_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_3"),
        "dest_name": "Stewart_Seccion_2_3_Razones_de_Cambio_en_las_Ciencias_Fisicas_y_Sociales.pdf",
        "description": "Capítulo 2 Sección 2.3 Standalone"
    },
    "seccion_2_4": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_4/seccion_02_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_4"),
        "dest_name": "Stewart_Seccion_2_4_Derivadas_de_Funciones_Trigonometricas.pdf",
        "description": "Capítulo 2 Sección 2.4 Standalone"
    },
    "seccion_2_5": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_5/seccion_02_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_5"),
        "dest_name": "Stewart_Seccion_2_5_La_Regla_de_la_Cadena.pdf",
        "description": "Capítulo 2 Sección 2.5 Standalone"
    },
    "seccion_2_6": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_6/seccion_02_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_6"),
        "dest_name": "Stewart_Seccion_2_6_Derivacion_Implicita.pdf",
        "description": "Capítulo 2 Sección 2.6 Standalone"
    },
    "seccion_2_7": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_7/seccion_02_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_7"),
        "dest_name": "Stewart_Seccion_2_7_Derivadas_de_Orden_Superior.pdf",
        "description": "Capítulo 2 Sección 2.7 Standalone"
    },
    "seccion_2_8": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_8/seccion_02_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_8"),
        "dest_name": "Stewart_Seccion_2_8_Razones_de_Cambio_Relacionadas.pdf",
        "description": "Capítulo 2 Sección 2.8 Standalone"
    },
    "seccion_2_9": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_9/seccion_02_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_9"),
        "dest_name": "Stewart_Seccion_2_9_Linealizacion_y_Diferenciales.pdf",
        "description": "Capítulo 2 Sección 2.9 Standalone"
    },
    "seccion_2_10": {
        "tex_path": os.path.join(base_dir, "derivadas/seccion_02_10/seccion_02_10_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/seccion_02_10"),
        "dest_name": "Stewart_Seccion_2_10_Metodo_de_Newton.pdf",
        "description": "Capítulo 2 Sección 2.10 Standalone"
    },
    "repaso_2": {
        "tex_path": os.path.join(base_dir, "derivadas/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/repaso"),
        "dest_name": "Stewart_Capitulo_2_Repaso.pdf",
        "description": "Capítulo 2 Repaso Standalone"
    },
    "problemas_adicionales_2": {
        "tex_path": os.path.join(base_dir, "derivadas/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "derivadas/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_2_Problemas_Adicionales.pdf",
        "description": "Capítulo 2 Problemas Adicionales Standalone"
    },
    "seccion_3_1": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_1/seccion_03_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_1"),
        "dest_name": "Stewart_Seccion_3_1_Valores_Maximos_y_Minimos.pdf",
        "description": "Capítulo 3 Sección 3.1 Standalone"
    },
    "seccion_3_2": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_2/seccion_03_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_2"),
        "dest_name": "Stewart_Seccion_3_2_El_Teorema_del_Valor_Medio.pdf",
        "description": "Capítulo 3 Sección 3.2 Standalone"
    },
    "seccion_3_3": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_3/seccion_03_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_3"),
        "dest_name": "Stewart_Seccion_3_3_Valores_Extremos_y_Comportamiento.pdf",
        "description": "Capítulo 3 Sección 3.3 Standalone"
    },
    "seccion_3_4": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_4/seccion_03_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_4"),
        "dest_name": "Stewart_Seccion_3_4_Concavidad_y_Puntos_de_Inflexion.pdf",
        "description": "Capítulo 3 Sección 3.4 Standalone"
    },
    "seccion_3_5": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_5/seccion_03_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_5"),
        "dest_name": "Stewart_Seccion_3_5_Limites_al_Infinito.pdf",
        "description": "Capítulo 3 Sección 3.5 Standalone"
    },
    "seccion_3_6": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_6/seccion_03_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_6"),
        "dest_name": "Stewart_Seccion_3_6_Limites_Infinitos.pdf",
        "description": "Capítulo 3 Sección 3.6 Standalone"
    },
    "seccion_3_7": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_7/seccion_03_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_7"),
        "dest_name": "Stewart_Seccion_3_7_Trazo_de_Curvas.pdf",
        "description": "Capítulo 3 Sección 3.7 Standalone"
    },
    "seccion_3_8": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_8/seccion_03_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_8"),
        "dest_name": "Stewart_Seccion_3_8_Problemas_de_Aplicacion.pdf",
        "description": "Capítulo 3 Sección 3.8 Standalone"
    },
    "seccion_3_9": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_9/seccion_03_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_9"),
        "dest_name": "Stewart_Seccion_3_9_Economia_Negocios.pdf",
        "description": "Capítulo 3 Sección 3.9 Standalone"
    },
    "seccion_3_10": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_10/seccion_03_10_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/seccion_03_10"),
        "dest_name": "Stewart_Seccion_3_10_Antiderivadas.pdf",
        "description": "Capítulo 3 Sección 3.10 Standalone"
    },
    "repaso_3": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/repaso"),
        "dest_name": "Stewart_Capitulo_3_Repaso.pdf",
        "description": "Capítulo 3 Repaso Standalone"
    },
    "problemas_adicionales_3": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_derivada/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_derivada/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_3_Problemas_Adicionales.pdf",
        "description": "Capítulo 3 Problemas Adicionales Standalone"
    },
    "seccion_4_1": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_1/seccion_04_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_1"),
        "dest_name": "Stewart_Seccion_4_1_Notacion_de_Sumatoria.pdf",
        "description": "Capítulo 4 Sección 4.1 Standalone"
    },
    "seccion_4_2": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_2/seccion_04_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_2"),
        "dest_name": "Stewart_Seccion_4_2_Area.pdf",
        "description": "Capítulo 4 Sección 4.2 Standalone"
    },
    "seccion_4_3": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_3/seccion_04_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_3"),
        "dest_name": "Stewart_Seccion_4_3_Integral_Definida.pdf",
        "description": "Capítulo 4 Sección 4.3 Standalone"
    },
    "seccion_4_4": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_4/seccion_04_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_4"),
        "dest_name": "Stewart_Seccion_4_4_Propiedades_de_la_Integral.pdf",
        "description": "Capítulo 4 Sección 4.4 Standalone"
    },
    "seccion_4_5": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_5/seccion_04_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_5"),
        "dest_name": "Stewart_Seccion_4_5_Teorema_Fundamental.pdf",
        "description": "Capítulo 4 Sección 4.5 Standalone"
    },
    "seccion_4_6": {
        "tex_path": os.path.join(base_dir, "integracion/seccion_04_6/seccion_04_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/seccion_04_6"),
        "dest_name": "Stewart_Seccion_4_6_Regla_Sustitucion.pdf",
        "description": "Capítulo 4 Sección 4.6 Standalone"
    },
    "repaso_4": {
        "tex_path": os.path.join(base_dir, "integracion/repaso_04/repaso_04_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/repaso_04"),
        "dest_name": "Stewart_Capitulo_4_Repaso.pdf",
        "description": "Capítulo 4 Repaso Standalone"
    },
    "problemas_adicionales_4": {
        "tex_path": os.path.join(base_dir, "integracion/problemas_adicionales_04/problemas_adicionales_04_standalone.tex"),
        "working_dir": os.path.join(base_dir, "integracion/problemas_adicionales_04"),
        "dest_name": "Stewart_Capitulo_4_Problemas_Adicionales.pdf",
        "description": "Capítulo 4 Problemas Adicionales Standalone"
    },
    "seccion_5_1": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_1/seccion_05_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_1"),
        "dest_name": "Stewart_Seccion_5_1_Areas_entre_Curvas.pdf",
        "description": "Capítulo 5 Sección 5.1 Standalone"
    },
    "seccion_5_2": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_2/seccion_05_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_2"),
        "dest_name": "Stewart_Seccion_5_2_Volumenes.pdf",
        "description": "Capítulo 5 Sección 5.2 Standalone"
    },
    "seccion_5_3": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_3/seccion_05_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_3"),
        "dest_name": "Stewart_Seccion_5_3_Volumenes_Envolventes_Cilindricas.pdf",
        "description": "Capítulo 5 Sección 5.3 Standalone"
    },
    "seccion_5_4": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_4/seccion_05_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_4"),
        "dest_name": "Stewart_Seccion_5_4_Trabajo.pdf",
        "description": "Capítulo 5 Sección 5.4 Standalone"
    },
    "seccion_5_5": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_5/seccion_05_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/seccion_05_5"),
        "dest_name": "Stewart_Seccion_5_5_Valor_Medio.pdf",
        "description": "Capítulo 5 Sección 5.5 Standalone"
    },
    "repaso_5": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/repaso_05/repaso_05_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/repaso_05"),
        "dest_name": "Stewart_Capitulo_5_Repaso.pdf",
        "description": "Capítulo 5 Repaso Standalone"
    },
    "problemas_adicionales_5": {
        "tex_path": os.path.join(base_dir, "aplicaciones_de_la_integral/problemas_adicionales_05/problemas_adicionales_05_standalone.tex"),
        "working_dir": os.path.join(base_dir, "aplicaciones_de_la_integral/problemas_adicionales_05"),
        "dest_name": "Stewart_Capitulo_5_Problemas_Adicionales.pdf",
        "description": "Capítulo 5 Problemas Adicionales Standalone"
    },
    "seccion_6_1": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_1/seccion_06_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_1"),
        "dest_name": "Stewart_Seccion_6_1_Funciones_Exponenciales.pdf",
        "description": "Capítulo 6 Sección 6.1 Standalone"
    },
    "seccion_6_2": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_2/seccion_06_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_2"),
        "dest_name": "Stewart_Seccion_6_2_Derivadas_y_Integrales_Exponenciales.pdf",
        "description": "Capítulo 6 Sección 6.2 Standalone"
    },
    "seccion_6_3": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_3/seccion_06_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_3"),
        "dest_name": "Stewart_Seccion_6_3_Funciones_Inversas.pdf",
        "description": "Capítulo 6 Sección 6.3 Standalone"
    },
    "seccion_6_4": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_4/seccion_06_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_4"),
        "dest_name": "Stewart_Seccion_6_4_Funciones_Logaritmicas.pdf",
        "description": "Capítulo 6 Sección 6.4 Standalone"
    },
    "seccion_6_5": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_5/seccion_06_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_5"),
        "dest_name": "Stewart_Seccion_6_5_Ejercicios.pdf",
        "description": "Capítulo 6 Sección 6.5 Standalone"
    },
    "seccion_6_6": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_6/seccion_06_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_6"),
        "dest_name": "Stewart_Seccion_6_6_Ejercicios.pdf",
        "description": "Capítulo 6 Sección 6.6 Standalone"
    },
    "seccion_6_7": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_7/seccion_06_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_7"),
        "dest_name": "Stewart_Seccion_6_7_Crecimiento_y_Decrecimiento_Exponenciales.pdf",
        "description": "Capítulo 6 Sección 6.7 Standalone"
    },
    "seccion_6_8": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_8/seccion_06_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_8"),
        "dest_name": "Stewart_Seccion_6_8_Ejercicios.pdf",
        "description": "Capítulo 6 Sección 6.8 Standalone"
    },
    "seccion_6_9": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_9/seccion_06_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_9"),
        "dest_name": "Stewart_Seccion_6_9_Ejercicios.pdf",
        "description": "Capítulo 6 Sección 6.9 Standalone"
    },
    "seccion_6_10": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/seccion_06_10/seccion_06_10_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/seccion_06_10"),
        "dest_name": "Stewart_Seccion_6_10_Forma_Indeterminada_y_Regla_de_L_Hospital.pdf",
        "description": "Capítulo 6 Sección 6.10 Standalone"
    },
    "repaso_6": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/repaso"),
        "dest_name": "Stewart_Capitulo_6_Repaso.pdf",
        "description": "Capítulo 6 Repaso Standalone"
    },
    "problemas_adicionales_6": {
        "tex_path": os.path.join(base_dir, "funciones_trascendentes/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "funciones_trascendentes/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_6_Problemas_Adicionales.pdf",
        "description": "Capítulo 6 Problemas Adicionales Standalone"
    },
    "seccion_7_1": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_1/seccion_07_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_1"),
        "dest_name": "Stewart_Seccion_7_1_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.1 Standalone"
    },
    "seccion_7_2": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_2/seccion_07_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_2"),
        "dest_name": "Stewart_Seccion_7_2_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.2 Standalone"
    },
    "seccion_7_3": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_3/seccion_07_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_3"),
        "dest_name": "Stewart_Seccion_7_3_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.3 Standalone"
    },
    "seccion_7_4": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_4/seccion_07_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_4"),
        "dest_name": "Stewart_Seccion_7_4_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.4 Standalone"
    },
    "seccion_7_5": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_5/seccion_07_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_5"),
        "dest_name": "Stewart_Seccion_7_5_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.5 Standalone"
    },
    "seccion_7_6": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_6/seccion_07_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_6"),
        "dest_name": "Stewart_Seccion_7_6_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.6 Standalone"
    },
    "seccion_7_7": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_7/seccion_07_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_7"),
        "dest_name": "Stewart_Seccion_7_7_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.7 Standalone"
    },
    "seccion_7_8": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_8/seccion_07_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_8"),
        "dest_name": "Stewart_Seccion_7_8_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.8 Standalone"
    },
    "seccion_7_9": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_9/seccion_07_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/seccion_07_9"),
        "dest_name": "Stewart_Seccion_7_9_Ejercicios.pdf",
        "description": "Capítulo 7 Sección 7.9 Standalone"
    },
    "repaso_7": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/repaso"),
        "dest_name": "Stewart_Capitulo_7_Repaso.pdf",
        "description": "Capítulo 7 Repaso Standalone"
    },
    "aplicaciones_adicionales_7": {
        "tex_path": os.path.join(base_dir, "tecnicas_de_integracion/aplicaciones_adicionales/aplicaciones_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "tecnicas_de_integracion/aplicaciones_adicionales"),
        "dest_name": "Stewart_Capitulo_7_Aplicaciones_Adicionales.pdf",
        "description": "Capítulo 7 Aplicaciones Adicionales Standalone"
    },
    "seccion_8_1": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_1/seccion_08_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_1"),
        "dest_name": "Stewart_Seccion_8_1_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.1 Standalone"
    },
    "seccion_8_2": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_2/seccion_08_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_2"),
        "dest_name": "Stewart_Seccion_8_2_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.2 Standalone"
    },
    "seccion_8_3": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_3/seccion_08_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_3"),
        "dest_name": "Stewart_Seccion_8_3_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.3 Standalone"
    },
    "seccion_8_4": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_4/seccion_08_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_4"),
        "dest_name": "Stewart_Seccion_8_4_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.4 Standalone"
    },
    "seccion_8_5": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_5/seccion_08_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_5"),
        "dest_name": "Stewart_Seccion_8_5_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.5 Standalone"
    },
    "seccion_8_6": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_6/seccion_08_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/seccion_08_6"),
        "dest_name": "Stewart_Seccion_8_6_Ejercicios.pdf",
        "description": "Capítulo 8 Sección 8.6 Standalone"
    },
    "repaso_8": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/repaso"),
        "dest_name": "Stewart_Capitulo_8_Repaso.pdf",
        "description": "Capítulo 8 Repaso Standalone"
    },
    "problemas_adicionales_8": {
        "tex_path": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/problemas_adicionales/problemas_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "mas_aplicaciones_de_la_integracion/problemas_adicionales"),
        "dest_name": "Stewart_Capitulo_8_Problemas_Adicionales.pdf",
        "description": "Capítulo 8 Problemas Adicionales Standalone"
    },
    "seccion_9_1": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_1/seccion_09_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_1"),
        "dest_name": "Stewart_Seccion_9_1_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.1 Standalone"
    },
    "seccion_9_2": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_2/seccion_09_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_2"),
        "dest_name": "Stewart_Seccion_9_2_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.2 Standalone"
    },
    "seccion_9_3": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_3/seccion_09_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_3"),
        "dest_name": "Stewart_Seccion_9_3_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.3 Standalone"
    },
    "seccion_9_4": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_4/seccion_09_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_4"),
        "dest_name": "Stewart_Seccion_9_4_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.4 Standalone"
    },
    "seccion_9_5": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_5/seccion_09_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_5"),
        "dest_name": "Stewart_Seccion_9_5_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.5 Standalone"
    },
    "seccion_9_6": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_6/seccion_09_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_6"),
        "dest_name": "Stewart_Seccion_9_6_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.6 Standalone"
    },
    "seccion_9_7": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_7/seccion_09_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_7"),
        "dest_name": "Stewart_Seccion_9_7_Ejercicios.pdf",
        "description": "Capítulo 9 Sección 9.7 Standalone"
    },
    "seccion_9_repaso": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/repaso"),
        "dest_name": "Stewart_Capitulo_9_Repaso.pdf",
        "description": "Capítulo 9 Repaso Standalone"
    },
    "seccion_9_aplicaciones": {
        "tex_path": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/aplicaciones_adicionales/aplicaciones_adicionales_standalone.tex"),
        "working_dir": os.path.join(base_dir, "ecuaciones_parametricas_y_coordenadas_polares/aplicaciones_adicionales"),
        "dest_name": "Stewart_Capitulo_9_Aplicaciones_Adicionales.pdf",
        "description": "Capítulo 9 Aplicaciones Adicionales Standalone"
    },
    "seccion_10_1": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_1/seccion_10_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_1"),
        "dest_name": "Stewart_Seccion_10_1_Ejercicios.pdf",
        "description": "Capítulo 10 Sección 10.1 Standalone"
    },
    "seccion_10_2": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_2/seccion_10_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_2"),
        "dest_name": "Stewart_Seccion_10_2_Series.pdf",
        "description": "Capítulo 10 Sección 10.2 Standalone"
    },
    "seccion_10_3": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_3/seccion_10_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_3"),
        "dest_name": "Stewart_Seccion_10_3_Criterio_Integral.pdf",
        "description": "Capítulo 10 Sección 10.3 Standalone"
    },
    "seccion_10_4": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_4/seccion_10_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_4"),
        "dest_name": "Stewart_Seccion_10_4_Criterios_Comparacion.pdf",
        "description": "Capítulo 10 Sección 10.4 Standalone"
    },
    "seccion_10_5": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_5/seccion_10_5_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_5"),
        "dest_name": "Stewart_Seccion_10_5_Series_Alternantes.pdf",
        "description": "Capítulo 10 Sección 10.5 Standalone"
    },
    "seccion_10_6": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_6/seccion_10_6_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_6"),
        "dest_name": "Stewart_Seccion_10_6_Convergencia_Absoluta.pdf",
        "description": "Capítulo 10 Sección 10.6 Standalone"
    },
    "seccion_10_7": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_7/seccion_10_7_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_7"),
        "dest_name": "Stewart_Seccion_10_7_Estrategia.pdf",
        "description": "Capítulo 10 Sección 10.7 Standalone"
    },
    "seccion_10_8": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_8/seccion_10_8_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_8"),
        "dest_name": "Stewart_Seccion_10_8_Series_Potencias.pdf",
        "description": "Capítulo 10 Sección 10.8 Standalone"
    },
    "seccion_10_9": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_9/seccion_10_9_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_9"),
        "dest_name": "Stewart_Seccion_10_9_Taylor_Maclaurin.pdf",
        "description": "Capítulo 10 Sección 10.9 Standalone"
    },
    "seccion_10_10": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_10/seccion_10_10_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_10"),
        "dest_name": "Stewart_Seccion_10_10_Serie_Binomial.pdf",
        "description": "Capítulo 10 Sección 10.10 Standalone"
    },
    "seccion_10_11": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_11/seccion_10_11_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/seccion_10_11"),
        "dest_name": "Stewart_Seccion_10_11_Polinomios_Taylor.pdf",
        "description": "Capítulo 10 Sección 10.11 Standalone"
    },
    "repaso": {
        "tex_path": os.path.join(base_dir, "sucesiones_y_series_infinitas/repaso/repaso_standalone.tex"),
        "working_dir": os.path.join(base_dir, "sucesiones_y_series_infinitas/repaso"),
        "dest_name": "Stewart_Capitulo_10_Repaso.pdf",
        "description": "Capítulo 10 Repaso Standalone"
    },
    "seccion_11_1": {
        "tex_path": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_1/seccion_11_1_standalone.tex"),
        "working_dir": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_1"),
        "dest_name": "Stewart_Seccion_11_1_Coordenadas_3D.pdf",
        "description": "Capítulo 11 Sección 11.1 Standalone"
    },
    "seccion_11_2": {
        "tex_path": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_2/seccion_11_2_standalone.tex"),
        "working_dir": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_2"),
        "dest_name": "Stewart_Seccion_11_2_Vectores.pdf",
        "description": "Capítulo 11 Sección 11.2 Standalone"
    },
    "seccion_11_3": {
        "tex_path": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_3/seccion_11_3_standalone.tex"),
        "working_dir": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_3"),
        "dest_name": "Stewart_Seccion_11_3_Producto_Escalar.pdf",
        "description": "Capítulo 11 Sección 11.3 Standalone"
    },
    "seccion_11_4": {
        "tex_path": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_4/seccion_11_4_standalone.tex"),
        "working_dir": os.path.join(base_dir, "geometria_analitica_tridimensional_y_vectores/seccion_11_4"),
        "dest_name": "Stewart_Seccion_11_4_Producto_Cruz.pdf",
        "description": "Capítulo 11 Sección 11.4 Standalone"
    }
}

def compile_latex(tex_path, working_dir, dest_name):
    print(f"\n🚀 Compilando: {os.path.basename(tex_path)}...")
    
    # Run pdflatex (2 passes for TOC and hyperref to build successfully)
    for pass_num in range(1, 3):
        print(f"   Paso {pass_num}/2...")
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(tex_path)],
            cwd=working_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )
        
        if result.returncode != 0:
            print(f"❌ Error al compilar {os.path.basename(tex_path)}:")
            log_path = tex_path.replace(".tex", ".log")
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8", errors="ignore") as log:
                    lines = log.readlines()
                    print("".join(lines[-20:]))
            return False
            
    pdf_name = os.path.basename(tex_path).replace(".tex", ".pdf")
    generated_pdf = os.path.join(working_dir, pdf_name)
    
    if os.path.exists(generated_pdf):
        # Determinar la carpeta de destino basada en la ruta del archivo TeX
        if "capitulo_0" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_0")
            rel_path = f"pdfs/capitulo_0/{dest_name}"
        elif "limites_y_continuidad" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_1")
            rel_path = f"pdfs/capitulo_1/{dest_name}"
        elif "derivadas_parciales" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_12")
            rel_path = f"pdfs/capitulo_12/{dest_name}"
        elif "aplicaciones_de_la_derivada" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_3")
            rel_path = f"pdfs/capitulo_3/{dest_name}"
        elif "derivadas" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_2")
            rel_path = f"pdfs/capitulo_2/{dest_name}"
        elif "integrales_multiples" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_13")
            rel_path = f"pdfs/capitulo_13/{dest_name}"
        elif "calculo_vectorial" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_14")
            rel_path = f"pdfs/capitulo_14/{dest_name}"
        elif "ecuaciones_diferenciales" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_15")
            rel_path = f"pdfs/capitulo_15/{dest_name}"
        elif "tecnicas_de_integracion" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_7")
            rel_path = f"pdfs/capitulo_7/{dest_name}"
        elif "mas_aplicaciones_de_la_integracion" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_8")
            rel_path = f"pdfs/capitulo_8/{dest_name}"
        elif "integracion" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_4")
            rel_path = f"pdfs/capitulo_4/{dest_name}"
        elif "aplicaciones_de_la_integral" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_5")
            rel_path = f"pdfs/capitulo_5/{dest_name}"
        elif "funciones_trascendentes" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_6")
            rel_path = f"pdfs/capitulo_6/{dest_name}"
        else:
            chapter_dir = output_dir
            rel_path = f"pdfs/{dest_name}"
            
        os.makedirs(chapter_dir, exist_ok=True)
        destination = os.path.join(chapter_dir, dest_name)
        shutil.copy2(generated_pdf, destination)
        print(f"✅ ¡Éxito! PDF guardado en: {rel_path}")
        return True
    else:
        print("❌ Error: No se encontró el archivo PDF resultante.")
        return False

def clean_temp_files():
    print("\n🧹 Limpiando archivos auxiliares de LaTeX...")
    extensions = [".aux", ".log", ".out", ".toc", ".pdf"]
    for target in targets.values():
        wdir = target["working_dir"]
        tex_file = os.path.basename(target["tex_path"])
        base_name = tex_file.replace(".tex", "")
        
        for ext in extensions:
            temp_file = os.path.join(wdir, base_name + ext)
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception:
                    pass

def main():
    parser = argparse.ArgumentParser(description="Automatizador de compilación para Cálculo de Stewart")
    parser.add_argument("--target", choices=list(targets.keys()) + ["all"], default="all",
                        help="Compilar un objetivo específico o 'all' (por defecto)")
    parser.add_argument("--clean", action="store_true", help="Limpiar archivos temporales de LaTeX")
    
    args = parser.parse_args()
    
    if not shutil.which("pdflatex"):
        print("❌ Error: 'pdflatex' no está instalado en este sistema. Por favor instala TexLive o similar.")
        return

    if args.clean:
        clean_temp_files()
        print("✨ Limpieza completada.")
        return

    if args.target == "all":
        print("📚 Iniciando compilación de todos los objetivos...")
        success_count = 0
        for name, spec in targets.items():
            if compile_latex(spec["tex_path"], spec["working_dir"], spec["dest_name"]):
                success_count += 1
        
        clean_temp_files()
        
        print(f"\n🎉 ¡Proceso finalizado! Compilados exitosamente: {success_count}/{len(targets)}")
        if success_count > 0:
            print(f"📂 Encuentra todos tus PDFs en la carpeta: {output_dir}")
    else:
        spec = targets[args.target]
        if compile_latex(spec["tex_path"], spec["working_dir"], spec["dest_name"]):
            clean_temp_files()

if __name__ == "__main__":
    main()
