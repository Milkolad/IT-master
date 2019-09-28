class Automat:

    def __init__(self, number):
        self.binary_number = int(bin(number)[-len(bin(number))+2:])
        self.rule = dict({
                "000" : 0,
                "001" : 0,
                "010" : 0,
                "011" : 0,
                "100" : 0,
                "101" : 0,
                "110" : 0,
                "111" : 0,
            })
        number = self.binary_number
        for key in self.rule:
            self.rule[key] = number % 10
            number = round(number / 10)
        self.vector = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
    
    def get_binary(self):
        return self.binary_number

    def get_rule(self):
        return self.rule

    def get_vector(self):
        return self.vector

    def run(self):
        for i in range(1, len(self.vector) - 2):
            frame = f"{self.vector[i - 1]}{self.vector[i]}{self.vector[i + 1]}"
            rule_value = self.rule[frame]
            self.vector[i] = rule_value
        print(self.vector)