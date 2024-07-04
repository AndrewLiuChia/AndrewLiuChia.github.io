# -*- coding: utf-8 -*-

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
def change_port(lines, old_ip_port, new_ip_port):
    new_lines = []
    for line in lines:
        if old_ip_port in line:
            new_line = line.replace(old_ip_port, new_ip_port)
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    return new_lines

# 主函數
def main():
    input_file_path = r'C:\Users\Andrew\Source\Repos\GithubPage\file\combine.txt'  # 原始檔案路徑

    # 定義需要替換的 IP 和端口
    replacements = {
        '108.181.20.159:55137': '108.181.20.159:12345',
        '108.181.32.169:34159': '108.181.32.169:54321'
    }

    # 讀取檔案內容
    lines = read_file(input_file_path)

    # 更改指定的 IP 和端口
    for old_ip_port, new_ip_port in replacements.items():
        lines = change_port(lines, old_ip_port, new_ip_port)

    # 將修改後的內容寫入原檔案
    write_file(input_file_path, lines)
    print(f"已將新的內容寫入 {input_file_path}")

# 執行主函數
if __name__ == "__main__":
    main()
