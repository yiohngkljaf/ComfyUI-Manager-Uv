import re
import sys

def replace_pip_commands(file_path, new_command=('uv', 'pip')):
    # 将新命令转换为字符串，确保格式一致
    new_command_str = f'"{new_command[0]}" "{new_command[1]}"'
    
    # 定义正则表达式模式来匹配sys.executable, '-m', 'pip'及其变体
    patterns = [
        r'\bsys\.executable\s*,\s*"-?m"\s*,\s*"pip"',  # 匹配 "sys.executable, '-m', 'pip'" 和 ""sys.executable, "-m", "pip""
        r'\bsys\.executable\s*,\s*"-?s"\s*,\s*"-?m"\s*,\s*"pip"',  # 匹配 "sys.executable, '-s', '-m', 'pip'" 和 "sys.executable, "-s", "-m", "pip""
    ]
    
    # 组合所有模式到一个大的正则表达式中
    combined_pattern = '|'.join(f'({pattern})' for pattern in patterns)
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 使用正则表达式进行替换
        modified_content = re.sub(combined_pattern, new_command_str, content, flags=re.IGNORECASE)
        
        # 写入修改后的内容回文件
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)
        
        print(f"成功替换了 {file_path} 中的所有匹配项.")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

# 指定文件路径
#install_script_path = 'path/to/your/install_script.py'

# 调用函数执行替换
#replace_pip_commands(install_script_path)