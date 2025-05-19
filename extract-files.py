#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/common/libqti-perfd-client',
    'hardware/qcom-caf/sdm845',
    'hardware/nubia',
    'vendor/qcom/opensource/display',
    'vendor/nubia/sdm845-common'
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/audio.primary.sdm845.so': blob_fixup()
        .add_needed('libprocessgroup.so'),
    'vendor/lib64/libgoodixfingerprintd_binder.so': blob_fixup()
        .add_needed('libbinder_shim.so'),
    'vendor/lib64/libSNPE.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/bin/ultrasonicd': blob_fixup()
        .remove_needed('libmedia.so++.so'),
    'vendor/lib64/vendor.goodix.hardware.fingerprintextension@1.0.so': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib/camera/components/com.nubia.node.realtimeaicamera.so': blob_fixup()
        .add_needed('libcutils.so'),
    'vendor/lib/hw/camera.qcom.so': blob_fixup()
        .clear_symbol_version('remote_handle64_close')
        .clear_symbol_version('remote_handle64_invoke')
        .clear_symbol_version('remote_handle64_open')
}  # fmt: skip

module = ExtractUtilsModule(
    'nx606j',
    'nubia',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sdm845-common', module.vendor)
    utils.run()
