from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)
    
    
# MODELS GO BELOW 

# we need to inherit from db.Model coming from SQLAlchemy that includes methods 

# next we create the table name 

# after that we move into definig the indiviual columns  
# id its the first , we call db.Column this is coming from SQLAlchemy ; then we specify a type in this case an integer (db.Integer)
# primary_key=True is just PRIMARY KEY from postgres UNIQUE NOT NULL 
#   autoincrement=True) is just SERIAL  from postgres
# next name=db.Column 
# db.String(50) is s string with a limit of 50 characters
# nullable=False is just NOT NULL  

# to create the table isnide ipython 
# %run app.py
# db.create_all()
# we can write it in this file but is something we do rarely  
class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     unique=True)
    species = db.Column(db.String(30), nullable=True)
    hunger = db.Column(db.Integer, nullable=False, default=20)

    def greet(self):
        """Greet using name."""

        return f"I'm {self.name} the {self.species or 'thing'}"

    def feed(self, units=10):
        """Nom nom nom."""

        self.hunger -= units
        self.hunger = max(self.hunger, 0)

    def __repr__(self):
        """Show info about pet."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.hunger}>"

    @classmethod
    def get_by_species(cls, species):
        """Get all pets matching that species."""

        return cls.query.filter_by(species=species).all()
