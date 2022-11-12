#!/usr/bin/python

#common project core
from types import FunctionType
from enum import Enum
from threading import Thread

class Class(Enum):
    FATAL = "FATAL"
    RECOVERABLE = "RECOVERABLE"
    WARN = "WARN"

def create_exception(Class:Enum,function:str,parameters:list,message:str)->Exception:
    exception=f"Error! Class: {Class}: Function: {function}: Parameters: {parameters}: Message: {message}"
    if Class.value==Class.FATAL.value:
        raise Exception(exception)
    else:
        print(exception)

def type_check(variable:any,expect:any)->bool:
    if type(variable) == expect:
        return True
    else:
        create_exception(Class=Class.WARN,function="type_check()",parameters=[variable,expect],message="Variable failed type check!")
        return False

def type_require(variable:any,expect:any)->bool:
    if type(variable) == expect:
        return True
    else:
        create_exception(Class=Class.FATAL,function="type_require()",parameters=[variable,expect],message="Variable failed type requirement!")   

def create_thread(function:FunctionType,parameters:list)->Thread:
    try: 
        return Thread(target=function, paramaters=parameters)
    except Exception as exception:
        create_exception(Class=Class.FATAL,function="create_thread()",parameters=parameters,message=exception)

def read(path:str,arg:str)->any:
    type_require(path,str)
    type_require(arg,str)
    try:
        file = open(path,arg)
        data:str = file.read()
        file.close()
    except Exception as exception:
        create_exception(Class=Class.FATAL,function="read()",parameters=[path,arg],message=exception)
    return data

def write(path:str,arg:str,data:any)->bool:
    type_require(path,str)
    type_require(arg,str)
    try:
        file = open(path,arg)
        data:str = file.write(data)
        file.close()
    except Exception as exception:
        create_exception(Class=Class.FATAL,function="write()",parameters=[path,arg,"File data not included in parameter printout!"],message=exception)
    return True

def sort_dict(data:dict,reverse:bool=True):
    type_require(data,dict)
    type_require(reverse,bool)
    tmp:dict={}
    for key in sorted(data,key=data.get,reverse=reverse):
        tmp[key]=data[key]
    return tmp