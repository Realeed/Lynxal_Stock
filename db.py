import pyodbc

try:
    # make db connection
    connection = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server=tcp:stockretrievaldb.database.windows.net,1433;Database=stockretrieval;Uid=hakob;Pwd=SomeGoodPassword007;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
    cursor = connection.cursor()

    try:
        # create table commands
        createCapacitorCommand = """CREATE TABLE "capacitors" (
                                        ID int IDENTITY(1,1) PRIMARY KEY,
                                        BoxName varchar(1024) DEFAULT NULL,
                                        ManufacturerPartNumber varchar(1024) DEFAULT NULL,
                                        Quantity int DEFAULT NULL,
                                        Package varchar(1024) DEFAULT NULL,
                                        Capacitance varchar(1024) DEFAULT NULL,
                                        Voltage varchar(1024) DEFAULT NULL,
                                        TemperatureCoefficient varchar(1024) DEFAULT NULL,
                                        Notes varchar(1024) DEFAULT NULL,
                                        LastUpdated varchar(1024) DEFAULT NULL
                                    )"""

        cursor.execute(createCapacitorCommand)
        cursor.commit()
        print("Table created successfully")
    except:
        print("Couldn't create Table capacitors")

except:
    print("Couldn't connect to the db")
