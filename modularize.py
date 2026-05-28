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
    ]
}

def format_folder_name(name):
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
    sec_name = filename.replace(".tex", "")
    sec_dir = os.path.join(TRANS_DIR, sec_name)
    file_path = os.path.join(sec_dir, filename)
    
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
