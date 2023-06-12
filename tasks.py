import csv


def add_task(tasks):
    name = input("Qual o nome da tarefa: ")
    description = input("Qual a descrição da tarefa: ")
    priority = input("Qual a prioridade da tarefa: ")
    category = input("Qual a categoria da tarefa: ")

    task = [name, description, priority, category]
    tasks.append(task)
    print("Tarefa adicionada com sucesso")


def view_tasks(tasks):
    print("Lista de tarefas:")
    for task in tasks:
        print(
            f"Nome: {task[0]}, Descrição: {task[1]}, Prioridade: {task[2]}, Categoria: {task[3]}")


def save_tasks_to_csv(tasks):
    with open("tasks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(tasks)
    print("Atualizado o arquivo local tasks.csv.")


def load_tasks_from_csv():
    tasks = []
    try:
        with open("tasks.csv", "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)
    except FileNotFoundError:
        print("Não foram encontradas tarefas")
    return tasks


def delete_task(tasks):
    name = input("Digite o nome da tarefa que deseja excluir: ")
    found = False

    for task in tasks:
        if task[0] == name:
            tasks.remove(task)
            found = True
            print("Tarefa removida da lista de tarefas!")

    if not found:
        print("Tarefa não encontrada.")
    else:
        save_tasks_to_csv(tasks)
        # print("Tarefa removida do arquivo CSV.")


def main():
    tasks = load_tasks_from_csv()

    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Ver tarefas")
        print("3. Salvar tarefas no arquivo local")
        print("4. Excluir tarefa")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            save_tasks_to_csv(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Obrigado por utilizar nossa aplicação")
            break
        else:
            print("Escolha inválida. Escolha corretamente as opções acima.")


if __name__ == "__main__":
    main()
