from collections import deque
import sys
import copy

sys.setrecursionlimit(10**7)

gy, gx = -1, -1
R, C = -1, -1

result_counter = sys.maxsize


def bfs_around(c_list, deque_list, counter):
    global result_counter
    out_list = deque_list.popleft()

    print(out_list)

    if out_list == [gy, gx]:
        result_counter = min(counter, result_counter)
        return

    if out_list[0] < 0 or out_list[0] >= R or out_list[1] < 0 or out_list[1] >= C:
        return

    if c_list[out_list[0]][out_list[1]] != '#':
        c_copy_list = copy.deepcopy(c_list)
        c_copy_list[out_list[0]][out_list[1]] = '#'

        deque_list.append([out_list[0] + 1, out_list[1]])
        bfs_around(c_copy_list, deque_list, counter + 1)

        deque_list.append([out_list[0] - 1, out_list[1]])
        bfs_around(c_copy_list, deque_list, counter + 1)

        deque_list.append([out_list[0], out_list[1] + 1])
        bfs_around(c_copy_list, deque_list, counter + 1)

        deque_list.append([out_list[0], out_list[1] - 1])
        bfs_around(c_copy_list, deque_list, counter + 1)
    else:
        return


def main():
    global gx, gy
    global R, C
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    gx -= 1
    gy -= 1
    c_list = []

    for _ in range(R):
        c_list.append(list(input()))

    # que_list = [sx - 1, sy - 1]
    # result_count = bfs(que_list, c_list)
    # print(result_count)

    que = deque([])
    que.append([sy - 1, sx - 1])
    bfs_around(c_list, que, 0)

    print(result_counter)


if __name__ == '__main__':
    main()
