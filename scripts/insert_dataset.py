import os
import datetime
from csv import DictReader

from dotenv import load_dotenv
import psycopg

load_dotenv()

def set_db_url(
    username: str,
    password: str,
    database: str="",
    rdbms: str='postgresql',
    hostname: str="localhost",
    port: int=5432,
):  
    if not database:
        return f'{rdbms}://{username}:{password}@{hostname}:{port}'
    return f'{rdbms}://{username}:{password}@{hostname}:{port}/{database}'

db_url = set_db_url(
    username=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME"),
    hostname="localhost",
    port=5432,
)

BASE_DIR = os.getcwd()
DATASET_PATH = 'dataset'
DATASET = dict(
    house='houses.csv',
    member='members.csv'
)

created_at = datetime.datetime.now().isoformat()

connection = psycopg.connect(db_url, autocommit=True)
with connection.cursor() as cursor:
    
    for label, filename in DATASET.items():
        print(f'Inserting {label}...')
        
        with open(os.path.join(BASE_DIR, DATASET_PATH, filename), 'r') as file:
            reader = DictReader(file, delimiter=';')
            
            for row in reader:
                print(f'Inserting {row}...')
                
                row['created_at'] = created_at
                row['updated_at'] = created_at
                row['is_active'] = str(True)
                
                sql = f"INSERT INTO {label} ( {', '.join(row.keys())} ) "
                if label == 'house':
                    values = [value.replace('\'', '`') for value in row.values()]
                    sql += "VALUES ( '{}' );".format( "', '".join(values) )
                else:
                    sql += "VALUES ( '{}', '{}', {}, '{}', '{}', '{}' );".format(
                        row['name'], row['description'], int(row['house_id']),
                        row['created_at'], row['updated_at'], str(row['is_active']),
                    )
                
                print(sql)
                cursor.execute(sql)
                connection.commit()
connection.close()