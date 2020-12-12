import sys


# 深さ優先探索を行うための関数
# number_list : [1, 2, 3, 4]
# postion : 位置
# result_number : 途中計算までの一時保存用数字
# result_list : 1+2+3-4
def dfs(number_list: list, position: int, result_number: int, result_list: list):
    # 探査範囲外に探査した場合
    # 結果が7であるかどうかを見る
    if position == len(number_list):
        if result_number == 7:
            # 計算結果を出力して終了する
            result_list += ['=', '7']
            print(''.join(map(str, result_list)))
            sys.exit(0)
    else:
        # 今現在の数字
        number_position = number_list[position]
        # プラス
        dfs(number_list, position+1, result_number+number_position, result_list+['+', number_position])
        # マイナス
        dfs(number_list, position+1, result_number-number_position, result_list+['-', number_position])


def main():
    # 標準入力
    ABCD_str = input()

    # 入力を1文字づつ分割してリスト化
    # その後，int型に変換
    ABCD_list = list(ABCD_str)
    ABCD_list = [int(str_number) for str_number in ABCD_list]

    # 深さ優先探索にて再帰計算
    dfs(ABCD_list, 1, ABCD_list[0], [ABCD_list[0]])


if __name__ == '__main__':
    main()
