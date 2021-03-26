import json
import os

from DjangoProject import settings


def is_json(name) -> bool:
    print(settings.BASE_DIR)
    print(name)
    f = open(settings.BASE_DIR / name)
    content = f.read()
    try:
        json_object = json.loads(content)
        print(json_object)
    except ValueError as e:
        os.remove(settings.BASE_DIR / name)
        return False
    return True
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



