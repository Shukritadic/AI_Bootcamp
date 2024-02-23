import psycopg2 
import pandas as pd
#create connection to the database
conn= psycopg2.connect(database ='Hospital',
                       user= 'Postgres',
                       password = 'postgres',
                       port= '5042')
