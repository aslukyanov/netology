
import psycopg2
from pprint import pprint


#1 Функция, создающая структуру БД (таблицы)
def create_table() :
    with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
        with conn.cursor() as cur:
            cur.execute("""
            create table if not exists clients (
                id serial primary key,
                first_name varchar(100) not null,
                second_name varchar(100)
            );
            """)

            cur.execute("""
            create table if not exists emails (
                id serial primary key,
                client integer references clients(id),
                email varchar(100)
            );
            """)

            cur.execute("""
            create table if not exists phones (
                id serial primary key,
                client integer references clients(id),
                phone_number varchar(15) unique
            );
            """)

            conn.commit()
    print('success')


#2 Функция, позволяющая добавить нового клиента
def add_new_client(first_name : str, second_name : str) :
    with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
        with conn.cursor() as cur:
            cur.execute("""
            INSERT INTO clients(first_name, second_name) VALUES(%s, %s);
            """, (first_name, second_name))
            conn.commit()


def is_client_exist(first_name : str, second_name : str):
    with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
        with conn.cursor() as cur:
            cur.execute("""
            SELECT id from clients WHERE first_name=%s and second_name = %s;
            """, (first_name, second_name))
            result = cur.fetchone()
            if result is not None :
                return result[0]
            else :
                return False


def add_email(first_name : str, second_name : str, email : str) :
    client_id = is_client_exist(first_name, second_name)
    if client_id is not False :
        with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
            with conn.cursor() as cur:
                cur.execute("""
                insert into emails(client, email) values(%s, %s);
                """, (client_id, email))
                conn.commit()
    else :
        print(f"Error! Client {first_name} {second_name} does not exist")


#3 Функция, позволяющая добавить телефон для существующего клиента
def add_phone_number(first_name : str, second_name : str, phone_number : str) :
    client_id = is_client_exist(first_name, second_name)
    if client_id is not False :
        with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
            with conn.cursor() as cur:
                cur.execute("""
                insert into phones(client, phone_number) values(%s, %s);
                """, (client_id, phone_number))
                conn.commit()
    else :
        print(f"Error! Client {first_name} {second_name} does not exist")


#4 Функция, позволяющая изменить данные о клиенте
def modify_first_second_name(**kwargs) :
    """
    Keys must have previous first and last name - first_name, second_name
    Keys must have previous first and last name - new_first_name, new_second_name
    """
    if is_client_exist(kwargs['first_name'], kwargs['second_name']) is not False :
        with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
            with conn.cursor() as cur:
                cur.execute("""
                update clients set first_name = %s, second_name = %s where first_name = %s and second_name = %s;
                """, (kwargs['new_first_name'], kwargs['new_second_name'], kwargs['first_name'], kwargs['second_name']))
                conn.commit()
    else :
        print(f"client {kwargs['first_name']} {kwargs['second_name']} does not exist!!!")


#5 Функция, позволяющая удалить телефон для существующего клиента
def delete_phone_number(first_name : str, second_name : str, phone_number : str) :
    client_id = is_client_exist(first_name, second_name)
    if client_id is not False :
        with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
            with conn.cursor() as cur:
                cur.execute("""
                delete from phones where phone_number = %s and client = %s;
                """, (phone_number, client_id))
                conn.commit()
    else :
        print(f"Error! Client {first_name} {second_name} does not exist")


#6 Функция, позволяющая удалить существующего клиента
def delete_current_client(first_name : str, second_name : str) :
    client_id = is_client_exist(first_name, second_name)
    if client_id is not False :
        with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
            with conn.cursor() as cur:
                cur.execute("""
                delete from phones where client = %s;
                """, ([client_id]))
                # conn.commit()

                cur.execute("""
                delete from emails where client = %s;
                """, ([client_id]))

                cur.execute("""
                delete from clients where id = %s;
                """, ([client_id]))

                conn.commit()
    else :
        print(f"Error! Client {first_name} {second_name} does not exist")


#7 Функция, позволяющая найти клиента по его данным (имени, фамилии, email-у или телефону)
def search(**kwargs) :
    pattern = ""
    for key in kwargs :
        if kwargs.get(key) is not None :
            pattern += key + ' = ' + "\'" + kwargs.get(key) + "\'" + ' and '
    fin_pettern = pattern[:-4]
    # print(fin_pettern)

    with psycopg2.connect(database="postgres", user="andrey", password="qwerty", port = "5432", host="localhost") as conn :
        with conn.cursor() as cur:
            cur.execute(
            f'select c.first_name, c.second_name, e.email, p.phone_number from clients c ' \
            f'left join emails e on c.id = e.client ' \
            f'left join phones p on c.id = p.client ' \
            f'where {fin_pettern};'
            )
            result = cur.fetchall()
            # pprint(result)
    if len(result) > 0 :
        print("Serach result:\n")
        for i in result :
            print(
                f'First name is : {i[0]}  ' \
                f'Second name is : {i[1]}  ' \
                f'Email is : {i[2]}  ' \
                f'Phone number is : {i[3]}\n'
            )
    else :
        print("Not found")






if __name__ == '__main__' :
    #create_table()
    #add_new_client('Ivan', 'Ivanov')
    #add_new_client('Vasya', 'Vasiliev')
    #print(is_client_exist('Ivan', 'Ivanov'))
    #add_phone_number('Vasya', 'Vasiliev', '+711111111')
    #add_phone_number('Ivan', 'Ivanov', '+712345937')
    #add_phone_number('Ivan', 'Ivanov', '+112345937')
    #add_phone_number('Ivan', 'Seleznev', '+12345523')
    #delete_phone_number('Ivan', 'Ivanov', '+112345937')
    #modify_first_second_name(first_name = 'Ivan', second_name = 'Ivanov', new_first_name = 'Ivan', new_second_name = 'Petrov')
    #modify_first_second_name(first_name = 'Ivan', second_name = 'Petrov', new_first_name = 'Ivan', new_second_name = 'Ivanov')
    #delete_current_client('Ivan', 'Ivanov')

    #add_email('Ivan', 'Ivanov', 'example.com')
    #add_email('Ivan', 'Ivanov', 'example2mail.com')
    #add_email('Vasya', 'Vasiliev', 'test@rambler.ru')
    search(first_name='Ivan', second_name='Seleznev', phone_number='+12345523')




