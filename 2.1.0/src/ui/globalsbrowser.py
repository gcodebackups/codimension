#
# -*- coding: utf-8 -*-
#
# codimension - graphics python two-way code editor and analyzer
# Copyright (C) 2010  Sergey Satskiy <sergey.satskiy@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# $Id: globalsbrowser.py 1316 2013-04-03 21:48:48Z sergey.satskiy@gmail.com $
#

#
# The file was taken from eric 4.4.3 and adopted for codimension.
# Original copyright:
# Copyright (c) 2007 - 2010 Detlev Offenbach <detlev@die-offenbachs.de>
#

" Globals browser with hierarchy browsing capabilities "

from utils.pixmapcache     import PixmapCache
from globalsbrowsermodel   import GlobalsBrowserModel
from objectsbrowserbase    import ObjectsBrowser


class GlobalsBrowser( ObjectsBrowser ):
    " Globals browser "

    def __init__( self, parent = None ):

        ObjectsBrowser.__init__( self, GlobalsBrowserModel(), parent )
        self.setRootIsDecorated( False )

        self.setWindowTitle( 'Globals browser' )
        self.setWindowIcon( PixmapCache().getIcon( 'icon.png' ) )
        return

