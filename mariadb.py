import mysql.connector

def get_oid_select():

    try:
        mydb = mysql.connector.connect(
            host = "192.168.56.101",
            user = "mib",
            password = "password",
            database = "net_snmp"
        )

        cursorObject = mydb.cursor()

        query = ("SELECT oid, traduccio from oids")

        cursorObject.execute(query)

        option_tuple = tuple(
                {"oid": oid, "traduccio": traduccio} for oid, traduccio in cursorObject
            )

        cursorObject.close()
        mydb.close()
        return option_tuple
    
    except mysql.connector.errors.DatabaseError:
        print(f'No podem connectar a base de dades')
        return None
    
# get_oid_select()

def get_oid_traduction(oid):

    try:
        mydb = mysql.connector.connect(
            host = "192.168.56.101",
            user = "mib",
            password = "password",
            database = "net_snmp"
        )

        cursorObject = mydb.cursor()

        query = (f"SELECT traduccio from oids where oid = '{oid}'")
        print(query)

        cursorObject.execute(query)

        traduction = next(cursorObject)

        print(traduction[0])

        cursorObject.close()
        mydb.close()
        return traduction[0]
    
    except mysql.connector.errors.DatabaseError:
        print(f'No podem connectar a base de dades')
        return None

    
# get_oid_traduction("1.3.6.1.2.1.4.20")

def get_traps(dateini='', datefi=''):
    try:
        mydb = mysql.connector.connect(
            host = "192.168.56.101",
            user = "mib",
            password = "password",
            database = "net_snmp"
        )

        cursorObject = mydb.cursor()

        query = ("select trap_id, date_time, transport from notifications")

        if dateini != '' and datefi != '':
            query = query + (f" WHERE date_time BETWEEN '{dateini}' AND '{datefi}'")

        elif datefi != '':
            query = query + (f" WHERE date_time <= '{datefi}'")

        elif dateini != '':
            query = query + (f" WHERE date_time >= '{dateini}'")

        cursorObject.execute(query)

        resposta_tuple = tuple(
                {"trap_id": trap_id, "date_time": date_time, "transport": transport} for trap_id, date_time, transport in cursorObject
            )

        cursorObject.close()
        mydb.close()
        return resposta_tuple
    
    except mysql.connector.errors.DatabaseError:
        print(f'No podem connectar a base de dades')
        return None
    
def get_traps_detall(trap_id):
    try:
        mydb = mysql.connector.connect(
            host = "192.168.56.101",
            user = "mib",
            password = "password",
            database = "net_snmp"
        )

        cursorObject = mydb.cursor()

        query = (f"select oid, type, value from varbinds where trap_id={trap_id}")

        cursorObject.execute(query)

        resposta_tuple = tuple(
                {"oid": oid, "type": type, "value": value} for oid, type, value in cursorObject
            )

        cursorObject.close()
        mydb.close()
        return resposta_tuple
    
    except mysql.connector.errors.DatabaseError:
        print(f'No podem connectar a base de dades')
        return None