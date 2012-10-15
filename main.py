from settings import app
from documents import syslog
from flask import render_template, request, redirect, url_for
from datetime import datetime, timedelta

today = datetime.strptime(datetime.now().strftime('%m/%d/%Y'), '%m/%d/%Y')
tomorrow = today + timedelta(days=1)


@app.route('/log/<category>/')
@app.route('/log/<category>/<int:page>')
def list_syslog(category, page=1):
    title = u'OPeration System Log'
    syslog.config_collection_name = 'syslog.' + category
    pagination = syslog.query.regexp(
                            bdate=today,
                            edate=tomorrow).descending('time').paginate(
                                                               page=page,
                                                               per_page=20)
    return render_template('/log/list_syslog.html',
                            category=category,
                            pagination=pagination,
                            title=title)

@app.route('/log/<category>/filter/', methods=['GET'])
@app.route('/log/<category>/filter/<int:page>')
def filter_syslog(category, page=1):
    title = u'OPeration System Log'
    syslog.config_collection_name = 'syslog.' + category
    re_host = request.args.get('hostname','')
    re_message = request.args.get('letter','')

    try:
        startdate = datetime.strptime(
                    request.args.get('daterange','').split('-')[0].strip(),
                    '%m/%d/%Y')
        enddate = datetime.strptime(
                    request.args.get('daterange','').split('-')[1].strip(),
                    '%m/%d/%Y')
    except:
        startdate = today
        enddate = tomorrow
    pagination = syslog.query.regexp(
        host=re_host,
        message=re_message,
        bdate=startdate,
        edate=enddate).descending(
            'time').paginate(page=page, per_page=20)
    return render_template('/log/filter_syslog.html',
                           category=category,
                           pagination=pagination,
                           title=title)


@app.route('/')
def index():
    return redirect(url_for('list_syslog', category='syslog'))

if __name__ == "__main__":
    app.run()
