from flask import Flask,render_template,request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/black/Desktop/Flask environment/spaceinfos/space1.db'
app.config['SECRET_KEY']='1234567890'

db=SQLAlchemy(app)

admin=Admin(app)

class Space(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(50))
	subtitle =  db.Column(db.String(20))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)

admin.add_view(ModelView(Space,db.session))

@app.route('/')
def index():
	posts=Space.query.order_by(Space.date_posted.desc()).all()
	return render_template('index.html',posts=posts)


@app.route('/yearly')
def yearly():
	return render_template('yearly.html')

@app.route('/telescope')
def telescope():
	return render_template('telescope.html')

@app.route('/spacewiki')
def spacewiki():
	return render_template('spacewiki.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Space.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)



@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Space(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/telescope/gbt')
def gbt():
	return render_template('gbt.html')

@app.route('/telescope/sbt')
def sbt():
	return render_template('sbt.html')

@app.route('/telescope/ngt')
def ngt():
	return render_template('ngt.html')

@app.route('/yearly/jan')
def jan():
	return render_template('jan.html')

@app.route('/yearly/febu')
def febu():
	return render_template('febu.html')

@app.route('/yearly/mar')
def mar():
	return render_template('mar.html')

@app.route('/yearly/april')
def april():
	return render_template('april.html')

@app.route('/yearly/may')
def may():
	return render_template('may.html')

@app.route('/yearly/jun')
def jun():
	return render_template('jun.html')

@app.route('/yearly/july')
def july():
	return render_template('july.html')

@app.route('/yearly/aug')
def aug():
	return render_template('aug.html')

@app.route('/yearly/sep')
def sep():
	return render_template('sep.html')

@app.route('/yearly/oct')
def oct():
	return render_template('oct.html')

@app.route('/yearly/nov')
def nov():
	return render_template('nov.html')

@app.route('/yearly/decem')
def decem():
	return render_template('decem.html')

@app.route('/telescope/gbt/gemini')
def gemini():
	return render_template('gemini.html')


@app.route('/telescope/gbt/hobby')
def hobby():
	return render_template('hobby.html')


@app.route('/telescope/gbt/keck')
def keck():
	return render_template('keck.html')


@app.route('/telescope/gbt/mmt')
def mmt():
	return render_template('mmt.html')


@app.route('/telescope/gbt/south')
def south():
	return render_template('south.html')


@app.route('/telescope/gbt/subaru')
def subaru():
	return render_template('subaru.html')


@app.route('/telescope/gbt/very')
def very():
	return render_template('very.html')


@app.route('/telescope/sbt/astro')
def astro():
	return render_template('astro.html')


@app.route('/telescope/sbt/chandra')
def chandra():
	return render_template('chandra.html')


@app.route('/telescope/sbt/galaxy')
def galaxy():
	return render_template('galaxy.html')


@app.route('/telescope/sbt/hubbler')
def hubble():
	return render_template('hubble.html')


@app.route('/telescope/sbt/kepler')
def kepler():
	return render_template('kepler.html')


@app.route('/telescope/sbt/tess')
def tess():
	return render_template('tess.html')


@app.route('/telescope/sbt/wide')
def wide():
	return render_template('wide.html')


@app.route('/telescope/nbt/europe')
def europe():
	return render_template('europe.html')

@app.route('/telescope/nbt/eulid')
def euclid():
	return render_template('euclid.html')

@app.route('/telescope/nbt/james')
def james():
	return render_template('james.html')

@app.route('/telescope/nbt/laser')
def laser():
	return render_template('laser.html')


@app.route('/telescope/nbt/gaint')
def gaint():
	return render_template('gaint.html')

@app.route('/telescope/nbt/thirty')
def thirty():
	return render_template('thirty.html')

@app.route('/spacewiki/asteroid')
def asteroid():
	return render_template('asteroid.html')

@app.route('/spacewiki/binary')
def binary():
	return render_template('binary.html')

@app.route('/spacewiki/black')
def black():
	return render_template('black.html')

@app.route('/spacewiki/comet')
def comet():
	return render_template('comet.html')

@app.route('/spacewiki/dwarf')
def dwarf():
	return render_template('dwarf.html')

@app.route('/spacewiki/earth')
def earth():
	return render_template('earth.html')

@app.route('/spacewiki/eclipse')
def eclipse():
	return render_template('eclipse.html')

@app.route('/spacewiki/galaxy1')
def galaxy1():
	return render_template('galaxy1.html')

@app.route('/spacewiki/jupiter')
def jupiter():
	return render_template('jupiter.html')

@app.route('/spacewiki/mars')
def mars():
	return render_template('mars.html')

@app.route('/spacewiki/mercury')
def mercury():
	return render_template('mercury.html')

@app.route('/spacewiki/meteriote')
def meteriote():
	return render_template('meteriote.html')

@app.route('/spacewiki/milky')
def milky():
	return render_template('milky.html')

@app.route('/spacewiki/moon')
def moon():
	return render_template('moon.html')

@app.route('/spacewiki/nebulae')
def nebulae():
	return render_template('nebulae.html')

@app.route('/spacewiki/neptune')
def neptune():
	return render_template('neptune.html')

@app.route('/spacewiki/neutron')
def neutron():
	return render_template('neutron.html')

@app.route('/spacewiki/pulsar')
def pulsar():
	return render_template('pulsar.html')

@app.route('/spacewiki/quasar')
def quasar():
	return render_template('quasar.html')

@app.route('/spacewiki/saturn')
def saturn():
	return render_template('saturn.html')

@app.route('/spacewiki/star')
def star():
	return render_template('star.html')

@app.route('/spacewiki/starcon')
def starcon():
	return render_template('starcon.html')

@app.route('/spacewiki/supernova')
def supernova():
	return render_template('supernova.html')

@app.route('/spacewiki/universe')
def universe():
	return render_template('universe.html')

@app.route('/spacewiki/uranus')
def uranus():
	return render_template('uranus.html')

@app.route('/spacewiki/venus')
def venus():
	return render_template('venus.html')

