

import tkinter as tik
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("Java Files", "*.java"), ("C# Files", "*.cs")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tik.END)
    with open(filepath,"r") as f:
        content = f.read()
        text_edit.insert(tik.END, content)
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("Java Files", "*.java"), ("C# Files", "*.cs")])


    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tik.END)
        f.write(content)
    window.title(f"Saved File: {filepath}")


def main():
    window = tik.Tk()
    window.title("FileReader")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tik.Text(window, font="Helvetica 20")
    text_edit.grid(row=0, column=1)

    frame = tik.Frame(window, relief=tik.RAISED, bd=2)
    save_button = tik.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tik.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=2.5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=2.5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()