import math


class Iter:
    @staticmethod
    def custom_iter_splitter(iter_, chunk_size=2):
        for chunk_index in range(0, math.ceil(len(iter_) / chunk_size)):
            yield iter_[chunk_index * chunk_size : (chunk_index + 1) * chunk_size]

    @staticmethod
    def custom_enumerator(iter__):
        count = 0
        for item in iter__:
            yield count, item
            count += 1
