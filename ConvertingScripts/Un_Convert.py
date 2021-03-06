import re

def Convert(text, convert_dic, case = True, start_command = '', end_command = ''):
    if not isinstance(convert_dic, dict) and len(convert_dic) != 0: return
    
    def Convert_text(text):
        if case:
            for char in text:
                if char in convert_dic and convert_dic[char] != None and convert_dic[char] != '':
                    text = text.replace(char, convert_dic[char])
        else:
            for k, v in convert_dic.items():
                if v != None and v != '':
                    text = text.replace(v, k)
        return text
    
    if start_command != '' and end_command != '':
        commands_chars = '.[]{}*+?()^'
        re_start_command = start_command
        re_end_command = end_command
        for char in commands_chars:
            re_start_command = re_start_command.replace(char, '\\'+char)
            re_end_command = re_end_command.replace(char, '\\'+char)
        pattern = re_start_command + "(.*?)" + re_end_command
        text_list = re.split(pattern, text)
        
        for _ in range(len(text_list)):
            if _%2 == 1:
                text_list[_] = start_command + text_list[_] + end_command
            else:
                if text_list[_] != '':
                    text_list[_] = Convert_text(text_list[_])
        text = ''.join(text_list)
    else:
        text = Convert_text(text)

    return text