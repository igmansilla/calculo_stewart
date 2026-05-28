#!/usr/bin/env python3
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRANS_DIR = os.path.join(BASE_DIR, "funciones_trascendentes")

CONFIGS = {
    "seccion_06_5.tex": [
        # Block 1: 1-10 interleaved
        {"type": "interleaved", "folders": [["01", "03", "05", "07", "09"], ["02", "04", "06", "08", "10"]]},
        # Block 2: 11-14 interleaved
        {"type": "interleaved", "folders": [["11", "13"], ["12", "14"]]},
        # Block 3: 15-36 interleaved
        {"type": "interleaved", "folders": [
            ["15", "17", "19", "21", "23", "25", "27", "29", "31", "33", "35"],
            ["16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36"]
        ]},
        # Block 4: 37-56 interleaved
        {"type": "interleaved", "folders": [
            ["37", "39", "41", "43", "45", "47", "49", "51", "53", "55"],
            ["38", "40", "42", "44", "46", "48", "50", "52", "54", "56"]
        ]},
        # Block 5: 57-58 single
        {"type": "single", "folders": ["57", "58"]},
        # Block 6: 59-62 interleaved
        {"type": "interleaved", "folders": [["59", "61"], ["60", "62"]]},
        # Block 7: 63-68 single
        {"type": "single", "folders": ["63", "64", "65", "66", "67", "68"]},
        # Block 8: 69-78 interleaved
        {"type": "interleaved", "folders": [
            ["69", "71", "73", "75", "77"],
            ["70", "72", "74", "76", "78"]
        ]},
        # Block 9: 79-92 interleaved
        {"type": "interleaved", "folders": [
            ["79", "81", "83", "85", "87", "89", "91"],
            ["80", "82", "84", "86", "88", "90", "92"]
        ]},
        # Block 10: 93-96 single
        {"type": "single", "folders": ["93", "94", "95", "96"]},
        # Block 11: 97-102 interleaved
        {"type": "interleaved", "folders": [["97", "99", "101"], ["98", "100", "102"]]},
        # Block 12: 103-109 single
        {"type": "single", "folders": ["103", "104", "105", "106", "107", "108", "109"]}
    ],
    "seccion_06_6.tex": [
        # Block 1: 1-11 single
        {"type": "single", "folders": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]}
    ],
    "seccion_06_7.tex": [
        # Block 1: 1-21 single
        {"type": "single", "folders": [f"{i:02d}" for i in range(1, 22)]}
    ],
    "seccion_06_8.tex": [
        # Block 1: 1-25 three columns (odds 1-15, evens 2-16, seq 17-25)
        {"type": "special_3cols", "folders": [
            ["01", "03", "05", "07", "09", "11", "13", "15"],
            ["02", "04", "06", "08", "10", "12", "14", "16"],
            ["17", "18", "19", "20", "21", "22", "23", "24", "25"]
        ]},
        # Block 2: 26 single
        {"type": "single", "folders": ["26"]},
        # Block 3: 28-35 single (Note: book skips 27 or it doesn't exist)
        {"type": "single", "folders": ["28", "29", "30", "31", "32", "33", "34", "35"]},
        # Block 4: 36-68 sequential columns
        {"type": "sequential_2cols", "folders": [
            [str(i) for i in range(36, 59)],
            [str(i) for i in range(61, 69)]
        ]},
        # Block 5: 69-71 single
        {"type": "single", "folders": ["69", "70", "71"]},
        # Block 6: 71-80 interleaved (71 is 71b because of collision)
        {"type": "interleaved", "folders": [
            ["71b", "73", "75", "77", "79"],
            ["72", "74", "76", "78", "80"]
        ]},
        # Block 7: 81-82 single
        {"type": "single", "folders": ["81", "82"]},
        # Block 8: 83-84 interleaved
        {"type": "interleaved", "folders": [["83"], ["84"]]},
        # Block 9: 87-91 interleaved (87, 89, 91 vs 88, 90)
        {"type": "interleaved", "folders": [["87", "89", "91"], ["88", "90"]]},
        # Block 10: 93-94 single
        {"type": "single", "folders": ["93", "94"]},
        # Block 11: 95-105 interleaved
        {"type": "interleaved", "folders": [
            ["95", "97", "99", "101", "103", "105"],
            ["96", "98", "100", "102", "104"]
        ]},
        # Block 12: 107-114 single
        {"type": "single", "folders": ["107", "108", "109", "110", "111", "112", "113", "114"]}
    ],
    "seccion_06_9.tex": [
        # Block 1: 1-15 sequential columns
        {"type": "sequential_2cols", "folders": [
            ["01", "02", "03", "04", "05", "06", "07"],
            ["08", "09", "10", "11", "12", "13", "14", "15"]
        ]},
        # Block 2: 16-25 single
        {"type": "single", "folders": [str(i) for i in range(16, 26)]},
        # Block 3: 26-45 single
        {"type": "single", "folders": [str(i) for i in range(26, 46)]},
        # Block 4: 46-53 sequential columns
        {"type": "sequential_2cols", "folders": [
            ["46", "47", "48", "49"],
            ["50", "51", "52", "53"]
        ]},
        # Block 5: 54-58 single
        {"type": "single", "folders": [str(i) for i in range(54, 59)]}
    ],
    "seccion_06_10.tex": [
        # Block 1: 1-75 in a single minipage
        {"type": "interleaved", "folders": [[f"{i:02d}" for i in range(1, 76)]]},
        # Block 2: 79-98 interleaved (suffix "b")
        {"type": "interleaved", "folders": [
            ["79b", "81b", "83b", "85b", "87b", "89b", "91b", "93b", "95b", "97b"],
            ["80b", "82b", "84b", "86b", "88b", "90b", "92b", "94b"]
        ]},
        # Block 3: 97-100 interleaved (suffix "c")
        {"type": "interleaved", "folders": [
            ["97c", "99c"],
            ["98c", "100c"]
        ]},
        # Block 4: 101-107 single
        {"type": "single", "folders": [str(i) for i in range(101, 108)]}
    ],
    "repaso.tex": [
        # Block 1: 1-8 interleaved
        {"type": "interleaved", "folders": [
            ["01", "03", "05", "07"],
            ["02", "04", "06", "08"]
        ]},
        # Block 2: 9-16 interleaved
        {"type": "interleaved", "folders": [
            ["09", "11", "13", "15"],
            ["10", "12", "14", "16"]
        ]},
        # Block 3: 17-32 single
        {"type": "single", "folders": [str(i) for i in range(17, 33)]},
        # Block 4: 47-48 single
        {"type": "single", "folders": [str(i) for i in range(47, 49)]},
        # Block 5: 49-50 single
        {"type": "single", "folders": [str(i) for i in range(49, 51)]},
        # Block 6: 51-54 single
        {"type": "single", "folders": [str(i) for i in range(51, 55)]},
        # Block 7: 55-78 single
        {"type": "single", "folders": [str(i) for i in range(55, 79)]},
        # Block 8: 79-86 single
        {"type": "single", "folders": [str(i) for i in range(79, 87)]},
        # Block 9: 87-93 single
        {"type": "single", "folders": [str(i) for i in range(87, 94)]},
        # Block 10: 94-99 single
        {"type": "single", "folders": [str(i) for i in range(94, 100)]},
        # Block 11: 100-109 single
        {"type": "single", "folders": [str(i) for i in range(100, 110)]},
        # Block 12: 110-114 single
        {"type": "single", "folders": [str(i) for i in range(110, 115)]}
    ],
    "problemas_adicionales.tex": [
        # Block 1: 1-25 single
        {"type": "single", "folders": [str(i) for i in range(1, 26)]}
    ],
    "seccion_07_1.tex": [
        # Block 1: 1-36 single
        {"type": "single", "folders": [str(i) for i in range(1, 37)]},
        # Block 2: 37-40 single
        {"type": "single", "folders": [str(i) for i in range(37, 41)]},
        # Block 3: 41-46 single
        {"type": "single", "folders": [str(i) for i in range(41, 47)]},
        # Block 4: 47-50 single
        {"type": "single", "folders": [str(i) for i in range(47, 51)]},
        # Block 5: 51-61 single
        {"type": "single", "folders": [str(i) for i in range(51, 62)]}
    ],
    "seccion_07_2.tex": [
        # Block 1: 1-56 single
        {"type": "single", "folders": [str(i) for i in range(1, 57)]},
        # Block 2: 57-58 single
        {"type": "single", "folders": [str(i) for i in range(57, 59)]},
        # Block 3: 59-60 single
        {"type": "single", "folders": [str(i) for i in range(59, 61)]},
        # Block 4: 61-64 single
        {"type": "single", "folders": [str(i) for i in range(61, 65)]},
        # Block 5: 65 single
        {"type": "single", "folders": ["65"]},
        # Block 6: 66-68 single
        {"type": "single", "folders": [str(i) for i in range(66, 69)]},
        # Block 7: 69 single
        {"type": "single", "folders": ["69"]}
    ],
    "seccion_07_3.tex": [
        # Block 1: 1-30 single
        {"type": "single", "folders": [str(i) for i in range(1, 31)]},
        # Block 2: 31-36 single
        {"type": "single", "folders": [str(i) for i in range(31, 37)]}
    ],
    "seccion_07_4.tex": [
        # Block 1: 1-18 single
        {"type": "single", "folders": [str(i) for i in range(1, 19)]},
        # Block 2: 19-64 single
        {"type": "single", "folders": [str(i) for i in range(19, 65)]},
        # Block 3: 65 single
        {"type": "single", "folders": ["65"]},
        # Block 4: 66-69 single
        {"type": "single", "folders": [str(i) for i in range(66, 70)]},
        # Block 5: 70-72 single
        {"type": "single", "folders": [str(i) for i in range(70, 73)]},
        # Block 6: 73 single
        {"type": "single", "folders": ["73"]}
    ],
    "seccion_07_5.tex": [
        # Block 1: 1-40 single
        {"type": "single", "folders": [str(i) for i in range(1, 41)]},
        # Block 2: 41-44 single
        {"type": "single", "folders": [str(i) for i in range(41, 45)]}
    ],
    "seccion_07_6.tex": [
        # Block 1: 1-42 single
        {"type": "single", "folders": [str(i) for i in range(1, 43)]},
        # Block 2: 43-80 single
        {"type": "single", "folders": [str(i) for i in range(43, 81)]}
    ],
    "seccion_07_7.tex": [
        # Block 1: 1-26 single
        {"type": "single", "folders": [str(i) for i in range(1, 27)]},
        # Block 2: 27-30 single
        {"type": "single", "folders": [str(i) for i in range(27, 31)]}
    ],
    "seccion_07_8.tex": [
        # Block 1: 1-2 single
        {"type": "single", "folders": [str(i) for i in range(1, 3)]},
        # Block 2: 3-6 single
        {"type": "single", "folders": [str(i) for i in range(3, 7)]},
        # Block 3: 7-10 single
        {"type": "single", "folders": [str(i) for i in range(7, 11)]},
        # Block 4: 11-20 single
        {"type": "single", "folders": [str(i) for i in range(11, 21)]},
        # Block 5: 21-36 single
        {"type": "single", "folders": [str(i) for i in range(21, 37)]}
    ],
    "seccion_07_9.tex": [
        # Block 1: 1-46 single
        {"type": "single", "folders": [str(i) for i in range(1, 47)]},
        # Block 2: 47-52 single
        {"type": "single", "folders": [str(i) for i in range(47, 53)]},
        # Block 3: 53-58 single
        {"type": "single", "folders": [str(i) for i in range(53, 59)]},
        # Block 4: 59-60 single
        {"type": "single", "folders": [str(i) for i in range(59, 61)]},
        # Block 5: 61-63 single
        {"type": "single", "folders": [str(i) for i in range(61, 64)]},
        # Block 6: 64-78 single
        {"type": "single", "folders": [str(i) for i in range(64, 79)]}
    ],
    "tecnicas_de_integracion/repaso/repaso.tex": [
        # Block 1: Temas Basicos 1-11 single
        {"type": "single", "folders": [f"tema_{i:02d}" for i in range(1, 12)]},
        # Block 2: Ejercicios 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 3: Ejercicios 9-44 single
        {"type": "single", "folders": [str(i) for i in range(9, 45)]},
        # Block 4: Ejercicios 45-62 single
        {"type": "single", "folders": [str(i) for i in range(45, 63)]},
        # Block 5: Ejercicios 63-66 single
        {"type": "single", "folders": [str(i) for i in range(63, 67)]},
        # Block 6: Ejercicios 67-68 single
        {"type": "single", "folders": [str(i) for i in range(67, 69)]},
        # Block 7: Ejercicios 69-70 single
        {"type": "single", "folders": [str(i) for i in range(69, 71)]},
        # Block 8: Ejercicios 71-81 single
        {"type": "single", "folders": [str(i) for i in range(71, 82)]}
    ],
    "tecnicas_de_integracion/aplicaciones_adicionales/aplicaciones_adicionales.tex": [
        # Block 1: 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_1/seccion_08_1.tex": [
        # Block 1: 1-10 single
        {"type": "single", "folders": [str(i) for i in range(1, 11)]},
        # Block 2: 11-20 single
        {"type": "single", "folders": [str(i) for i in range(11, 21)]},
        # Block 3: 21-30 single
        {"type": "single", "folders": [str(i) for i in range(21, 31)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_2/seccion_08_2.tex": [
        # Block 1: 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 2: 5-8 single
        {"type": "single", "folders": [str(i) for i in range(5, 9)]},
        # Block 3: 9-20 single
        {"type": "single", "folders": [str(i) for i in range(9, 21)]},
        # Block 4: 21-26 single
        {"type": "single", "folders": [str(i) for i in range(21, 27)]},
        # Block 5: 27-32 single
        {"type": "single", "folders": [str(i) for i in range(27, 33)]},
        # Block 6: 33-36 single
        {"type": "single", "folders": [str(i) for i in range(33, 37)]},
        # Block 7: 37-38 single
        {"type": "single", "folders": [str(i) for i in range(37, 39)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_3/seccion_08_3.tex": [
        # Block 1: 1-14 single
        {"type": "single", "folders": [str(i) for i in range(1, 15)]},
        # Block 2: 15-22 single
        {"type": "single", "folders": [str(i) for i in range(15, 23)]},
        # Block 3: 23-24 single
        {"type": "single", "folders": [str(i) for i in range(23, 25)]},
        # Block 4: 25-34 single
        {"type": "single", "folders": [str(i) for i in range(25, 35)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_4/seccion_08_4.tex": [
        # Block 1: 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 2: 5-18 single
        {"type": "single", "folders": [str(i) for i in range(5, 19)]},
        # Block 3: 19-22 single
        {"type": "single", "folders": [str(i) for i in range(19, 23)]},
        # Block 4: 23-23 single
        {"type": "single", "folders": [str(i) for i in range(23, 24)]},
        # Block 5: 24-27 single
        {"type": "single", "folders": [str(i) for i in range(24, 28)]},
        # Block 6: 28-30 single
        {"type": "single", "folders": [str(i) for i in range(28, 31)]},
        # Block 7: 31-31 single
        {"type": "single", "folders": [str(i) for i in range(31, 32)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_5/seccion_08_5.tex": [
        # Block 1: 1-2 single
        {"type": "single", "folders": [str(i) for i in range(1, 3)]},
        # Block 2: 3-12 single
        {"type": "single", "folders": [str(i) for i in range(3, 13)]},
        # Block 3: 13-22 single
        {"type": "single", "folders": [str(i) for i in range(13, 23)]}
    ],
    "mas_aplicaciones_de_la_integracion/seccion_08_6/seccion_08_6.tex": [
        # Block 1: 1-20 single
        {"type": "single", "folders": [str(i) for i in range(1, 21)]}
    ],
    "mas_aplicaciones_de_la_integracion/repaso/repaso.tex": [
        # Block 1: Temas Basicos 1-12 single
        {"type": "single", "folders": [f"tema_{i:02d}" for i in range(1, 13)]},
        # Block 2: Ejercicios 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 3: Ejercicios 5-6 single
        {"type": "single", "folders": [str(i) for i in range(5, 7)]},
        # Block 4: Ejercicios 7-8 single
        {"type": "single", "folders": [str(i) for i in range(7, 9)]},
        # Block 5: Ejercicios 9-14 single
        {"type": "single", "folders": [str(i) for i in range(9, 15)]},
        # Block 6: Ejercicios 15-16 single
        {"type": "single", "folders": [str(i) for i in range(15, 17)]},
        # Block 7: Ejercicios 17-18 single
        {"type": "single", "folders": [str(i) for i in range(17, 19)]},
        # Block 8: Ejercicios 19-27 single
        {"type": "single", "folders": [str(i) for i in range(19, 28)]}
    ],
    "mas_aplicaciones_de_la_integracion/problemas_adicionales/problemas_adicionales.tex": [
        # Block 1: 1-16 single
        {"type": "single", "folders": [str(i) for i in range(1, 17)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_1/seccion_09_1.tex": [
        # Block 1: 1-20 single
        {"type": "single", "folders": [str(i) for i in range(1, 21)]},
        # Block 2: 21-26 single
        {"type": "single", "folders": [str(i) for i in range(21, 27)]},
        # Block 3: 27-30 single
        {"type": "single", "folders": [str(i) for i in range(27, 31)]},
        # Block 4: 31-40 single
        {"type": "single", "folders": [str(i) for i in range(31, 41)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_2/seccion_09_2.tex": [
        # Block 1: 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: 7-10 single
        {"type": "single", "folders": [str(i) for i in range(7, 11)]},
        # Block 3: 11-18 single
        {"type": "single", "folders": [str(i) for i in range(11, 19)]},
        # Block 4: 19-24 single
        {"type": "single", "folders": [str(i) for i in range(19, 25)]},
        # Block 5: 25-40 single
        {"type": "single", "folders": [str(i) for i in range(25, 41)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_3/seccion_09_3.tex": [
        # Block 1: 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 2: 5-12 single
        {"type": "single", "folders": [str(i) for i in range(5, 13)]},
        # Block 3: 13-14 single
        {"type": "single", "folders": [str(i) for i in range(13, 15)]},
        # Block 4: 15-16 single
        {"type": "single", "folders": [str(i) for i in range(15, 17)]},
        # Block 5: 17-20 single
        {"type": "single", "folders": [str(i) for i in range(17, 21)]},
        # Block 6: 21-26 single
        {"type": "single", "folders": [str(i) for i in range(21, 27)]},
        # Block 7: 27-28 single
        {"type": "single", "folders": [str(i) for i in range(27, 29)]},
        # Block 8: 29-34 single
        {"type": "single", "folders": [str(i) for i in range(29, 35)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_4/seccion_09_4.tex": [
        # Block 1: 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: 9-16 single
        {"type": "single", "folders": [str(i) for i in range(9, 17)]},
        # Block 3: 17-20 single
        {"type": "single", "folders": [str(i) for i in range(17, 21)]},
        # Block 4: 21-26 single
        {"type": "single", "folders": [str(i) for i in range(21, 27)]},
        # Block 5: 27 single
        {"type": "single", "folders": ["27"]},
        # Block 6: 29-34 single
        {"type": "single", "folders": [str(i) for i in range(29, 35)]},
        # Block 7: 35-40 single
        {"type": "single", "folders": [str(i) for i in range(35, 41)]},
        # Block 8: 41-72 single
        {"type": "single", "folders": [str(i) for i in range(41, 73)]},
        # Block 9: 73-76 single
        {"type": "single", "folders": [str(i) for i in range(73, 77)]},
        # Block 10: 77-84 single
        {"type": "single", "folders": [str(i) for i in range(77, 85)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_5/seccion_09_5.tex": [
        # Block 1: 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: 7-8 single
        {"type": "single", "folders": [str(i) for i in range(7, 9)]},
        # Block 3: 9-18 single
        {"type": "single", "folders": [str(i) for i in range(9, 19)]},
        # Block 4: 19-24 single
        {"type": "single", "folders": [str(i) for i in range(19, 25)]},
        # Block 5: 25-30 single
        {"type": "single", "folders": [str(i) for i in range(25, 31)]},
        # Block 6: 31-36 single
        {"type": "single", "folders": [str(i) for i in range(31, 37)]},
        # Block 7: 37-38 single
        {"type": "single", "folders": [str(i) for i in range(37, 39)]},
        # Block 8: 39-44 single
        {"type": "single", "folders": [str(i) for i in range(39, 45)]},
        # Block 9: 45-52 single
        {"type": "single", "folders": [str(i) for i in range(45, 53)]},
        # Block 10: 53-56 single
        {"type": "single", "folders": [str(i) for i in range(53, 57)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_6/seccion_09_6.tex": [
        # Block 1: 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: 9-20 single
        {"type": "single", "folders": [str(i) for i in range(9, 21)]},
        # Block 3: 21-38 single
        {"type": "single", "folders": [str(i) for i in range(21, 39)]},
        # Block 4: 39-41 single
        {"type": "single", "folders": [str(i) for i in range(39, 42)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/seccion_09_7/seccion_09_7.tex": [
        # Block 1: 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: 9-20 single
        {"type": "single", "folders": [str(i) for i in range(9, 21)]},
        # Block 3: 21-28 single
        {"type": "single", "folders": [str(i) for i in range(21, 29)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/repaso/repaso.tex": [
        # Block 1: Temas Basicos 1-17 single
        {"type": "single", "folders": [f"tema_{i:02d}" for i in range(1, 18)]},
        # Block 2: Ejercicios 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 3: Ejercicios 5-12 single
        {"type": "single", "folders": [str(i) for i in range(5, 13)]},
        # Block 4: Ejercicios 13-14 single
        {"type": "single", "folders": [str(i) for i in range(13, 15)]},
        # Block 5: Ejercicios 15-18 single
        {"type": "single", "folders": [str(i) for i in range(15, 19)]},
        # Block 6: Ejercicios 19-20 single
        {"type": "single", "folders": [str(i) for i in range(19, 21)]},
        # Block 7: Ejercicios 21-28 single
        {"type": "single", "folders": [str(i) for i in range(21, 29)]},
        # Block 8: Ejercicios 29-32 single
        {"type": "single", "folders": [str(i) for i in range(29, 33)]},
        # Block 9: Ejercicios 33 single
        {"type": "single", "folders": ["33"]},
        # Block 10: Ejercicios 35-38 single
        {"type": "single", "folders": [str(i) for i in range(35, 39)]},
        # Block 11: Ejercicios 39-47 single
        {"type": "single", "folders": [str(i) for i in range(39, 48)]}
    ],
    "ecuaciones_parametricas_y_coordenadas_polares/aplicaciones_adicionales/aplicaciones_adicionales.tex": [
        # Block 1: 1-12 single
        {"type": "single", "folders": [str(i) for i in range(1, 13)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_1/seccion_10_1.tex": [
        # Block 1: Ejercicios 1-10 single
        {"type": "single", "folders": [str(i) for i in range(1, 11)]},
        # Block 2: Ejercicios 11-18 single
        {"type": "single", "folders": [str(i) for i in range(11, 19)]},
        # Block 3: Ejercicios 19-20 single
        {"type": "single", "folders": [str(i) for i in range(19, 21)]},
        # Block 4: Ejercicios 21-56 single
        {"type": "single", "folders": [str(i) for i in range(21, 57)]},
        # Block 5: Ejercicios 57-58 single
        {"type": "single", "folders": [str(i) for i in range(57, 59)]},
        # Block 6: Ejercicios 59-66 single
        {"type": "single", "folders": [str(i) for i in range(59, 67)]},
        # Block 7: Ejercicios 67-76 single
        {"type": "single", "folders": [str(i) for i in range(67, 77)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_2/seccion_10_2.tex": [
        # Block 1: Ejercicios 1-36 single
        {"type": "single", "folders": [str(i) for i in range(1, 37)]},
        # Block 2: Ejercicios 37-42 single
        {"type": "single", "folders": [str(i) for i in range(37, 43)]},
        # Block 3: Ejercicios 43-48 single
        {"type": "single", "folders": [str(i) for i in range(43, 49)]},
        # Block 4: Ejercicios 49-58 single
        {"type": "single", "folders": [str(i) for i in range(49, 59)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_3/seccion_10_3.tex": [
        # Block 1: Ejercicios 1-22 single
        {"type": "single", "folders": [str(i) for i in range(1, 23)]},
        # Block 2: Ejercicios 23-26 single
        {"type": "single", "folders": [str(i) for i in range(23, 27)]},
        # Block 3: Ejercicios 27-30 single
        {"type": "single", "folders": [str(i) for i in range(27, 31)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_4/seccion_10_4.tex": [
        # Block 1: Ejercicios 1-38 single
        {"type": "single", "folders": [str(i) for i in range(1, 39)]},
        # Block 2: Ejercicios 39-46 single
        {"type": "single", "folders": [str(i) for i in range(39, 47)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_5/seccion_10_5.tex": [
        # Block 1: Ejercicios 1-27 single
        {"type": "single", "folders": [str(i) for i in range(1, 28)]},
        # Block 2: Ejercicios 28-30 single
        {"type": "single", "folders": [str(i) for i in range(28, 31)]},
        # Block 3: Ejercicios 31-38 single
        {"type": "single", "folders": [str(i) for i in range(31, 39)]},
        # Block 4: Ejercicios 39 single
        {"type": "single", "folders": ["39"]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_6/seccion_10_6.tex": [
        # Block 1: Ejercicios 1-28 single
        {"type": "single", "folders": [str(i) for i in range(1, 29)]},
        # Block 2: Ejercicios 29-30 single
        {"type": "single", "folders": [str(i) for i in range(29, 31)]},
        # Block 3: Ejercicios 31-36 single
        {"type": "single", "folders": [str(i) for i in range(31, 37)]},
        # Block 4: Ejercicios 37-42 single
        {"type": "single", "folders": [str(i) for i in range(37, 43)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_7/seccion_10_7.tex": [
        # Block 1: Ejercicios 1-40 single
        {"type": "single", "folders": [str(i) for i in range(1, 41)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_8/seccion_10_8.tex": [
        # Block 1: Ejercicios 1-2 single
        {"type": "single", "folders": [str(i) for i in range(1, 3)]},
        # Block 2: Ejercicios 3-32 single
        {"type": "single", "folders": [str(i) for i in range(3, 33)]},
        # Block 3: Ejercicios 33-38 single
        {"type": "single", "folders": [str(i) for i in range(33, 39)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_9/seccion_10_9.tex": [
        # Block 1: Ejercicios 1-12 single
        {"type": "single", "folders": [str(i) for i in range(1, 13)]},
        # Block 2: Ejercicios 13-24 single
        {"type": "single", "folders": [str(i) for i in range(13, 25)]},
        # Block 3: Ejercicios 25-42 single
        {"type": "single", "folders": [str(i) for i in range(25, 43)]},
        # Block 4: Ejercicios 43-44 single
        {"type": "single", "folders": [str(i) for i in range(43, 45)]},
        # Block 5: Ejercicios 45-50 single
        {"type": "single", "folders": [str(i) for i in range(45, 51)]},
        # Block 6: Ejercicios 51-56 single
        {"type": "single", "folders": [str(i) for i in range(51, 57)]},
        # Block 7: Ejercicios 57-58 single
        {"type": "single", "folders": [str(i) for i in range(57, 59)]},
        # Block 8: Ejercicios 59-64 single
        {"type": "single", "folders": [str(i) for i in range(59, 65)]},
        # Block 9: Ejercicios 65-68 single
        {"type": "single", "folders": [str(i) for i in range(65, 69)]},
        # Block 10: Ejercicios 69-72 single
        {"type": "single", "folders": [str(i) for i in range(69, 73)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_10/seccion_10_10.tex": [
        # Block 1: Ejercicios 1-12 single
        {"type": "single", "folders": [str(i) for i in range(1, 13)]},
        # Block 2: Ejercicios 13-21 single
        {"type": "single", "folders": [str(i) for i in range(13, 22)]}
    ],
    "sucesiones_y_series_infinitas/seccion_10_11/seccion_10_11.tex": [
        # Block 1: Ejercicios 1-12 single
        {"type": "single", "folders": [str(i) for i in range(1, 13)]},
        # Block 2: Ejercicios 13-14 single
        {"type": "single", "folders": [str(i) for i in range(13, 15)]},
        # Block 3: Ejercicios 15-26 single
        {"type": "single", "folders": [str(i) for i in range(15, 27)]},
        # Block 4: Ejercicios 27-38 single
        {"type": "single", "folders": [str(i) for i in range(27, 39)]},
        # Block 5: Ejercicios 39-40 single
        {"type": "single", "folders": [str(i) for i in range(39, 41)]},
        # Block 6: Ejercicios 41-44 single
        {"type": "single", "folders": [str(i) for i in range(41, 45)]},
        # Block 7: Ejercicios 45-53 single
        {"type": "single", "folders": [str(i) for i in range(45, 54)]}
    ],
    "sucesiones_y_series_infinitas/repaso/repaso.tex": [
        # Block 1: Temas Basicos 1-35 single
        {"type": "single", "folders": [f"tema_{i:02d}" for i in range(1, 36)]},
        # Block 2: Ejercicios 1-14 single
        {"type": "single", "folders": [str(i) for i in range(1, 15)]},
        # Block 3: Ejercicios 15-22 single
        {"type": "single", "folders": [str(i) for i in range(15, 23)]},
        # Block 4: Ejercicios 23-34 single
        {"type": "single", "folders": [str(i) for i in range(23, 35)]},
        # Block 5: Ejercicios 35-38 single
        {"type": "single", "folders": [str(i) for i in range(35, 39)]},
        # Block 6: Ejercicios 39-42 single
        {"type": "single", "folders": [str(i) for i in range(39, 43)]},
        # Block 7: Ejercicios 43-47 single
        {"type": "single", "folders": [str(i) for i in range(43, 48)]},
        # Block 8: Ejercicios 48-51 single
        {"type": "single", "folders": [str(i) for i in range(48, 52)]},
        # Block 9: Ejercicios 52-54 single
        {"type": "single", "folders": [str(i) for i in range(52, 55)]},
        # Block 10: Ejercicios 55-62 single
        {"type": "single", "folders": [str(i) for i in range(55, 63)]},
        # Block 11: Ejercicios 63-64 single
        {"type": "single", "folders": [str(i) for i in range(63, 65)]},
        # Block 12: Ejercicios 65-66 single
        {"type": "single", "folders": [str(i) for i in range(65, 67)]},
        # Block 13: Ejercicios 67-68 single
        {"type": "single", "folders": [str(i) for i in range(67, 69)]},
        # Block 14: Ejercicios 69-72 single
        {"type": "single", "folders": [str(i) for i in range(69, 73)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_1/seccion_11_1.tex": [
        # Block 1: Ejercicios 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: Ejercicios 7-10 single
        {"type": "single", "folders": [str(i) for i in range(7, 11)]},
        # Block 3: Ejercicios 11-12 single
        {"type": "single", "folders": [str(i) for i in range(11, 13)]},
        # Block 4: Ejercicios 13-16 single
        {"type": "single", "folders": [str(i) for i in range(13, 17)]},
        # Block 5: Ejercicios 17-22 single
        {"type": "single", "folders": [str(i) for i in range(17, 23)]},
        # Block 6: Ejercicios 23-29 single
        {"type": "single", "folders": [str(i) for i in range(23, 30)]},
        # Block 7: Ejercicios 30-45 single
        {"type": "single", "folders": [str(i) for i in range(30, 46)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_2/seccion_11_2.tex": [
        # Block 1: Ejercicios 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: Ejercicios 7-10 single
        {"type": "single", "folders": [str(i) for i in range(7, 11)]},
        # Block 3: Ejercicios 11-18 single
        {"type": "single", "folders": [str(i) for i in range(11, 19)]},
        # Block 4: Ejercicios 19-24 single
        {"type": "single", "folders": [str(i) for i in range(19, 25)]},
        # Block 5: Ejercicios 25-26 single
        {"type": "single", "folders": [str(i) for i in range(25, 27)]},
        # Block 6: Ejercicios 27-35 single
        {"type": "single", "folders": [str(i) for i in range(27, 36)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_3/seccion_11_3.tex": [
        # Block 1: Ejercicios 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: Ejercicios 9-10 single
        {"type": "single", "folders": [str(i) for i in range(9, 11)]},
        # Block 3: Ejercicios 11-16 single
        {"type": "single", "folders": [str(i) for i in range(11, 17)]},
        # Block 4: Ejercicios 17-18 single
        {"type": "single", "folders": [str(i) for i in range(17, 19)]},
        # Block 5: Ejercicios 19-24 single
        {"type": "single", "folders": [str(i) for i in range(19, 25)]},
        # Block 6: Ejercicios 25-28 single
        {"type": "single", "folders": [str(i) for i in range(25, 29)]},
        # Block 7: Ejercicios 29-30 single
        {"type": "single", "folders": [str(i) for i in range(29, 31)]},
        # Block 8: Ejercicios 31-36 single
        {"type": "single", "folders": [str(i) for i in range(31, 37)]},
        # Block 9: Ejercicios 37-42 single
        {"type": "single", "folders": [str(i) for i in range(37, 43)]},
        # Block 10: Ejercicios 43-57 single
        {"type": "single", "folders": [str(i) for i in range(43, 58)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_4/seccion_11_4.tex": [
        # Block 1: Ejercicios 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: Ejercicios 9-20 single
        {"type": "single", "folders": [str(i) for i in range(9, 21)]},
        # Block 3: Ejercicios 21-24 single
        {"type": "single", "folders": [str(i) for i in range(21, 25)]},
        # Block 4: Ejercicios 25-26 single
        {"type": "single", "folders": [str(i) for i in range(25, 27)]},
        # Block 5: Ejercicios 27-28 single
        {"type": "single", "folders": [str(i) for i in range(27, 29)]},
        # Block 6: Ejercicios 29-40 single
        {"type": "single", "folders": [str(i) for i in range(29, 41)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_5/seccion_11_5.tex": [
        # Block 1: Ejercicios 1-4 single
        {"type": "single", "folders": [str(i) for i in range(1, 5)]},
        # Block 2: Ejercicios 5-10 single
        {"type": "single", "folders": [str(i) for i in range(5, 11)]},
        # Block 3: Ejercicios 11-14 single
        {"type": "single", "folders": [str(i) for i in range(11, 15)]},
        # Block 4: Ejercicios 15-18 single
        {"type": "single", "folders": [str(i) for i in range(15, 19)]},
        # Block 5: Ejercicios 19-22 single
        {"type": "single", "folders": [str(i) for i in range(19, 23)]},
        # Block 6: Ejercicios 23-26 single
        {"type": "single", "folders": [str(i) for i in range(23, 27)]},
        # Block 7: Ejercicios 27-30 single
        {"type": "single", "folders": [str(i) for i in range(27, 31)]},
        # Block 8: Ejercicios 31-34 single
        {"type": "single", "folders": [str(i) for i in range(31, 35)]},
        # Block 9: Ejercicios 35-38 single
        {"type": "single", "folders": [str(i) for i in range(35, 39)]},
        # Block 10: Ejercicios 39-40 single
        {"type": "single", "folders": [str(i) for i in range(39, 41)]},
        # Block 11: Ejercicios 41-46 single
        {"type": "single", "folders": [str(i) for i in range(41, 47)]},
        # Block 12: Ejercicios 47-48 single
        {"type": "single", "folders": [str(i) for i in range(47, 49)]},
        # Block 13: Ejercicios 49-50 single
        {"type": "single", "folders": [str(i) for i in range(49, 51)]},
        # Block 14: Ejercicios 51-56 single
        {"type": "single", "folders": [str(i) for i in range(51, 57)]},
        # Block 15: Ejercicios 57-60 single
        {"type": "single", "folders": [str(i) for i in range(57, 61)]},
        # Block 16: Ejercicios 61-66 single
        {"type": "single", "folders": [str(i) for i in range(61, 67)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_6/seccion_11_6.tex": [
        # Block 1: Ejercicios 1-16 single
        {"type": "single", "folders": [str(i) for i in range(1, 17)]},
        # Block 2: Ejercicios 17-28 single
        {"type": "single", "folders": [str(i) for i in range(17, 29)]},
        # Block 3: Ejercicios 29-36 single
        {"type": "single", "folders": [str(i) for i in range(29, 37)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_7/seccion_11_7.tex": [
        # Block 1: Ejercicios 1-8 single
        {"type": "single", "folders": [str(i) for i in range(1, 9)]},
        # Block 2: Ejercicios 9-10 single
        {"type": "single", "folders": [str(i) for i in range(9, 11)]},
        # Block 3: Ejercicios 11-14 single
        {"type": "single", "folders": [str(i) for i in range(11, 15)]},
        # Block 4: Ejercicios 15-22 single
        {"type": "single", "folders": [str(i) for i in range(15, 23)]},
        # Block 5: Ejercicios 23-28 single
        {"type": "single", "folders": [str(i) for i in range(23, 29)]},
        # Block 6: Ejercicios 29-32 single
        {"type": "single", "folders": [str(i) for i in range(29, 33)]},
        # Block 7: Ejercicios 33-38 single
        {"type": "single", "folders": [str(i) for i in range(33, 39)]},
        # Block 8: Ejercicios 39-40 single
        {"type": "single", "folders": [str(i) for i in range(39, 41)]},
        # Block 9: Ejercicios 41-44 single
        {"type": "single", "folders": [str(i) for i in range(41, 45)]},
        # Block 10: Ejercicios 45-59 single
        {"type": "single", "folders": [str(i) for i in range(45, 60)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_8/seccion_11_8.tex": [
        # Block 1: Ejercicios 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: Ejercicios 7-10 single
        {"type": "single", "folders": [str(i) for i in range(7, 11)]},
        # Block 3: Ejercicios 11-16 single
        {"type": "single", "folders": [str(i) for i in range(11, 17)]},
        # Block 4: Ejercicios 17-22 single
        {"type": "single", "folders": [str(i) for i in range(17, 23)]},
        # Block 5: Ejercicios 23-26 single
        {"type": "single", "folders": [str(i) for i in range(23, 27)]},
        # Block 6: Ejercicios 27-28 single
        {"type": "single", "folders": [str(i) for i in range(27, 29)]},
        # Block 7: Ejercicios 29-30 single
        {"type": "single", "folders": [str(i) for i in range(29, 31)]},
        # Block 8: Ejercicios 31-38 single
        {"type": "single", "folders": [str(i) for i in range(31, 39)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/seccion_11_10/seccion_11_10.tex": [
        # Block 1: Ejercicios 1-6 single
        {"type": "single", "folders": [str(i) for i in range(1, 7)]},
        # Block 2: Ejercicios 7-12 single
        {"type": "single", "folders": [str(i) for i in range(7, 13)]},
        # Block 3: Ejercicios 13-18 single
        {"type": "single", "folders": [str(i) for i in range(13, 19)]},
        # Block 4: Ejercicios 19-24 single
        {"type": "single", "folders": [str(i) for i in range(19, 25)]},
        # Block 5: Ejercicios 25-28 single
        {"type": "single", "folders": [str(i) for i in range(25, 29)]},
        # Block 6: Ejercicios 29-32 single
        {"type": "single", "folders": [str(i) for i in range(29, 33)]},
        # Block 7: Ejercicios 33-50 single
        {"type": "single", "folders": [str(i) for i in range(33, 51)]},
        # Block 8: Ejercicios 51-58 single
        {"type": "single", "folders": [str(i) for i in range(51, 59)]},
        # Block 9: Ejercicios 59-62 single
        {"type": "single", "folders": [str(i) for i in range(59, 63)]},
        # Block 10: Ejercicio 63 single
        {"type": "single", "folders": ["63"]}
    ],
    "geometria_analitica_tridimensional_y_vectores/repaso/repaso.tex": [
        # Block 1: Temas Basicos 1-40 single
        {"type": "single", "folders": [f"tema_{i:02d}" for i in range(1, 41)]},
        # Block 2: Ejercicios 75-87 single
        {"type": "single", "folders": [str(i) for i in range(75, 88)]}
    ],
    "geometria_analitica_tridimensional_y_vectores/aplicaciones_adicionales/aplicaciones_adicionales.tex": [
        # Block 1: Ejercicios 1-11 single
        {"type": "single", "folders": [str(i) for i in range(1, 12)]}
    ]
}

def format_folder_name(name):
    if name.startswith("tema_") or name.startswith("ejercicio_"):
        return name
    if name.isdigit():
        return f"ejercicio_{int(name):02d}"
    else:
        m = re.match(r"^(\d+)(.*)$", name)
        if m:
            num = int(m.group(1))
            suffix = m.group(2)
            return f"ejercicio_{num:02d}{suffix}"
        return f"ejercicio_{name}"

def strip_indentation(text):
    lines = text.split('\n')
    non_empty_lines = [l for l in lines if l.strip()]
    if not non_empty_lines:
        return text.strip()
    
    first_line = non_empty_lines[0]
    indent_len = len(first_line) - len(first_line.lstrip())
    indent = first_line[:indent_len]
    
    new_lines = []
    for line in lines:
        if line.startswith(indent):
            new_lines.append(line[indent_len:])
        else:
            new_lines.append(line.lstrip())
            
    return '\n'.join(new_lines).strip()

def find_blocks(text, begin_tag, end_tag):
    blocks = []
    i = 0
    n = len(text)
    begin_len = len(begin_tag)
    end_len = len(end_tag)
    
    while i < n:
        start_idx = text.find(begin_tag, i)
        if start_idx == -1:
            break
            
        # Find matching end_tag keeping track of nested begin/end
        depth = 1
        curr = start_idx + begin_len
        end_idx = -1
        while curr < n and depth > 0:
            next_begin = text.find(begin_tag, curr)
            next_end = text.find(end_tag, curr)
            
            if next_end == -1:
                break
                
            if next_begin != -1 and next_begin < next_end:
                depth += 1
                curr = next_begin + begin_len
            else:
                depth -= 1
                curr = next_end + end_len
                if depth == 0:
                    end_idx = next_end
                    
        if end_idx != -1:
            blocks.append({
                "start": start_idx,
                "end": end_idx + end_len,
                "content": text[start_idx + begin_len : end_idx]
            })
            i = end_idx + end_len
        else:
            i = start_idx + begin_len
            
    return blocks

def parse_block_elements(text):
    tokens = []
    i = 0
    n = len(text)
    depth = 0
    current_token_chars = []
    current_token_type = 'other'
    
    while i < n:
        if text[i:i+6] == '\\begin':
            depth += 1
            current_token_chars.append(text[i:i+6])
            i += 6
        elif text[i:i+4] == '\\end':
            depth -= 1
            current_token_chars.append(text[i:i+4])
            i += 4
        elif depth == 0 and text[i:i+5] == '\\item':
            if current_token_chars:
                tokens.append((current_token_type, ''.join(current_token_chars)))
                current_token_chars = []
            current_token_type = 'item'
            current_token_chars.append('\\item')
            i += 5
        elif depth == 0 and (text[i:i+13] == '\\addtocounter' or text[i:i+11] == '\\setcounter' or text[i:i+7] == '\\vspace'):
            if current_token_chars:
                tokens.append((current_token_type, ''.join(current_token_chars)))
                current_token_chars = []
            current_token_type = 'other'
            
            cmd_start = i
            if text[i:i+13] == '\\addtocounter':
                cmd_len = 13
            elif text[i:i+11] == '\\setcounter':
                cmd_len = 11
            else:
                cmd_len = 7
                
            i += cmd_len
            num_brace_groups = 2 if cmd_len in (13, 11) else 1
            cmd_text = text[cmd_start:i]
            
            for _ in range(num_brace_groups):
                while i < n and text[i].isspace():
                    cmd_text += text[i]
                    i += 1
                if i < n and text[i] == '{':
                    brace_depth = 1
                    brace_start = i
                    i += 1
                    while i < n and brace_depth > 0:
                        if text[i] == '{':
                            brace_depth += 1
                        elif text[i] == '}':
                            brace_depth -= 1
                        i += 1
                    cmd_text += text[brace_start:i]
            current_token_chars.append(cmd_text)
        else:
            current_token_chars.append(text[i])
            i += 1
            
    if current_token_chars:
        tokens.append((current_token_type, ''.join(current_token_chars)))
        
    return tokens

def process_section(filename, config_list):
    if "/" in filename or "\\" in filename:
        file_path = os.path.join(BASE_DIR, filename)
        sec_dir = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
    else:
        if filename.startswith("seccion_06") or filename in ("repaso.tex", "problemas_adicionales.tex"):
            sec_name = filename.replace(".tex", "")
            sec_dir = os.path.join(BASE_DIR, "funciones_trascendentes", sec_name)
            file_path = os.path.join(sec_dir, filename)
        elif filename.startswith("seccion_07"):
            sec_name = filename.replace(".tex", "")
            sec_dir = os.path.join(BASE_DIR, "tecnicas_de_integracion", sec_name)
            file_path = os.path.join(sec_dir, filename)
        else:
            raise ValueError(f"Unknown chapter directory for {filename}")
    
    if not os.path.exists(file_path):
        print(f"⚠️ File {file_path} not found. Skipping.")
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if the section has already been modularized
    if "\\subimport{" in content:
        print(f"⏭️ {filename} is already modularized. Skipping.")
        return
        
    # Find all top-level enumerate blocks
    enum_blocks = find_blocks(content, "\\begin{enumerate}", "\\end{enumerate}")
    if len(enum_blocks) != len(config_list):
        raise ValueError(f"Expected {len(config_list)} enumerate blocks in {filename}, found {len(enum_blocks)}")
        
    # Process blocks in REVERSE order to avoid index shifts!
    for b_idx in reversed(range(len(enum_blocks))):
        block = enum_blocks[b_idx]
        b_config = config_list[b_idx]
        b_content = block["content"]
        
        # Check if block has minipages
        mp_blocks = find_blocks(b_content, "\\begin{minipage}", "\\end{minipage}")
        
        if mp_blocks:
            # Multi-column block
            if b_config["type"] not in ("interleaved", "sequential_2cols", "special_3cols"):
                raise ValueError(f"Block {b_idx} in {filename} has minipages, but config type is {b_config['type']}")
                
            expected_cols = len(b_config["folders"])
            if len(mp_blocks) != expected_cols:
                raise ValueError(f"Block {b_idx} in {filename} has {len(mp_blocks)} minipages, but config expected {expected_cols}")
                
            # Process minipages in reverse order to keep indices correct if we edit inside
            # But wait! We can just reconstruct the block content completely or edit them in place (using reverse).
            # To be absolutely safe, let's process minipages in REVERSE order of columns.
            reconstructed_b_content = b_content
            for m_idx in reversed(range(len(mp_blocks))):
                mp = mp_blocks[m_idx]
                col_folders = b_config["folders"][m_idx]
                
                # Parse elements of the minipage
                elements = parse_block_elements(mp["content"])
                
                # Count items
                item_count = sum(1 for t, _ in elements if t == 'item')
                if item_count != len(col_folders):
                    raise ValueError(f"Block {b_idx} Col {m_idx} in {filename} has {item_count} items, but config expected {len(col_folders)}")
                    
                # Replace items
                f_idx = 0
                new_elements = []
                for t, text in elements:
                    if t == 'item':
                        folder_name = format_folder_name(col_folders[f_idx])
                        f_idx += 1
                        
                        # Create folder
                        ex_dir = os.path.join(sec_dir, folder_name)
                        os.makedirs(ex_dir, exist_ok=True)
                        
                        # Clean content (must start with \item, zero leading space)
                        cleaned = strip_indentation(text)
                        ex_file_path = os.path.join(ex_dir, "ejercicio.tex")
                        with open(ex_file_path, "w", encoding="utf-8") as exf:
                            exf.write(cleaned + "\n")
                            
                        # Replace in main file with \subimport
                        # We preserve whatever indent matches the \item indentation, plus we keep a clean newline
                        new_elements.append(f"\\subimport{{{folder_name}/}}{{ejercicio.tex}}\n")
                    else:
                        new_elements.append(text)
                        
                new_mp_content = ''.join(new_elements)
                
                # Replace minipage content in reconstructed_b_content
                reconstructed_b_content = (
                    reconstructed_b_content[:mp["start"]] +
                    "\\begin{minipage}" + mp["content"].replace(mp["content"], new_mp_content) + "\\end{minipage}" +
                    reconstructed_b_content[mp["end"]:]
                )
                
            # Replace enumerate content
            content = (
                content[:block["start"]] +
                "\\begin{enumerate}" + reconstructed_b_content + "\\end{enumerate}" +
                content[block["end"]:]
            )
            
        else:
            # Single column block
            if b_config["type"] != "single":
                raise ValueError(f"Block {b_idx} in {filename} has NO minipages, but config type is {b_config['type']}")
                
            folders = b_config["folders"]
            elements = parse_block_elements(b_content)
            
            item_count = sum(1 for t, _ in elements if t == 'item')
            if item_count != len(folders):
                raise ValueError(f"Block {b_idx} in {filename} has {item_count} items, but config expected {len(folders)}")
                
            f_idx = 0
            new_elements = []
            for t, text in elements:
                if t == 'item':
                    folder_name = format_folder_name(folders[f_idx])
                    f_idx += 1
                    
                    ex_dir = os.path.join(sec_dir, folder_name)
                    os.makedirs(ex_dir, exist_ok=True)
                    
                    cleaned = strip_indentation(text)
                    ex_file_path = os.path.join(ex_dir, "ejercicio.tex")
                    with open(ex_file_path, "w", encoding="utf-8") as exf:
                        exf.write(cleaned + "\n")
                        
                    new_elements.append(f"\\subimport{{{folder_name}/}}{{ejercicio.tex}}\n")
                else:
                    new_elements.append(text)
                    
            new_b_content = ''.join(new_elements)
            
            content = (
                content[:block["start"]] +
                "\\begin{enumerate}" + new_b_content + "\\end{enumerate}" +
                content[block["end"]:]
            )
            
    # Write back the updated main section file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✨ Successfully modularized {filename}!")

def main():
    print("🚀 Starting modularization process...")
    for filename, config in CONFIGS.items():
        process_section(filename, config)
    print("\n🎉 ALL SECTIONS PROCESSED!")

if __name__ == "__main__":
    main()
