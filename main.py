import flask
import pymysql
from app import app
from db_config import mysql
from flask import abort, jsonify
from flask import flash, request
from sqlReturn import *
from db_config import dataName
from utils import *
# from werkzeug import generate_password_hash, check_password_hash


# ---------------------------------------------------etudiants---------------------------------------------------------------------------------------------


# @app.route('/etudiants', methods=['GET'])
# def getStudetns():
#     try:
#         sql = "SELECT * FROM {0}.etudiant".format(dataName)
#         print(sql)
#         resp = requestSelect(sql=sql)
#         return resp
#     except Exception as e:
#         return constant.resquestErrorResponse(e)

'''
{
    "nom":"Doumbouya 6",
    "prenom":"Fode 6",
    "email":"doumbouyaf6.fode@gmail.com",
    "password":"1234",
    "tel":"0778847887",
    "role":"etudiant",
    "diplome_etudiant": "Master Développeur Full Stack",
    "id_filiere":1

}
'''


@app.route('/etudiant', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getStudetnById():
    if request.method == "GET":
        id = flask.request.values.get('id')
        try:
            if id == None:
                sql = "SELECT * FROM {0}.etudiant".format(
                    dataName)
            else:
                sql = "SELECT * FROM {0}.etudiant id_utilisateur={1}".format(
                    dataName, id)
            resp = requestSelect(sql=sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)
    if request.method == "POST" or request.method == "PUT":
        return manageUtilisateur(request)


@app.route('/etudiantNote/<int:id>', methods=['GET'])
def getStudetnNoteById(id):
    try:
        sql = "SELECT * FROM {0}.notes id_utilisateur={1}".format(dataName, id)
        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)


# ------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------Diplome---------------------------------------------------------------------------------------------


@app.route('/diplomes', methods=['GET'])
def getDiplomes():
    try:
        # sql select distinct all
        sql = "SELECT DISTINCT diplome_etudiant FROM {0}.etudiant".format(
            dataName)
        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)

# ------------------------------------------------------------------------------------------------------------------------------------------------


# # ---------------------------------------------------Filière---------------------------------------------------------------------------------------------


@app.route('/filieres', methods=['GET'])
def getFilieres():
    try:
        sql = "SELECT * FROM {0}.filiere".format(dataName)
        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)


@app.route('/etudiant/<int:id>/filiere', methods=['GET'])
def getStudentFiliere(id):
    try:
        # _json = request.json
        # id = _json["id"]
        sql = "SELECT DISTINCT * FROM {0}.filiere INNER JOIN {0}.etudiant on {0}.etudiant.id_filiere = {0}.filiere.id_filiere where {0}.etudiant.id_utilisateur= {1}".format(
            dataName, id)
        resp = requestSelect(sql=sql)
        # print(sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)

# ------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------Emploi du temps---------------------------------------------------------------------------


@app.route('/edt/<int:id>/etudiant', methods=['GET'])
def getEtudiantEDT(id):
    try:
        sql = "SELECT  * FROM {0}.edt INNER JOIN {0}.etudiant on {0}.etudiant.id_filiere = {0}.edt.id_filiere where {0}.etudiant.id_utilisateur= {1}".format(
            dataName, id)
        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)


# body
# {
#   "id_filiere":1,
#   "id_cours":1,
#   "date_debut": "2023-02-01 10:15:00",
#   "date_fin":"2023-02-5 10:15:00",
#   "type_cours":"td"
# }


@app.route('/add_edt', methods=['POST'])
def add_edt():
    if not request.json:
        abort(400)
    _json = request.json
    id_filiere = _json["id_filiere"]
    id_cours = _json["id_cours"]
    date_debut = _json["date_debut"]
    date_fin = _json["date_fin"]
    type_cours = _json["type_cours"]
    sql = "INSERT INTO {0}.edt (id_filiere,id_cours,date_debut,date_fin,type_cours) VALUES(%s,%s,%s,%s,%s)".format(
        dataName)
    data = (id_filiere, id_cours, date_debut, date_fin, type_cours)
    resp = insert(sql=sql, data=data)
    return resp


# ----------------------------------------------------Utilisateur -----------------------------------------------------------------------------------

@app.route('/utilisateur', methods=['GET'])
def getUtilisateur():
    id = flask.request.values.get('id')
    try:
        if id == None:
            sql = "SELECT  * FROM {0}.utilisateur ".format(
                dataName)
        else:
            sql = "SELECT  * FROM {0}.utilisateur  where {0}.utilisateur.id_utilisateur= {1}".format(
                dataName, id)

        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)


# @app.route('/utilisateur', methods=['PUT', 'POST'])
# def manageUtilisateur():
#     if not request.json:
#         abort(400)
#     _json = request.json
#     # ------------- Data --------------
#     if 'id' in _json:
#         id = _json['id']
#     nom = _json["nom"]
#     prenom = _json['prenom']
#     email = _json['email']
#     password = _json['password']
#     tel = _json['tel']
#     if 'role' in _json:
#         role = _json['role']

#     if request.method == 'PUT':
#         sql = "UPDATE {0}.utilisateur SET nom = '{1}', prenom = '{2}', email = '{3}', password = '{4}', tel = '{5}' where id_utilisateur= {6}".format(
#             dataName, nom, prenom, email, password, tel, id)
#         resp = update(sql)

#     if request.method == 'POST':
#         sql = "INSERT INTO {0}.utilisateur (role, nom, prenom, email, password, tel) VALUES(%s,%s,%s,%s,%s,%s)".format(
#             dataName)
#         data = (role, nom, prenom, email, password, tel)
#         resp = insert(sql=sql, data=data)
#     return resp


# ----------------------------------------------------notes-------------------------------------------------------------------------------------------------------------

# body
# {
#   "id_utilisateur":3,
#   "id_cours":1,
#   "note": "20"

# }

@app.route('/add_note', methods=['POST'])
def addNotes():
    if not request.json:
        abort(400)
    _json = request.json
    id_utilisateur = _json["id_utilisateur"]
    id_cours = _json["id_cours"]
    note = _json["note"]
    sql = "INSERT INTO {0}.note (id_utilisateur,id_cours,note) VALUES(%s,%s,%s)".format(
        dataName)
    data = (id_utilisateur, id_cours, note)
    resp = insert(sql=sql, data=data)
    return resp

# id = flask.request.values.get('id')
#     if id == None:
#         return constant.resquestErrorResponse(msg="Cette request a besoin d'un id")


@app.route('/delete_note<int:id>', methods=['GET'])
def DeleteNote(id):

    try:
        sql = "DELETE FROM {0}.note WHERE id_note = {1}".format(
            dataName, id)
        resp = requestSelect(sql=sql)
        return resp
    except Exception as e:
        return constant.resquestErrorResponse(e)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------Cours-------------------------------------------------------------------------------------------------------------


@app.route('/cours', methods=['GET', 'POST', 'PUT', 'DELETE'])
def cours():
    if request.method == 'GET':
        id = flask.request.values.get('id')
        try:
            if id == None:
                sql = "SELECT * from {0}.cours".format(dataName)
            else:
                sql = "SELECT * from {0}.cours where id_cours = {1}".format(
                    dataName, id)
            resp = requestSelect(sql=sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)
    if request.method == 'POST':
        if not request.json:
            abort(400)
        _json = request.json
        # id_cours = _json['id_cours']
        id_enseignant = _json['id_enseignant']
        id_ue = _json['id_ue']
        try:
            sql = "INSERT INTO {0}.cours ( id_enseignant, id_ue) VALUES(%s,%s)".format(
                dataName)
            data = (id_enseignant, id_ue)
            resp = insert(sql=sql, data=data)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)

    if request.method == 'PUT':
        if not request.json:
            abort(400)
        try:
            _json = request.json
            id_cours = _json['id_cours']
            id_enseignant = _json['id_enseignant']
            id_ue = _json['id_ue']
            sql = "UPDATE {0}.cours SET id_enseignant = '{1}', id_ue = '{2}' where id_cours= {3}".format(
                dataName, id_enseignant, id_ue, id_cours)
            resp = update(sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)

    if request.method == 'DELETE':
        try:
            sql = "DELETE FROM {0}.cours WHERE id_cours = {1}".format(
                dataName, id)
            resp = requestSelect(sql=sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)


# ----------------------------------------------------enseignant-------------------------------------------------------------------------------------------------------------
'''
{
    "nom":"Doumbouya 9",
    "prenom":"Fode 9",
    "email":"doumbouyaf9.fode@gmail.com",
    "password":"1234",
    "tel":"0778847887",
    "role":"enseignant",
    "responsabilite_ens": "Professeur",
    "volume_horaire":150

}
'''


@app.route('/enseignant', methods=['GET', 'POST', 'PUT', 'DELETE'])
def enseignant():
    if request.method == 'GET':
        id = flask.request.values.get('id')
        try:
            if id == None:
                sql = "SELECT * from {0}.enseignant".format(dataName)
            else:
                sql = "SELECT * from {0}.enseignant where id_utilisateur = {1}".format(
                    dataName, id)
            resp = requestSelect(sql=sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)
    if request.method == "POST" or request.method == "PUT":
        return manageUtilisateur(request)
    # if request.method == 'POST':
    #     if not request.json:
    #         abort(400)
    #     _json = request.json
    #     id_utilisateur = _json['id_utilisateur']
    #     responsabilite_ens = _json['responsabilite_ens']
    #     volume_horaire = _json['volume_horaire']
    #     try:
    #         sql = "INSERT INTO {0}.enseignant (id_utilisateur, responsabilite_ens, volume_horaire) VALUES(%s,%s,%s)".format(
    #             dataName)
    #         data = (id_utilisateur, responsabilite_ens, volume_horaire)
    #         resp = insert(sql=sql, data=data)
    #         return resp
    #     except Exception as e:
    #         return constant.resquestErrorResponse(e)

    if request.method == 'PUT':
        if not request.json:
            abort(400)
        try:
            _json = request.json
            id_utilisateur = _json['id_utilisateur']
            responsabilite_ens = _json['responsabilite_ens']
            volume_horaire = _json['volume_horaire']
            sql = "UPDATE {0}.enseignant SET responsabilite_ens = '{1}', volume_horaire = '{2}' where id_utilisateur= {3}".format(
                dataName, responsabilite_ens, volume_horaire, id_utilisateur)
            resp = update(sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)

    if request.method == 'DELETE':
        try:
            sql = "DELETE FROM {0}.enseignant WHERE id_utilisateur = {1}".format(
                dataName, id)
            resp = requestSelect(sql=sql)
            return resp
        except Exception as e:
            return constant.resquestErrorResponse(e)
# ---------------------------------------------------NO FOUND ERROR ---------------------------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=80)
