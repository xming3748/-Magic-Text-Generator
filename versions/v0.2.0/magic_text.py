# -*- coding: utf-8 -*-
"""
魔法文本生成器 (Magic Text Generator)
版本: 0.2.0 (测试版)
作者: Cove工作室 小铭xming制作，ppj的游柳 测试
版权: © 2025 小铭xming & Cove Studio. 保留所有权利。

更新记录:
v0.1.0 - 初始版本，基础功能实现
v0.2.0 - 修正RLO字符导致的文本顺序错误问题，优化隐藏效果

本工具采用【知识共享 署名-非商业性使用-相同方式共享 4.0 国际】协议开源
"""

import re

def make_magic_text(visible_part, hidden_part):
    """
    生成魔法文本
    visible_part: 前面显示的文本
    hidden_part: 后面隐藏的文本(注意: 由于RLO字符，此文本的顺序会反转)
    """
    control_chars = '\u2067\u2061\u2067\u2061\u2067'
    return f"{visible_part}{control_chars}{hidden_part}\u2067\u2061"

def clean_magic_text(magic_text):
    """清理魔法文本中的特殊控制字符"""
    return re.sub(r'[\u0000-\u001F\u007F-\u009F\u200B-\u200F\u202A-\u202E\u2060-\u206F]', '', magic_text)

def main():
    language = input("请选择语言 / Select language (zh/en): ").strip().lower()
    
    if language not in ['zh', 'en']:
        language = 'zh'
    
    messages = {
        'zh': {
            'welcome': "\n=== 魔法文本生成器 v0.2.0 ===",
            'visible_prompt': "请输入前面显示的文字: ",
            'hidden_prompt': "请输入后面隐藏的文字(注意顺序会反转): ",
            'result': "\n生成的魔法文本:",
            'copy_tip': "(请完整复制上方虚线内的所有内容)",
            'clean_prompt': "\n输入要清理的魔法文本 (直接回车跳过): ",
            'cleaned': "清理后的文本:",
            'warning': "\n注意: 请谨慎使用，不要用于恶意用途。"
        },
        'en': {
            'welcome': "\n=== Magic Text Generator v0.2.0 ===",
            'visible_prompt': "Enter text to show in front: ",
            'hidden_prompt': "Enter text to hide at the back (order will be reversed): ",
            'result': "\nGenerated magic text:",
            'copy_tip': "(Please copy ALL content above the dashes)",
            'clean_prompt': "\nEnter magic text to clean (press Enter to skip): ",
            'cleaned': "Cleaned text:",
            'warning': "\nWarning: Use carefully, do not use for malicious purposes."
        }
    }
    
    msg = messages[language]
    
    print(msg['welcome'])
    
    visible_text = input(msg['visible_prompt'])
    hidden_text = input(msg['hidden_prompt'])
    
    magic_result = make_magic_text(visible_text, hidden_text)
    
    print(msg['result'])
    print("-" * 40)
    print(magic_result)
    print("-" * 40)
    print(msg['copy_tip'])
    
    clean_input = input(msg['clean_prompt'])
    if clean_input.strip():
        cleaned = clean_magic_text(clean_input)
        print(f"{msg['cleaned']} {cleaned}")
    
    print(msg['warning'])

if __name__ == "__main__":
    main()