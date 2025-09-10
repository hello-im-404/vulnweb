from flask import Flask, render_template, request
from database import get_db_connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    query = ""
    
    if request.method == 'POST':
        query = request.form.get('query', '')
        
        if query:
            try:
                conn = get_db_connection()
                cursor = conn.execute(f"SELECT * FROM users WHERE username = '{query}'")
                results = cursor.fetchall()
                conn.close()
                
            except Exception as e:
                error = f"Ошибка: {str(e)}"
                results = []
    
    return render_template('index.html', results=results, error=error, query=query)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
