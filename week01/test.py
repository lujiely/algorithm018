#coding:utf-8
class Solution(object):

    def getSum(self, num):
        if num == 0:
            return 0
        if num:
            res = num + self.getSum(num-1)
        return res

import sys
def twoSum():
    lines = sys.stdin.readline().split()
    print(lines)


if __name__ == '__main__':
    import sys
    line = sys.stdin.readline().split()
    a = int(line[0])
    b = int(line[1])

    print(a + b)
    sys.stdout.write("a")