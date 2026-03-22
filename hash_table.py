from typing import Optional


class Node:
    # Lista Encadeada

    def __init__(self, acronym: str, state_name: str) -> None:
        self.acronym = acronym
        self.state_name = state_name
        self.next = None


class HashTable:
    def __init__(self) -> None:
        # Inicializa a tabela com 10 posições definidas como None
        self.table: list[Optional[Node]] = [None] * 10

    @staticmethod
    def hash_function(acronym: str) -> int:
        # Retorna a posição do hash baseada em valores ASCII ou regras específicas
        if acronym == "DF":
            return 7

        # Soma dos valores ASCII das duas letras módulo 10
        position = (ord(acronym[0]) + ord(acronym[1])) % 10
        return position

    def insert(self, acronym: str, state_name: str) -> None:
        # Insere um novo estado no início da lista
        position = self.hash_function(acronym)
        new_node = Node(acronym, state_name)

        if self.table[position] is None:
            self.table[position] = new_node
        else:
            # Insere no início da cadeia (inserção na cabeça)
            new_node.next = self.table[position]
            self.table[position] = new_node

    def display(self) -> None:
        # Dá um print na Tabela Hash mostrando o encadeamento
        for i in range(10):
            print(f"{i}: ", end="")
            current = self.table[i]
            if current is None:
                print("None")
            else:
                while current:
                    print(f"{current.acronym}", end=" -> ")
                    current = current.next
                print("None")


def run_hash_system() -> None:
    hash_map = HashTable()

    print("Tabela HASH")
    hash_map.display()

    brazilian_states = [
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    ]

    for acronym, name in brazilian_states:
        hash_map.insert(acronym, name)

    print()
    print("Tabela HASH com os 27 estados brasileiros")
    hash_map.display()

    fictitious_name = "GABRIEL RIBEIRO"
    fictitious_acronym = "GR"
    hash_map.insert(fictitious_acronym, fictitious_name)

    print()
    print(f"Final Hash Table with Fictitious State ({fictitious_acronym})")
    hash_map.display()


if __name__ == "__main__":
    run_hash_system()
