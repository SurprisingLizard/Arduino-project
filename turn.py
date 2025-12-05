'''
根據簡譜轉換成音名格式
其中由於 main 中控制函示需有音高(頻率) 並且一首歌之音符數量眾多
因此將簡譜轉換結果以逗號分隔輸出 供後續複製於對音高檔案中使用
'''

import re
# 簡譜對應音名
base_notes = {
    '1': ('C', 4),
    '2': ('D', 4),
    '3': ('E', 4),
    '4': ('F', 4),
    '5': ('G', 4),
    '6': ('A', 4),
    '7': ('B', 4),
    '0': ('REST', None),
}

# 升降音對應表
sharp_map = {
    'C': 'CS',
    'D': 'DS',
    'E': 'E',
    'F': 'FS',
    'G': 'GS',
    'A': 'AS',
    'B': 'B',
}

# 處理升降音
def apply_sharp(note, octave):
    if note == 'REST': # 休止符
        return note, octave

    if the_sharp := sharp_map.get(note): # 不能升半音 
        if note == 'E':
            return 'F', octave
        if note == 'B':
            return 'C', octave + 1
        return the_sharp, octave
    
    return note, octave

# 簡譜音名轉換
def convert_token(token):
    m = re.findall(r'(#+)?([0-7])([+]+)?', token)
    if not m:
        return []

    results = []
    for sharp_signs, digit, oct_signs in m:
        base_note, base_oct = base_notes[digit] # 一次讀兩個值

        if base_note == 'REST': # 休止符
            results.append("REST")
            continue
        
        # 升降八度
        octave = base_oct + (len(oct_signs) if oct_signs else 0)
        
        # 升降半音
        if sharp_signs:
            for _ in range(len(sharp_signs)):
                base_note, octave = apply_sharp(base_note, octave)

        results.append(f"{base_note}{octave}")

    return results

# 抓出 token(一個音) 並轉換
def convert_string(s):
    tokens = re.findall(r'[#+0-7]+', s) # 判斷 token

    output = []
    for t in tokens: # 引用函式轉換
        output.extend(convert_token(t))
    return output

# 整理格式
def format_single_line(demo):
    return ",".join(convert_string(demo)) + ","

# 讀取檔案
def open_file(song):
    with open(song, "r", encoding="utf-8") as f:
        content = f.read()
        return content

# 處理並輸出結果
song = "01.txt" # 檔案名稱
muics = format_single_line(open_file(song))
print(muics)