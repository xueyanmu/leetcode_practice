"""
two numbers represented by a linked list where each node is a single digit.
digits are stored in reverse order.

follow up:
digits are stored in forward order. repeat problem
"""

from _basic_linkedlist import Node, LinkedList


def addLists(l1, l2, carry):
    if l1 is None and l2 is None and carry == 0:
        return None

    result = Node()

    value = carry
    if l1 is not None:
        value += l1.data

    if l2 is not None:
        value += l2.data

    result.data = value % 10

    # RECURSE
    # TODO: UNDERSTAND
    if l1 is not None and l2 is not None:
        more = addLists(None if l1 is None else l1.next, None if l2 is None else l2.next, 1 if value >= 10 else 0)
        result.setNext(more)

    return result

def addLists2(l1: Node, l2: Node):
    return addLists(l1, l2, 0)


"""
followup
"""

class PartialSum:
    def __init__(self):
        self.sum = None
        self.carry = 0

    def addListsHelper(self, l1, l2):
        sum = self.sum

        if l1 is None and l2 is None:
            sum = PartialSum()
            return sum

        # add smaller digits recursively
        sum = self.addListsHelper(l1.next, l2.next)

        #add carry to current data
        val = sum.carry + l1.data + l2.data

        #insert sum of current digits
        full_result = Node.insertBefore(sum.sum, val % 10)

        #return sum so far, then carry value
        sum.sum = full_result
        sum.carry = val / 10
        return sum


    def addLists3(self, l1: Node, l2: Node):
        len1 = len(l1)
        len2 = len(l2)

       # pad shorter list with zeros (see note 1)
        if len1 < len2:
            l1.padList(l1, len2-len1)
        else:
            l2.padList(l2, len1-len2)


        # add lists
        sum = self.addListsHelper(l1, l2)

        # if there waas a carry value left over, insert this at the fronto f the list
        # otherwise, return the linked list
        if sum.carry == 0:
            return sum.sum

        else:
            result = Node.insertBefore(sum.sum, sum.carry)
            return result
