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