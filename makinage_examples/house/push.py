import rx.operators as ops
import rxsci.io.file as file
import rxsci.framing.line as line


def read_house_data(filename):
    data = file.read(filename, size=64*1024).pipe(
        line.unframe(),
        ops.skip(1),
    )

    return data


def forward_house_data(config, house_data):
    return house_data,
