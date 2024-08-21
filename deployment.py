from getpass import getpass
from subprocess import Popen, PIPE, STDOUT

SQL_SCRIPT = r'db/test.dump'


def main():
    if input('Full deployment [y/n]?') == 'y':
        with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
            p = Popen([r'python', '-m', 'venv', 'venv'], stdout=out, stderr=err)
        with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
            p = Popen([r'.\venv\Scripts\activate'], stdout=out, stderr=err)
        with open('test.log', 'wb') as out, open('test-error.log', 'wb') as err:
            p = Popen(['pip', 'install', '-r' 'markets_requirements.txt'], stdout=out, stderr=err)
        import psycopg2
        host = input('Please enter your host name: ')
        database = input('Please enter your database name: ')
        user = input('Please enter the username: ')
        password = getpass(f'Enter the password for the user [user]: ')
        port = input('Please enter your port number: ')
        try:
            conn = psycopg2.connect(
                host=host,
                database="postgres",
                user=user,
                password=password,
                port=port
            )
            conn.autocommit = True
            cur = conn.cursor()
            cur.execute(f"CREATE DATABASE {database};")
            print(f"Database {database} created successfully.")
            with open(SQL_SCRIPT, 'r') as file:
                cur.execute(file.read())
            print(f"Database initialized successfully from file: {SQL_SCRIPT}")
        except psycopg2.OperationalError as e:
            print(f"Error: {e}")
        finally:
            if conn:
                cur.close()
                conn.close()
        with open('main.py', 'r') as inp, open('main_deployed.py', 'w') as outp:
            for line in inp:
                line = line.replace("dbname='farmers_markets'", f"dbname={database}")\
                        .replace("host='localhost'", f"host={host}")\
                        .replace("user='marketsuser'", f"user={user}")\
                        .replace("password='Pa$$W0rd'", f"password={password}")\
                        .replace("port='5432'", f"port={port}")
                outp.write(line)
            with open('Utils.py', 'r') as inpp, open('utils_deployed.py', 'w') as outpp:
                for line in inpp:
                    line = line.replace("dbname='farmers_markets'", f"dbname={database}") \
                        .replace("host='localhost'", f"host={host}") \
                        .replace("user='marketsuser'", f"user={user}") \
                        .replace("password='Pa$$W0rd'", f"password={password}") \
                        .replace("port='5432'", f"port={port}")
                    outpp.write(line)


if __name__ == "__main__":
    main()
