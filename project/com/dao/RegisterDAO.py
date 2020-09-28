from project import db

class RegisterDAO():
    def insertRegister(self, registerVO):
        db.session.add(registerVO)
        db.session.commit()