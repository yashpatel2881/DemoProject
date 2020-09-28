from project import db

class GroupVO(db.Model):
    __tablename__ = 'groupmaster'
    memberId = db.Column('memberId', db.Integer, primary_key = True, autoincrement = True)
    memberUsername = db.Column('memberUsername', db.String(122), nullable=False)
    memberFirstname = db.Column('memberFirstname', db.String(122), nullable=False)
    memberLastname = db.Column('memberLastname', db.String(122), nullable = False)
    groupName = db.Column('groupName', db.String(122), nullable= False)

    def as_dict(self):
        return {
            'memberId': self.memberId,
            'memberUsername': self.memberUsername,
            'memberFirstname': self.memberFirstname,
            'memberLastname': self.memberLastname,
            'groupName': self.groupName
        }

db.create_all()