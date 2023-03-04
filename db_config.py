from app import app
from flaskext.mysql import MySQL
mysql = MySQL()

dataName = "laravel"

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '130231322'
app.config['MYSQL_DATABASE_DB'] = dataName
# 'dinasty'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
