from collections import namedtuple
import rx.operators as ops
import rxsci.io.file as file
import rxsci.framing.line as line


def pull_house_predict(config, data):
    data.subscribe(
        on_next=print,
        on_error=lambda e: print(e),
        on_completed=lambda: print("completed")
    )
