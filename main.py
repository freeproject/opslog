from settings import app
from documents import syslog, server_info
from flask import render_template, request, redirect, url_for
from datetime import datetime, timedelta

today = datetime.strptime(datetime.now().strftime('%m/%d/%Y'), '%m/%d/%Y')
tomorrow = today + timedelta(days=1)


@app.route('/log/<category>/')
@app.route('/log/<category>/<int:page>')
def list_log(category, page=1):
    title = u'OPeration System Log'
    syslog.config_collection_name = category
    pagination = syslog.query.regexp(
                            bdate=today,
                            edate=tomorrow).descending('time').paginate(
                                                               page=page,
                                                               per_page=100)
    return render_template('/log/list_all.html',
                            category=category,
                            pagination=pagination,
                            title=title)


@app.route('/log/<category>/filter/', methods=['POST', 'GET'])
@app.route('/log/<category>/filter/<int:page>', methods=['POST', 'GET'])
def list_filter(category, page=1):
    if request.method == 'POST':
        title = u'OPeration System Log'
        syslog.config_collection_name = category
        re_host = request.form['hostname']
        re_message = request.form['letter']

        try:
            startdate = datetime.strptime(
                        request.form['daterange'].split('-')[0].strip(),
                        '%m/%d/%Y')
            enddate = datetime.strptime(
                        request.form['daterange'].split('-')[1].strip(),
                        '%m/%d/%Y')
        except:
            startdate = today
            enddate = tomorrow
        pagination = syslog.query.regexp(
                        host=re_host,
                        message=re_message,
                        bdate=startdate,
                        edate=enddate).descending(
                               'time').paginate(page=page, per_page=100)
        return render_template('/log/list_filter.html',
                               category=category,
                               pagination=pagination,
                               title=title)


@app.route('/')
def index():
    return redirect(url_for('list_log', category='syslog'))

if __name__ == "__main__":
    app.run()
