import os
import re
import pandas as pd
from pathlib import Path


def extract_frequencies(file_path):
    frequencies = []
    pattern = re.compile(r'\s+(\d+)\s+\S+\s+\S+\s+(\S+)\s+')

    with open(file_path, 'r', encoding='gbk') as file:
        content = file.read()
        # 找到特征值输出部分的开始
        start_idx = content.find('E I G E N V A L U E    O U T P U T')
        if start_idx == -1:
            return frequencies

        # 提取特征值输出部分的内容
        eigenvalue_section = content[start_idx:]
        matches = pattern.finditer(eigenvalue_section)

        for match in matches:
            mode_no = int(match.group(1))
            frequency = float(match.group(2))
            frequencies.append((mode_no, frequency))
            if len(frequencies) >= 10:
                break

    # 如果不足5阶，填充空值
    while len(frequencies) < 10:
        frequencies.append(None)
        print(f"从 {os.path.basename(dat_file)} 中未提取到频率")

    return frequencies


def process_dat_files(folder_path, output_excel):
    """批量处理DAT文件并保存到Excel"""
    data = []
    folder_path = Path(folder_path)

    for dat_file in folder_path.glob("*.txt"):
        print(f"🔍 正在处理: {dat_file.name}")
        freqs = extract_frequencies(dat_file)

        data.append({
            "DAT文件名": dat_file.name,
            "f1": freqs[0] if freqs[0] is not None else "",
            "f2": freqs[1] if freqs[1] is not None else "",
            "f3": freqs[2] if freqs[2] is not None else "",
            "f4": freqs[3] if freqs[3] is not None else "",
            "f5": freqs[4] if freqs[4] is not None else ""
        })

    # 保存到Excel
    if data:
        df = pd.DataFrame(data)
        df.to_excel(output_excel, index=False)
        print(f"\n✅ 处理完成！结果已保存到: {output_excel}")
    else:
        print("⚠️ 没有找到任何包含频率数据的TXT文件")


if __name__ == "__main__":
    # 配置路径（修改为你的实际路径）
    dat_folder = r"E:\ABAQUS study\paramodle\linkage_opti\dat_1000"
    output_excel = r"E:\ABAQUS study\paramodle\linkage_opti\dat_1000\frequencies_summary.xlsx"
    process_dat_files(dat_folder, output_excel)