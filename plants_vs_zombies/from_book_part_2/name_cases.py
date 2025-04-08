message="Hi,Shan,would you like to learn some python today?"
print(message)

#：个性化消息 ⽤变量表⽰⼀个⼈的名字，并向其显⽰⼀条消息。显⽰的消息应⾮常简单，如下所⽰。
#Hello Eric, would you like to learn some Python today?
name='eric'
msp=f'Hello {name.title()},would you like to learn some Python today?'
print(msp)


#用变量表示一个人的名字，再分别以全小写、全大写和首字母大写的方式显示这个人名

name='alice'
print(name.upper())
print(name.lower())
print(name.title())

#找到你钦佩的名人说的一句名言，将这个名人的姓名和名言打印出来。输出应类似于下面这样（包括引号）。
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')

#⽤变量famous_person 表⽰名⼈的姓名，再创建要显⽰的消息并将其赋给变量message，然后打印这条消息

famous_person = 'Albert Einstein'
message = ' \"A person who never made a mistake never tried anything new.\"'
print(famous_person+message)

message=f'{famous_person} once said,"A person who never made a mistake never tried anything new."'
print(message)

#⽤变量表⽰⼀个⼈的名字，并在其开头和末尾都包含⼀些空⽩字符。务必⾄少使⽤字符组合"\t" 和"\n" 各⼀次。
# 打印这个⼈名，显⽰其开头和末尾的空⽩。然后，分别使⽤函数lstrip()、rstrip() 和strip() 对⼈名进⾏处理
# 并将结果打印出来

person=' \tEric\n  '
print(person)
print((person.lstrip()).rstrip())
print(person.strip())

#Python提供了removesuffix() ⽅法，其⼯作原理与removeprefix() 很像。请将值'python_notes.txt'
# 赋给变量filename,再使⽤removesuffix() ⽅法来显⽰不包含扩展名的⽂件名，就像⽂件浏览器所做的那样。

filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')
print(simple_filename)