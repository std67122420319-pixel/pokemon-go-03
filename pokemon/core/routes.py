from flask import Blueprint, render_template,render_template_string

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pokemons = db.paginate(db.select(Pokemon), per_page=10, page=page)
    return render_template('core/home.html',
                           title='Home Page',
                           page=page,
                           pokemons=pokemons)