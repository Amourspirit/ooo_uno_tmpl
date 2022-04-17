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
# Interface Class
# this is a auto generated file generated by Cheetah
# Libre Office Version: 7.3
# Namespace: com.sun.star.rendering
from typing_extensions import Literal
import typing
from .x_canvas import XCanvas as XCanvas_b19b0b7a
if typing.TYPE_CHECKING:
    from ..geometry.real_size2_d import RealSize2D as RealSize2D_ca1a0c09
    from .x_animated_sprite import XAnimatedSprite as XAnimatedSprite_1bc70eb8
    from .x_animation import XAnimation as XAnimation_d6910cbe
    from .x_bitmap import XBitmap as XBitmap_b1b70b7b
    from .x_custom_sprite import XCustomSprite as XCustomSprite_3a0e10
    from .x_sprite import XSprite as XSprite_b2470b95

class XSpriteCanvas(XCanvas_b19b0b7a):
    """
    Specialization of a XCanvas, where moving, animated objects (called sprites) are supported.

    See Also:
        `API XSpriteCanvas <https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1rendering_1_1XSpriteCanvas.html>`_
    """
    __pyunointerface__: Literal['com.sun.star.rendering.XSpriteCanvas']

    def createClonedSprite(self, original: 'XSprite_b2470b95') -> 'XSprite_b2470b95':
        """
        Create a cloned version of an already existing sprite object.
        
        The cloned sprite always shows the same content as its original, but of course the sprite position, visibility, alpha etc. can be modified independently.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def createCustomSprite(self, spriteSize: 'RealSize2D_ca1a0c09') -> 'XCustomSprite_3a0e10':
        """
        Create a custom, user-handles-it-all sprite object.
        
        A sprite is a back-buffered object with its own, independent animation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def createSpriteFromAnimation(self, animation: 'XAnimation_d6910cbe') -> 'XAnimatedSprite_1bc70eb8':
        """
        Create a sprite object from the specified animation sequence.
        
        A sprite is a back-buffered object with its own, independent animation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
        """
    def createSpriteFromBitmaps(self, animationBitmaps: 'typing.Tuple[XBitmap_b1b70b7b, ...]', interpolationMode: int) -> 'XAnimatedSprite_1bc70eb8':
        """
        Create a sprite object from the specified animation sequence.
        
        A sprite is a back-buffered object with its own, independent animation.

        Raises:
            com.sun.star.lang.IllegalArgumentException: ``IllegalArgumentException``
            VolatileContentDestroyedException: ``VolatileContentDestroyedException``
        """
    def updateScreen(self, bUpdateAll: bool) -> bool:
        """
        Tells the sprite canvas to now update the screen representation.
        
        Required to display rendered changes to the canvas, and updates to stopped animations and XCustomSprites in general. This method will return only after the screen update is done, or earlier if an error happened.
        
        If double buffering is enabled via XBufferController, no explicit call of updateScreen() is necessary, since the XBufferController methods will automatically notify all associated XSpriteCanvas instances.
        """

