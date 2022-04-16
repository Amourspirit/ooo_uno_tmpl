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


class Matrix2D(object):
    """
    Struct Class

    This structure defines a 2 by 2 matrix.
    
    This constitutes a linear mapping of a point in 2D to another point in 2D.
    
    The matrix defined by this structure constitutes a linear mapping of a point in 2D to another point in 2D. In contrast to the com.sun.star.geometry.AffineMatrix2D, this matrix does not include any translational components.
    
    A linear mapping, as performed by this matrix, can be written out as follows, where xs and ys are the source, and xd and yd the corresponding result coordinates:
    
    xd = m00*xs + m01*ys; yd = m10*xs + m11*ys;
    
    Thus, in common matrix language, with M being the Matrix2D and vs=[xs,ys]^T, vd=[xd,yd]^T two 2D vectors, the linear mapping is written as vd=M*vs. Concatenation of transformations amounts to multiplication of matrices, i.e. a scaling, given by S, followed by a rotation, given by R, is expressed as vd=R*(S*vs) in the above notation. Since matrix multiplication is associative, this can be shortened to vd=(R*S)*vs=M'*vs. Therefore, a set of consecutive transformations can be accumulated into a single Matrix2D, by multiplying the current transformation with the additional transformation from the left.
    
    Due to this transformational approach, all geometry data types are points in abstract integer or real coordinate spaces, without any physical dimensions attached to them. This physical measurement units are typically only added when using these data types to render something onto a physical output device, like a screen or a printer. Then, the total transformation matrix and the device resolution determine the actual measurement unit.
    
    **since**
    
        OOo 2.0

    See Also:
        `API Matrix2D <https://api.libreoffice.org/docs/idl/ref/structcom_1_1sun_1_1star_1_1geometry_1_1Matrix2D.html>`_
    """
    typeName: Literal['com.sun.star.geometry.Matrix2D']

    def __init__(self, m00: typing.Optional[float] = ..., m01: typing.Optional[float] = ..., m10: typing.Optional[float] = ..., m11: typing.Optional[float] = ...) -> None:
        """
        Constructor

        Arguments:
            m00 (float, optional): m00 value.
            m01 (float, optional): m01 value.
            m10 (float, optional): m10 value.
            m11 (float, optional): m11 value.
        """


    @property
    def m00(self) -> float:
        """
        The top, left matrix entry.
        """


    @property
    def m01(self) -> float:
        """
        The top, right matrix entry.
        """


    @property
    def m10(self) -> float:
        """
        The bottom, left matrix entry.
        """


    @property
    def m11(self) -> float:
        """
        The bottom, right matrix entry.
        """


