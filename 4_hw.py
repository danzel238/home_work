class Rectangle:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height
    def square(self):
        print(f'Площадь прямоугольника равна {self.width * self.height}')
    def perimetr(self):
        print(f'Периметр прямоугольника равен {2 * (self.width + self.height)}')


rec1 = Rectangle(4,5)
rec2 = Rectangle(6,10)
rec3 = Rectangle(5,5)
rec1.square()
rec1.perimetr()
rec2.square()
rec2.perimetr()
rec3.square()
rec3.perimetr()

class Math:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b


    def division(self):
        return self.a / self.b

numbers1 = Math(6,3)
print( numbers1.addition(), numbers1.multiplication(), numbers1.division())


class SidebarButton:
    def __init__(self, text):
        self.text = text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {self.text}"


buttons = [
    SidebarButton("Text Box"),
    SidebarButton("Check Box"),
    SidebarButton("Radio Button"),
    SidebarButton("Web Tables"),
    SidebarButton("Buttons"),
    SidebarButton("Links"),
    SidebarButton("Broken Links - Images"),
    SidebarButton("Upload and Download"),
    SidebarButton("Dynamic Properties")
]


print("Тексты всех кнопок:")
for button in buttons:
    print(f"- {button.text} ({button.type})")

print("\n")


print("Результаты кликов:")
for button in buttons:
    print(button.click())
