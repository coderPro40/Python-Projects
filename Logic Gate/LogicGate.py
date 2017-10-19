"""
Name: ThankGod Ofurum
Project: Create a classes that implement the logic gate
methods consisting of binary and unary classes which in
turn consists of and, or and not classes
"""
class LogicGate:
    """Class constructor consisting of instance variables
       n stands for the name assigned to the gate
    """
    def __init__(self, n):
        self.label = n
        self.output = None

    """return label"""
    def getLabel(self):
        return self.label

    """Return output"""
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    """Class constructor consisting of instance variables"""
    def __init__(self, n):
        super().__init__(n)
        """Multiple inputs"""
        self.pinA = None
        self.pinB = None

    """Capture 1st pin from user"""
    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + \
                             self.getLabel() + "--> "))
        else:
            return self.pinA.getFrom().getOutput()

    """Capture 2nd pin from user"""
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + \
                             self.getLabel() + "--> "))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB ==None:
                self.pinB = source

            else:
                raise RuntimeError("fnBinaryGateRerror: NO EMPTY PINS")

class UnaryGate(LogicGate):
    """Class constructor consisting of instance variables"""
    def __init__(self, n):
        super().__init__(n)
        """Single input"""
        self.pin = None

    """Capture pin from user"""
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + \
                             self.getLabel() + "--> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("fnBinaryGateRerror: NO EMPTY PINS")

class AndGate(BinaryGate):
    """Class constructor consisting of instance variables"""
    def __init__(self, n):
        super().__init__(n)

    """Determine what value to return"""
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    """Class constructor consisting of instance variables"""
    def __init__(self, n):
        super().__init__(n)

    """Determine what value to return"""
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    """Class constructor consisting of instance variables"""
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 1:
            return 0
        else:
            return 1

class Connector:
    """Class constructor consisting of instance variables"""
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

        

