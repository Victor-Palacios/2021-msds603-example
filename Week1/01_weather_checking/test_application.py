from application import *


def test_api_call():
    assert retreive_web_data()[0] is not None
    assert retreive_web_data()[1] is not None
    assert len(read_s3_obj(bucket_name, output_file)) > 1
