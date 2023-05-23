# coding: utf-8
#
# Copyright 2023 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 7.4
import typing


class AffineMatrix2D(object):
    """
    Struct Class

    This structure defines a 2 by 3 affine matrix.
    
    The matrix defined by this structure constitutes an affine mapping of a point in 2D to another point in 2D. The last line of a complete 3 by 3 matrix is omitted, since it is implicitly assumed to be [0,0,1].
    
    An affine mapping, as performed by this matrix, can be written out as follows, where xs and ys are the source, and xd and yd the corresponding result coordinates:
    
    xd = m00*xs + m01*ys + m02; yd = m10*xs + m11*ys + m12;
    
    Thus, in common matrix language, with M being the AffineMatrix2D and vs=[xs,ys]^T, vd=[xd,yd]^T two 2D vectors, the affine transformation is written as vd=M*vs. Concatenation of transformations amounts to multiplication of matrices, i.e. a translation, given by T, followed by a rotation, given by R, is expressed as vd=R*(T*vs) in the above notation. Since matrix multiplication is associative, this can be shortened to vd=(R*T)*vs=M'*vs. Therefore, a set of consecutive transformations can be accumulated into a single AffineMatrix2D, by multiplying the current transformation with the additional transformation from the left.
    
    Due to this transformational approach, all geometry data types are points in abstract integer or real coordinate spaces, without any physical dimensions attached to them. This physical measurement units are typically only added when using these data types to render something onto a physical output device, like a screen or a printer, Then, the total transformation matrix and the device resolution determine the actual measurement unit.
    
    **since**
    
        OOo 2.0

    See Also:
        `API AffineMatrix2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1AffineMatrix2D.html>`_
    """
    typeName: str = 'com.sun.star.geometry.AffineMatrix2D'

    def __init__(self, m00: typing.Optional[float] = ..., m01: typing.Optional[float] = ..., m02: typing.Optional[float] = ..., m10: typing.Optional[float] = ..., m11: typing.Optional[float] = ..., m12: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            m00 (float, optional): m00 value.
            m01 (float, optional): m01 value.
            m02 (float, optional): m02 value.
            m10 (float, optional): m10 value.
            m11 (float, optional): m11 value.
            m12 (float, optional): m12 value.
        """
        ...

    @property
    def m00(self) -> float:
        """
        The top, left matrix entry.
        """
        ...
    @m00.setter
    def m00(self, value: float) -> None:
        ...
    @property
    def m01(self) -> float:
        """
        The top, middle matrix entry.
        """
        ...
    @m01.setter
    def m01(self, value: float) -> None:
        ...
    @property
    def m02(self) -> float:
        """
        The top, right matrix entry.
        """
        ...
    @m02.setter
    def m02(self, value: float) -> None:
        ...
    @property
    def m10(self) -> float:
        """
        The bottom, left matrix entry.
        """
        ...
    @m10.setter
    def m10(self, value: float) -> None:
        ...
    @property
    def m11(self) -> float:
        """
        The bottom, middle matrix entry.
        """
        ...
    @m11.setter
    def m11(self, value: float) -> None:
        ...
    @property
    def m12(self) -> float:
        """
        The bottom, right matrix entry.
        """
        ...
    @m12.setter
    def m12(self, value: float) -> None:
        ...
