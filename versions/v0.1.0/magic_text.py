import sys
import re

def make_magic_text(visible_part, hidden_part):
    control_chars = '\u2067\u2061\u2067\u2061\u2067'
    return f"{visible_part}{control_chars}{hidden_part}\u2067\u2061"

def clean_magic_text(magic_text):
    return re.sub(r'[\u0000-\u001F\u007F-\u009F\u200B-\u200F\u202A-\u202E\u2060-\u206F]', '', magic_text)

def main():
    language = input("请选择语言 / Select language (zh/en): ").strip().lower()
    
    if language not in ['zh', 'en']:
        language = 'zh'
    
    messages = {
        'zh': {
            'welcome': "\n=== 魔法文本生成器 ===",
            'visible_prompt': "请输入前面显示的文字: ",
            'hidden_prompt': "请输入后面隐藏的文字(注意顺序会反转，如要显示'~