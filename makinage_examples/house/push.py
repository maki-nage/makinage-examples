from collections import namedtuple
import rx.operators as ops
import rxsci.io.file as file


def push_house_data(config):
    data = file.read('/opt/dataset/HomeC.csv', size=64*1024).pipe(
        line.unframe(),
        ops.skip(1),
    )

    return data,
