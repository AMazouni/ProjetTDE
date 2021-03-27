import json
import os
import random

from django.core.files.storage import FileSystemStorage
from jsonschema import validate, Draft7Validator
from DjangoProject import settings
from DjangoProject.settings import BASE_DIR




def openUploadedfile(path) -> str:

    f = open(path,encoding='utf-8')
    content = f.read()

    return content

def is_json(path) -> bool:


    try:

        json_object = json.loads(openUploadedfile(path))

    except ValueError as e:
        print(str(e))
        os.remove(path)
        return False
    return True

import jsonschema
def jsonschemavalidate(path) :
    input = openUploadedfile(path)
    ins=json.loads(input)
    if 'validate' in ins:
        if ins['validate']==False :
            return True
    try :
      validate(instance=ins,schema=JSON_SCHEMA)
      print('succeess ???')
      return True
    except Exception as es :
        print(type(es))
        print(str(es))
        return str(es)



########################################################################
from lxml import etree


tei_root = etree.Element('TEI')

def getDict(path) :
    input = openUploadedfile(path)
    ins=json.loads(input)
    return ins

def addAttr(listattr, element):
    for a in listattr:
        if ('name' in a) and ('value' in a):
            element.set(a['name'], a['value'])

def addGlobAttr(listattr):
    global tei_root

    addAttr(listattr,tei_root)

def addContent(list, parent):
    for c in list :
        if 'elementName' in c :
            element = etree.SubElement(parent,c['elementName'])
            if 'attr' in c:
                addAttr(c['attr'],element)
            if 'content' in c :
                addContent(c['content'],element)
        elif 'text' in c:
            parent.text = c['text']


def createPubStmt(dic, tei_header : etree.Element):
    tei_pubStmt = etree.SubElement(tei_header,'publicationStmt')
    if 'attr' in dic:
        addAttr(dic['attr'], tei_pubStmt)
    if 'addContent' in dic :
         addContent(dic['addContent'],tei_pubStmt)


def createRespStmt(dic,tei_titleStmt):
    tei_RespStmt = etree.SubElement(tei_titleStmt,'respStmt')
    if 'resp' in dic:
        resp= etree.SubElement(tei_RespStmt,'resp')
        resp.text = dic['resp']
    if 'name' in dic:
        name= etree.SubElement(tei_RespStmt,'name')
        name.text = dic['name']
    if 'addContent' in dic:
        addContent(dic['addContent'],tei_RespStmt)


def createTitleStmt(dic, tei_filedesc):
    tei_titlestmt = etree.SubElement(tei_filedesc, 'titleStmt')
    if 'title' in dic:
        tei_title= etree.SubElement(tei_titlestmt,'title')
        tei_title.text = dic['title']
    if 'respStmt' in dic :
        createRespStmt(dic['respStmt'],tei_titlestmt)
    if 'attr' in dic:
        addAttr(dic['attr'], tei_titlestmt)
    if 'addContent' in dic:
        addContent(dic['addContent'], tei_titlestmt)


def createSourceDesc(dic, tei_filedesc):
    tei_sourceDesc = etree.SubElement(tei_filedesc,'sourceDesc')
    if 'attr' in dic:
        addAttr(dic['attr'], tei_sourceDesc)
    if 'addContent' in dic:
        addContent(dic['addContent'],tei_sourceDesc)


def createFileDesc(dic, tei_header):
    tei_filedesc= etree.SubElement(tei_header,'fileDesc')
    if 'attr' in dic:
        addAttr(dic['attr'], tei_filedesc)
    if 'titleStmt' in dic:
        createTitleStmt(dic['titleStmt'],tei_filedesc)
    if 'publicationStmt' in dic:
        print("pubstmt found")
        createPubStmt(dic['publicationStmt'], tei_filedesc)
    if 'sourceDesc' in dic:
        createSourceDesc(dic['sourceDesc'],tei_filedesc)
    if 'addContent' in dic:
        addContent(dic['addContent'],tei_filedesc)


def createHeader(dic):
     tei_header= etree.SubElement(tei_root,'teiHeader')
     if 'attr' in dic:
         addAttr(dic['attr'], tei_header)
     if 'fileDesc' in dic :
         createFileDesc(dic['fileDesc'],tei_header)
     if 'addContent' in dic:
         addContent(dic['addContent'], tei_header)




##############################################################################################




def createXml(path) :
    global tei_root
    tei_root = etree.Element('TEI')
    try :
        dic = getDict(path)


        if 'globAttr' in dic:
            print('adding globAttr')
            addGlobAttr(dic['globAttr'])
        if 'teiHeader' in dic:
             print('adding Header')
             createHeader(dic['teiHeader'])
             createText(dic['text'])
        print(etree.tostring(tei_root, pretty_print=True, encoding='unicode'))
    except Exception as ex :
        str(ex)
        tei_root = etree.Element("TEI")
        return False,str(ex)
    return True, etree.tostring(tei_root, pretty_print=True, encoding='unicode')

########################################################################
def createText(dic):
    tei_text = etree.SubElement(tei_root,'text')

    if 'front' in dic:
        tei_front = etree.SubElement(tei_text,'front')
        if 'content' in dic['front']:
            addContent(dic['front']['content'],tei_front)
    if 'body' in dic:
        tei_body = etree.SubElement(tei_text,'body')
        if 'content' in dic['body']:
            addContent(dic['body']['content'],tei_body)
    if 'back' in dic:
        tei_back = etree.SubElement(tei_text,'back')
        if 'content' in dic['back']:
            addContent(dic['back']['content'],tei_back)

#####################################################################
##################### STRUCTURE #####################################
#####################################################################
TEI_STRUCT={
    'validate': False,
    'globAttr':[{
        'name':"%attr.name%",
        'value':"%attr.value%"
    },
    {
        'name':"%attr.name%",
        'value':"%attr.value%"
    }
    ],
    'teiHeader':{
       'attr':[],
       'fileDesc':{
          'attr':[],
          'titleStmt':{
              'title':"title",
              'respStmt':{
                  'resp':"%StatementOfResponsability%",
                  'name':"%name%",
                  'addContent':[]
              }

          },
          'sourceDesc':{
            'addContent':[{"elementName":"%notEmpty%"}]
          },
          'publicationStmt':{
             'addContent':[{"elementName":"%notEmpty%"}]
          }
       },
       'addContent':[
           {
            'elementName':"%name%",
            'attr':[],
            'content':[
                    {'text':"%textNode%"},
                    {'elementName':"%name%"}
                ]
           }
           ]
    },
    'text':{
       'front':{},
       'body':{
           'attr':[],
           'content':[]
       },
       'back':{}

    }
}

########################################################################
##################################JSON_MIN
########################################################################
MIN_JSON={
    "validate": True,
    "globAttr": [
    ],
    "teiHeader": {
        "fileDesc": {
            "titleStmt": {
                "title": "Title PlaceHolder"

            },
            "sourceDesc": {
                "addContent": [{"elementName": "MandatorySubElement"}]
            },
            "publicationStmt": {
                "addContent": [{"elementName": "MandatorySubElement"}]
            }
        },
        "addContent": [

        ]
    },
    "text": {
        "front": {

        },
        "body": {

            "content": [

            ]
        },
        "back": {

        }
    }
}

########################################################################
#####################JSON SCHEMA##############################
#####################################################################
JSON_SCHEMA={
    "$schema": "http://json-schema.org/draft-07/schema",

    "type": "object",
    "title": "TEI JSON Schema",
    "description": "Json structure to create a minimal TEI document.",
    "default": {},
"definitions" : {
    "Attr" : {
      "type" : "object",
      "properties" : {
        "name" : {
          "type" : "string"
        },
        "value" : {
          "type" : "string"
        }
      },
      "required" : [ "name", "value" ]
    },
    "Element" : {
      "type" : "object",
      "properties" : {
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "content" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Node"
          }
        },
        "elementName" : {
          "type" : "string"
        }
      },
      "required" : [ "elementName" ]
    },
    "FileDesc" : {
      "type" : "object",
      "properties" : {
        "addContent" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "publicationStmt" : {
          "$ref" : "#/definitions/PublicationStmt-nullable"
        },
        "sourceDesc" : {
          "$ref" : "#/definitions/SourceDesc-nullable"
        },
        "titleStmt" : {
          "$ref" : "#/definitions/TitleStmt-nullable"
        }
      },
      "required" : [ "titleStmt","publicationStmt","sourceDesc" ]
    },
    "NamedElement" : {
      "type" : "object",
      "properties" : {
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "content" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Node"
          }
        }
      }
    },
    "NamedElement-nullable" : {
      "anyOf" : [ {
        "type" : "null"
      }, {
        "$ref" : "#/definitions/NamedElement"
      } ]
    },
    "Node" : {
      "type" : "object"
    },
    "PublicationStmt-nullable" : {
      "type" : [ "object", "null" ],
      "properties" : {
        "addContent" : {
          "minItems" : 1,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        }
      },
      "required" : [ "addContent" ]
    },
    "RespStmt" : {
      "type" : "object",
      "properties" : {
        "addContent" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "name" : {
          "type" : "string"
        },
        "resp" : {
          "type" : "string"
        }
      },
      "required" : [ "name", "resp" ]
    },
    "SourceDesc-nullable" : {
      "type" : [ "object", "null" ],
      "properties" : {
        "addContent" : {
          "minItems" : 1,
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        }
      },
      "required" : [ "addContent" ]
    },
    "TeiHeader" : {
      "type" : "object",
      "properties" : {
        "addContent" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "fileDesc" : {
          "$ref" : "#/definitions/FileDesc"
        }
      },
      "required" : [ "fileDesc" ]
    },
    "Text" : {
      "type" : "object",
      "properties" : {
        "addContent" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "back" : {
          "$ref" : "#/definitions/NamedElement-nullable"
        },
        "body" : {
          "$ref" : "#/definitions/NamedElement"
        },
        "front" : {
          "$ref" : "#/definitions/NamedElement-nullable"
        }
      },
      "required" : [ "body" ]
    },
    "TitleStmt-nullable" : {
      "type" : [ "object", "null" ],
      "properties" : {
        "addContent" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Element"
          }
        },
        "attr" : {
          "type" : [ "array", "null" ],
          "items" : {
            "$ref" : "#/definitions/Attr"
          }
        },
        "respStmt" : {
          "$ref" : "#/definitions/RespStmt"
        },
        "title" : {
          "type" : "string"
        }
      },
      "required" : [ "title" ]
    }
  },
  "type" : "object",
  "properties" : {
    "globAttr" : {
      "type" : [ "array", "null" ],
      "items" : {
        "$ref" : "#/definitions/Attr"
      }
    },
    "teiHeader" : {
      "$ref" : "#/definitions/TeiHeader"
    },
    "text" : {
      "$ref" : "#/definitions/Text"
    },
    "validate" : {
      "type" : "boolean"
    }
  },
  "required" : [ "teiHeader", "text" ]
}



