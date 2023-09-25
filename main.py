import sqlite3


def task_f(number):
    sql_path = f'SQLs/query_{number}.sql'
    with open(sql_path, 'r') as f:
        sql = f.read()

    db_name = f't{number}.db'
    with sqlite3.connect('university_data.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()
    


def main_function():
    while True:
        inp = input('Which task(number 1-12)? >>> ')

        if inp in ['exit', 'close']:
            print('\nGood bye!')
            break

        try:
            if int(inp) in range(1, 12+1):

                print(task_f(int(inp)))
        
            else:
                print('\nThere are just 12 tasks!!!\n')
        except ValueError:
            print('\nIt has to be a number(1-12)!!!\n')


if __name__ == '__main__':
    main_function()