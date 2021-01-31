from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='fused',
    ext_modules=[
        CUDAExtension('fused', [
            'fused_bias_act.cpp',
            'fused_bias_act_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })


setup(
    name='upfirdn2d',
    ext_modules=[
        CUDAExtension('upfirdn2d', [
            'upfirdn2d.cpp',
            'upfirdn2d_kernel.cu',
        ])
    ],
    cmdclass={
        'build_ext': BuildExtension
    })