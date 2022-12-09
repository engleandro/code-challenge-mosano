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