import re


class Monomial:
    def __init__(self, monomial):
        self.sign = monomial
        self.variable = monomial
        self.exponent = monomial
        self.coefficient = monomial

    def __str__(self):
        monomial_str = ''
        if self.coefficient != 1:
            monomial_str += str(self.coefficient)
        if self.variable != '':
            monomial_str += self.variable
        elif self.variable == '' and self.coefficient == 1:
            monomial_str += str(self.coefficient)
        if self.exponent > 1:
            monomial_str += '^' + str(self.exponent)
        return monomial_str

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.coefficient == other.coefficient and self.exponent == other.exponent

    def __gt__(self, other):
        return self.exponent > other.exponent

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, monomial):
        pattern = re.compile(r'[-+]')
        sign = pattern.search(monomial)
        self._sign = sign[0] if sign else '+'

    @property
    def variable(self):
        return self._variable

    @variable.setter
    def variable(self, monomial):
        pattern = re.compile(r'[a-zA-Z]')
        variable = pattern.search(monomial)
        self._variable = variable[0] if variable else ''

    @property
    def exponent(self):
        return self._exponent

    @exponent.setter
    def exponent(self, monomial):
        if self.variable == '':
            self._exponent = 0
        else:
            pattern = re.compile('({})\\^?(\\d*)'.format(self.variable))
            match = pattern.search(monomial)
            if match:
                try:
                    self._exponent = int(match.group(2))
                except ValueError:
                    self._exponent = 1

    @property
    def coefficient(self):
        return self._coefficient

    @coefficient.setter
    def coefficient(self, monomial):
        pattern = re.compile('\+?-?(\\d*)\*?{}?'.format(self.variable))
        match = pattern.search(monomial)
        self._coefficient = int(match.group(1)) if match.group(1) else 1

    def get_first_derivative(self):
        if self.variable is '':
            return __class__('0')
        derivative = ''
        coefficient = self.coefficient * self.exponent
        exponent = self.exponent - 1
        if coefficient == 0:
            return __class__('')
        elif coefficient >= 1:
            derivative += str(coefficient) + '*'
        if exponent == 0:
            return __class__(self.sign + derivative)
        if exponent == 1:
            derivative += self.variable
        elif exponent > 1:
            derivative += self.variable + '^' + str(exponent)
        return __class__(self.sign + derivative)


class Polynomial:
    def __init__(self, polynomial):
        self.monomial_list = polynomial

    @property
    def monomial_list(self):
        return self._monomial_list

    @monomial_list.setter
    def monomial_list(self, polynomial):
        pattern = re.compile(r'\+?-?[0-9a-zA-Z*^]*')
        print(re.findall(pattern, polynomial)[:-1:])
        self._monomial_list = [Monomial(monomial)
                               for monomial in re.findall(pattern, polynomial)[:-1:]]

    def get_first_derivative(self):
        deriv_list = [monomial.get_first_derivative()
                      for monomial in self.monomial_list]
        return deriv_list

    def print_first_derivative(self):
        deriv_list = self.get_first_derivative()
        deriv_list.sort(key=lambda monomial: monomial.exponent, reverse=True)
        try:
            first_deriv = str(deriv_list[0]) if str(deriv_list[0]) != '0' else ''
            for deriv in deriv_list[1:]:
                if str(deriv) != '0':
                    first_deriv += deriv.sign + str(deriv)
        except IndexError:
            pass
        else:
            return first_deriv


if __name__ == "__main__":
    # m1 = Monomial('x^2')
    # m2 = Monomial('2x')
    # print(m2.get_first_derivative())
    # print(m1.get_first_derivative(), m2.get_first_derivative())
    p = Polynomial('x^3+x+2*x+x^10')
    print(p.print_first_derivative())


