from flask import request, redirect, url_for, render_template, flash, jsonify
from flaskr import app, db
from flaskr.models import Entry
import time

from flaskr import serializer


@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    app.logger.info("show entries")
    return render_template('show_entries.html', entries=entries)

@app.route('/map')
def show_map_entries():
    return render_template('show_map.html')

@app.route('/json')
def json_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return jsonify({'data': serializer.serializer(entries, 'sqlalchemy')})

@app.route('/add', methods=['POST','GET'])
def add_entry():
    try:
        if request.method == 'POST':
            app.logger.info("hoge")
            app.logger.info("lat: " + request.form['lat'])
            app.logger.info("long: " + request.form['long'])
            app.logger.info("timestamp: " + request.form['timestamp'])
            app.logger.info("client: " + request.form['client'])

            entry = Entry(
                lat=request.form['lat'],
                long=request.form['long'],
                timestamp=int(request.form['timestamp']),
                client=request.form['client']
            )
            app.logger.info(entry)

        else:
            entry = Entry(
                lat=request.args.get('lat', ''),
                long=request.args.get('long', ''),
                timestamp=int(request.args.get('timestamp', time.time())),
                client=request.args.get('client', '')
            )

    except Exception as e:
        return str(e)

    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

