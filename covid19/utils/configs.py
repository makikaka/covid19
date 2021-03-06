import configparser

parser = configparser.ConfigParser()

parser["DEFAULT"] = {

}

parser['file'] = {
    "att_names": 'Date,Total_Cases,New_Cases,Total_Deaths,New_Deaths,Total_Recovered,Active_cases,' \
                 'Serious_or_Critical,' \
                 'Total_Cases_per_1M ',

    "file_name": "stats_covid19.csv"

}

parser["DB"] = {
    'att_names_db': 'Date,Total_Cases text,New_Cases integer,Total_Deaths integer,New_Deaths integer,Total_Recovered integer,Active_cases integer,' \
                    'Serious_or_Critical integer,' \
                    'Total_Cases_per_1M real',
    "db_name": "covid19.db",
    "stats_table": "covid_19",
    'countries_table': "countries"
}

parser["HTTP"] = {
    'URL': "https://www.worldometers.info/coronavirus/?fbclid=IwAR1OutjUurc_K" \
           "4BH9F4smkLpC0yKfndoShfUtrs4cJZehqS7PQs0Ek85Xlw",
    'local_server_ip': "127.0.0.1",
    'public_server_ip': "0.0.0.0",
    'port_number': 2021
}
parser["mc_keys"] = {
    'stats_db_key': "stats_db",
    'stats_key': "stats",
    'date_key': "last_datetime_key",
    'header_key': 'key_header',
    'database_key': "db_key1"
}

with open("configs.ini", "w") as configfile:
    parser.write(configfile)
