# https://atcoder.jp/contests/abc176/tasks/abc176_d

h, w = list(map(int, input().split()))
# 魔法使い
ch, cw = list(map(int, input().split()))
start = (ch - 1, cw - 1)
# マス
dh, dw = (list((map(int, input().split()))))
goal = (dh - 1, dw - 1)
stage = []
for _ in range(h):
    stage.append(list(str(input())))

stage[goal[0]][goal[1]] = 'G'

walk_pattern = [
    (0, -1),
    (-1, 0),
    (1, 0),
    (0, 1),
]


# return ワープ回数
def bfs():
    # キューには、今の場所とワープ回数を入れる
    que = [[start, 0]]

    while len(que) != 0:
        position, warp = que.pop(0)
        if stage[position[0]][position[1]] == 'G':
            return warp
        # すでに歩いていたら何もしない
        if stage[position[0]][position[1]] == 'W':
            continue

        # 歩いたという履歴を残す
        stage[position[0]][position[1]] = 'W'

        can_walk = False
        for tmpH, tmpW in walk_pattern:
            nh = position[0] + tmpH
            nw = position[1] + tmpW

            # 移動が可能かの判定
            if 0 <= nh < h and 0 <= nw < w and (stage[nh][nw] == '.' or stage[nh][nw] == 'G'):
                que.append([(nh, nw), warp])
                can_walk = True


        # ワープする処理
        if not can_walk:
            for tmpH in range(-2, 3):
                for tmpW in range(-2, 3):
                    nh = position[0] + tmpH
                    nw = position[1] + tmpW

                    # 移動が可能かの判定
                    if 0 <= nh < h and 0 <= nw < w and (stage[nh][nw] == '.' or stage[nh][nw] == 'G'):
                        que.append([(nh, nw), warp + 1])

    return -1


result = bfs()
print(result)
