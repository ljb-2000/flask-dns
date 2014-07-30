from flask import Flask, render_template, request, flash
from forms import ContactForm
import dns.reversename

app = Flask(__name__)

app.secret_key = 'you are a big donkey | 1492'

@app.route('/', methods=['GET', 'POST'])
def lookup():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            revname = str(dns.reversename.from_address(request.form['ipaddr']))
            return revname
        else:
            flash('IP address is required.')
            return render_template('lookup.html', form=form)
                 
    elif request.method == 'GET':
        return render_template('lookup.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
