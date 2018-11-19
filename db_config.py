import psycopg2

url = "dbname='comments' host='localhost' port='5432' user='postgres' password='v0k3ch!97'"


def connection(url):
    """connection to our database"""
    con = psycopg2.connect(url)
    return con


def init_db():
    """This is the initialization of our db"""
    con = connection(url)
    return con


def create_tables():
    """This is the function to create our tables"""
    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    """this endpoint is used to destroy our tables"""
    conn = connection(url)
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE users, comments, logs;""")
    conn.commit()


def tables():
    """queries for our database to create our tables"""
    users = """ CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY,
            user_name VARCHAR(96) UNIQUE,
            password VARCHAR(48) NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
            role VARCHAR NOT NULL DEFAULT 'user'
            );
            """

    comments = """ CREATE TABLE IF NOT EXISTS comments(
               comments_id serial PRIMARY KEY,
               user_id serial NOT NULL,
               comment VARCHAR(100),
               created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
               updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
               FOREIGN KEY (user_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            );
            """

    logs = """ CREATE TABLE IF NOT EXISTS logs(
                     log_id serial PRIMARY KEY,
                     user_id serial NOT NULL,
                     logged_in_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                     logged_out_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                     FOREIGN KEY (user_id)
                             REFERENCES users (user_id)
                             ON UPDATE CASCADE ON DELETE CASCADE                                          
                     );"""
    queries = [users, comments, logs]
    return queries
