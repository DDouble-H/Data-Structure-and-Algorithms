class Node:
    def __init__(self):
        self.data = None
        self.link = None


class LinkedList:
    state = True

    def __init__(self):
        self.head = Node()
        self.before = None
        self.current = None
        self.tail = self.head
        self.nodelist = [self.head]
        self.nodenum = 0

    def newNode(self, data):

        newNode = Node()
        newNode.data = data
        newNode.link = None

        return newNode

    def insert(self, LinkedList, newnode, mode='tail'):

        if mode == 'head': # 노드리스트의 1번째(head 뒤)에 노드 추가
            newnode.link = LinkedList.nodelist[0].link
            LinkedList.nodelist.insert(1, newnode)
            LinkedList.nodelist[0].link = LinkedList.nodelist[1]
            self.nodenum += 1

        elif mode == 'middle': # idx위치에 삽입 (예, 3번째에 입력하는 경우)

            while True:
                try:
                    idx = int(input('노드의 위치(정수)를 입력해주세요 > '))
                    break
                except ValueError as e:
                    print('값이 입력되지 않았거나 정수가 아닌 다른 문자가 입력되었습니다. ')

            newnode.link = LinkedList.nodelist[idx-1].link
            LinkedList.nodelist.insert(idx, newnode)
            LinkedList.nodelist[idx-1].link = LinkedList.nodelist[idx]
            self.nodenum += 1

        elif mode == 'tail': # 노드리스트의 제일 마지막에 노드 추가
            LinkedList.tail = newnode
            LinkedList.nodelist[-1].link = newnode
            LinkedList.nodelist.append(newnode)  # 뒤에 붙임
            self.nodenum += 1

        else:
            print('head, middle, tail 모드 중 하나를 입력해주세요. ')
            return

    def info(linkedlist):
        print('LinkedList Head : ', linkedlist.head,
              'LinkedList Tail : ', linkedlist.tail)

        for i in range(len(linkedlist.nodelist)):
            print(i, 'Node :', linkedlist.nodelist[i],
                  i, 'Node Data : ', linkedlist.nodelist[i].data,
                  i, 'Node Link : ', linkedlist.nodelist[i].link)

    def isEmpty(self, LinkedList):
        if LinkedList is None:
            return True
        else:
            return False

    def getSize(self):
        #return self.nodenum
        return len(self.nodelist)

    # 삭제 (중복 값 없음)
    # Value, Index
    def delete(self, LinkedList, removeData):
        if self.isEmpty(LinkedList):
            return 'No node to delete'

        # 지우고자 하는 값이 Tail인 경우
        elif LinkedList.nodelist[-1].data == removeData:
            LinkedList.tail = LinkedList.nodelist[-2]
            LinkedList.nodelist[-2].link = None
            del LinkedList.nodelist[-1]
            return 'Node Remove'

        # 지우고자 하는 값이 중간에 있는 경우
        else:
            for i in range(len(LinkedList.nodelist)):
                if LinkedList.nodelist[i].data == removeData:
                    # swap
                    LinkedList.nodelist[i - 1].link = LinkedList.nodelist[i].link
                    del LinkedList.nodelist[i]
                    return 'Node Remove'

    # 검색 (몇번째 노드인지 출력)
    def search(self, LinkedList, data):
        # self.nodenum = 0
        if self.isEmpty(LinkedList):
            return 'No node to search'
        else:
            for i in range(len(LinkedList.nodelist)):
                if LinkedList.nodelist[i].data == data:
                    print('nodenum : ', i)
                    return self.nodenum
                elif LinkedList.nodelist[i + 1].data == data:
                    i += 1


if __name__ == '__main__':
    LinkedList = LinkedList()

    while (True):
        word = input('Input Command > ')

        if word == 'quit' or word == 'q':
            break

        elif word == 'insert':
            data = input('Input Node Data > ')
            node = LinkedList.newNode(data)

            mode = input('노드의 추가 위치(head, middle, tail)을 선택해주세요. (기본 tail)> ') or 'tail'
            LinkedList.insert(LinkedList, node, mode)

        elif word == 'delete':
            data = input('Delete Node Data > ')
            LinkedList.delete(LinkedList, removeData=data)

        elif word == 'search':
            data = input('Search Node Data > ')
            LinkedList.search(LinkedList, data)

        elif word == 'size':
            LinkedList.getSize()

        elif word == 'info':
            LinkedList.info()

        else:
            print('Command Not Found')
