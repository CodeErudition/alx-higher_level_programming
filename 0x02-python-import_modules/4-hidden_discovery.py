#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_name = dir(hidden_4)
    for name in all_name:
        if name[:2] != "__":
            print(name)
