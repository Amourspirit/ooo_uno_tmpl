# coding: utf-8
#
# Copyright 2022 :Barry-Thomas-Paul: Moss
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http: // www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Struct Class
# this is a auto generated file generated by Cheetah
# Namespace: com.sun.star.geometry
# Libre Office Version: 7.3
from typing_extensions import Literal
import typing


class AffineMatrix3D(object):
    """
    Struct Class

    This structure defines a 3 by 4 affine matrix.
    
    The matrix defined by this structure constitutes an affine mapping of a point in 3D to another point in 3D. The last line of a complete 4 by 4 matrix is omitted, since it is implicitly assumed to be [0,0,0,1].
    
    An affine mapping, as performed by this matrix, can be written out as follows, where xs, ys and zs are the source, and xd, yd and zd the corresponding result coordinates:
    
    xd = m00*xs + m01*ys + m02*zs + m03; yd = m10*xs + m11*ys + m12*zs + m13; zd = m20*xs + m21*ys + m22*zs + m23;
    
    Thus, in common matrix language, with M being the AffineMatrix3D and vs=[xs,ys,zs]^T, vd=[xd,yd,zd]^T two 3D vectors, the affine transformation is written as vd=M*vs. Concatenation of transformations amounts to multiplication of matrices, i.e. a translation, given by T, followed by a rotation, given by R, is expressed as vd=R*(T*vs) in the above notation. Since matrix multiplication is associative, this can be shortened to vd=(R*T)*vs=M'*vs. Therefore, a set of consecutive transformations can be accumulated into a single AffineMatrix3D, by multiplying the current transformation with the additional transformation from the left.
    
    Due to this transformational approach, all geometry data types are points in abstract integer or real coordinate spaces, without any physical dimensions attached to them. This physical measurement units are typically only added when using these data types to render something onto a physical output device. For 3D coordinates there is also a projection from 3D to 2D device coordinates needed. Only then the total transformation matrix (including projection to 2D) and the device resolution determine the actual measurement unit in 3D.
    
    **since**
    
        OOo 2.0

    See Also:
        `API AffineMatrix3D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1AffineMatrix3D.html>`_
    """
    typeName: Literal['com.sun.star.geometry.AffineMatrix3D']

    def __init__(self, m00: typing.Optional[float] = ..., m01: typing.Optional[float] = ..., m02: typing.Optional[float] = ..., m03: typing.Optional[float] = ..., m10: typing.Optional[float] = ..., m11: typing.Optional[float] = ..., m12: typing.Optional[float] = ..., m13: typing.Optional[float] = ..., m20: typing.Optional[float] = ..., m21: typing.Optional[float] = ..., m22: typing.Optional[float] = ..., m23: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            m00 (float, optional): m00 value.
            m01 (float, optional): m01 value.
            m02 (float, optional): m02 value.
            m03 (float, optional): m03 value.
            m10 (float, optional): m10 value.
            m11 (float, optional): m11 value.
            m12 (float, optional): m12 value.
            m13 (float, optional): m13 value.
            m20 (float, optional): m20 value.
            m21 (float, optional): m21 value.
            m22 (float, optional): m22 value.
            m23 (float, optional): m23 value.
        """
        ...


    @property
    def m00(self) -> float:
        """
        The top, left matrix entry.
        """
        ...


    @property
    def m01(self) -> float:
        """
        The top, left middle matrix entry.
        """
        ...


    @property
    def m02(self) -> float:
        """
        The top, right middle matrix entry.
        """
        ...


    @property
    def m03(self) -> float:
        """
        The top, right matrix entry.
        """
        ...


    @property
    def m10(self) -> float:
        """
        The middle, left matrix entry.
        """
        ...


    @property
    def m11(self) -> float:
        """
        The middle, middle left matrix entry.
        """
        ...


    @property
    def m12(self) -> float:
        """
        The middle, middle right matrix entry.
        """
        ...


    @property
    def m13(self) -> float:
        """
        The middle, right matrix entry.
        """
        ...


    @property
    def m20(self) -> float:
        """
        The bottom, left matrix entry.
        """
        ...


    @property
    def m21(self) -> float:
        """
        The bottom, middle left matrix entry.
        """
        ...


    @property
    def m22(self) -> float:
        """
        The bottom, middle right matrix entry.
        """
        ...


    @property
    def m23(self) -> float:
        """
        The bottom, right matrix entry.
        """
        ...


