# 最終計算結果を入れる変数
total_count = 0


# 深さ優先探索を行うための関数
def dfs(number_list: list, position: int, tmp_str: str, sum_list: list):
    # 探査範囲外に探査した場合
    # total_countに加算する
    if len(number_list) == position:
        global total_count
        total_count += int(tmp_str) + sum(sum_list)
    # dfsを利用する
    # 数字を連結する・数字を足すの2通り
    else:
        # 連結
        dfs(number_list, position + 1, tmp_str + number_list[position], sum_list)
        # 計算
        dfs(number_list, position + 1, number_list[position], sum_list + [int(tmp_str)])


def main():
    # 標準入力
    S = input()

    # 入力を1文字づつ分割してリスト化
    S_List = list(S)

    # 深さ優先探索にて再帰計算
    dfs(S_List, 1, S_List[0], [])

    # 結果出力
    print(total_count)


if __name__ == '__main__':
    main()
