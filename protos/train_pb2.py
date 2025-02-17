# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/train.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import optimizer_pb2 as protos_dot_optimizer__pb2
from protos import preprocessor_pb2 as protos_dot_preprocessor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12protos/train.proto\x12\x06protos\x1a\x16protos/optimizer.proto\x1a\x19protos/preprocessor.proto\"\x89\x07\n\x0bTrainConfig\x12\x16\n\nbatch_size\x18\x01 \x01(\r:\x02\x33\x32\x12<\n\x19\x64\x61ta_augmentation_options\x18\x02 \x03(\x0b\x32\x19.protos.PreprocessingStep\x12\x1c\n\rsync_replicas\x18\x03 \x01(\x08:\x05\x66\x61lse\x12+\n\x1dkeep_checkpoint_every_n_hours\x18\x04 \x01(\r:\x04\x31\x30\x30\x30\x12$\n\toptimizer\x18\x05 \x01(\x0b\x32\x11.protos.Optimizer\x12$\n\x19gradient_clipping_by_norm\x18\x06 \x01(\x02:\x01\x30\x12\x1e\n\x14\x66ine_tune_checkpoint\x18\x07 \x01(\t:\x00\x12#\n\x19\x66ine_tune_checkpoint_type\x18\x16 \x01(\t:\x00\x12,\n\x19\x66rom_detection_checkpoint\x18\x08 \x01(\x08:\x05\x66\x61lseB\x02\x18\x01\x12\x31\n\"load_all_detection_checkpoint_vars\x18\x13 \x01(\x08:\x05\x66\x61lse\x12\x14\n\tnum_steps\x18\t \x01(\r:\x01\x30\x12\x1f\n\x13startup_delay_steps\x18\n \x01(\x02:\x02\x31\x35\x12\x1f\n\x14\x62ias_grad_multiplier\x18\x0b \x01(\x02:\x01\x30\x12\x18\n\x10\x66reeze_variables\x18\x0c \x03(\t\x12 \n\x15replicas_to_aggregate\x18\r \x01(\x05:\x01\x31\x12!\n\x14\x62\x61tch_queue_capacity\x18\x0e \x01(\x05:\x03\x31\x35\x30\x12\"\n\x17num_batch_queue_threads\x18\x0f \x01(\x05:\x01\x38\x12\"\n\x17prefetch_queue_capacity\x18\x10 \x01(\x05:\x01\x35\x12)\n\x1amerge_multiple_label_boxes\x18\x11 \x01(\x08:\x05\x66\x61lse\x12$\n\x15use_multiclass_scores\x18\x18 \x01(\x08:\x05\x66\x61lse\x12%\n\x17\x61\x64\x64_regularization_loss\x18\x12 \x01(\x08:\x04true\x12 \n\x13max_number_of_boxes\x18\x14 \x01(\x05:\x03\x31\x30\x30\x12\'\n\x19unpad_groundtruth_tensors\x18\x15 \x01(\x08:\x04true\x12%\n\x16retain_original_images\x18\x17 \x01(\x08:\x05\x66\x61lse')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.train_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRAINCONFIG.fields_by_name['from_detection_checkpoint']._options = None
  _TRAINCONFIG.fields_by_name['from_detection_checkpoint']._serialized_options = b'\030\001'
  _TRAINCONFIG._serialized_start=82
  _TRAINCONFIG._serialized_end=987
# @@protoc_insertion_point(module_scope)
