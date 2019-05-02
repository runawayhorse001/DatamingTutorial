user = 'kadvseg'
pw='Aak@Dv5eg'
host = '10.243.165.10'
database = 'dst'
table_name = 'kasina_advisor.kasina_consortium_list'

# load the library 
library("sqldf")
library('RODBC')
library('RPostgreSQL')

# Create a driver
drv <- DBI::dbDriver( "PostgreSQL" )
# Create the database connection
conn <- dbConnect( drv, dbname = database, host = host,port = '5432', 
                   user = user, password = pw )

# Create the SQL query string. Include a semi-colon to terminate
querystring = sprintf('SELECT * FROM %s;', table_name)
# Execute the query and return results as a data frame
df = dbGetQuery(conn, querystring )

head(df)