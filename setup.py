#!/usr/bin/env python
# Copyright (C) 2016 Dr. Ralf Schlatterbeck Open Source Consulting.
# Reichergasse 131, A-3411 Weidling.
# Web: http://www.runtux.com Email: office@runtux.com
# All rights reserved
# ****************************************************************************
#
# This library is free software; you can redistribute it and/or modify
# it under the terms of the GNU Library General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
# ****************************************************************************


from distutils.core import setup, Extension
license = 'GNU Library or Lesser General Public License (LGPL)'

description = []
f = open ('README.rst')
for line in f :
    description.append (line)
f.close ()

setup \
    ( name             = "secret_split"
    , py_modules       = ['secret_split']
    , version          = "1.0"
    , description      = "Secret Splitting Algorithm"
    , long_description = ''.join (description)
    , license          = license
    , author           = "Ralf Schlatterbeck"
    , author_email     = "rsc@runtux.com"
    , platforms        = 'Any'
    , url              = "https://github.com/schlatterbeck/secret-splitting"
    , scripts          = ['secret-combine', 'secret-split']
    , classifiers      = \
        [ 'Development Status :: 4 - Beta'
        , 'License :: OSI Approved :: ' + license
        , 'Operating System :: OS Independent'
        , 'Programming Language :: Python'
        , 'Intended Audience :: Developers'
        , 'Intended Audience :: Science/Research'
        , 'Intended Audience :: Information Technology'
        ]
    )

