from project import db

class GroupDAO():
    def insertGroup(self, groupVO):
        db.session.add(groupVO)
        db.session.commit()

