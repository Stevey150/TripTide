from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)
CSV_DIRECTORY = 'csv_files'  # Directory where CSV files are stored

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_csv', methods=['POST'])
def get_csv():
    days = request.form['days']
    csv_filename = f'Belgium{days}days.csv'
    csv_path = os.path.join(CSV_DIRECTORY, csv_filename)
    
    try:
        return send_file(csv_path, as_attachment=True)
    except FileNotFoundError:
        return "CSV file not found."

if __name__ == '__main__':
    app.run(debug=True)
