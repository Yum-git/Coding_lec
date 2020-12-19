top_list = []
uv_list = []

bool_flag = False


def dfs(position, before_postion):
    global bool_flag
    for u in uv_list[position]:
        if u != before_postion:
            if top_list[u] is True:
                bool_flag = False
                return
            else:
                top_list[u] = True
                dfs(u, position)


def main():
    global uv_list
    global bool_flag
    global top_list

    result = 0
    N, M = map(int, input().split())
    uv_list = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        uv_list[u].append(v)
        uv_list[v].append(u)

    top_list = [False for i in range(N)]

    for top_key in range(N):
        if top_list[top_key] is False:
            bool_flag = True
            dfs(top_key, -1)
            if bool_flag is True:
                result += 1

    print(result)


if __name__ == '__main__':
    main()
