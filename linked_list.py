from typing import Optional


class Node:
    # Fila

    def __init__(self, number: int, color: str) -> None:
        self.number = number
        self.color = color
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.green_counter: int = 1  # Contador para cartões Verdes (V) (começa em 1)
        self.yellow_counter: int = 201  # Contador para cartões Amarelos (A) (começa em 201)

    def insert_without_priority(self, node: Node) -> None:
        # Adiciona o nó ao final da lista.
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_with_priority(self, node: Node) -> None:
        # Insere o nó depois de todos os nós 'A' mas antes de qualquer nó 'V'.
        if self.head is None:
            self.head = node
            return

        if self.head.color == "A":
            # Busca o último 'A' na lista
            current = self.head
            while current.next and current.next.color == "A":
                current = current.next

            # Insere após o último 'A' encontrado
            node.next = current.next
            current.next = node
        else:
            # Se a cabeça é 'V', insere o novo 'A' no início
            node.next = self.head
            self.head = node

    def insert(self) -> None:
        color = input("Enter card color (A/V): ").upper().strip()
        while color not in ["A", "V"]:
            color = input("Invalid color. Please enter A or V: ").upper().strip()

        if color == "V":
            num = self.green_counter
            self.green_counter += 1
        else:
            num = self.yellow_counter
            self.yellow_counter += 1

        new_node = Node(num, color)

        if self.head is None:
            self.head = new_node
        elif color == "V":
            self.insert_without_priority(new_node)
        elif color == "A":
            self.insert_with_priority(new_node)

        print(f"Patient [{color}, {num}] added to the queue.")

    def display_wait_list(self) -> None:
        if self.head is None:
            print("The waitlist is currently empty.")
            return

        current = self.head
        print("Queue -> ", end="")
        while current:
            print(f"[{current.color}, {current.number}]", end=" ")
            current = current.next
        print()

    def serve_patient(self) -> None:
        if self.head is None:
            print("No patients in queue to serve.")
            return

        removed_node = self.head
        self.head = self.head.next
        print(f"Calling patient with card color {removed_node.color} and number {removed_node.number} for service.")


def main_menu() -> None:
    queue = LinkedList()
    while True:
        print("\n1 – Add patient to queue")
        print("2 – Show patients in queue")
        print("3 – Call patient")
        print("4 – Exit")
        choice = input("Select an option: ")

        if choice == '1':
            queue.insert()
        elif choice == '2':
            queue.display_wait_list()
        elif choice == '3':
            queue.serve_patient()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
