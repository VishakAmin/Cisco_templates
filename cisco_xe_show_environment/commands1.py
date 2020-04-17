import sys
import json
from textfsm import TextFSM


def f1(input_file, template_file):
    try:
        _tm = TextFSM(open(template_file))
        _raw = open(input_file).read()
        _header = _tm.header
        _fsm = _tm.ParseText(_raw)
        print("-".center(100, "-"))
        print(_raw)
        print("-".center(100, "-"))
        print(_header)
        print("-".center(100, "-"))
        print(_fsm)
        print("-".center(100, "-"))
        data = []
        for j in [dict(zip(_header, i)) for i in _fsm]:
            print(j)
            data.append(j)
        print("-".center(100, "-"))
        print(len(_fsm))
        print("-".center(100, "-"))
        open(output_file, 'w').write(json.dumps(data))
    except Exception as e:
        raise e


if __name__ == "__main__":
    input_file = sys.argv[1]
    template_file = sys.argv[2]
    output_file = sys.argv[3]
    f1(input_file, template_file)