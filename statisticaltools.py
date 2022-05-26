class InterCumulSamp:

    def __init__(self, dist, space):
        self.dist = dist
        self.space = space
        self.interpolation_coef = self.interpolate()
        self.cumulative_coef = self.cumulative_all_points()
        self.s_coef = self.sampler_coef()

    def interpolate(self):
        p = []
        for i in range(0, len(self.space) - 1):
            dy = self.dist[i + 1] - self.dist[i]
            dx = self.space[i + 1] - self.space[i]
            coef_a = dy / dx
            coef_b = -dy / dx * self.space[i] + self.dist[i]
            p.append((coef_a, coef_b, self.space[i], self.space[i + 1]))
        return p

    def interpolated_point(self,point):
        coef = self.interpolation_coef
        for item in coef:
            if point >= item[2] and point <= item[3]:
                return item[0] * point + item[1]

    def cumulative(self, point):
        integral_i = 0

        for item in self.interpolation_coef:
            if point >= item[2] and point >= item[3]:
                integral_i += item[0] / 2 * (item[3] ** 2 - item[2] ** 2) + item[1] * (item[3] - item[2])

            elif point >= item[2] and point < item[3]:
                integral_i += item[0] / 2 * (point ** 2 - item[2] ** 2) + item[1] * (point - item[2])

        return integral_i

    def cumulative_all_points(self):
        cumulative_all = []

        for i in self.space:
            c = self.cumulative(i)
            cumulative_all.append((c,i))
        return cumulative_all


    def sampler_coef(self):
        s = []
        cumulative_all = self.cumulative_all_points()
        for j in range(0, len(cumulative_all) - 1):
            dc = cumulative_all[j + 1][0] - cumulative_all[j][0]
            dx = cumulative_all[j + 1][1] - cumulative_all[j][1]
            coefs_a = dx / dc
            coefs_b = -dx / dc * cumulative_all[j][0] + cumulative_all[j][1]
            s.append((coefs_a, coefs_b, cumulative_all[j][0], cumulative_all[j + 1][0]))
        return s

    def sampler(self, point):

        for item in self.s_coef:
            if point >= item[2] and point <= item[3]:
                return item[0] * point + item[1]


    def sampler_list_points(self, s_list):
        sampler_list = []
        for i in s_list:
            s = self.sampler(i)
            sampler_list.append(s)

        return sampler_list

#########################################################################################################################################################
#########################################################################################################################################################

class Statisticaltools1:

    def __init__(self, data1):

        self.data1 = data1
        self.soma_total = self.soma()
        self.med = self.media_aritmetica()
        self.var_list = self.var_list()
        self.soma_var = self.soma_variance()
        self.var = self.variance()

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

    def skew(self):
        list_skew = []
        for i in range(0, len(self.data1)):
            ri = ((self.data1[i] - self.med) ** 3)
            list_skew.append(ri)
        s = 0
        for i in list_skew:
            s = s + i

        skew = s /(len(self.data1) * ((self.var ** (0.5)) ** 3))

        return skew

    def curtosis(self):
        c1_list =[]
        for i in range(0, len(self.data1)):
            ri = ((self.data1[i] - self.med) ** 4)
            c1_list.append(ri)

        soma_c1 = 0
        for i in c1_list:
            soma_c1 = soma_c1 + i

        a = soma_c1 / len(c1_list)
        b = (self.var ** (0.5)) ** 4

        curtosis = ((1 / (b ** 4)) * a) - 3

        return curtosis






#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

class Statisticaltools2:

    def __init__(self, data1, data2):

        self.data1 = data1
        self.data2 = data2
        self.cov = self.covariance()

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
            rj = (self.data2[i] - media2)
            data2_dif.append(rj)

        cov_list= []
        for i in range(0, len(data1_dif)):
            cov_i = data1_dif[i] * data2_dif[i]
            cov_list.append(cov_i)

        k=0
        for i in cov_list:
            k = k + i

        covariance = k / len(self.data1)


        return covariance











