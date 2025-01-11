class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data attribute, this node class has both 
    a coefficient and an exponent attribute, which is used to represent each 
    term in a polynomial.
    """
    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)

        self.head = None


    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current is not None and current.exp > exp:
                previous = current
                current = current.next
            if current is not None and current.exp == exp:
                current.coeff += coeff
            else:
                new_node.next = current
                if previous is not None:
                    previous.next = new_node
                else:
                    self.head = new_node

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        result = LinkedList()
        current_self = self.head
        current_p = p.head
        while current_self is not None and current_p is not None:
            if current_self.exp > current_p.exp:
                result.insert_term(current_self.coeff, current_self.exp)
                current_self = current_self.next
            elif current_self.exp < current_p.exp:
                result.insert_term(current_p.coeff, current_p.exp)
                current_p = current_p.next
            else:
                coeff_sum = current_self.coeff + current_p.coeff
                if coeff_sum != 0:
                    result.insert_term(coeff_sum, current_self.exp)
                current_self = current_self.next
                current_p = current_p.next
        while current_self is not None:
            result.insert_term(current_self.coeff, current_self.exp)
            current_self = current_self.next
        while current_p is not None:
            result.insert_term(current_p.coeff, current_p.exp)
            current_p = current_p.next
        current = result.head
        prev = None
        while current is not None and current.next is not None:
            if current.exp < current.next.exp:
                current.coeff, current.next.coeff = current.next.coeff, current.coeff
                current.exp, current.next.exp = current.next.exp, current.exp
                if prev is None:
                    result.head = current
                else:
                    prev.next = current
                current = result.head
                prev = None
            else:
                prev = current
                current = current.next
        return result

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result = LinkedList()
        current_self = self.head
        while current_self is not None:
            current_p = p.head
            while current_p is not None:
                coeff = current_self.coeff * current_p.coeff
                exp = current_self.exp + current_p.exp
                result.insert_term(coeff, exp)
                current_p = current_p.next
            current_self = current_self.next
        return result

    # Return a string representation of the polynomial.
    def __str__ (self):
        if self.head is None:
            return ""
        current = self.head
        result_str = f"({current.coeff}, {current.exp})"
        current = current.next
        while current is not None:
            result_str += f" + ({current.coeff}, {current.exp})"
            current = current.next
        return result_str

def main():
    p = LinkedList()
    n = int(input())
    for _ in range(n):
        coeff, exp = map(int, input().split())
        p.insert_term(coeff, exp)
    q = LinkedList()
    input()
    m = int(input())
    for _ in range(m):
        coeff, exp = map(int, input().split())
        q.insert_term(coeff, exp)
    sum_poly = p.add(q)
    product_poly = p.mult(q)
    print(sum_poly)
    print(product_poly)

if __name__ == "__main__":
    main()
