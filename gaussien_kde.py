from scipy import optimize, integrate
import scipy.stats as stats

class Gaussian_kde(stats.gaussian_kde):
    
    def cdf(self, x, *args):
        self.a = -np.inf
        return integrate.quad(self.pdf, self.a, x, args=args)[0]
    
    def _ppf_to_solve(self, x, q,*args):
         return self.cdf(*(x, )+args)-q

    def ppf(self, q, *args):
        if q == 0:
            q = q + 0.001
        if q == 1:
            q = q - 0.001
        self.a = -np.inf
        self.b = np.inf
        left = right = None
        if self.a > -np.inf:
            left = self.a
        if self.b < np.inf:
            right = self.b

        factor = 10.
        if  not left: # i.e. self.a = -inf
            left = -1.*factor
            while self._ppf_to_solve(left, q,*args) > 0.:
                right = left
                left *= factor
            # left is now such that cdf(left) < q
        if  not right: # i.e. self.b = inf
            right = factor
            while self._ppf_to_solve(right, q,*args) < 0.:
                left = right
                right *= factor
            # right is now such that cdf(right) > q

        return optimize.brentq(self._ppf_to_solve, left, right, args=(q,)+args, maxiter= 1000)
