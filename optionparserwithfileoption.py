"""an example of parsing options from a file"""
from optparse import OptionParser
 
class OptionParserWithFileOption(OptionParser):
    """A siple wrapper around OptionParse 
       to provide parsing options from a file"""
     
    def __init__(self, *ar, **kwar):
        """just a wrapper for inherited __init__
           except keyword argument 'filefirst'
           and adding the default -f option
           (would be a good idea to parametrize this, 
           as -f is a fairly common switch ...)"""
            
        if 'filefirst' in kwar:
            self.filefirst = kwar['filefirst']
            kwar.pop('filefirst')
        else:
            self.filefirst = False
             
        OptionParser.__init__(self, *ar, **kwar)
        self.add_option("-f", "--from-file", 
                        action="store",  dest="optionsfromfile",
                        help="Loads options from file",
                        default =None)
         
    def parse_args(self, *ar, **kwar):
        """this is the only overriden method.
           in practice a wrapper around  OptionParser.parse_args"""
        (startOptions, startArgs) = OptionParser.parse_args(self, *ar, **kwar)
  
        if not startOptions.optionsfromfile:
            return (startOptions, startArgs)
         
        else:
            optionsAndArgsFromFile = self.loadOptionsFromFile(startOptions.optionsfromfile)
            (newOptions, newArgs) = OptionParser.parse_args(self, optionsAndArgsFromFile)
         
        if self.filefirst:
            firstOptions = newOptions
            secondOptions = startOptions
        else:
            firstOptions = startOptions
            secondOptions = newOptions
         
        for x in secondOptions.__dict__:
            if x not in firstOptions.__dict__:
                firstOptions.__dict__[x] = secondOptions.__dict__[x]
        startArgs.extend(newArgs)
         
        return  (firstOptions, startArgs)
 
 
    def loadOptionsFromFile(self, filename, commentPrefix="#"):
        """this simply loads all the lines in a files
        except those preceded with prefix and concatenates them
        in order to create a new options set """
        try:
            linesList = []
            optsFile = open(filename, 'rb')
            for line in optsFile.readlines():
                if not line.lstrip().startswith(commentPrefix):
                    linesList.append(line)
            argsFromFileString = " ".join(linesList)
            argsFromFile = argsFromFileString.split()
            optsFile.close()
            return argsFromFile
        except BaseException, e:
            raise e
 
 

