# Magic Text Generator / 魔法文本生成器 - 全功能正式版
# Version: V1.0.0
# Author: Cove Studio - Created by xming, tested by ppjdeyouliu
# Copyright: © 2025 xming & Cove Studio. All rights reserved.

import re

def make_magic_text(visible_part, hidden_part):
    """
    生成魔法文本
    """
    control_chars = '\u2067\u2061\u2067\u2061\u2067'
    return f"{visible_part}{control_chars}{hidden_part}\u2067\u2061"

def clean_magic_text(magic_text):
    """
    清理魔法文本中的特殊控制字符
    """
    return re.sub(r'[\u0000-\u001F\u007F-\u009F\u200B-\u200F\u202A-\u202E\u2060-\u206F]', '', magic_text)

def validate_input(text):
    """
    增强的输入验证
    """
    if len(text) > 50:
        return False, "输入过长（最多50个字符）"
    
    dangerous_patterns = ['<script>', 'javascript:', 'onload=']
    for pattern in dangerous_patterns:
        if pattern in text.lower():
            return False, f"检测到不安全内容: {pattern}"
    
    return True, ""

def display_warning():
    """
    显示完整的警告信息
    """
    print("\n" + "="*60)
    print("⚠️  重要安全警告 / Important Security Warning")
    print("="*60)
    print("• 本工具仅供娱乐和学习使用")
    print("• 请勿用于恶意或欺诈用途")
    print("• 生成的文本可能在某些平台无法正常显示")
    print("• 使用特殊字体可能导致效果异常")
    print("• 您需对使用后果自行承担责任")
    print("• This tool is for entertainment and learning only")
    print("• Do not use for malicious or fraudulent purposes")
    print("="*60)

def display_main_menu():
    """
    显示主菜单
    """
    print("\n" + "="*40)
    print("🎩 Magic Text Generator V1.0.0")
    print("🎩 魔法文本生成器 V1.0.0")
    print("="*40)
    print("请选择操作 / Please select an operation:")
    print("1. 🚀 生成魔法文本 / Generate Magic Text")
    print("2. 🧹 清理魔法文本 / Clean Magic Text")
    print("3. 📖 查看使用说明 / View Instructions")
    print("4. ⚠️ 查看免责声明 / View Disclaimer")
    print("5. 🏃 退出程序 / Exit Program")
    print("="*40)

def display_instructions():
    """
    显示使用说明
    """
    print("\n" + "="*50)
    print("📖 使用说明 / Instructions")
    print("="*50)
    print("• 前面显示的文字：在聊天中正常显示的内容")
    print("• 后面隐藏的文字：会被特殊处理后显示的内容")
    print("• 程序会自动处理文本顺序，您只需正常输入")
    print("• Front text: Normally displayed content in chat")
    print("• Hidden text: Content that will be specially processed")
    print("• The program automatically handles text order")
    print("="*50)

def display_disclaimer():
    """
    显示免责声明
    """
    print("\n" + "="*50)
    print("📄 免责声明 / Disclaimer")
    print("="*50)
    print("• 本工具仅为技术研究和学习交流提供")
    print("• 使用者需对使用后果自行承担全部责任")
    print("• 作者不对任何直接或间接后果负责")
    print("• This tool is provided for technical research only")
    print("• Users are solely responsible for consequences")
    print("• Author is not liable for any direct/indirect effects")
    print("="*50)

def generate_text_flow():
    """
    生成文本的完整流程
    """
    print("\n" + "🚀 生成魔法文本模式 / Generate Magic Text Mode")
    print("-" * 40)
    
    # 输入前面显示的文字
    while True:
        visible_text = input("请输入前面显示的文字 / Enter front text: ")
        is_valid, error_msg = validate_input(visible_text)
        if is_valid:
            break
        else:
            print(f"❌ 输入无效: {error_msg}")
            print("请重新输入 / Please re-enter")
    
    # 输入后面隐藏的文字
    while True:
        hidden_text = input("请输入后面隐藏的文字 / Enter hidden text: ")
        is_valid, error_msg = validate_input(hidden_text)
        if is_valid:
            break
        else:
            print(f"❌ 输入无效: {error_msg}")
            print("请重新输入 / Please re-enter")
    
    # 生成并显示结果
    result = make_magic_text(visible_text, hidden_text)
    
    print("\n" + "✅ 生成成功！ / Generated successfully!")
    print("📋 生成的文本 / Generated text:")
    print("-" * 50)
    print(result)
    print("-" * 50)
    print("💡 提示：请完整复制上方所有内容使用")
    print("💡 Tip: Please copy ALL content above for use")
    
    input("\n按回车键继续... / Press Enter to continue...")

def clean_text_flow():
    """
    清理文本的完整流程
    """
    print("\n" + "🧹 清理魔法文本模式 / Clean Magic Text Mode")
    print("-" * 40)
    
    magic_text = input("请输入要清理的魔法文本 / Enter magic text to clean: ")
    cleaned_text = clean_magic_text(magic_text)
    
    print("\n" + "✅ 清理完成！ / Cleanup completed!")
    print("📋 清理后的文本 / Cleaned text:")
    print("-" * 40)
    print(cleaned_text)
    print("-" * 40)
    
    input("\n按回车键继续... / Press Enter to continue...")

def main():
    """
    主程序
    """
    # 显示安全警告
    display_warning()
    
    # 主循环
    while True:
        display_main_menu()
        
        try:
            choice = input("\n请输入选择 (1-5) / Please enter choice (1-5): ").strip()
            
            if choice == '1':
                generate_text_flow()
            elif choice == '2':
                clean_text_flow()
            elif choice == '3':
                display_instructions()
                input("\n按回车键继续... / Press Enter to continue...")
            elif choice == '4':
                display_disclaimer()
                input("\n按回车键继续... / Press Enter to continue...")
            elif choice == '5':
                print("\n👋 感谢使用！再见！ / Thank you for using! Goodbye!")
                print("📧 如有问题请联系: Cove Studio")
                break
            else:
                print("❌ 无效选择，请输入 1-5 之间的数字")
                print("❌ Invalid choice, please enter a number between 1-5")
                input("\n按回车键继续... / Press Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\n👋 程序被用户中断。再见！ / Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ 发生错误: {e}")
            print("❌ An error occurred")
            input("\n按回车键继续... / Press Enter to continue...")

if __name__ == "__main__":
    main()