import pathlib

if __name__ == '__main__':
    p = pathlib.Path("D://data")
    print(p)
    print(p.parent)

    p = p / "channel-proxy"
    print(p)
    print(p.exists())
