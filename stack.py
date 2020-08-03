class Stack():

    def __init__(self, stack_list):
        self.stack_list = list(stack_list)

    def isEmpty(self):
        if self.stack_list:
            print('True')
        else:
            print('False')

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        peek = self.stack_list[-1]
        print(peek)
        return peek

    def size(self):
        size = len(self.stack_list)
        return size

    def eqal_bracket(self):
        rigth_list_bracket = []
        slice =  int(self.size()/ 2)
        sort_left_list = sorted(self.stack_list[:slice])
        for el in self.stack_list[slice:]:
            item = self.pop()
            if item == '}':
                rigth_list_bracket.append('{')
            if item == ')':
                rigth_list_bracket.append('(')
            if item == ']':
                rigth_list_bracket.append('[')
        rigth_list_bracket = sorted(rigth_list_bracket)
        if rigth_list_bracket == sort_left_list:
            print('Сбалансированно')
        else:
            print('Несбалансированно')


massive_object = '{{[()]}}'
massive = Stack(massive_object)
massive.eqal_bracket()


