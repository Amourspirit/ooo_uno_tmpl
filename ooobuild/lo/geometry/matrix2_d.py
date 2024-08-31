# coding: utf-8
#
# Copyright 2023-2024 :Barry-Thomas-Paul: Moss
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
# Libre Office Version: 2024.2
from ooo.oenv.env_const import UNO_NONE
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
    __ooo_ns__: str = 'com.sun.star.geometry'
    __ooo_full_ns__: str = 'com.sun.star.geometry.Matrix2D'
    __ooo_type_name__: str = 'struct'
    typeName: str = 'com.sun.star.geometry.Matrix2D'
    """Literal Constant ``com.sun.star.geometry.Matrix2D``"""

    def __init__(self, m00: typing.Optional[float] = 0.0, m01: typing.Optional[float] = 0.0, m10: typing.Optional[float] = 0.0, m11: typing.Optional[float] = 0.0) -> None:
        """
        Constructor

        Arguments:
            m00 (float, optional): m00 value.
            m01 (float, optional): m01 value.
            m10 (float, optional): m10 value.
            m11 (float, optional): m11 value.
        """
        super().__init__()

        if isinstance(m00, Matrix2D):
            oth: Matrix2D = m00
            self.m00 = oth.m00
            self.m01 = oth.m01
            self.m10 = oth.m10
            self.m11 = oth.m11
            return

        kargs = {
            "m00": m00,
            "m01": m01,
            "m10": m10,
            "m11": m11,
        }
        self._init(**kargs)

    def _init(self, **kwargs) -> None:
        self._m00 = kwargs["m00"]
        self._m01 = kwargs["m01"]
        self._m10 = kwargs["m10"]
        self._m11 = kwargs["m11"]


    @property
    def m00(self) -> float:
        """
        The top, left matrix entry.
        """
        return self._m00

    @m00.setter
    def m00(self, value: float) -> None:
        self._m00 = value

    @property
    def m01(self) -> float:
        """
        The top, right matrix entry.
        """
        return self._m01

    @m01.setter
    def m01(self, value: float) -> None:
        self._m01 = value

    @property
    def m10(self) -> float:
        """
        The bottom, left matrix entry.
        """
        return self._m10

    @m10.setter
    def m10(self, value: float) -> None:
        self._m10 = value

    @property
    def m11(self) -> float:
        """
        The bottom, right matrix entry.
        """
        return self._m11

    @m11.setter
    def m11(self, value: float) -> None:
        self._m11 = value


__all__ = ['Matrix2D']
