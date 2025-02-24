import tkinter as tk

root = tk.Tk()


def say_hello():
    print(
        '\n'.join
            ([
            ''.join
                ([
                (
                    'Love'[(x - y) % len('Love')]
                    if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' '
                ) for x in range(-30, 30)
            ])
            for y in range(30, -30, -1)
        ])
    )


root = tk.Tk()
root.title("小猫头鹰")
button = tk.Button(root, text="启动", command=say_hello)
button.pack(pady=20)

root.mainloop()
