
from flask import abort, jsonify
from db_config import dataName
from sqlReturn import *


def manageUtilisateur(request) -> Response:
    try:
        if not request.json:
            abort(400)
        _json = request.json
        # ------------- Data --------------
        if 'id' in _json:
            id = _json['id']
        nom = _json["nom"]
        prenom = _json['prenom']
        email = _json['email']
        password = _json['password']
        tel = _json['tel']
        if 'role' in _json:
            role = _json['role']
        if request.method == 'PUT':
            sql = "UPDATE {0}.utilisateur SET nom = '{1}', prenom = '{2}', email = '{3}', password = '{4}', tel = '{5}' where id_utilisateur= {6}".format(
                dataName, nom, prenom, email, password, tel, id)
            resp = update(sql)

        if request.method == 'POST':

            sql = "INSERT INTO {0}.utilisateur (role, nom, prenom, email, password, tel) VALUES(%s,%s,%s,%s,%s,%s)".format(
                dataName)
            data = (role, nom, prenom, email, password, tel)
            if checkParams(_json):
                resp = insert(sql=sql, data=data)
                return createStudentOrTeacher(_json, resp[1])[0]
            else:
                return constant.resquestErrorResponse("Les donnees ne sont pas correcte")
    except Exception as e:
        return constant.resquestErrorResponse(e)


def checkParams(_json):
    if "role" in _json:
        if _json['role'] == "etudiant":
            if "diplome_etudiant" or "id_filiere" in _json:
                return True
            else:
                return False
        if _json['role'] == "enseignant":
            if "responsabilite_ens" or "volume_horaire" in _json:
                return True
            else:
                return False
    else:
        return False


def createStudentOrTeacher(_json, id):
    try:
        if _json['role'] == "etudiant":
            sql = "INSERT INTO {0}.etudiant(id_utilisateur, diplome_etudiant, id_filiere) VALUES(%s,%s,%s)".format(
                dataName)
            data = (id,
                    _json["diplome_etudiant"], _json["id_filiere"])
            resp = insert(sql=sql, data=data)
            return resp
        if _json["role"] == "enseignant":
            sql = "INSERT INTO {0}.enseignant(id_utilisateur, responsabilite_ens, volume_horaire) VALUES(%s,%s,%s)".format(
                dataName)
            data = (id,
                    _json["responsabilite_ens"], _json["volume_horaire"])
            resp = insert(sql=sql, data=data)
            return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)
