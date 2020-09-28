from project import db

class RegisterVO(db.Model):
    __tablename__ = 'registermaster'
    registerId = db.Column('registerId', db.Integer, primary_key = True, autoincrement = True)
    registerUsername = db.Column('registerUsername', db.String(122), nullable=False)
    registerFirstname = db.Column('registerFirstname', db.String(122), nullable=False)
    registerLastname = db.Column('registerLastname', db.String(122), nullable = False)
    registerPassword = db.Column('registerPassword', db.String(122), nullable= False)

    def as_dict(self):
        return {
            'registerId': self.registerId,
            'registerUsername': self.registerUsername,
            'registerFirstname': self.registerFirstname,
            'registerLastname': self.registerLastname,
            'registerPassword': self.registerPassword
        }

db.create_all()