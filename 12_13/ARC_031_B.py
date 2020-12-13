import copy

# xとyが固定されているので最初に宣言しておく
X_RANGE = 10
Y_RANGE = 10

bool_result = False


# 深さ優先探索を行う関数
def dfs(a_list: list, x_position: int, y_position: int):
    global bool_result
    # 範囲外に探査・またはxを探査しようとした際
    if x_position < 0 or x_position >= X_RANGE or y_position < 0 or y_position >= Y_RANGE or a_list[x_position][y_position] == 'x':
        # 陸カウンター
        # 0のままなら1つの陸であると証明できる
        m_counter = 0
        for x_value in a_list:
            m_counter += x_value.count('o')

        # 陸が0なら条件適合なので探査完了
        if m_counter == 0:
            # print(a_list)
            bool_result = True
        return

    # 一度探査した先は探査する必要がないので海とする
    a_list[x_position][y_position] = 'x'

    # dfsを利用する
    # 上下左右に移動する4通り
    dfs(a_list, x_position + 1, y_position)
    dfs(a_list, x_position - 1, y_position)
    dfs(a_list, x_position, y_position + 1)
    dfs(a_list, x_position, y_position - 1)


def main():
    # 標準入力を入れる配列
    a_list = []

    # X回入力を受け付ける
    for _ in range(X_RANGE):
        a_list.append(list(input()))

    # どのxの場所をoにするかの処理を行う
    for x_position in range(X_RANGE):
        for y_position in range(Y_RANGE):
            if a_list[x_position][y_position] == 'x':
                fanction_list = copy.deepcopy(a_list)
                fanction_list[x_position][y_position] = 'o'

                # 深さ優先探索にて再帰計算
                dfs(fanction_list, x_position, y_position)

    # 結果出力
    if bool_result is True:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
