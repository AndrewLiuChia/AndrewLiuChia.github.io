# -*- coding: utf-8 -*-

import re

# 定義讀取檔案的函數
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# 定義寫入檔案的函數
def write_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

# 定義更改 port 的函數
def change_port(lines, ip_address, new_port):
    new_lines = []
    for line in lines:
        pattern = re.compile(f'{ip_address}:\d+')
        if pattern.search(line):
            new_line = pattern.sub(f'{ip_address}:{new_port}', line)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines

# 主函數
def main():
    file_paths = [
        #r'C:\Users\Andrew\Source\Repos\GithubPage\file\combine.txt',
        r'C:\Users\Andrew\Source\Repos\GithubPage\file\TaiwanLive.txt'
    ]  # 原始檔案路徑

    # 定義需要替換的 IP 和新 port
    replacements = {
        '108.181.20.159': '60528',
        '108.181.32.169': '24652'
    }

    for file_path in file_paths:
        # 讀取檔案內容
        lines = read_file(file_path)

        # 更改指定的 IP 和 port
        for ip_address, new_port in replacements.items():
            lines = change_port(lines, ip_address, new_port)

        # 將修改後的內容寫入原檔案
        write_file(file_path, lines)
        print(f"已將新的內容寫入 {file_path}")

# 執行主函數
if __name__ == "__main__":
    main()
