from django.shortcuts import render
from calculator.calculate import doCal
import re
import logging


def cal(request):
    try:
        val = request.GET["btn"]
        tmp1 = request.GET["test1"]
        tmpop = request.GET["testop"]
        tmp2 = request.GET["test2"]
        area = helper(val, tmp1, tmpop, tmp2)
    except Exception:
        dic = {'display': '0', "help1": '', "helpop": '', "help2": ''}
        return render(request, 'interface.html', dic)
    return render(request, 'interface.html', area)


def helper(val, tmp1, tmpop, tmp2):
    if re.match('^[0-9\-]$', val):
        if val == '-' and tmp1 == '' and tmpop == '' and tmp2 == '':
            tmp1 = tmp1 + val
            return {"display": '0', "help1": tmp1, "helpop": tmpop, "help2": tmp2}
        elif val == '-' and '-' in tmp1 and tmpop == '' and tmp2 == '':
            return {"display": tmp1, "help1": tmp1, "helpop": val, "help2": tmp2}
        elif val == '-' and '-' not in tmp1 and tmpop == '' and tmp2 == '':
            return place_op(val, tmp1, tmp2)
        elif val == '-' and tmp1 != '' and tmpop != '':
            if tmp2 == '':
                return put_second(val, tmp1, tmpop, tmp2)
            elif tmp2 == '-0':
                return erroMeg()
            return calNemp(val, tmp1, tmpop, tmp2)

        if re.match('^[0-9]$', val):
            if tmpop != '':
                if tmp1 != '':
                    return put_second(val, tmp1, tmpop, tmp2)
                else:
                    return erroMeg()
            return {"display": tmp1 + val, "help1": tmp1 + val, "helpop": tmpop, "help2": tmp2}
    elif re.match('^[\+\×\÷]$', val):
        if tmp1 == '':
            return erroMeg()
        elif tmpop != '':
            if tmpop == '÷' and (tmp2 == '0' or tmp2 == '-0'):
                return erroMeg()
            # user may switch if she wants to change the sign on their choice of +, x, /.
            # Due to the possible changes of an equation meant,
            # changing sign upon an exisiting '-' operator is not allowed. Calculation will continue -> num - (-num)
            elif tmpop != '-' and tmp2 == '':
                return place_op(val, tmp1, tmp2)
            return calNemp(val, tmp1, tmpop, tmp2)
        return place_op(val, tmp1, tmp2)
    elif val == '=':
        if tmpop == '÷' and (tmp2 == '0' or tmp2 == '-0'):
            return erroMeg()
        elif tmp1 != '' and tmpop == '' and tmp2 == '':
            return {"display": tmp1, "help1": '', "helpop": '', 'help2': ''}
        return calNemp_equal(tmp1, tmpop, tmp2)


def put_second(val, tmp1, tmpop, tmp2):
    return {"display": tmp2 + val, "help1": tmp1, "helpop": tmpop, "help2": tmp2 + val}


def calNemp(val, tmp1, tmpop, tmp2):
    tmp1 = doCal(tmp1, tmpop, tmp2)
    return {"display": tmp1, "help1": tmp1, "helpop": val, "help2": ''}


def calNemp_equal(tmp1, tmpop, tmp2):
    tmp1 = doCal(tmp1, tmpop, tmp2)
    return {"display": tmp1, "help1": '', "helpop": '', "help2": ''}


def erroMeg():
    return {"display": 'Error, reset to 0', "help1": '', "helpop": '', "help2": ''}


def place_op(val, tmp1, tmp2):
    return {"display": tmp1, "help1": tmp1, "helpop": val, "help2": tmp2}
