import json
import MySQLdb

def lambda_handler(event, context):
    # TODO implement
    region = event['queryStringParameters']['region']
    #region = "East of England"
    result = get_uni(region)

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

def get_connection():
    """Returns a connection to the database"""
    connection = MySQLdb.connect(
        host="db706.ciankffgrtkz.us-east-1.rds.amazonaws.com",
        user="admin",
        passwd="12345678",
        db="proj4",
    )
    return connection
    
def get_uni(region):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM universities where region = '" + region + "';"
    cursor.execute(sql)
    data = cursor.fetchall()
    
    result = {};
    result['University_name'] = []
    result['Region'] = []
    result['Founded_year'] = []
    result['Motto'] = []
    result['World_rank'] = []
    result['Website'] = []
    
    for row in data:
        result['University_name'].append(str(row[0]))
        result['Region'].append(str(row[1]))
        result['Founded_year'].append(str(row[2]))
        result['Motto'].append(str(row[3]))
        result['World_rank'].append(str(row[4]))
        result['Website'].append(str(row[5]))
        
    connection.close()
    return result