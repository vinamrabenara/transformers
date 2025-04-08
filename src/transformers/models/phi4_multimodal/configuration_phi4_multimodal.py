#                🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
#           This file was automatically generated from src/transformers/models/phi4_multimodal/modular_phi4_multimodal.py.
#               Do NOT edit this file manually as any edits will be overwritten by the generation of
#             the file from the modular. If any change should be done, please apply the change to the
#                          modular_phi4_multimodal.py file directly. One of our CI enforces this.
#                🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨
# Copyright 2025 Microsoft and the HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math

from ...configuration_utils import PretrainedConfig


class Phi4MultimodalVisionConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Phi4MultimodalVisionModel`]. It is used to instantiate a
    Phi4Multimodal vision encoder according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the vision encoder of
    [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 1152):
            Dimensionality of the encoder layers and the pooler layer.
        intermediate_size (`int`, *optional*, defaults to 4304):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_hidden_layers (`int`, *optional*, defaults to 27):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_channels (`int`, *optional*, defaults to 3):
            Number of channels in the input images.
        image_size (`int`, *optional*, defaults to 448):
            The size (resolution) of each image.
        patch_size (`int`, *optional*, defaults to 14):
            The size (resolution) of each patch.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu_pytorch_tanh"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` `"quick_gelu"` are supported.
        layer_norm_eps (`float`, *optional*, defaults to 1e-06):
            The epsilon used by the layer normalization layers.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        crop_size (`int`, *optional*, defaults to 448):
            Crop size for the input images.
        image_token_id (`int`, *optional*, defaults to 200010):
            The image token id.
        feature_layer (`int`, *optional*, defaults to -2):
            The index of the layer of the encoder from which to extract image features.

    Example:

    ```python
    >>> from transformers import Phi4MultimodalVisionConfig

    >>> # Initializing a Phi4MultimodalVisionConfig with microsoft/Phi-4-multimodal-instruct style configuration
    >>> configuration = Phi4MultimodalVisionConfig()
    ```"""

    model_type = "phi4_multimodal_vision"
    base_config_key = "vision_config"

    def __init__(
        self,
        hidden_size=1152,
        intermediate_size=4304,
        num_hidden_layers=27,
        num_attention_heads=16,
        num_channels=3,
        image_size=448,
        patch_size=14,
        hidden_act="gelu_pytorch_tanh",
        layer_norm_eps=1e-6,
        attention_dropout=0.0,
        crop_size: int = 448,
        image_token_id: int = 200010,
        feature_layer: int = -2,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.num_channels = num_channels
        self.patch_size = patch_size
        self.image_size = image_size
        self.attention_dropout = attention_dropout
        self.layer_norm_eps = layer_norm_eps
        self.hidden_act = hidden_act
        self.crop_size = crop_size
        self.image_token_id = image_token_id
        self.feature_layer = feature_layer


class Phi4MultimodalAudioConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Phi4MultimodalAudioModel`]. It is used to instantiate a
    Phi4Multimodal audio encoder according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the audio encoder of
    [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        hidden_size (`int`, *optional*, defaults to 1024):
            Dimensionality of the encoder layers.
        intermediate_size (`int`, *optional*, defaults to 1536):
            Dimensionality of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        num_blocks (`int`, *optional*, defaults to 24):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 16):
            Number of attention heads for each attention layer in the Transformer encoder.
        activation (`str`, *optional*, defaults to `"swish"`):
            The non-linear activation function in the MLPs.
        chunk_size (`int`, *optional*, defaults to -1):
            The chunk size to create the masks.
        left_chunk (`int`, *optional*, defaults to 18):
            The left chunk to create the masks.
        dropout_rate (`float`, *optional*, defaults to 0.0):
            The dropout ratio.
        ext_pw_out_channel (`int`, *optional*, defaults to 1024):
            Number of out channels in the point-wise conv modules.
        depthwise_seperable_out_channel (`int`, *optional*, defaults to 1024):
            Number of out channels in the depth-wise separable conv modules.
        depthwise_multiplier (`int`, *optional*, defaults to 1):
            Input size multiplier for the depth-wise separable conv modules.
        kernel_size (`int`, *optional*, defaults to 3):
            Kernel size for the depth-wise separable conv modules.
        conv_activation (`str`, *optional*, defaults to `"swish"`):
            The non-linear activation function in the conv modules.
        input_size (`int`, *optional*, defaults to 80):
            Input size for the audio model.
        conv_glu_type (`str`, *optional*, defaults to `"swish"`):
            The non-linear activation function in the point-wise conv modules.
        time_reduction (`int`, *optional*, defaults to 8):
            Time reduction (subsampling factor).
        bias_max_distance (`int`, *optional*, defaults to 1000):
            Max distance for the relative attention bias module.
        bias_symmetric (`bool`, *optional*, defaults to `False`):
            Whether the relative attention bias should be symmetric or not.
        nemo_activation (`str`, *optional*, defaults to `"relu"`):
            The non-linear activation function in the nemo conv modules.
        nemo_conv_channels (`int`, *optional*, defaults to 1024):
            Number of channels in the nemo conv modules.
        downsample_rate (`int`, *optional*, defaults to 1):
            Downsample rate for the audio feature extractor.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        audio_token_id (`int`, *optional*, defaults to 200011):
            The audio token id.
        feature_layer (`int`, *optional*, defaults to -2):
            The index of the layer of the encoder from which to extract audio features.

    Example:

    ```python
    >>> from transformers import Phi4MultimodalAudioConfig

    >>> # Initializing a Phi4MultimodalAudioConfig with microsoft/Phi-4-multimodal-instruct style configuration
    >>> configuration = Phi4MultimodalAudioConfig()
    ```"""

    model_type = "phi4_multimodal_audio"

    def __init__(
        self,
        hidden_size: int = 1024,
        intermediate_size: int = 1536,
        num_blocks: int = 24,
        num_attention_heads: int = 16,
        activation: str = "swish",
        chunk_size: int = -1,
        left_chunk: int = 18,
        dropout_rate: float = 0.0,
        ext_pw_out_channel: int = 1024,
        depthwise_seperable_out_channel: int = 1024,
        depthwise_multiplier: int = 1,
        kernel_size: int = 3,
        conv_activation: str = "swish",
        input_size: int = 80,
        conv_glu_type: str = "swish",
        time_reduction: int = 8,
        bias_max_distance: int = 1000,
        bias_symmetric: bool = False,
        nemo_activation: str = "relu",
        nemo_conv_channels: int = 1024,
        downsample_rate: int = 1,
        initializer_range: float = 0.02,
        audio_token_id: int = 200011,
        feature_layer: int = -2,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.hidden_size = hidden_size
        self.num_attention_heads = num_attention_heads
        self.intermediate_size = intermediate_size
        self.activation = activation
        self.chunk_size = chunk_size
        self.left_chunk = left_chunk
        self.num_blocks = num_blocks
        self.dropout_rate = dropout_rate
        self.ext_pw_out_channel = ext_pw_out_channel
        self.depthwise_seperable_out_channel = depthwise_seperable_out_channel
        self.depthwise_multiplier = depthwise_multiplier
        self.kernel_size = kernel_size
        self.conv_activation = conv_activation
        self.input_size = input_size
        self.conv_glu_type = conv_glu_type
        self.time_reduction = time_reduction
        self.bias_max_distance = bias_max_distance
        self.bias_symmetric = bias_symmetric
        self.nemo_activation = nemo_activation
        self.nemo_conv_channels = nemo_conv_channels
        self.downsample_rate = downsample_rate
        self.audio_token_id = audio_token_id
        self.initializer_range = initializer_range
        self.feature_layer = feature_layer

        if time_reduction % 2 != 0:
            raise ValueError("`time_reduction` should be a multiple of 2!")
        length = input_size
        for _ in range(int(math.log(time_reduction, 2))):
            length = math.floor((length - 1) / 2 + 1)
        self.nemo_final_size = length


class Phi4MultimodalConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`Phi4MultimodalModel`]. It is used to instantiate a
    Phi4Multimodal model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the
    [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        vocab_size (`int`, *optional*, defaults to 200064):
            Vocabulary size of the Phi-3 model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`Phi3Model`].
        hidden_size (`int`, *optional*, defaults to 3072):
            Dimension of the hidden representations.
        intermediate_size (`int`, *optional*, defaults to 8192):
            Dimension of the MLP representations.
        num_hidden_layers (`int`, *optional*, defaults to 32):
            Number of hidden layers in the Transformer decoder.
        num_attention_heads (`int`, *optional*, defaults to 32):
            Number of attention heads for each attention layer in the Transformer decoder.
        num_key_value_heads (`int`, *optional*, defaults to 8):
            This is the number of key_value heads that should be used to implement Grouped Query Attention. If
            `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if
            `num_key_value_heads=1` the model will use Multi Query Attention (MQA) otherwise GQA is used. When
            converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed
            by meanpooling all the original heads within that group. For more details checkout [this
            paper](https://arxiv.org/pdf/2305.13245.pdf). If it is not specified, will default to
            `num_attention_heads`.
        resid_pdrop (`float`, *optional*, defaults to 0.0):
            Dropout probability for mlp outputs.
        embd_pdrop (`int`, *optional*, defaults to 0.0):
            The dropout ratio for the embeddings.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio after computing the attention scores.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the decoder.
        max_position_embeddings (`int`, *optional*, defaults to 131072):
            The maximum sequence length that this model might ever be used with.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        rms_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon value used for the RMSNorm.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`. Whether to tie weight embeddings or not.
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether to tie weight embeddings
        rope_theta (`float`, *optional*, defaults to 10000.0):
            The base period of the RoPE embeddings.
        rope_scaling (`dict`, *optional*):
            The scaling strategy for the RoPE embeddings. If `None`, no scaling is applied. If a dictionary, it must
            contain the following keys: `type`, `short_factor` and `long_factor`. The `type` must be `longrope` and
            the `short_factor` and `long_factor` must be lists of numbers with the same length as the hidden size
            divided by the number of attention heads divided by 2.
        partial_rotary_factor (`float`, *optional*, defaults to `1.0`):
            Percentage of the query and keys which will have rotary embedding. Must be between 0.0 and 1.0.
        bos_token_id (`int`, *optional*, defaults to 199999):
            The id of the "beginning-of-sequence" token.
        eos_token_id (`int` or `list[int]`, *optional*, defaults to `[199999, 200020]`):
            The id of the "end-of-sequence" token.
        pad_token_id (`int`, *optional*, defaults to 199999):
            The id of the padding token.
        original_max_position_embeddings (`int`, *optional*, defaults to 4096):
            The maximum sequence length that this model was trained with. This is used to determine the size of the
            original RoPE embeddings when using long scaling.
        sliding_window (`int`, *optional*):
            Sliding window attention window size. If `None`, no sliding window is applied.
        vision_config (`Phi4MultimodalVisionConfig` or `dict`, *optional*):
            The vision config for the underlying image embedding model. If not provided, will default to the configuration
            used to instantiate a model similar in architecture as
            [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct).
        audio_config (`Phi4MultimodalAudioConfig` or `dict`, *optional*):
            The audio config for the underlying audio embedding model. If not provided, will default to the configuration
            used to instantiate a model similar in architecture as
            [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct).

    Example:

    ```python
    >>> from transformers import Phi4MultimodalModel, Phi4MultimodalConfig

    >>> # Initializing a Phi4Multimodal style configuration
    >>> configuration = Phi4MultimodalConfig.from_pretrained("microsoft/Phi-4-multimodal-instruct")

    >>> # Initializing a model from the configuration
    >>> model = Phi4MultimodalModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "phi4_multimodal"
    keys_to_ignore_at_inference = ["past_key_values"]
    base_model_tp_plan = {
        "layers.*.self_attn.qkv_proj": "colwise_rep",  # we need to replicate here due to the slicing of qkv
        "layers.*.self_attn.o_proj": "rowwise_rep",  # we need to replicate here due to the slicing of qkv
        "layers.*.mlp.gate_up_proj": "colwise_rep",  # we need to replicate here due to the `chunk` operation
        "layers.*.mlp.down_proj": "rowwise_rep",  # we need to replicate here due to the `chunk` operation
    }
    base_model_pp_plan = {
        "embed_tokens": (["input_ids"], ["inputs_embeds"]),
        "layers": (["hidden_states", "attention_mask"], ["hidden_states"]),
        "norm": (["hidden_states"], ["hidden_states"]),
    }

    sub_configs = {"audio_config": Phi4MultimodalAudioConfig, "vision_config": Phi4MultimodalVisionConfig}

    def __init__(
        self,
        vocab_size=200064,
        hidden_size=3072,
        intermediate_size=8192,
        num_hidden_layers=32,
        num_attention_heads=32,
        num_key_value_heads=8,
        resid_pdrop=0.0,
        embd_pdrop=0.0,
        attention_dropout=0.0,
        hidden_act="silu",
        max_position_embeddings=131072,
        initializer_range=0.02,
        rms_norm_eps=1e-5,
        use_cache=True,
        tie_word_embeddings=False,
        rope_theta=10000.0,
        rope_scaling=None,
        partial_rotary_factor=1,
        bos_token_id=199999,
        eos_token_id=[199999, 200020],
        pad_token_id=199999,
        original_max_position_embeddings=4096,
        sliding_window=None,
        vision_config=None,
        audio_config=None,
        **kwargs,
    ):
        super().__init__(
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            pad_token_id=pad_token_id,
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )
        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads

        if num_key_value_heads is None:
            num_key_value_heads = num_attention_heads

        self.num_key_value_heads = num_key_value_heads
        self.resid_pdrop = resid_pdrop
        self.embd_pdrop = embd_pdrop
        self.attention_dropout = attention_dropout
        self.hidden_act = hidden_act
        self.max_position_embeddings = max_position_embeddings
        self.original_max_position_embeddings = original_max_position_embeddings
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.rope_theta = rope_theta
        self.rope_scaling = rope_scaling
        self.partial_rotary_factor = partial_rotary_factor
        self._rope_scaling_adjustment()
        self._rope_scaling_validation()
        self.sliding_window = sliding_window

        if isinstance(vision_config, dict):
            vision_config = Phi4MultimodalVisionConfig(**vision_config)
        elif vision_config is None:
            Phi4MultimodalVisionConfig()
        self.vision_config = vision_config

        if isinstance(audio_config, dict):
            audio_config = Phi4MultimodalAudioConfig(**audio_config)
        elif vision_config is None:
            audio_config = Phi4MultimodalAudioConfig()
        self.audio_config = audio_config

    def _rope_scaling_adjustment(self):
        """
        Adjust the `type` of the `rope_scaling` configuration for backward compatibility.
        """
        if self.rope_scaling is None:
            return

        rope_scaling_type = self.rope_scaling.get("type", None)

        # For backward compatibility if previous version used "su" or "yarn"
        if rope_scaling_type is not None and rope_scaling_type in ["su", "yarn"]:
            self.rope_scaling["type"] = "longrope"

    def _rope_scaling_validation(self):
        """
        Validate the `rope_scaling` configuration.
        """
        if self.rope_scaling is None:
            return

        if not isinstance(self.rope_scaling, dict) or len(self.rope_scaling) != 3:
            raise ValueError(
                "`rope_scaling` must be a dictionary with three fields, `type`, `short_factor` and `long_factor`, "
                f"got {self.rope_scaling}"
            )
        rope_scaling_type = self.rope_scaling.get("type", None)
        rope_scaling_short_factor = self.rope_scaling.get("short_factor", None)
        rope_scaling_long_factor = self.rope_scaling.get("long_factor", None)
        if rope_scaling_type is None or rope_scaling_type not in ["longrope"]:
            raise ValueError(f"`rope_scaling`'s type field must be one of ['longrope'], got {rope_scaling_type}")
        if not (
            isinstance(rope_scaling_short_factor, list)
            and all(isinstance(x, (int, float)) for x in rope_scaling_short_factor)
        ):
            raise ValueError(
                f"`rope_scaling`'s short_factor field must be a list of numbers, got {rope_scaling_short_factor}"
            )
        rotary_ndims = int(self.hidden_size // self.num_attention_heads * self.partial_rotary_factor)
        if not len(rope_scaling_short_factor) == rotary_ndims // 2:
            raise ValueError(
                f"`rope_scaling`'s short_factor field must have length {rotary_ndims // 2}, got {len(rope_scaling_short_factor)}"
            )
        if not (
            isinstance(rope_scaling_long_factor, list)
            and all(isinstance(x, (int, float)) for x in rope_scaling_long_factor)
        ):
            raise ValueError(
                f"`rope_scaling`'s long_factor field must be a list of numbers, got {rope_scaling_long_factor}"
            )
        if not len(rope_scaling_long_factor) == rotary_ndims // 2:
            raise ValueError(
                f"`rope_scaling`'s long_factor field must have length {rotary_ndims // 2}, got {len(rope_scaling_long_factor)}"
            )


__all__ = ["Phi4MultimodalVisionConfig", "Phi4MultimodalAudioConfig", "Phi4MultimodalConfig"]
