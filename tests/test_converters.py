import os
import hashlib

from pressurecooker import converters

test_dir = os.path.dirname(__file__)


def test_srt2vtt():
    def get_hash_file(path):
        hash = hashlib.md5()
        with open(path, 'rb') as fobj:
            for chunk in iter(lambda: fobj.read(2097152), b""):
                hash.update(chunk)
            return hash

    original_vtt = os.path.abspath(os.path.join(test_dir, "files", "original.vtt"))
    original_srt = os.path.abspath(os.path.join(test_dir, "files", "original.srt"))

    resulting_vtt = "/tmp/test_vtt.vtt"
    converters.srt2vtt(original_srt, resulting_vtt)
    original_vtt_hash = get_hash_file(original_vtt)
    resulting_vtt_hash = get_hash_file(resulting_vtt)

    assert original_vtt_hash.hexdigest() == resulting_vtt_hash.hexdigest()

