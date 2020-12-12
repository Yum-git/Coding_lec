faction_result = 0


# 深さ優先探索を行う関数
def dfs(xy_list: list, member_count: int, position: int, member_list: list):
    # 探査範囲外に探査した場合
    # 選択した人と人の組み合わせを全てxy_listと比較する
    # xy_list内になければそれは条件に合致しないとわかる
    if member_count < position:
        for first_member in range(len(member_list) - 1):
            for second_member in range(first_member + 1, len(member_list)):
                Disc_list = [member_list[first_member], member_list[second_member]]
                if Disc_list not in xy_list:
                    return

        # faction_resultと値を比較して小さい値を代入する
        global faction_result
        if faction_result < len(member_list):
            faction_result = len(member_list)

    # dfsを利用する
    # その人を選択しないか，するかの2通り
    else:
        # 選択しない
        dfs(xy_list, member_count, position+1, member_list)
        # 選択する
        dfs(xy_list, member_count, position+1, member_list + [position])


def main():
    # 標準入力
    N, M = map(int, input().split())

    # 標準入力を入れる配列
    xy_list = []

    # M回入力を受け付ける
    for _ in range(M):
        xy_list.append(list(map(int, input().split())))

    # 深さ優先探索にて再帰計算
    dfs(xy_list, N, 1, [])

    # 結果出力
    print(faction_result)


if __name__ == '__main__':
    main()
