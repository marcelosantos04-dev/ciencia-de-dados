from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import csv
import uuid
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'troque_esta_chave_por_uma_secreta'  # altere antes de deploy

DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
CSV_PATH = DATA_DIR / 'responses.csv'

HEADERS = [
    'response_id',
    'submitted_at',
    'consent',
    'days_physical_activity_week',
    'portions_fruit_week',
    'sleep_hours_weekday',
    'sugary_drinks_week',
    'mobile_video_hours_week',
    'age_range',
    'gender',
    'notes'
]


def save_row(row: dict):
    write_header = not CSV_PATH.exists()
    with CSV_PATH.open('a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if write_header:
            writer.writeheader()
        writer.writerow(row)


@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.form.get('consent') != 'on':
        flash('É necessário concordar com o consentimento para enviar.')
        return redirect(url_for('index'))

    try:
        days = int(request.form.get('days_physical_activity_week', '0'))
        if not (0 <= days <= 7):
            raise ValueError('days out of range')

        portions = int(request.form.get('portions_fruit_week', '0'))
        if portions < 0:
            raise ValueError('portions negative')

        sleep = float(request.form.get('sleep_hours_weekday', '0'))
        if not (0 <= sleep <= 24):
            raise ValueError('sleep out of range')

        sugary = int(request.form.get('sugary_drinks_week', '0'))
        if sugary < 0:
            raise ValueError('sugary negative')

        mobile = float(request.form.get('mobile_video_hours_week', '0'))
        if mobile < 0:
            raise ValueError('mobile negative')

    except Exception:
        flash('Entradas inválidas — verifique os valores e tente novamente.')
        return redirect(url_for('index'))

    row = {
        'response_id': str(uuid.uuid4()),
        'submitted_at': datetime.utcnow().isoformat(),
        'consent': 'true',
        'days_physical_activity_week': days,
        'portions_fruit_week': portions,
        'sleep_hours_weekday': sleep,
        'sugary_drinks_week': sugary,
        'mobile_video_hours_week': mobile,
        'age_range': request.form.get('age_range', ''),
        'gender': request.form.get('gender', ''),
        'notes': request.form.get('notes', '')
    }

    save_row(row)
    return render_template('thanks.html')


@app.route('/download', methods=['GET'])
def download():
    if not CSV_PATH.exists():
        flash('Ainda não há respostas para baixar.')
        return redirect(url_for('index'))
    return send_file(CSV_PATH, as_attachment=True, download_name='responses.csv')


if __name__ == '__main__':
    app.run(debug=True)
