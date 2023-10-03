from math import ceil

def calc_account(m):
    if m <= 0:
        return None

    # 初乗り運賃
    min_fare = 610

    # 初乗り距離
    min_distance = 1700

    # 料金計算
    if m <= min_distance:
        return min_fare
    else:
        additional_distance = m - min_distance
        additional_fare = (additional_distance // 315) * 80

        # 初乗り運賃 + 増加料金
        return min_fare + additional_fare
    pass

if __name__ == "__main__":
    from argparse import ArgumentParser
    import sys

    parser = ArgumentParser(description="引数に金額を渡すとタクシー料金を計算します")
    parser.add_argument("distance", help="走行距離(メートル)", type=int)

    args = parser.parse_args()
    d = args.distance
    a = calc_account(d)
    if a == None:
        print("不正な数値です、1以上の整数値を渡してください", file=sys.stderr)
        sys.exit(1)
    print(f"走行距離 {args.distance}m => 金額は {calc_account(args.distance)}円です。")


