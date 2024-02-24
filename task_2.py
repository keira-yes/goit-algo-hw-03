import turtle

def koch_snowflake(t, order, size):
    """
    Малювання сніжинки Коха за допомогою рекурсії.

    :param t: Об'єкт черепахи для малювання
    :param order: Порядок сніжинки Коха (глибина рекурсії)
    :param size: Довжина сторони початкового трикутника
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def get_order():
    """
    Отримання рівня рекурсії від користувача
    """
    order = turtle.numinput("Рівень рекурсії", "Введіть рівень рекурсії (ціле число більше або дорівнює 0): ", minval=0)
    return int(order) if order is not None else None

def draw_koch_snowflake(size = 300):
    order = get_order()

    # Ініціалізація черепахи
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    # Позиціонування черепахи
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    # Малюємо сніжинку Коха
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
    screen.mainloop()

if __name__ == "__main__":
    draw_koch_snowflake()