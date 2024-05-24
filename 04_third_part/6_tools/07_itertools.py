import itertools as ittools
import time


def count():
    it = ittools.count(5, 3)
    try:
        while True:
            print(next(it))
            time.sleep(1)
    except StopIteration:
        pass


def cycle():
    it = ittools.cycle([3, 4, 5])
    try:
        while True:
            print(it.__next__())
            time.sleep(1)
    except StopIteration:
        pass


def repeat():
    it = ittools.repeat([1, 2, 3], 5)
    try:
        while True:
            print(it.__next__())
            time.sleep(1)
    except StopIteration:
        pass


def accumulate():
    '''
    # accumulate(列表, 累积函数) 将列表参数中的元素一个一个用累加函数计算到一块
    :return:
    '''
    it = ittools.accumulate(iterable=['abc', 'efg', '123'],
                                       func=lambda a, b: "#".join([a, b]),
                                       initial='{{{{')
    try:
        while True:
            print(next(it))
            time.sleep(1)
    except StopIteration:
        pass

def batched():
    '''
    # batched(列表，批量处理个数) 批量处理，从元素列表中，批量取出数据
    :return:
    '''
    it = ittools.batched(['roses', 'red', 'violets', 'blue', 'sugar', 'sweet'], 4)
    try:
        while True:
            print(next(it))
            time.sleep(1)
    except StopIteration:
        pass

def chain():
    '''
    # chain(多个列表) 多个列表的逐个迭代
    :return:
    '''
    it = ittools.chain([1,2,3], ('abc','b'))
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass

def chain_from_iterable():
    it = ittools.chain.from_iterable([('abc','[5,6,7]'), '124'])
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass


# itertools.combinations(iterable, r)
# combinations('ABCD', 2) → AB AC AD BC BD CD

# itertools.combinations_with_replacement(iterable, r)
# combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC
# 排列组合，不在意顺序

# itertools.compress(data, selectors)
# compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
def compress():
    it = ittools.compress(['a','b','c'], [1,0])
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass

# itertools.dropwhile(predicate, iterable)
# dropwhile(lambda x: x<5, [1,4,6,4,1]) → 6 4 1 满足条件的都丢弃，直到遇上不满足条件的，然后后面的都放行

# itertools.filterfalse(predicate, iterable)
# filterfalse(lambda x: x%2, range(10)) → 0 2 4 6 8 所有满足条件的都留下

# itertools.groupby(iterable, key=None)
# groupby并不是可以单独使用的方法，一般用于其他方法的中间过程，另外它所接收的iterable参数，也应该是用key对应的函数进行过排序的
# groupby的意思是，将iterable的每一个值经过key描述的函数进行计算，获得的值相同，就分到一个list里边，如果不相等就放另一个组里
# 和sql中的groupby不同的是，它会考虑iterable的元素的顺序，哪怕计算出来同一个值了，但因为中间隔着了其他的值了，也不能分都一起
def groupby():
    it = ittools.groupby([1,2,3,4,5], key=lambda x : x%2)
    try:
        while True:
            print(next(it))
    except StopIteration:
        pass

# islice('ABCDEFG', 2) → A B
    # islice('ABCDEFG', 2, 4) → C D
    # islice('ABCDEFG', 2, None) → C D E F G
    # islice('ABCDEFG', 0, None, 2) → A C E G
# islice(iteable, start, stop, step) 从start的下一个开始，知道stop结束，可以没隔step个挑一个

# itertools.pairwise(iterable) 返回列表中临近两个值
# pairwise('ABCDEFG') → AB BC CD DE EF FG

# itertools.permutations(iterable, r=None)
# permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
# 排列组合，在意顺序的

# itertools.product(*iterables, repeat=1)
# 笛卡尔积

# itertools.starmap(function, iterable)
# starmap(pow, [(2,5), (3,2), (10,3)]) → 32 9 1000
# 把iterable中的每一个element当参数放入function中获得的结果组成新的iterable

# itertools.takewhile(predicate, iterable)
# takewhile(lambda x: x<5, [1,4,6,4,1]) → 1 4
# 满足条件的就被取出来，知道不满足条件了就停止获取

# itertools.tee(iterable, n=2) 返回多个迭代器

# zip_longest('ABCD', 'xy', fillvalue='-') → Ax By C- D- 有点像左连接




if __name__ == '__main__':
    # print([list(g) for k, g in ittools.groupby([1,2,4,3,5], key=lambda x:x%2)])
    #[[1], [2, 4], [3, 5]]

    it = ittools.tee([1,2,4,3,5], 2)
    for it_rec in it:
        try:
            while True:
                print(next(it_rec))
        except StopIteration:
            pass

