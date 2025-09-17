# Image Manager is a Krita plugin to displays and organizes images.
# Copyright (C) 2025  .
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


# Imports
from krita import *
from .image_manager_extension import *
from .image_manager_docker import *


# Name the Python Script for the program
DOCKER_ID = "pykrita_image_manager"

# Register Krita Docker
Application.addDockWidgetFactory( DockWidgetFactory( DOCKER_ID, DockWidgetFactoryBase.DockRight, imagemanager_Docker ) )
