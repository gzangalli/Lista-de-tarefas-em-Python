import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    name = entry_name.get()
    description = entry_description.get()
    priority = entry_priority.get()
    category = entry_category.get()

    if name and description and priority and category:
        task = [name, description, priority, category]
        tasks.append(task)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        clear_entries()
        update_task_list()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

def delete_task():
    name = entry_name.get()

    for task in tasks:
        if task[0] == name:
            tasks.remove(task)
            messagebox.showinfo("Sucesso", "Tarefa removida com sucesso!")
            clear_entries()
            update_task_list()
            break

    else:
        messagebox.showerror("Erro", "Tarefa não encontrada.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_priority.delete(0, tk.END)
    entry_category.delete(0, tk.END)

def save_tasks_to_csv():
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
    messagebox.showinfo("Sucesso", "Tarefas salvas no arquivo tasks.csv.")

def load_tasks_from_csv():
    try:
        with open("tasks.csv", "r") as file:
            reader = csv.reader(file)
            tasks.extend(list(reader))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhum arquivo tasks.csv encontrado.")

def update_task_list():
    task_list.delete(0, tk.END)
    priority_filter = combobox_priority.get()

    for task in tasks:
        if priority_filter == "Todas" or task[2] == priority_filter:
            task_info = f"Nome: {task[0]:20} Descrição: {task[1]:20} Prioridade: {task[2]:10} Categoria: {task[3]:10}"
            task_list.insert(tk.END, task_info)

def on_priority_filter_changed(event):
    update_task_list()

tasks = []

window = tk.Tk()
window.title("Gerenciador de Tarefas")

# Labels
label_name = tk.Label(window, text="Nome:")
label_name.grid(row=0, column=0, sticky=tk.E)

label_description = tk.Label(window, text="Descrição:")
label_description.grid(row=1, column=0, sticky=tk.E)

label_priority = tk.Label(window, text="Prioridade:")
label_priority.grid(row=2, column=0, sticky=tk.E)

label_category = tk.Label(window, text="Categoria:")
label_category.grid(row=3, column=0, sticky=tk.E)

# Entry fields
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

entry_description = tk.Entry(window)
entry_description.grid(row=1, column=1)

entry_priority = tk.Entry(window)
entry_priority.grid(row=2, column=1)

entry_category = tk.Entry(window)
entry_category.grid(row=3, column=1)

# Buttons
button_add = tk.Button(window, text="Adicionar Tarefa", command=add_task)
button_add.grid(row=4, column=0, columnspan=2, pady=10)

button_delete = tk.Button(window, text="Excluir Tarefa", command=delete_task)
button_delete.grid(row=5, column=0, columnspan=2, pady=10)

button_save = tk.Button(window, text="Salvar Tarefas", command=save_tasks_to_csv)
button_save.grid(row=6, column=0, columnspan=2, pady=10)

# Priority Filter
priorities = ["Todas", "Baixa", "Media", "Alta"]
combobox_priority = ttk.Combobox(window, values=priorities, state="readonly")
combobox_priority.current(0)
combobox_priority.grid(row=7, column=0, pady=10)
combobox_priority.bind("<<ComboboxSelected>>", on_priority_filter_changed)

# Task List
task_list = tk.Listbox(window, width=80)
task_list.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky=tk.W+tk.E)

# Load tasks from CSV
load_tasks_from_csv()
update_task_list()

window.mainloop()
