import sys
# 再帰限界を実質外す
sys.setrecursionlimit(10**7)

# グローバル変数にてH,Wを定義
H, W = -1, -1
# 最終的に
bool_result = False


# 深さ優先探索を行う関数
def dfs(c_list: list, x_position: int, y_position: int):
    global bool_result
    # すでにゴールへの行き方が分かっている場合処理を終了する
    if bool_result is True:
        return
    # 街の範囲外を探査する場合は処理を終了する
    if 0 > x_position or H <= x_position or 0 > y_position or W <= y_position:
        return
    # 探査先が壁の場合は進めないので処理を終了する
    if c_list[x_position][y_position] == '#':
        return
    # 探査先がゴールの場合は探査完了なので処理を終了する
    if c_list[x_position][y_position] == 'g':
        bool_result = True
        return

    # 一度探査した先は探査する必要がないので壁とする
    c_list[x_position][y_position] = '#'

    # dfsを利用する
    # 上下左右に移動する4通り
    dfs(c_list, x_position + 1, y_position)
    dfs(c_list, x_position - 1, y_position)
    dfs(c_list, x_position, y_position - 1)
    dfs(c_list, x_position, y_position + 1)


def main():
    # 標準入力
    global H, W
    H, W = map(int, input().split())

    # 標準入力を入れる配列
    c_list = []

    # H回入力を受け付ける
    for _ in range(H):
        c_list.append(list(input()))

    # スタートの位置を見つける
    x_start = -1
    y_start = -1
    for x_key, x_value in enumerate(c_list):
        try:
            x_start, y_start = x_key, x_value.index('s')
        except ValueError:
            continue

    # 深さ優先探索にて再帰計算
    dfs(c_list, x_start, y_start)

    # 結果出力
    if bool_result is True:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
