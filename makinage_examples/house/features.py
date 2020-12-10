from collections import namedtuple
import rx
import rx.operators as ops
import rxsci as rs
import rxsci.container.csv as csv


Features = namedtuple('Features', ['label', 'pspeed_ratio', 'temperature', 'temperature_stddev'])

parser = csv.create_line_parser(
    dtype=[
        ('time', 'int'),
        ('use', 'float'),
        ('gen', 'float'),
        ('house_overall', 'float'),
        ('dishwasher', 'float'),
        ('furnace1', 'float'),
        ('furnace2', 'float'),
        ('home_office', 'float'),
        ('fridge', 'float'),
        ('wine_cellar', 'float'),
        ('garage_door', 'float'),
        ('kitchen_12', 'float'),
        ('kitchen_14', 'float'),
        ('kitchen_38', 'float'),
        ('barn', 'float'),
        ('well', 'float'),
        ('microwave', 'float'),
        ('living_room', 'float'),
        ('solar', 'float'),
        ('temperature', 'float'),
        ('icon', 'str'),
        ('humidity', 'float'),
        ('visibility', 'float'),
        ('summary', 'str'),
        ('apparent_temperature', 'float'),
        ('pressure', 'float'),
        ('wind_speed', 'float'),
        ('cloud_cover', 'str'),
        ('wind_bearing', 'float'),
        ('precip_intensity', 'float'),
        ('dew_point', 'float'),
        ('precip_probability', 'float'),
    ]
)


def compute_house_features(config, data):
    epsilon = 1e-5
    features = data.pipe(
        csv.load(parser),
        rs.ops.map(lambda i: Features(
            label=i.house_overall,
            pspeed_ratio=i.pressure / (i.wind_speed + epsilon),
            temperature=i.temperature,
            temperature_stddev=0.0,
        )),
        rs.state.with_memory_store(rx.pipe(
            rs.data.roll(
                window=60*6, stride=60,
                pipeline=rs.ops.tee_map(
                    rx.pipe(
                        rs.ops.last(),
                    ),
                    rx.pipe(
                        rs.ops.map(lambda i: i.temperature),
                        rs.math.stddev(reduce=True),
                    ),
                )
            ),
        )),
        rs.ops.map(lambda i: i[0]._replace(temperature_stddev=i[1])),
    )

    return features,
