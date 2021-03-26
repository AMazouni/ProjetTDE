import json
import os
import random

from django.core.files.storage import FileSystemStorage
from jsonschema import validate
from DjangoProject import settings
from DjangoProject.settings import BASE_DIR




def openUploadedfile(path) -> str:
    print(path)
    f = open(path)
    content = f.read()
    return content

def is_json(path) -> bool:
    print(settings.BASE_DIR)
    print(path)

    try:
        print("here")
        json_object = json.loads(openUploadedfile(path))
        print(json_object)
    except ValueError as e:
        print(str(e))
        os.remove(path)
        return False
    return True

def jsonschemavalidate(path) :
    input = openUploadedfile(path)
    ins=json.loads(input)
    if 'validate' in ins:
        if ins['validate']==False :
            return True
    try :
      validate(instance=ins,schema=JSON_SCHEMA)
      return True
    except Exception as es :
        return str(es)



########################################################################
from lxml import etree

def getDict(path) :
    input = openUploadedfile(path)
    ins=json.loads(input)
    return ins


def createHeader(dic):
     tei_header= etree.Element('teiHeader')
     return tei_header



def createXml(path) :
    dic = getDict(path)
    print(dic)
    print(type(dic))
    print('validate' in dic)
    print(dic['validate'])
    tei_root = etree.Element('tei')
    if 'globAttr' in dic :
        print()
    if 'teiHeader' in dic :
       print()
    print("")



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
#####################JSON SCHEMA##############################
#####################################################################
JSON_SCHEMA={
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "localhost:8000/json/jsonschema",
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
      }
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
      "required" : [ "respStmt", "title" ]
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



