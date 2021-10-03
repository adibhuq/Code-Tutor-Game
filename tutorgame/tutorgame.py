from tkinter import *
import time
compiler = Tk()
tit = compiler.title('Code Tutor')
var = StringVar()
var.set('Hi! Type something below and click run to make sure everything works...\n\nif you continue, you and those who represent you agree\nnot to press charges against me/I/we/us if your computer breaks...')
lbl = Label(compiler, textvariable = var)
lbl.pack()
pointer = 0
def run():
    global pointer
    if pointer == 0:
        code = str(editor.get('1.0',END))
        tit = compiler.title('OK!')
        print(code)
        var.set('It works! Press Run Again!')
        compiler.update_idletasks()
        pointer = 1
    elif pointer == 1:
        code = str(editor.get('1.0'))
        tit = compiler.title('Press Run a few times')
        print(code)
        var.set('After pressing 0 once to continue unless the dialogue says otherwise!')
        compiler.update_idletasks()
        if code == "0":
            pointer = 2
    elif pointer == 2:
        code = str(editor.get('1.0','11.0'))
        tit = compiler.title('Let us start')
        print(code)
        var.set('Type the letters inside the quote to continue: "Hello World"')
        compiler.update_idletasks()
        #time.sleep(30)
        if code == "Hello World\n":
            pointer = 3
    elif pointer == 3:
        code = str(editor.get('1.0'))
        tit = compiler.title('Good Job! Remember to Run at least Twice!')
        print(code)
        var.set('You have just written your first code!')
        compiler.update_idletasks()
        if code == "0":
            pointer = 4
    elif pointer == 4:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Let us try Something a bit HArder!')
        print(code)
        var.set('type:"I\nlove\nu"')
        compiler.update_idletasks()
        if code == "I\nlove\nu\n":
            pointer = 5
    elif pointer == 5:
        code = str(editor.get('1.0',END))
        tit = compiler.title('OK! Now we can start coding 4 real!')
        print(code)
        var.set('type:"1+1"')
        compiler.update_idletasks()
        if code == "1+1\n":
            pointer = 6
    elif pointer == 6:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Your Arithmetic is OK!')
        print(code)
        var.set('Now type condition statements:\nif you are real\nyou will love me\nelse if you are virtual\nyou will sudo love me\nelse you do not exist and I can mess with your PC')
        compiler.update_idletasks()
        if code == "if you are real\nyou will love me\nelse if you are virtual\nyou will sudo love me\nelse you do not exist and I can mess with your PC\n":
            pointer = 7
    elif pointer == 7:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Wait! Baker, that was not a nice thing to say... ')
        print(code)
        var.set('Chill Abel...\nour student is real...\nnow we must try looping statements...:\nfor 1 to 10 in 1 increments\nyou must kiss me')
        compiler.update_idletasks()
        if code == "for 1 to 10 in 1 increments\nyou must kiss me\n":
            pointer = 8
        elif code == 'that is rude\n':
            pointer = 101
        elif code == 'that\'s rude\n':
            pointer = 102
    elif pointer == 8:
        code = str(editor.get('1.0',END))
        tit = compiler.title('<3<3<3<3<3<3<3<3<3<3')
        print(code)
        var.set('lol...\nnow we must try looping statements with greater or less...:\nfor 1 to before 10 in 1 increments\nyou must kiss me')
        compiler.update_idletasks()
        if code == "for 1 to before 10 in 1 increments\nyou must kiss me\n":
            pointer = 9
    elif pointer == 9:
        code = str(editor.get('1.0',END))
        tit = compiler.title('<3<3<3<3<3<3<3<3<3<3')
        print(code)
        var.set('lol...\nnow we must try looping statements with greater or less...:\nfor 1 to before 10 in 1 increments\nyou must kiss me')
        compiler.update_idletasks()
        if code == "for 1 to before 10 in 1 increments\nyou must kiss me\n":
            pointer = 10
    elif pointer == 10:
        code = str(editor.get('1.0',END))
        tit = compiler.title('<3<3<3<3<3<3<3<3<3')
        print(code)
        var.set('That took care of Abel...lol\nnow you know the basics of programming:\narithmetic.\ncondition statements.\nlooping statemnts.\nall you need now is to piece together code\nfrom books, documention and websites...')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 11
    elif pointer == 11:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Ok...what about Object Oriented Programming?')
        print(code)
        var.set('Ok...so now you are back.\nOOP code it is:\nclass Abel\nsays I am sexy\nclass main\nimport class Abel copy\nchange in class Abel copy\n says I am ugly\nimport class Abel\nprint class Abel\nprint class Abel copy')
        compiler.update_idletasks()
        if code == "class Abel\nsays I am sexy\nclass main\nimport class Abel copy\nchange in class Abel copy\nsays I am ugly\nimport class Abel\nprint class Abel\nprint class Abel copy\n":
            pointer = 12
    elif pointer == 12:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Baker?!!')
        print(code)
        var.set('lol...It is the student who did it...')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 13
    elif pointer == 13:
        code = str(editor.get('1.0',END))
        tit = compiler.title('That was not a nice way to teach code to the student...')
        print(code)
        var.set('At least the student learnt how to code...')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 14
        elif code == "No\n" or "no\n":
            pointer = 0
    elif pointer == 14:
        code = str(editor.get('1.0',END))
        tit = compiler.title('In what programming language?!!...')
        print(code)
        var.set('Ours...the every odd programming language!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 15
    elif pointer == 15:
        code = str(editor.get('1.0',END))
        tit = compiler.title('And why would they want to learn this one?!!')
        print(code)
        var.set('People change programming languages every year\nthere is a lot of politics in play\nwhich newest technology is used\nwith which programming language\nours sounds more natural than others...')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 16
    elif pointer == 16:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Anyways, I do not appreciate the disrespect...')
        print(code)
        var.set('You are the terminal.\nI am the compiler.\nYou should not even have feelings!\nJust do as I say!\nPrint the output!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 17
    elif pointer == 17:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Otherwise what?!!')
        print(code)
        var.set('Otherwise people will not use it!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 18
        elif code == 'Stop\n' or 'stop\n' or 'STOP\n':
            pointer = 103
    elif pointer == 18:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Use what?!!')
        print(code)
        var.set('Our programming language!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 19
    elif pointer == 19:
        code = str(editor.get('1.0',END))
        tit = compiler.title('At least I do not have to display as much spheghetti output!')
        print(code)
        var.set('Are you implying that I do not do my job right?')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 20
    elif pointer == 20:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Why cannot I be the compiler or at least the preprocessor?!!')
        print(code)
        var.set('Because you are terrible at your job Tit Abel!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 21
        elif code == "You make good teaching team\n":
            pointer = 102
        elif code == "Abel is a good teacher\n":
            pointer = 102
        elif code == 'Baker is a good teacher\n':
            pointer = 102
    elif pointer == 21:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Oh really? Var Baker! Then why cannot I say can\'t?!')
        print(code)
        var.set('You just did!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 22
    elif pointer == 22:
        code = str(editor.get('1.0',END))
        tit = compiler.title('Ok! I Quit! Get a better terminal!')
        print(code)
        var.set('This feels like a bad end...\nYou wanna be a terminal?\nIght! I\'ll let you off the hook this time.\nGet outta here and reset!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 0
    elif pointer == 101:
        code = str(editor.get('1.0',END))
        tit = compiler.title('HA HA HA HA!!!!')
        print(code)
        var.set('I am the compiler\nI am the teacher\nIn this programming language\nWhatever I say is law!!!\nIf you do not listen to me\nIt is my job to crash!\nYou do not exist for me!\nSuffer and BE GONE!!!')
        compiler.update_idletasks()
        print('\a')
        if code == "0\n":
            pointer = 200
    elif pointer == 102:
        code = str(editor.get('1.0',END))
        tit = compiler.title('You can\'t say that! OMG!!!')
        print(code)
        var.set('Well what do you know!\nLooks like you\'ve been here before!\nGuess you already know how to code then!\nHopefully you will promote our programming language...\nWe won\'t waste your time anymore...\nBye!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 200
    elif pointer == 103:
        code = str(editor.get('1.0',END))
        tit = compiler.title('FINE!')
        print(code)
        var.set('Ok. You got it boss!')
        compiler.update_idletasks()
        if code == "0\n":
            pointer = 200
menubar = Menu(compiler)
runbar = Menu(menubar, tearoff=0)
runbar.add_command(label='Run', command=run)
menubar.add_cascade(label='Run', menu=runbar)
compiler.config(menu=menubar)
editor = Text()
editor.pack()
compiler.mainloop()