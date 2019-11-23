"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class PyhtmlTemplate :
    _CODE_CONTENT_DEBUG = ...

    def __init__(self) :
    	"""
    	- None
    	"""
    	...

    def OnRequest(self, microWebSrv2, request) :
    	"""
    	- microWebSrv2
    	- request
    	"""
    	...

    def SetGlobalVar(self, globalVarName, globalVar) :
    	"""
    	- globalVarName
    	- globalVar
    	"""
    	...

    def GetGlobalVar(self, globalVarName) :
    	"""
    	- globalVarName
    	"""
    	...

    @property
    def ShowDebug(self) :
    	"""
    	- None
    	"""
    	...

    @ShowDebug.setter
    def ShowDebug(self, value) :
    	"""
    	- value
    	"""
    	...

class CodeTemplateException(Exception) :
    pass

class CodeTemplate :
    TOKEN_OPEN              = ...
    TOKEN_CLOSE             = ...
    TOKEN_OPEN_LEN          = ...
    TOKEN_CLOSE_LEN         = ...

    INSTRUCTION_PYTHON      = ...
    INSTRUCTION_IF          = ...
    INSTRUCTION_ELIF        = ...
    INSTRUCTION_ELSE        = ...
    INSTRUCTION_FOR         = ...
    INSTRUCTION_END         = ...

    RE_IDENTIFIER           = ...


    def __init__(self, code, escapeStrFunc=None) :
    	"""
    	- code
    	- escapeStrFunc
    	"""
    	...

    def Validate(self, pyGlobalVars=None, pyLocalVars=None) :
    	"""
    	- pyGlobalVars
    	- pyLocalVars
    	"""
    	...

    def Execute(self, pyGlobalVars=None, pyLocalVars=None) :
    	"""
    	- pyGlobalVars
    	- pyLocalVars
    	"""
    	...

    def _parseCode(self, pyGlobalVars, pyLocalVars, execute) :
    	"""
    	- pyGlobalVars
    	- pyLocalVars
    	- execute
    	"""
    	...

    def _parseBloc(self, execute) :
    	"""
    	- execute
    	"""
    	...

    def _processToken(self, tokenContent, execute) :
    	"""
    	- tokenContent
    	- execute
    	"""
    	...

    def _processInstructionPYTHON(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionIF(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionELIF(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionELSE(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionFOR(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionEND(self, instructionBody, execute) :
    	"""
    	- instructionBody
    	- execute
    	"""
    	...
