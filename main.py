from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


class RuffierTest:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.heartbeat1 = 0
        self.heartbeat2 = 0
        self.heartbeat3 = 0

    def result(self):
        result = (self.heartbeat1 + self.heartbeat2 + self.heartbeat3 - 200)/10
        if result < 0:
            result = 0
        if self.age >= 15:
            if result == 0:
                return 'Great'
            elif 0.5 <= result <= 5:
                return 'Good'
            elif 6 <= result <= 10:
                return 'Satisfactorily'
            elif 11 <= result <= 15:
                return 'Weak'
            elif result >= 15:
                return 'Bad'
        elif 13 <= self.age <= 14:
            if result == 1.5:
                return 'Great'
            elif 2 <= result <= 6.5:
                return 'Good'
            elif 7.5 <= result <= 11.5:
                return 'Satisfactorily'
            elif 12.5 <= result <= 16.5:
                return 'Weak'
            elif result >= 16.5:
                return 'Bad'
        elif 11 <= self.age <= 12:
            if result == 3:
                return 'Great'
            elif 3.5 <= result <= 8:
                return 'Good'
            elif 9 <= result <= 13:
                return 'Satisfactorily'
            elif 14 <= result <= 18:
                return 'Weak'
            elif result >= 18:
                return 'Bad'
        elif 9 <= self.age <= 10:
            if result == 4.5:
                return 'Great'
            elif 5 <= result <= 9.5:
                return 'Good'
            elif 10.5 <= result <= 14.5:
                return 'Satisfactorily'
            elif 15.5 <= result <= 19.5:
                return 'Weak'
            elif result >= 19.5:
                return 'Bad'
        elif self.age <= 8:
            if result == 6:
                return 'Great'
            elif 6.5 <= result <= 11:
                return 'Good'
            elif 12 <= result <= 16:
                return 'Satisfactorily'
            elif 17 <= result <= 21:
                return 'Weak'
            elif result >= 21:
                return 'Bad'





screen_manager = ScreenManager()
ruffier_test = RuffierTest()


class NextButton(Button):
    def __init__(self, **kwargs):
        if 'target' in kwargs:
            self.target = kwargs['target']
            del kwargs['target']
        else:
            self.target = None

        if 'direction' in kwargs:
            self.direction = kwargs['direction']
            del kwargs['direction']
        else:
            self.direction = 'right'

        if 'function' in kwargs:
            self.function = kwargs['function']
            del kwargs['function']
        else:
            self.function = None

        super().__init__(**kwargs)

    def on_press(self):
        status = True
        if self.function is not None:
            status = self.function()
        if 'target' is None or not status:
            return
        screen_manager.transition.direction = self.direction
        screen_manager.current = self.target




class Screen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        layout = BoxLayout(orientation='horizontal')
        txt = Label(text='hello. This is a ruffier test. To start the test,\n enter your name and age')
        txt2 = Label(text='During the test, use heart rate values during different\n periods of recovery after relatively small loads.')
        self.txt_input = TextInput(hint_text='Enter name')
        self.txt_input2 = TextInput(hint_text='Enter age')
        btn = NextButton(text='further', target='screen2', direction='left', function=self.get_name_and_age)

        root.add_widget(txt)
        root.add_widget(txt2)
        root.add_widget(layout)
        layout.add_widget(self.txt_input)
        layout.add_widget(self.txt_input2)
        root.add_widget(btn)

        self.add_widget(root)

    def get_name_and_age(self):
        name = self.txt_input.text
        ruffier_test.name = name
        age = self.txt_input2.text
        age = age.replace(' ', '')
        age = age.replace('\n', '')
        if age.isdigit():
            ruffier_test.age = int(age)
            self.txt_input.text = ''
            self.txt_input2.text = ''
            return True
        return False

class Screen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        txt = Label(text='Sit in a relaxed position\n and measure your heart rate for 15 seconds.')
        self.txt_input = TextInput(hint_text='enter heartbeat')
        btn = NextButton(text='further', target='screen3', direction='left', function=self.get_heartbeat1)

        layout = BoxLayout()

        root.add_widget(txt)
        root.add_widget(self.txt_input)
        root.add_widget(btn)

        self.add_widget(root)

    def get_heartbeat1(self):
        heartbeat1 = self.txt_input.text
        heartbeat1 = heartbeat1.replace(' ', '')
        heartbeat1 = heartbeat1.replace('\n', '')
        if heartbeat1.isdigit():
            ruffier_test.heartbeat1 = int(heartbeat1)
            self.txt_input.text = ''
            return True
        return False



class Screen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        txt2 = Label(text='Do 30 squats within 45 seconds.')
        self.txt_input = TextInput(hint_text='enter heartbeat')
        btn = NextButton(text='further', target='screen4', direction='left', function=self.get_heartbeat2)

        layout = BoxLayout()

        root.add_widget(txt2)
        root.add_widget(self.txt_input)
        root.add_widget(btn)

        self.add_widget(root)

    def get_heartbeat2(self):
        heartbeat2 = self.txt_input.text
        heartbeat2 = heartbeat2.replace(' ', '')
        heartbeat2 = heartbeat2.replace('\n', '')
        if heartbeat2.isdigit():
            ruffier_test.heartbeat2 = int(heartbeat2)
            self.txt_input.text = ''
            return True
        return False


class Screen4(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        txt = Label(text='Immediately after finishing the squats, measure your heart rate for 15 seconds.\n Repeat the measurement 1 minute after the exercise.')
        self.txt_input = TextInput(hint_text='enter heartbeat')
        btn = NextButton(text='further', target='screen5', direction='left', function=self.get_heartbeat3)

        layout = BoxLayout()

        root.add_widget(txt)
        root.add_widget(self.txt_input)
        root.add_widget(btn)

        self.add_widget(root)

    def get_heartbeat3(self):
        heartbeat3 = self.txt_input.text
        heartbeat3 = heartbeat3.replace(' ', '')
        heartbeat3 = heartbeat3.replace('\n', '')
        if heartbeat3.isdigit():
            ruffier_test.heartbeat3 = int(heartbeat3)
            self.txt_input.text = ''
            return True
        return False


class Screen5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        root = BoxLayout(orientation='vertical')
        txt1 = Label(text='Thank you for taking the test!\n Click to calculate your results.')
        self.txt2 = Label(text='results')
        btn1 = NextButton(text='calculate results', function=self.result)
        btn2 = NextButton(text='again', target='screen1', direction='right', function=self.again)

        layout = BoxLayout()

        root.add_widget(txt1)
        root.add_widget(self.txt2)
        root.add_widget(btn1)
        root.add_widget(btn2)

        self.add_widget(root)

    def result(self):
        grade = ruffier_test.result()
        self.txt2.text = str(grade)

    def again(self):
        self.txt2.text = ''
        return True



class MyApp(App):
    def build(self):
        global screen_manager
        sm = ScreenManager()
        screen_manager = sm
        sm.add_widget(Screen1(name='screen1'))
        sm.add_widget(Screen2(name='screen2'))
        sm.add_widget(Screen3(name='screen3'))
        sm.add_widget(Screen4(name='screen4'))
        sm.add_widget(Screen5(name='screen5'))
        self.title = 'Ruffier Test'
        return sm


MyApp().run()
