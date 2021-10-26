from flask import Flask, redirect, url_for, render_template, request, g, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'mybiggestsecret'

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'User: {self.username}, Password: {self.password}'

users = []
users.append(User(id=1, username='lynxal_team', password='lynxal2020'))

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        for i in range(len(users)):
            if users[i].id == session.get('user_id'):
                g.user = users[i]

@app.route('/sign_in', methods = ['POST', 'GET'])
def signIn():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for i in range(len(users)):
            if username == users[i].username and password == users[i].password:
                session.permanent = True
                session['user_id'] = users[i].id
                return redirect(url_for('chooseAction'))
        return render_template('signin.html', failed = True)
    return render_template('signin.html')

@app.route('/sign_out', methods = ['GET'])
def signOut():
    if session.get('user_id'): 
        session.pop('user_id')
    return redirect(url_for('signIn'))

@app.route('/', methods = ['GET'])
def main():
    if not g.user:
        return redirect(url_for('signIn'))
    return redirect(url_for('chooseAction'))

@app.route('/choose_action', methods = ['POST', 'GET'])
def chooseAction():
    if not g.user:
        return redirect(url_for('signIn'))
    if request.method == 'POST':
        action = request.form['action']
        # if action == 'search' or action == 'inventorization' or action == 'add' or action == 'withdraw':  
        #     return redirect(url_for('chooseStock', action = action))
        if action == 'search' or action == 'withdraw':
            return redirect(url_for('chooseStock', action = action))
        # elif action == 'move': 
        #     return redirect(url_for('chooseStocksToMove'))
        else:
            return redirect(url_for('underDev'))
    return render_template('home.html')

@app.route('/choose_stock', methods = ['POST', 'GET'])
def chooseStock():
    if not g.user:
        return redirect(url_for('signIn'))
    if request.method == 'POST':
        stock = request.form['stock']
        if stock == 'all':
            return redirect(url_for('underDev'))
        if stock == 'all' or stock == 'main' or stock == 'production' or stock == 'prototyping':
            return redirect(url_for('getInfo', action = request.form['action'], stock = stock))
    if request.args['action']:
        return render_template('Stocks/mainProdProt.html')

@app.route('/oops_bug', methods = ['GET'])
def underDev():
    return render_template('/Responses/underDev.html')

@app.route('/choose_stocks_to_move', methods = ['POST', 'GET'])
def chooseStocksToMove():
    if not g.user:
        return redirect(url_for('signIn'))
    if request.method == 'POST':
        print('')
    return render_template('Stocks/moveStocks.html')

@app.route('/info_query', methods = ['GET'])
def getInfo():
    if not g.user:
        return redirect(url_for('signIn'))
    action = request.args.get('action')
    if action == 'search':
        return render_template('Queries/search.html')
    elif action == 'withdraw':
        return render_template('Queries/withdraw.html')

@app.route('/search_by_mpn', methods = ['POST'])
def searchByMpn():
    try:
        database = mysql.connector.connect(host = 'localhost', user = g.user.username, password = g.user.password)
        cursor = database.cursor()
        stock = request.form['stock']
        mpn = request.form['mpn']
        stockNames = []
        tableNames = []
        columnNames = []
        def appendTables(tableName):
            if tableName == 'diodes_leds':
                tableNames.append('Diodes and LEDs')
            elif tableName == 'electrolytic_capacitors':
                tableNames.append('Electrolytic Capacitors')
            elif tableName == 'ics':
                tableNames.append('Integrated Circuits')
            elif tableName == 'zener_diodes':
                tableNames.append('Zener Diodes')
            else:
                tableNames.append(tableName.capitalize())
        def appendColumns(tableColName):
            #region (append column names)
            if tableColName == 'BoxName':
                columnNames.append('Box Name')
            elif tableColName == 'Capacitance':
                columnNames.append('Capacitance')
            elif tableColName == 'ID':
                columnNames.append('Id')
            elif tableColName == 'LastUpdated':
                columnNames.append('Last Updated')
            elif tableColName == 'ManufacturerPartNumber':
                columnNames.append('Manufacturer Part Number')
            elif tableColName == 'Notes':
                columnNames.append('Notes')
            elif tableColName == 'Package':
                columnNames.append('Package')
            elif tableColName == 'Quantity':
                columnNames.append('Quantity')
            elif tableColName == 'StandardPackQty':
                columnNames.append('Reel Quantity')
            elif tableColName == 'TemperatureCoefficient':
                columnNames.append('Temperature Coefficient')
            elif tableColName == 'Voltage':
                columnNames.append('Voltage')
            elif tableColName == 'Frequency':
                columnNames.append('Frequency')
            elif tableColName == 'LoadCapacitance':
                columnNames.append('Load Capacitance')
            elif tableColName == 'Type':
                columnNames.append('Type')
            elif tableColName == 'Current':
                columnNames.append('Current')
            elif tableColName == 'Size':
                columnNames.append('Size')
            elif tableColName == 'CurrentRating':
                columnNames.append('Current Rating')
            elif tableColName == 'Impedance':
                columnNames.append('Impedance')
            elif tableColName == 'Description':
                columnNames.append('Description')
            elif tableColName == 'Inductance':
                columnNames.append('Inductance')
            elif tableColName == 'Shielding':
                columnNames.append('Shielding')
            elif tableColName == 'PowerRating':
                columnNames.append('Power Rating')
            elif tableColName == 'Resistance':
                columnNames.append('Resistance')
            elif tableColName == 'Tolerance':
                columnNames.append('Tolerance')
            elif tableColName == 'Channel':
                columnNames.append('Channel')
            #endregion
        params = []
        if stock == 'all':
            getDbs = 'SHOW DATABASES'
            cursor.execute(getDbs)
            dbs = cursor.fetchall()
            for db in dbs:
                if db[0] != 'information_schema' and db[0] != 'mysql' and db[0] != 'performance_schema':
                    use = f'USE {db[0]}'
                    cursor.execute(use)
                    getTables = 'SHOW TABLES'
                    cursor.execute(getTables)
                    tables = cursor.fetchall()
                    for table in tables:
                        query = f'SELECT * FROM {table[0]} WHERE ManufacturerPartNumber = \'{mpn}\''
                        cursor.execute(query)
                        components = cursor.fetchall()
                        if components:
                            if db[0] == 'main_stock':
                                stockNames.append('Main')
                            elif db[0] == 'production_stock':
                                stockNames.append('Production')
                            elif db[0] == 'prototyping_stock':
                                stockNames.append('Prototyping')
                            appendTables(table[0])
                        for component in components:
                            print(component)
                            print(f'found in {db[0]}')
                            print(f'found in {table[0]}')
                            print()
                            getColumnNames = f'SHOW COLUMNS FROM {table[0]}'
                            cursor.execute(getColumnNames)
                            colNames = cursor.fetchall()
                            for colName in colNames:
                                print(colName[0])
                                appendColumns(colName[0])
                            print()
                            print()
                            for param in component:
                                if param == 'None':
                                    params.append('')
                                else:
                                    params.append(param)
        else:
            if stock == 'main':
                use = 'USE main_stock'
                stockNames.append('Main')
            elif stock == 'production':
                use = 'USE production_stock'
                stockNames.append('Prodiction')
            elif stock == 'prototyping':
                use = 'USE prototyping_stock'
                stockNames.append('Prototyping')
            cursor.execute(use)
            getTables = 'SHOW TABLES'
            cursor.execute(getTables)
            tables = cursor.fetchall()
            for table in tables:
                query = f'SELECT * FROM {table[0]} WHERE ManufacturerPartNumber = \'{mpn}\''
                cursor.execute(query)
                components = cursor.fetchall()
                if components:
                    appendTables(table[0])
                for component in components:
                    print(component)
                    getColumnNames = f'SHOW COLUMNS FROM {table[0]}'
                    cursor.execute(getColumnNames)
                    colNames = cursor.fetchall()
                    for colName in colNames:
                        print(colName[0])
                        appendColumns(colName[0])
                    print()
                    print()
                    for param in component:
                        if param == None:
                            params.append('')
                        else:
                            params.append(param)

        database.close()  
    except:
        return 'Couldn\'t connect to the data'
    for index, columnName in enumerate(columnNames):
        if columnName == 'Reel Quantity':
            if params[index - 1] % params[index] == 0:
                params[index] = params[index - 1] // params[index]
            else:
                params[index] = round(params[index - 1] / params[index], 2)
    return render_template('Responses/search.html', stock = stock, mpn = mpn, stocks = stockNames, tables = tableNames, columns = columnNames, params = params)

@app.route('/search_by_values', methods = ['POST'])
def searchByValues():
    return redirect(url_for('underDev'))

@app.route('/search_by_file', methods = ['POST'])
def searchByFile():
    return redirect(url_for('underDev'))

if __name__  == "__main__":
    app.run(host='0.0.0.0', port=80)