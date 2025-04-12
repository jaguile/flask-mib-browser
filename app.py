import asyncio
from flask import Flask
from flask import render_template, request
from snmpget import snmpget
from snmpset import snmpset
from snmpnext import snmpnext
from snmpbulkwalk import snmpbulkwalk

app = Flask(__name__)

@app.route("/mib")
def mib():
    return render_template("mib.html")

# https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data
@app.route("/snmpquery", methods=['POST'])
def snmpquery():
    valor_version   = request.form['version']
    
    if (request.form['version'] == '1'):
        valor_version = 0
    else:
        valor_version = 1

    valor_rocomm    = request.form['rocommunity']
    valor_agent     = request.form['agent']
    valor_mib       = request.form['MIB']
    valor_query     = request.form['query']
    valor_set       = request.form['set']

    if valor_query == 'snmpbulkwalk':
        valor_oid       = request.form['OID']
    else:
        valor_oid       = request.form['OID'] + '.' + '0'

    varBinds = run_query(valor_query, valor_version, valor_rocomm, valor_agent, valor_mib, valor_oid, valor_set)

    resultat = [
            {"oid": str(varBind[0]), "value": varBind[1]} 
            for varBind in varBinds
        ]        

    return render_template("mib_resposta.html", 
                            version = valor_version,
                            rocomm = valor_rocomm,
                            agent = valor_agent ,
                            mib = valor_mib   ,
                            oid = valor_oid   ,
                            query = valor_query ,
                            resultat = resultat
                           ) 


def run_query(query, version, comm, agent, mib, oid, set=''):
    
    match query:
        case 'snmpget':
            print("snmpget")
            return asyncio.run(snmpget(version, comm, agent, mib, oid))
        case 'snmpnext':
            print("snmpnext")
            return asyncio.run(snmpnext(version, comm, agent, mib, oid))
        case 'snmpbulkwalk':
            print("snmpbulkwalk")
            return asyncio.run(snmpbulkwalk(version, comm, agent, mib, oid))
        case 'snmpset':
            print("snmpset")
            return asyncio.run(snmpset(version, comm, agent, mib, oid, set))
    return None