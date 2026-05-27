#!/usr/bin/env python3
import os
import subprocess
import shutil
import argparse

base_dir = "/home/ignacio/personas/calculo_stewart"
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
        elif "derivadas_parciales" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_12")
            rel_path = f"pdfs/capitulo_12/{dest_name}"
        elif "integrales_multiples" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_13")
            rel_path = f"pdfs/capitulo_13/{dest_name}"
        elif "calculo_vectorial" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_14")
            rel_path = f"pdfs/capitulo_14/{dest_name}"
        elif "ecuaciones_diferenciales" in tex_path:
            chapter_dir = os.path.join(output_dir, "capitulo_15")
            rel_path = f"pdfs/capitulo_15/{dest_name}"
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
