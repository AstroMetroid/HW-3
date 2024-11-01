from flask import Flask, render_template
import util

# Creating and application instance
app = Flask(__name__)

# Log in variables
username = 'garrett'
password = 'Silver1@'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# Creating a route
@app.route('/')

# Creating the index page
def indext():
	# Conncecting to database
	cursor, connection = util.connect_to_db(username, password, host, port, database)
	# SQL command to get the items of fruit from the two baskets
	record = util.run_and_fetch_sql(cursor, "select * from basket_a full join basket_b on basket_a.a = basket_b.b;")
	# Checking if record was retrieved
	if record == -1:
		print('SQL command is invalid')
	else:
		# Return the column names of the results
		col_names = [desc[0] for desc in cursor.description]
		# Limiting to first 5 rows
		log = record[:5]
	# Disconnecting from database
	util.disconnect_from_db(connection, cursor)
	# Returning data
	return render_template('index.html', sql_table = log, table_title = col_names)
	
@app.route('/api/update_basket_a')

# Updating basket_a 
def update_basket_a():
	try:
		# Connect to database
		cursor, connection = util.connect_to_db(username, password, host, port, database)
		# Checking if the entry already exists
		cursor.execute("Select 1 deom basket_a where a = 5")
		exists = cursor.fetchnone()
		if exists:
			return "Entry (5, 'Cherry') already exists in basket_a", 200
		else:
			cursor.execute("insert into basket_a (a, fruit_a) values (5, 'Cherry')")
			connection.commit()
			return "Successfully updated"
	except Exception as e:
		error_message = f"Error: {e}"
		print(error_message)
		return error_message, 500
	# Disconnecting from database
	util.disconnect_from_db(connection, cursor)
	
@app.route('/api/unique')

# Separating unique fruits
def unique_fruits():
	try:
		# Connect to database
		cursor, connection = util.connect_to_db(username, password, host, port, database)
		# Separate fruit
		fruits_a = set(row[0] for row in util.run_and_fetch_sql(cursor, "select fruit_a from basket_a"))
		fruits_b = set(row[0] for row in util.run_and_fetch_sql(cursor, "select fruit_b from basket_b"))
		# Get fruits into the table
		table_title = ["Unique to basket_a", "Unique to basket_b"]
		sql_table = [[", ".join(unique_a), ", ".join(unique_b)]]
		# Rendering the table
		return render_template('index.html', table_title = table_title, sql_table = sql_table)
	except Exception as e:
		return f"Error: {e}", 500
	# Disconnecting from database
	util.disconnect_from_db(connection, cursor)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1')
