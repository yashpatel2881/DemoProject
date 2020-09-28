from project import app
from flask import render_template,request,redirect
from project.com.vo.RegisterVO import RegisterVO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.GroupVO import GroupVO
from project.com.dao.GroupDAO import GroupDAO

@app.route('/', methods=['GET'])
def loadLoginPage():
    try:
        return render_template('Login.html')

    except Exception as ex:
        print(ex)

@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        print("*******************")
        loginVO = LoginVO()
        loginDAO = LoginDAO()

        username = request.form['username']
        password = request.form['password']

        print(username)
        print(password)

        loginVO.loginUsername = username
        loginVO.loginPassword = password

        loginVOList = loginDAO.validateLogin(loginVO)

        loginDictList = [i.as_dict() for i in loginVOList]
        lenLoginDictList = len(loginDictList)
        print(loginDictList)

        if lenLoginDictList == 0:

                msg = 'Username and Password is Incorrect !'

                return render_template('Login.html', error=msg)

        else:
            for i in loginDictList:
                if i['loginUsername'] == username or i['loginPassword'] == password:
                    return render_template('index.html')

                else:
                    msg1 = 'You are Inactive user !'

                    return render_template('Login.html', error=msg1)


    except Exception as ex:
        print(ex)

@app.route('/register', methods=["GET"])
def loadRegisterPage():
    try:
        return render_template('Register.html')

    except Exception as ex:
        print(ex)

@app.route('/insertRegister', methods=['POST'])
def insertRegister():
    try:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']

        registerVO = RegisterVO()
        registerDAO = RegisterDAO()

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        registerVO.registerFirstname = firstname
        registerVO.registerLastname = lastname
        registerVO.registerUsername = username
        registerVO.registerPassword = password

        loginVO.loginUsername = username
        loginVO.loginPassword = password

        registerDAO.insertRegister(registerVO)
        loginDAO.insertRegister(loginVO)

        return render_template('Login.html')

    except Exception as ex:
        print(ex)


@app.route('/loadcreateGroup', methods=["GET"])
def loadcreateGroup():
    try:
        return render_template('createGroup.html')

    except Exception as ex:
        print(ex)

@app.route('/insertGroup', methods=['POST'])
def insertGroup():
    try:

        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        groupName = request.form['groupName']

        groupVO = GroupVO()
        groupDAO = GroupDAO()

        groupVO.memberFirstname = firstname
        groupVO.memberLastname = lastname
        groupVO.memberUsername = username
        groupVO.groupName = groupName

        groupDAO.insertGroup(groupVO)

        return render_template('viewGroup.html')


    except Exception as ex:
        print(ex)
