class templateClass:

    def __init__(self):

        print('this is the template class constructor')



class test:

    def __init__(self):

        print('welcome to the test class')


    def testTemplateClass(self):

        from templateFile import templateClass

        templateClassObj = templateClass()



class workspace:

    def __init__(self):

        print('initialising workspace')

        self.initialiseDefaults()


    def getTestObj(self):

        self.reloadClasses()
        self.testObj = self.test()

        return self.testObj

    def getClassObj(self):

        self.reloadClasses()
        self.templateClassObj = self.templateClass()

        return self.templateClassObj



    def initialiseDefaults(self):

        import templateFile

        from templateFile import templateClass
        from templateFile import test

        self.templateFile = templateFile
        self.test = test

        from importlib import reload
        self.reload = reload

        print("workspace defaults initiated")

    def reloadClasses(self):

        reload = self.reload

        import templateFile
        reload(templateFile)


        from templateFile import templateClass
        from templateFile import test

        self.templateClass = templateClass
        self.test = test


def printHelp():

    print('hello, welcome to the templateClass module')

    print(' ')

    print('to load test modules use:')

    print(' ')

    print('import templateFile')
    print('from templateFile import workspace')
    print('self = workspace()')

    print(' ')
    print('testObj = self.getTestObj()')
    print('testObj.testTemplateClass')



printHelp()


