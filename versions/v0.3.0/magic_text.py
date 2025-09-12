# -*- coding: utf-8 -*-
"""
魔法文本生成器 (Magic Text Generator)
版本: 0.3.0 (测试版)
作者: 小铭xming @ Cove Studio
协作者: ppjdeyouliu
版权: © 2025 小铭xming & Cove Studio. 保留所有权利。
许可证: 知识共享 署名-非商业性使用-相同方式共享 4.0 国际
"""

import re

def make_magic_text(visible_part, hidden_part):
    """
    生成魔法文本
    visible_part: 前面显示的文本
    hidden_part: 后面隐藏的文本(程序会自动处理显示顺序)
    """
    control_chars = '\u2067\u2061\u2067\u2061\u2067'
    return f"{visible_part}{control_chars}{hidden_part}\u2067\u2061"

def clean_magic_text(magic_text):
    """清理魔法文本中的特殊控制字符"""
    return re.sub(r'[\u0000-\u001F\u007F-\u009F\u200B-\u200F\u202A-\u202E\u2060-\u206F]', '', magic_text)

def validate_nickname(nickname):
    """验证昵称是否包含危险字符"""
    if len(nickname) > 20:
        return False, "昵称过长（最多20个字符）"
    
    dangerous_chars = ['@', '#', '$', '%', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '?', '/']
    for char in dangerous_chars:
        if char in nickname:
            return False, f"昵称包含不安全字符: {char}"
    
    return True, ""

def generate_suggestions(visible_text):
    """生成常用的隐藏文本建议"""
    suggestions = {
        'zh': ['喵~', '哟~', '哈哈', '嘻嘻', '嘿嘿', '哦豁', '哇塞'],
        'en': ['~meow', '~hey', '~lol', '~haha', '~wow', '~nice', '~cool']
    }
    return suggestions

def display_copyright(language):
    """显示版权信息"""
    if language == 'zh':
        print("\n" + "="*50)
        print("魔法文本生成器 v0.3.0")
        print("作者: 小铭xming @ Cove Studio")
        print("协作者: ppjdeyouliu")
        print("© 2025 小铭xming & Cove Studio. 保留所有权利。")
        print("="*50)
        print("更新日志:")
        print("v0.1.0 - 初始版本，基础功能实现")
        print("v0.2.0 - 修正RLO字符导致的文本顺序错误")
        print("v0.3.0 - 添加昵称验证、建议功能和更好的提示")
        print("="*50 + "\n")
    else:
        print("\n" + "="*50)
        print("Magic Text Generator v0.3.0")
        print("Author: xming @ Cove Studio")
        print("Collaborator: ppjdeyouliu")
        print("© 2025 xming & Cove Studio. All rights reserved.")
        print("="*50)
        print("Changelog:")
        print("v0.1.0 - Initial version with basic functionality")
        print("v0.2.0 - Fixed text order issue with RLO characters")
        print("v0.3.0 - Added nickname validation, suggestions and better prompts")
        print("="*50 + "\n")

def main():
    language = input("请选择语言 / Select language (zh/en): ").strip().lower()
    
    if language not in ['zh', 'en']:
        language = 'zh'
    
    # 显示版权信息
    display_copyright(language)
    
    messages = {
        'zh': {
            'welcome': "=== 魔法文本生成器 ===",
            'visible_prompt': "请输入前面显示的文字（如昵称）: ",
            'hidden_prompt': "请输入后面隐藏的文字（程序会自动处理）: ",
            'suggestions': "常用建议: ",
            'result': "生成的魔法文本:",
            'copy_tip': "(请完整复制上方虚线内的所有内容)",
            'clean_prompt': "输入要清理的魔法文本 (直接回车跳过): ",
            'cleaned': "清理后的文本:",
            'warning': "注意: 请谨慎使用，不要用于恶意用途。",
            'font_warning': "提醒: 在QQ中使用特殊字体可能会导致显示效果异常",
            'platform_warning': "注意: 微信等平台可能不支持此类特殊字符，使用前请先测试",
            'risk_warning': "免责声明: 使用此工具产生的任何后果由用户自行承担，作者不负责因使用本工具导致的账号封禁等问题",
            'nickname_error': "昵称验证失败: ",
            'retry': "请重新输入: "
        },
        'en': {
            'welcome': "=== Magic Text Generator ===",
            'visible_prompt': "Enter text to show in front (e.g. nickname): ",
            'hidden_prompt': "Enter text to hide at the back (auto-processed): ",
            'suggestions': "Common suggestions: ",
            'result': "Generated magic text:",
            'copy_tip': "(Please copy ALL content above the dashes)",
            'clean_prompt': "Enter magic text to clean (press Enter to skip): ",
            'cleaned': "Cleaned text:",
            'warning': "Warning: Use carefully, do not use for malicious purposes.",
            'font_warning': "Note: Using special fonts in QQ may cause abnormal display effects",
            'platform_warning': "Note: Platforms like WeChat may not support such special characters, please test first",
            'risk_warning': "Disclaimer: Users are solely responsible for any consequences of using this tool. The author is not responsible for account bans or other issues caused by using this tool",
            'nickname_error': "Nickname validation failed: ",
            'retry': "Please re-enter: "
        }
    }
    
    msg = messages[language]
    
    print(msg['welcome'])
    
    # 输入前面显示的文字
    while True:
        visible_text = input(msg['visible_prompt'])
        is_valid, error_msg = validate_nickname(visible_text)
        if is_valid:
            break
        else:
            print(f"{msg['nickname_error']}{error_msg}")
            print(msg['retry'])
    
    # 显示建议
    suggestions = generate_suggestions(language)
    print(f"{msg['suggestions']}{', '.join(suggestions[language])}")
    
    # 输入后面隐藏的文字
    hidden_text = input(msg['hidden_prompt'])
    
    magic_result = make_magic_text(visible_text, hidden_text)
    
    print(msg['result'])
    print("-" * 40)
    print(magic_result)
    print("-" * 40)
    print(msg['copy_tip'])
    
    # 平台兼容性警告
    print(f"\n{msg['platform_warning']}")
    
    # 字体警告
    print(f"{msg['font_warning']}")
    
    # 风险警告
    print(f"\n{msg['risk_warning']}")
    
    clean_input = input(f"\n{msg['clean_prompt']}")
    if clean_input.strip():
        cleaned = clean_magic_text(clean_input)
        print(f"{msg['cleaned']} {cleaned}")
    
    print(f"\n{msg['warning']}")

if __name__ == "__main__":
    main()