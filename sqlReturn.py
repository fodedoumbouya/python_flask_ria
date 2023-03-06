from db_config import mysql
from flask import Response, jsonify
import constant


def getOnlyData(sql) -> list:
    data = []
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        # Get the column names for the table
        column_names = [description[0] for description in cursor.description]
    # Create a list of dictionaries, where each dictionary represents a row in the table
        data = [dict(zip(column_names, row)) for row in rows]

        # column_names = [i[0] for i in cursor.description]
        # for row in rows:
        #     row_data = {}
        #     print("row: ", row)
        #     for i in range(len(column_names)):
        #         row_data[column_names[i]] = row[i]
        #         print("row_data: ", row_data)

        #         data.append(row_data)
    finally:
        cursor.close()
        conn.close()
    return data


def requestSelect(sql) -> Response:
    data = getOnlyData(sql)
    resp = jsonify(constant.requestRespond(
        m="data",
        data=data, code=200))
    resp.status_code = 200
    return resp


def update(sql):
    resp = jsonify(constant.requestRespond(
        data="Table update Failed!", code=400))
    resp.status_code = 400
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        resp = jsonify(constant.requestRespond(
            data="Table updated successfully!", code=200))
        resp.status_code = 200
    finally:
        cursor.close()
        conn.close()
    return resp


def insert(sql, data):
    resp = jsonify(constant.requestRespond(
        data="Table insert Failed!", code=400))
    resp.status_code = 400
    id = -1
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        f = cursor.execute(sql, data)
        d = conn.commit()
        # print("insert Result ", d, f, )
        id = cursor.lastrowid
        resp = jsonify(constant.requestRespond(
            data="Table inserted successfully!", code=200))
        resp.status_code = 200
    finally:
        cursor.close()
        conn.close()
    return resp, id


def delete(sql):
    resp = jsonify(constant.requestRespond(
        data="Table delete Failed!", code=400))
    resp.status_code = 400
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        resp = jsonify(constant.requestRespond(
            data="Table deleted successfully!", code=200))
        resp.status_code = 200
    finally:
        cursor.close()
        conn.close()
    return resp
