from prettytable import PrettyTable
table = PrettyTable()
table.add_column("nama pokemon",["pikachu", "charmander","squirel"])
table.add_column("type",["petir", "api","air"])
table.align=("c")
print(table)
