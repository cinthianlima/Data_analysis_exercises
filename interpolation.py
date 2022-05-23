class Interpolation:


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
