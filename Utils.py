import math
import geocoder
import psycopg2
# from main import conn

EARTH_RADIUS_MI = 3959.191

conn = psycopg2.connect(dbname='farmers_markets',
                        host='localhost',
                        user='marketsuser',
                        password='Pa$$W0rd',
                        port='5432')


def do_select():
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM markets;""")
    res = cursor.fetchall()
    return res


def do_select_full_data(name):
    cursor = conn.cursor()
    cursor.execute("""SELECT markets.market_name, string_agg(categories.category, ', ' ORDER BY categories.category) 
                            AS produce,markets.street, cities.city, states.state_full, markets.zip,markets.lat, markets.lon
                            FROM markets_categories
                            INNER JOIN markets ON markets_categories.market_id = markets.market_id
                            INNER JOIN categories ON markets_categories.category_id = categories.category_id
                            INNER JOIN cities ON markets.city = cities.city_id
                            INNER JOIN states ON markets.state = states.state_id 
                            WHERE markets.market_name = %(name)s
                            GROUP BY markets.market_name, markets.street, cities.city, states.state_full, markets.zip,
                            markets.lat, markets.lon""", {'name': name})

    res = cursor.fetchall()
    return res


def do_select_by_city(city_name):
    cursor = conn.cursor()
    cursor.execute("""SELECT markets.market_name, markets.street, cities.city, states.state_full, markets.zip
                      FROM markets
                      INNER JOIN cities ON markets.city = cities.city_id
                      INNER JOIN states ON markets.state = states.state_id
                      WHERE cities.city = %(city_name)s""", {'city_name': city_name})
    res = cursor.fetchall()
    return res


def do_select_by_state(state_name):
    cursor = conn.cursor()
    cursor.execute("""SELECT markets.market_name, markets.street, cities.city, states.state_full, markets.zip
                      FROM markets
                      INNER JOIN cities ON markets.city = cities.city_id
                      INNER JOIN states ON markets.state = states.state_id
                      WHERE states.state_full = %(state_name)s""", {'state_name': state_name})
    res = cursor.fetchall()
    return res


def do_select_by_zip(zip):
    cursor = conn.cursor()
    cursor.execute("""SELECT markets.market_name, markets.street, cities.city, states.state_full, markets.zip
                      FROM markets
                      INNER JOIN cities ON markets.city = cities.city_id
                      INNER JOIN states ON markets.state = states.state_id
                      WHERE markets.zip = %(zip)s""", {'zip': zip})
    res = cursor.fetchall()
    return res


def log_user(user_data):
    with open('user_log.txt', 'w') as file:
        file.write(user_data)


def fetch_all_markets(order_param='reviews.score'):
    cursor = conn.cursor()
    cursor.execute(f'SELECT markets.market_name, street, cities.city, states.state_full, markets.zip, reviews.score '
                   f'FROM markets '
                   f'INNER JOIN cities ON markets.city = cities.city_id '
                   f'LEFT JOIN reviews ON markets.market_id = reviews.market_id '
                   f'INNER JOIN states ON markets.state = states.state_id '
                   f'ORDER BY {order_param};')

    raw = list(cursor.fetchall())
    res = []
    for i in raw:
        res.append(format_pretty_markets(i))
    elements_on_page = 30
    res = [(res[x:y]) for (x, y) in [(x, x + elements_on_page) for x in range(0, len(res), elements_on_page)]]
    return res


def get_my_coords():
    return geocoder.ip('me').latlng


def calc_distance(loc1, loc2):
    lon1 = math.radians(loc1[1])
    lon2 = math.radians(loc2[1])
    lat1 = math.radians(loc1[0])
    lat2 = math.radians(loc2[0])
    d_lon = lon2 - lon1
    d_lat = lat2 - lat1
    angle = math.sin(d_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(d_lon / 2) ** 2

    return round((2 * math.asin(math.sqrt(angle))) * EARTH_RADIUS_MI, 2)


def format_raw_markets(line):
    line = format_nulls(line)
    res = (f"ID: {line[0]}, Name: {line[1]}, Street: {line[2]}, City: {line[3]}, State: {line[4]}, ZIP: {line[5]}, "
           f"LAT: {line[6]}, LON: {line[7]}")
    return res


def format_pretty_markets(line):
    line = format_nulls(line)
    res = (f"Name: {line[0]}, Street: {line[1]}, City: {line[2]}, State: {line[3]}, ZIP: {line[4]}, "
           f"Review score: {line[5]}")
    return res


def format_search(line):
    line = format_nulls(line)
    res = f"Name: {line[0]}, Street: {line[1]}, City: {line[2]}, State: {line[3]}, ZIP: {line[4]}"
    return res


def format_full_data(line):
    line = format_nulls(line)

    res = (
        f"Name: {line[0]}\nProduce: {line[1]}\nStreet: {line[2]}\nCity: {line[3]}\nState: {line[4]}\nZIP: {line[5]}\n"
        f"Latitude: {line[6]}\nLongitude: {line[7]}")
    return res


def format_closest(line):
    res = f"Name: {line[1]}, Distance: {line[0]} miles"
    return res


def format_nulls(line):
    line = list(line)
    for i in range(len(line)):
        if line[i] == 0 or line[i] is None:
            line[i] = "n/a"
    return line


def validate_signing(sign_request_data):
    if sign_request_data:
        return True
    else:
        return False
