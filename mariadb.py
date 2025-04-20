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

    
get_oid_traduction("1.3.6.1.2.1.4.20")