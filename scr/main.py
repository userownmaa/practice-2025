import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

filepath = None


def open_file(window, text_edit):
    """
    @brief Открывает текстовый файл и загружает его содержимое в текстовое поле.

    @param window Главное окно приложения.
    @param text_edit Виджет Text для отображения содержимого файла.

    @details
    Вызывает диалоговое окно выбора файла, загружает выбранный текстовый файл,
    отображает его содержимое в text_edit и обновляет заголовок окна.
    """
    global filepath
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    """
    @brief Сохраняет содержимое текстового поля в текущий файл.

    @param window Главное окно приложения.
    @param text_edit Виджет Text, содержимое которого сохраняется.

    @details
    Если файл ещё не был сохранён ранее, вызывает save_as_file для выбора имени.
    """
    global filepath

    if not filepath:
        save_as_file(window, text_edit)
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def save_as_file(window, text_edit):
    """
    @brief Сохраняет содержимое текстового поля в новый файл.

    @param window Главное окно приложения.
    @param text_edit Виджет Text, содержимое которого сохраняется.

    @details
    Вызывает диалоговое окно для выбора пути сохранения файла.
    Сохраняет содержимое text_edit в указанный файл.
    """
    global filepath
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def new_file(window, text_edit):
    """
    @brief Создаёт новый пустой документ.

    @param window Главное окно приложения.
    @param text_edit Виджет Text, который очищается.

    @details
    Очищает содержимое text_edit и сбрасывает текущий путь к файлу.
    """
    global filepath
    filepath = None

    text_edit.delete(1.0, tk.END)
    window.title("Open File: Untitled")


def main():
    """
    @brief Основная функция запуска текстового редактора.

    @details
    Создаёт главное окно, инициализирует интерфейс: текстовое поле и кнопки управления
    (New, Open, Save, Save As). Также назначает горячие клавиши для этих действий.
    """
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Helvetica 18")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    save_as_button = tk.Button(frame, text="Save As", command=lambda: save_as_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))
    new_button = tk.Button(frame, text="New", command=lambda: new_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    save_as_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    new_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-Shift-S>", lambda x: save_as_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-n>", lambda x: new_file(window, text_edit))

    window.mainloop()


main()
