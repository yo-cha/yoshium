import yoshium

if __name__ == '__main__':
    # ===============
    # テスト
    # ===============
    # monitor_nk(0)

    ys = yoshium.Yoshium(headless=True)
    ys.go_to('https://www5.cao.go.jp/keizai3/getsurei/getsurei-index.html')
    elm = ys.elem_text(to_left_of='5月（PDF形式：479KB）')
    txt = yoshium.get_text(elm)
    print(txt)