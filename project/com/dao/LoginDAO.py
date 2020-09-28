from project import db
from project.com.vo.LoginVO import LoginVO

class LoginDAO():
    def insertRegister(self, registerVO):
        db.session.add(registerVO)
        db.session.commit()

    def validateLogin(self, loginVO):
        loginVOList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername,
                                            loginPassword=loginVO.loginPassword)
        return loginVOList