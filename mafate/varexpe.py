class Expe(object):

    def __init__(self, project, model, name, member=[1], ybeg=1850, yend=1850, is_Obs=False, expe_control=None, color='k', marker='.', linestyle='-'):
        self.project = project # CLIMAF project name (pre-existing or user)
        self.model = model
        self.name = name
        self.member = member
        self.ybeg = ybeg
        self.yend = yend
        self.is_Obs = is_Obs
        if expe_control is None:
            self.expe_control = self
        else:
            self.expe_control = expe_control
        self.color = color
        self.marker = marker
        self.linestyle = linestyle
        
    def __str__(self):
        print self.name, self.ybeg

    def period(self):
        return str(self.ybeg)+'-'+str(self.yend)

    def expid(self):
        if self.is_Obs:
            return str(self.model)
        else:
            if len(self.member) > 1:
                return str(self.model)+'_'+str(self.name)+'_r1-'+str(len(self.member))
            else:
                return str(self.model)+'_'+str(self.name)+'_r'+str(self.member[0])


class Variable(object):

    def __init__(self, name=None, table=None, grid='gr'):
        self.name = name
        self.table = table
        self.grid = grid

    def varid(self):
        return str(self.name)+'_'+str(self.table)

    def __str__(self):
        print self.name, self.table
