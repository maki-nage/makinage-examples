from collections import namedtuple
import rx.operators as ops
import rxsci.io.file as file
import rxsci.framing.line as line


def print_to_console():
    def _print_to_console(data):
        return data.pipe(
            ops.do_action(
                on_next=print,
                on_error=lambda e: print(e),
                on_completed=lambda: print("completed")
            ),
        )

    return _print_to_console


def forward_house_features(config, house_features):
    return house_features,
