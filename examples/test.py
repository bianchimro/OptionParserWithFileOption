if __name__ == "__main__":
    import sys
    sys.path.append('../')
    from optionparserwithfileoption import OptionParserWithFileOption
     
    usage = "Usage: %prog ...."
    parser = OptionParserWithFileOption(usage, filefirst=True, long_option='--options-from-file')    
    parser.add_option("-a", "--another-option", action="store",
                      dest="anotheroption",  help="Another option",  default ='')
    (options, args) = parser.parse_args()    

    print "options:", options.anotheroption
    print "arguments", args

