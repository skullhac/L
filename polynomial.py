#Implementation of the Polynomial ADT using a sorted linked list
class Polynomial:
    def __init__(self, degree = None, coefficient = None):
        if degree is None:
            self._polyHead = None
        else:
            self._polyHead = _PolyTermNode(degree, coefficient)
        self._polyTail = self._polyHead


    def degree(self):
        if self._polyHead is None:
            return -1
        else:
            return self._polyHead.degree

    def __getitem__(self, degree):
        assert self.degree() >= 0, \
            "Operation not permitted in empty polynomial."
        curNode = self._polyHead
        while curNode is not None and curNode.degree >= degree:
            curNode = curNode.next
        if curNode is None or curNode.degree != degree:
            return 0.0
        else:
            return curNode.degree

    def evaluate(self, scalar):
        assert self.degree() >= 0, \
            "Only non-empty polynomials can be evaluated!"
        result = 0.0
        curNode = self._polyHead
        while curNode is not None:
            result += curNode.coefficient * (scalar ** curNode.degree)
            curNode = curNode.next
        return result

    def __add__(self, rhsPoly):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
            "Addition only allowed in non-empty Polynomials"
        newPoly = Polynomial()
        nodeA = self._polyHead
        nodeB = self._polyHead

        while nodeA is not None and nodeB is not None:
            if nodeA.degree > nodeB.degree:
                degree = nodeA.degree
                value = nodeA.coefficient
                nodeA = nodeA.next
            elif nodeA.degree < nodeB.degree:
                degree = nodeB.degree
                value = nodeB.coefficient
                nodeB = nodeB.next
            else:
                degree = nodeA.degree
                value = nodeA.coefficient + nodeB.coefficient
                #adds when degree is same
                nodeA = nodeA.next
                nodeB = nodeB.next
            newPoly._appendTerm(degree, value)

        while nodeA is not None:
            newPoly._appendTerm(nodeA.degree, nodeA.coefficient)
            nodeA = nodeA.next
            #if the list itself is longer
        while nodeB is not None:
            newPoly._appendTerm(nodeB.degree, nodeB.coefficient)
            nodeB = nodeB.next
        return newPoly


    def __sub__(self, rhsPoly):
        pass
    def __mul__( self, rhsPoly ):
        assert self.degree() >= 0 and rhsPoly.degree() >= 0, \
        "Multiplication only allowed on non-empty polynomials."

        # Create a new polynomial by multiplying rhsPoly by the first term.
        node = self._polyHead
        newPoly = rhsPoly._termMultiply( node )

        # Iterate through the remaining terms of the poly computing the
        # product of the rhsPoly by each term.
        node = node.next
        while node is not None :
            tempPoly = rhsPoly._termMultiply( node )
            newPoly = newPoly.add( tempPoly )
            node = node.next

        return newPoly

    # Helper method for creating a new polynomial from multiplying an
    # existing polynomial by another term.
    def _termMultiply( self, termNode ):
        newPoly = Polynomial()
        curr=self._polyHead
    # Iterate through the terms and compute the product of each term and
    # the term in termNode.
        curr = curr.next
        while curr is not None :
            # Compute the product of the term.
            newDegree = curr.degree + termNode.degree
            newCoeff = curr.coefficient * termNode.coefficient

            # Append it to the new polynomial.
            newPoly._appendTerm( newDegree, newCoeff )

            # Advance the current pointer.
            curr = curr.next
        return newPoly


    #Helper method for appending terms in the polynomial
    def _appendTerm(self, degree, coefficient):
        if coefficient != 0.0:
            newTerm = _PolyTermNode(degree, coefficient)
            if self._polyHead is None:
                self._polyHead = newTerm
            else:
                self._polyTail.next = newTerm
            self._polyTail = newTerm


class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None
