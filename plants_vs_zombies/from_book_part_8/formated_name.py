def format_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"
#capitalize()方法用于将字符串的第一个字母转为大写，并将其余字母转为小写。
#与title()方法类似，但title()方法将所有单词的首字母都转为大写，而capitalize()方法只对第一个字母进行操作。first_name = "jOhN"

first_name = "jOhN"
print(first_name.capitalize())  # 输出: John
print(first_name.title())  # 输出: John

first_name = "jOhN doe"
print(first_name.capitalize())  # 输出: John Doe
print(first_name.title())  # 输出: John

sentence = "this is a test sentence"
print(sentence.title())  # 输出: This Is A Test Sentence

print(format_name("john", "doe"))  # Output: John Doe
