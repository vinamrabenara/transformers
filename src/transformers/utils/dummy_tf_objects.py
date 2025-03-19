# This file is autogenerated by the command `make fix-copies`, do not edit.
from ..utils import DummyObject, requires_backends


class TFForcedBOSTokenLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFForcedEOSTokenLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFForceTokensLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFGenerationMixin(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFLogitsProcessorList(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFLogitsWarper(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFMinLengthLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFNoBadWordsLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFNoRepeatNGramLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFRepetitionPenaltyLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFSuppressTokensAtBeginLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFSuppressTokensLogitsProcessor(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFTemperatureLogitsWarper(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFTopKLogitsWarper(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFTopPLogitsWarper(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class KerasMetricCallback(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class PushToHubCallback(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFPreTrainedModel(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFSequenceSummary(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class TFSharedEmbeddings(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


def shape_list(*args, **kwargs):
    requires_backends(shape_list, ["tf"])


class AdamWeightDecay(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class GradientAccumulator(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


class WarmUp(metaclass=DummyObject):
    _backends = ["tf"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["tf"])


def create_optimizer(*args, **kwargs):
    requires_backends(create_optimizer, ["tf"])
