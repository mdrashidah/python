def table_gen(n):
    table =""
# "" means empty string to generate table in empty space
    for i in range (1, 11):
        table += f"{n} x {i} = {n*i}\n"
    
    # += represent new line for the table
    with open (f"tables/table.txt_{n}", "w") as f:
        f.write(table)
    return table

for n in range(2, 21):
    table_gen(n)