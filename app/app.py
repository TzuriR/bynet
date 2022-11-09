#docker stop $(docker ps -a -q)
#docker rm $(docker ps -a -q)
#docker rmi 08c2bf651059

# docker container ps -a
# docker logs container_id
# docker system prune -a

from typing import List, Dict
from flask import Flask, render_template
import mysql.connector
import json

app = Flask(__name__)

def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'hellotable'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    result = cursor.fetchall()
    #results = [{word1: word2} for (word1, word2) in cursor]
    #cursor.close()
    #connection.close()
    print(result)
    return result


@app.route('/')
def index() -> str:
    #return json.dumps({'test_table': test_table()})
    return render_template('index.html')
    #return "Hello World!"
    #return test_table()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
