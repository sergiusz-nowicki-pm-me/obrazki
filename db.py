import sqlite3

def print_table1():
    global con
    res = con.execute("select * from tabela1")
    row1 = res.fetchall()
    print(row1)

con = sqlite3.connect(":memory:")

con.execute("create table if not exists tabela1 (id, col1, col2, col3)")
con.execute("create table tabela2 (id, col1, col4, col5)")

con.execute("insert into tabela1 (col1, col2, col3) values ('test1_1', 'test1_2', 'test1_3')")
con.execute("insert into tabela1 (col1) values ('test2')")
# print_table1()

con.execute("insert into tabela2 (col1, col4, col5) values ('test1_1', 'test1_4', 'test1_5')")
con.execute("insert into tabela2 (col1, col4, col5) values ('test1_1', 'test1_4_2', 'test1_5_2')")
con.execute("insert into tabela2 (col1) values ('test4')")
# res = con.execute("""
#                   select * 
#                   from tabela1,
#                        tabela2
#                   where tabela1.col1 = tabela2.col1
#                         or tabela1.col1 = 'test2'
#                   """)
# print(res.fetchall())

con.execute("""create view test_view as select tabela1.col1, tabela2.col4 
                  from tabela1,
                       tabela2
                where tabela1.col1 = tabela2.col1""")

res = con.execute("select * from test_view")
print(res.fetchall())
# con.execute("update tabela1 set col2 = 'nowa wartosc' where col1 = 'test2'")
# print_table1()

# con.execute("delete from tabela1 where col1 = 'test2'")
# print_table1()

