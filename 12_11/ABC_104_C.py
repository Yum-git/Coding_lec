import sys
# 出力する値
result = sys.maxsize
# Gの値をグローバル変数にて宣言
G_number = 0


# 深さ優先探索を行うための関数
def dfs(pc_list: list, position: int, total_sum: int, total_count: int, none_list: list):
    # グローバル変数へのアクセス
    global result
    global G_number

    # 探査範囲外に探査した場合
    if len(pc_list) == position:
        # 総合スコアが目標に届いているかどうか判断
        remainder = G_number - total_sum
        if remainder > 0:
            # 逆順で配列を回す
            # 点数が高い順から探査
            for key in range(len(none_list) - 1, -1, -1):
                # その点数が利用されていない場合
                if none_list[key] == 0:
                    # 後何個点数が必要か計算
                    tmp = remainder / ((key + 1) * 100)
                    # 必要な個数が持っている個数以内の場合
                    if tmp <= pc_list[key][0]:
                        total_count += int(tmp)
                        if tmp != int(tmp):
                            total_count += 1
                        break
                    else:
                        return
            else:
                return
        if total_count < result:
            result = total_count

    else:
        # 全足し算しない時
        dfs(pc_list, position + 1, total_sum, total_count, none_list + [0])

        # 全足し算する時
        sum_add = pc_list[position][0] * ((position + 1) * 100)
        count_add = pc_list[position][0]
        dfs(pc_list, position + 1, total_sum + sum_add + pc_list[position][1], total_count + count_add, none_list + [1])


def main():
    # グローバル変数へのアクセス
    global G_number
    # 標準入力
    D, G_number = map(int, input().split())

    # pとcを入れる配列宣言
    pc_list = []

    # 標準入力を配列に入れる
    for _ in range(D):
        pc_list.append(list(map(int, input().split())))

    # 深さ優先探索にて再帰計算
    dfs(pc_list, 0, 0, 0, [])

    # 結果出力
    print(result)


if __name__ == '__main__':
    main()
