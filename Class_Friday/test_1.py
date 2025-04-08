while True:
    try:
        score = eval(input('请输入你的成绩:'))
        if score<0:
            print('你输入的成绩非法!')
        elif score<=60:
            print('You failed the exam!')
        elif score <=70:
            print('You got D!')
        elif score<=80:
            print('You gou C!')
        elif score<=90:
            print('You got B!')
        elif score<=100:
            print('You got A!')
        elif score>100:
            print('你输入的成绩非法!')
    except ValueError:
        print('请重新输入数字!')

