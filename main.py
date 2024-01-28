import tkinter as tk
from tkinter import ttk


def calculate_orders():
    level = float(level_entry.get())
    stop_percent = float(stop_percent_entry.get()) / 100
    risk = float(risk_entry.get())
    position_type = position_type_var.get()

    stop = round_up_to_nearest_five(level * stop_percent)
    loft = stop * 0.20
    take_profit = stop * risk

    if position_type == 'шорт':
        entry_point = level - loft
        stop_loss_level = entry_point + stop
        take_profit_price = entry_point - take_profit
    else:
        entry_point = level + loft
        stop_loss_level = entry_point - stop
        take_profit_price = entry_point + take_profit

    result_text = (
        f"Тип позиции: {position_type}\n"
        f"ТВХ (Точка Входа): {entry_point:.2f}\n"
        f"Стоп: {stop:.2f}\n"
        f"Люфт: {loft:.2f}\n"
        f"Уровень Стоп-лосса: {stop_loss_level:.2f}\n"
        f"Тейк-профит: {take_profit:.2f}\n"
        f"Цена Тейк-профита: {take_profit_price:.2f}\n"
    )

    if position_type == 'шорт':
        orders = (
            "Ордера для шорт позиции:\n"
            f" - Limit Sell ордер на уровне {entry_point:.2f}\n"
            f" - Stop Loss Buy ордер на уровне {stop_loss_level:.2f}\n"
            f" - Take Profit Buy ордер на уровне {take_profit_price:.2f}"
        )
    else:
        orders = (
            "Ордера для лонг позиции:\n"
            f" - Limit Buy ордер на уровне {entry_point:.2f}\n"
            f" - Stop Loss Sell ордер на уровне {stop_loss_level:.2f}\n"
            f" - Take Profit Sell ордер на уровне {take_profit_price:.2f}"
        )

    result_label.config(text=result_text + "\n" + orders)


def round_up_to_nearest_five(n):
    return n if n % 5 == 0 else n + 5 - n % 5


# Создание основного окна
root = tk.Tk()
root.title("Расчет ордеров")

# Ввод уровня
level_label = ttk.Label(root, text="Уровень:")
level_label.pack()
level_entry = ttk.Entry(root)
level_entry.pack()

# Ввод процента стопа
stop_percent_label = ttk.Label(root, text="Процент стопа:")
stop_percent_label.pack()
stop_percent_entry = ttk.Entry(root)
stop_percent_entry.pack()

# Ввод риска
risk_label = ttk.Label(root, text="Риск:")
risk_label.pack()
risk_entry = ttk.Entry(root)
risk_entry.pack()

# Выбор типа позиции
position_type_var = tk.StringVar(value='шорт')
position_type_label = ttk.Label(root, text="Тип позиции:")
position_type_label.pack()
short_rb = ttk.Radiobutton(
    root, text="Шорт", variable=position_type_var, value='шорт')
long_rb = ttk.Radiobutton(
    root, text="Лонг", variable=position_type_var, value='лонг')
short_rb.pack()
long_rb.pack()

# Кнопка расчета
calculate_button = ttk.Button(
    root, text="Рассчитать", command=calculate_orders)
calculate_button.pack()

# Место для отображения результатов
result_label = ttk.Label(root, text="", justify='left')
result_label.pack()

# Запуск приложения
root.mainloop()
