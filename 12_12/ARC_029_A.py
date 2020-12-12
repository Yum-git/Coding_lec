import sys
# int型の最大値を定義
result_time = sys.maxsize


# 深さ優先探索を行う関数
def dfs(t_list: list, position: int, time_first: int, time_second: int):
    # 探査範囲外に探査した場合
    # result_timeと値を比較して小さい値を代入する
    if len(t_list) == position:
        min_time = max(time_first, time_second)
        global result_time
        result_time = min(min_time, result_time)
    # dfsを利用する
    # 1つ目と2つ目の肉焼き機のどちらで焼くかの2通り
    else:
        # 1つ目の肉焼き機で焼く
        dfs(t_list, position+1, time_first+t_list[position], time_second)
        # 2つ目の肉焼き機で焼く
        dfs(t_list, position+1, time_first, time_second+t_list[position])


def main():
    # 標準入力
    N = int(input())

    # 標準入力を入れる配列
    t_list = []

    # N回入力を受け付ける
    for _ in range(N):
        t_list.append(int(input()))

    # 深さ優先探索にて再帰計算
    dfs(t_list, 0, 0, 0)

    # 結果出力
    print(result_time)


if __name__ == '__main__':
    main()
