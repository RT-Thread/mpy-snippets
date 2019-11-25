"""
The MIT License (MIT)
Copyright © 2019 Jean-Christophe Bos & HC² (www.hc2.fr)
"""

class PyhtmlTemplate :
    _CODE_CONTENT_DEBUG = ...

    def __init__(self) :
    	"""
    	__init__
    	
    	- None
    	"""
    	...

    def OnRequest(self, microWebSrv2, request) :
    	"""
    	OnRequest
    	
    	- microWebSrv2
    	- request
    	"""
    	...

    def SetGlobalVar(self, globalVarName, globalVar) :
    	"""
    	SetGlobalVar
    	
    	- globalVarName
    	- globalVar
    	"""
    	...

    def GetGlobalVar(self, globalVarName) :
    	"""
    	GetGlobalVar
    	
    	- globalVarName
    	"""
    	...

    @property
    def ShowDebug(self) :
    	"""
    	ShowDebug
    	
    	- None
    	"""
    	...

    @ShowDebug.setter
    def ShowDebug(self, value) :
    	"""
    	ShowDebug
    	
    	- value
    	"""
    	...

class CodeTemplateException(Exception) :
    ...

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
    	__init__
    	
    	- code
    	- escapeStrFunc
    	"""
    	...

    def Validate(self, pyGlobalVars=None, pyLocalVars=None) :
    	"""
    	Validate
    	
    	- pyGlobalVars
    	- pyLocalVars
    	"""
    	...

    def Execute(self, pyGlobalVars=None, pyLocalVars=None) :
    	"""
    	Execute
    	
    	- pyGlobalVars
    	- pyLocalVars
    	"""
    	...

    def _parseCode(self, pyGlobalVars, pyLocalVars, execute) :
    	"""
    	_parseCode
    	
    	- pyGlobalVars
    	- pyLocalVars
    	- execute
    	"""
    	...

    def _parseBloc(self, execute) :
    	"""
    	_parseBloc
    	
    	- execute
    	"""
    	...

    def _processToken(self, tokenContent, execute) :
    	"""
    	_processToken
    	
    	- tokenContent
    	- execute
    	"""
    	...

    def _processInstructionPYTHON(self, instructionBody, execute) :
    	"""
    	_processInstructionPYTHON
    	
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionIF(self, instructionBody, execute) :
    	"""
    	_processInstructionIF
    	
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionELIF(self, instructionBody, execute) :
    	"""
    	_processInstructionELIF
    	
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionELSE(self, instructionBody, execute) :
    	"""
    	_processInstructionELSE
    	
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionFOR(self, instructionBody, execute) :
    	"""
    	_processInstructionFOR
    	
    	- instructionBody
    	- execute
    	"""
    	...

    def _processInstructionEND(self, instructionBody, execute) :
    	"""
    	_processInstructionEND
    	
    	- instructionBody
    	- execute
    	"""
    	...
