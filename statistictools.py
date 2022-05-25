class Statistictools1:

    def __init__(self, data1):

        self.data1 = data1
        self.soma_total = self.soma()
        self.med = self.media_aritmetica()
        self.var_list = self.var_list()
        self.soma_var = self.soma_variance()

#Media aritmetica
    def soma(self):
        m = 0
        for i in self.data1:
            m = m + i
        return (m)

    def media_aritmetica(self):
        media_aritmetica = self.soma_total / len(self.data1)
        return media_aritmetica

#Variancia
    def var_list(self):
        list_var = []
        for i in range(0, len(self.data1)):
            ri = ((self.data1[i] - self.med) ** 2)
            list_var.append(ri)
        return list_var

    def soma_variance(self):
        m = 0
        for i in self.var_list:
            m = m + i
        return (m)

    def variance(self):
        var = self.soma_var / len(self.data1)
        return var

#Covariancia

class Statistictools2:

    def __init__(self, data1, data2):

        self.data1 = data1
        self.data2 = data2

    # Erro absoluto
    def absolute_error(self):
        err = []
        for i in range(0, len(self.data1)):
            s = self.data1[i] - self.data2[i]
            ri = abs(s)
            err.append(ri)
        return err

    # Erro relativo
    def relative_error(self):
        rel_err = []
        for i in range(0, len(self.data1)):
            s = self.data1[i] - self.data2[i]
            r = abs(s)
            ri = r / self.data2[i]
            rel_err.append(ri)

        return rel_err

    #Covariancia
    def covariance(self):
        m1 = 0
        m2 = 0
        for i in self.data1:
            m1 = m1 + i

        for j in self.data2:
            m2 = m2 + j

        media1 = m1 / len(self.data1)
        media2 = m2 / len(self.data2)

        data1_dif = []
        for i in range(0, len(self.data1)):
            ri = (self.data1[i] - media1)
            data1_dif.append(ri)

        data2_dif = []
        for i in range(0, len(self.data1)):
            ri = (self.data2[i] - media2)
            data2_dif.append(ri)

        cov_list= []
        for i in range(0, len(data1_dif)):
            cov_i = data1_dif[i] * data2_dif[i]
            cov_list.append(cov_i)

        k=0
        for k in cov_list:
            k = k + i

        covariance = k / len(self.data1)


        return covariance







