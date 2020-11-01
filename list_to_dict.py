# change two list into dictionary 

def list_to_dict(pl, jl):
    return dict(zip(pl, jl))

print(list_to_dict(["Annie", "Steven", "Lisa", "Osman"],["Teacher", "Engineer", "Doctor", "Cashier"]))