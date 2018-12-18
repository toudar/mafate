class Expe(object):

    def __init__(self, project, model, name, number=1, ybeg=1850, yend=1850, is_Obs=False, expe_control=None, color='k', marker='.', linestyle='-', label=None, adds=dict()):
        self.project = project # CLIMAF project name (pre-existing or user)
        self.model = model
        self.name = name
        self.ybeg = ybeg
        self.yend = yend
        self.is_Obs = is_Obs
        self.expe_control = expe_control
        self.color = color
        self.marker = marker
        self.linestyle = linestyle
        if label == None:
            self.label = self.name
        else:
            self.label = label
        self.adds = adds
        self.number = number
        
    def __str__(self):
        xstr = '---------------------------------------------------'
        xstr += '\n'
        xstr += 'Model  : %s'%(self.model)
        xstr += '\n'
        xstr += 'Name   : %s'%(self.name)
        xstr += '\n'
        xstr += 'Period : %i - %i'%(self.ybeg, self.yend)
        xstr += '\n'
        xstr += '---------------------------------------------------'
        return xstr

    def period(self):
        return str(self.ybeg)+'-'+str(self.yend)

    def expid(self, number=''):
        if self.is_Obs:
            return str(self.model)
        else:
            return str(self.model)+'_'+str(self.name)+'_r'+str(number)


class Variable(object):

    def __init__(self, name=None, table=None, grid='gr'):
        self.name = name
        self.table = table
        self.grid = grid

    def varid(self):
        return str(self.name)
#        return str(self.name)+'_'+str(self.table)

    def __str__(self):
        print(self.name, self.table)
