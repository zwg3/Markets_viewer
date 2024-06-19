from getpass import getpass
from subprocess import Popen, PIPE, STDOUT

SQL_SCRIPT = r'db/test.dump'

if input('Full deployment [y/n]?') == 'y':
    with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
        p = Popen([r'python', '-m', 'venv', 'venv'], stdout=out, stderr=err)
    with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
        p = Popen([r'.\venv\Scripts\activate'], stdout=out, stderr=err)
    with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
        p = Popen(['pip', 'install', '-r' 'markets_requirements.txt'], stdout=out, stderr=err)
    print('hi')

    from psycopg2 import connect
    from psycopg2 import errors

    host = input('Please enter your host name: ')
    database = input('Please enter your database name: ')
    user = input('Please enter the username: ')
    password = getpass(f'Enter the password for the user [user]: ')
    port = input('Please enter your port number: ')

    with connect(
            dbname=database,
            host=host,
            user=user,
            password=password,
            port=port
    ) as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(f'CREATE DATABASE {database}')
            except Exception as err:
                print(err)
