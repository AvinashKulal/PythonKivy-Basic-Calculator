
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty

class Manager(ScreenManager):
    pass

class Calc(Screen):
    textbox1 = ObjectProperty(None)
    textbox2 = ObjectProperty(None)
    #infix expression evaluation
    @staticmethod
    def evaluate(exp):
        oprStack = list()
        numStack = list()
        top = -1
        precedence = {'+': 1, '-': 1, '/': 2, '*': 2}
        for op in exp:
            if op in precedence:
                if top == -1:
                    oprStack.append(op)
                    top += 1
                else:
                    if precedence[oprStack[top]] < precedence[op]:
                        oprStack.append(op)
                    else:
                        op2, op1 = numStack.pop(), numStack.pop()
                        opr = oprStack.pop()
                        if opr == '+':
                            numStack.append(op1 + op2)
                        elif opr == '-':
                            numStack.append(op1 - op2)
                        elif opr == '*':
                            numStack.append(op1 * op2)
                        else:
                            numStack.append(op1 / op2)
                        oprStack.append(op)
            else:
                numStack.append(float(op))
        while oprStack:
            op2, op1 = numStack.pop(), numStack.pop()
            opr = oprStack.pop()
            if opr == '+':
                numStack.append(op1 + op2)
            elif opr == '-':
                numStack.append(op1 - op2)
            elif opr == '*':
                numStack.append(op1 * op2)
            else:
                numStack.append(op1 / op2)
        return ('%.2f' % numStack[0]) if int(numStack[0]) != numStack[0] else int(numStack[0])

    def doCalculation(self,infix):
        print(infix)
        try:
            answer  = str(self.evaluate(infix.split('#')))
        except:
            answer = 'Error..'
        finally:
            self.textbox2.text = answer

class MainApp(MDApp):

    def build(self):
        Window.size = 360,640
        self.theme_cls.theme_style='Dark'
        KV =  Builder.load_file('calculator.kv')
        sc = ScreenManager()
        cl = Calc()
        sc.add_widget(cl)
        return sc

MainApp().run()

